from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.const import (
    CLOSED_PROJECT_INVESTMENT,
    DELETE_NOT_ALLOWED,
    INVESTMENT_AMOUNT_EXCEED,
    OBJECT_NOT_FOUND,
    PROJECT_ALREADY_EXIST,
)
from app.crud.charity_project import charity_project_crud
from app.models import CharityProject
from app.schemas.charity_project import CharityProjectUpdate


async def check_name_duplicate(
    room_name: str,
    session: AsyncSession,
) -> None:
    room_id = await charity_project_crud.get_charity_project_id_by_name(
        room_name, session
    )
    if room_id is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=PROJECT_ALREADY_EXIST,
        )


async def check_charity_project_exists(
    project_id: int,
    session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(project_id, session)
    if charity_project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail=OBJECT_NOT_FOUND
        )
    return charity_project


async def check_updating_project(
    obj_in: CharityProjectUpdate,
    project_id: int,
    session: AsyncSession,
):
    charity_project = await check_charity_project_exists(project_id, session)
    await check_name_duplicate(obj_in.name, session)
    if (
        obj_in.full_amount
        and obj_in.full_amount < charity_project.invested_amount
    ):
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            detail=INVESTMENT_AMOUNT_EXCEED,
        )
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=CLOSED_PROJECT_INVESTMENT,
        )
    return charity_project


async def check_charity_project_before_delete(
    charity_project: CharityProject,
):
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail=DELETE_NOT_ALLOWED
        )
    if charity_project.invested_amount != 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail=DELETE_NOT_ALLOWED
        )
