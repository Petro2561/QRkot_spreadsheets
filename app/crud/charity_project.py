from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject

from .base import CRUDBase


class CRUDCharityProject(CRUDBase):
    async def get_charity_project_id_by_name(
        self, name: str, session: AsyncSession
    ):
        charity_project = await session.execute(
            select(CharityProject.id).where(CharityProject.name == name)
        )
        return charity_project.scalars().first()

    async def get_projects_by_completion_rate(self, session: AsyncSession):
        projects = await session.execute(
            select([CharityProject]).where(CharityProject.fully_invested == 1)
        )
        projects = projects.scalars().all()
        projects_list = sorted(
            [
                {
                    "name": project.name,
                    "duration": project.close_date - project.create_date,
                    "description": project.description,
                }
                for project in projects
            ],
            key=lambda x: x["duration"],
        )
        return projects_list


charity_project_crud = CRUDCharityProject(CharityProject)
