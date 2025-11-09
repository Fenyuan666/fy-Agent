"""RBAC service layer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from .models import Permission, Role, RoleAssignment


@dataclass
class InMemoryRBACService:
    roles: Dict[str, Role] = field(default_factory=dict)
    assignments: List[RoleAssignment] = field(default_factory=list)

    def upsert_role(self, role: Role) -> Role:
        self.roles[role.name] = role
        return role

    def list_roles(self) -> List[Role]:
        return list(self.roles.values())

    def assign_role(self, assignment: RoleAssignment) -> RoleAssignment:
        self.assignments.append(assignment)
        return assignment

    def list_assignments(self, user_id: str | None = None) -> List[RoleAssignment]:
        if user_id is None:
            return list(self.assignments)
        return [assignment for assignment in self.assignments if assignment.user_id == user_id]


rbac_service = InMemoryRBACService()
