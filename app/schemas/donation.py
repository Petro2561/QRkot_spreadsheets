from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field

from app.core.const import INVESTMENT_AMOUNT_MIN


class DonationBase(BaseModel):
    comment: Optional[str]
    full_amount: int = Field(..., ge=INVESTMENT_AMOUNT_MIN)

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    pass


class DonationUserDB(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationAllDB(DonationUserDB):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
