# fy-Agent 模块化框架

一个高内聚、低耦合、可插拔的 AI Agent 前后端框架示例：

- 后端：FastAPI（Python）
- 前端：Vue 3 + Vite
- 数据源：MongoDB / MySQL / Redis 按需启用
- 功能插件：Auth、RBAC、Agent、Caching 可随时移除

核心理念：**核心最小化，功能可插拔**。删除一个功能 ≈ 删除该目录 + 关闭 `.env` 开关。

---

## 架构速览

```
backend/
  core/                # 框架核心：配置、应用工厂、健康检查
  plugins/             # 功能插件目录（可增删）
    auth/              # 登录注册、当前用户依赖
    rbac/              # 角色/权限管理逻辑
    agent/             # Agent 问答接口，支持多种引擎
    caching/           # Redis 缓存封装
  db/                  # 按需加载的数据库适配器
  main.py              # FastAPI 入口
frontend/
  src/core/            # Vue 基础模块（router、http 客户端）
  src/plugins/         # 前端功能插件（与后端插件对应）
  vite.config.js       # 定义别名 & 反向代理
.env.example           # 后端功能开关模板
frontend/.env.example  # 前端功能开关模板
```

核心代码文件：
- `backend/core/config.py` 读取所有开关，并暴露 `settings`
- `backend/core/app.py` 根据开关按需注册路由、初始化依赖
- `backend/plugins/**` 内部自包含路由、服务、依赖
- `frontend/src/core/router.js` 根据环境变量组合路由
- `frontend/src/plugins/**` 与后端插件一一对应

---

## 功能开关

### 后端 `.env`

```ini
FEATURE_AUTH=true
FEATURE_RBAC=false
FEATURE_AGENT=true
FEATURE_REDIS=false
AUTH_DATABASE_BACKEND=mongo
RBAC_DATABASE_BACKEND=mysql
DATABASE_MONGO_URI=mongodb://localhost:27017/agent
DATABASE_MYSQL_URI=mysql+pymysql://user:password@localhost:3306/agent
REDIS_URI=redis://localhost:6379/0
DEFAULT_AGENT_ENGINE=echo
```

1. 拷贝模板：`cp .env.example .env`
2. 将对应插件的 `FEATURE_*` 改为 `false` 即可关闭，并且可以删除整个插件目录。

### 前端 `frontend/.env`

```ini
VITE_API_BASE=/api/v1
VITE_FEATURE_AUTH=true
VITE_FEATURE_AGENT=true
VITE_FEATURE_RBAC=false
VITE_MOCK_USER_EMAIL=demo@example.com
```

1. 拷贝模板：`cp frontend/.env.example frontend/.env`
2. 控制路由和视图加载，未启用的功能不会被打包。

---

## 本地启动

**后端**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

**前端**
```bash
cd frontend
npm install
npm run dev
```

- 前端默认请求 `/api/v1`，可通过 `VITE_API_BASE` 修改。
- 已提供 Docker Compose 示例，可按需取消注释 Mongo / MySQL / Redis 服务。

---

## 插件开发流程

1. 在 `backend/plugins/` 新建目录（例如 `chat/`），包含 `routes.py`、`services.py` 等。
2. 在 `.env` 增加 `FEATURE_CHAT=true`，并在 `backend/core/app.py` 中按开关注册路由。
3. 如需数据库，请在 `backend/db/` 添加适配器或复用现有客户端。
4. 前端在 `frontend/src/plugins/` 新增对应组件，通过 `VITE_FEATURE_CHAT` 控制加载。

> 插件之间通过依赖注入 (`fastapi.Depends`) 共享服务，例如 RBAC 依赖 `auth` 的 `get_current_user`，即使 Auth 关闭也不会阻塞启动。

---

## 目录可移除性

| 模块 | 删除方式 | 影响 |
|------|----------|------|
| Auth | 删除 `backend/plugins/auth` + 关闭 `FEATURE_AUTH` | 登录接口及依赖自动移除 |
| RBAC | 删除 `backend/plugins/rbac` + 关闭 `FEATURE_RBAC` | 权限接口不再注册 |
| Agent | 删除 `backend/plugins/agent` + 关闭 `FEATURE_AGENT` | Agent API 与前端页面移除 |
| Caching | 删除 `backend/plugins/caching` + 关闭 `FEATURE_REDIS` | Redis 不再初始化 |

> 核心目录 `backend/core` 与 `frontend/src/core` 不可删除，它们提供应用生命周期与基础设施。

---

## Docker Compose（可选）

1. 构建镜像
   ```bash
   docker compose build
   docker compose up
   ```
2. 按需取消注释 Mongo / MySQL / Redis 服务即可启用，后端配置通过 `.env` 同步。

---

## 下一步建议

- 将内存实现替换为真实数据库读写
- 在 Agent 插件 `engines/` 目录下集成 LangChain、LlamaIndex 等引擎
- 为每个插件编写独立测试，确保在关闭其他插件时仍可运行
- 扩展前端插件机制（菜单、权限指令等）
