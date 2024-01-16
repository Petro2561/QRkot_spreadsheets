from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models.user import User
from app.schemas.donation import DonationAllDB, DonationCreate, DonationUserDB
from app.services.investing_logic import investing_logic

router = APIRouter()


@router.post(
    "/",
    response_model=DonationUserDB,
    response_model_exclude_none=True,
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    donation = await donation_crud.create(donation, session, user)
    await investing_logic(charity_project_crud, donation, session)
    return donation


@router.get(
    "/",
    response_model=list[DonationAllDB],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    return await donation_crud.get_multi(session)


@router.get("/my", response_model=list[DonationUserDB])
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await donation_crud.get_multi(session, user)
