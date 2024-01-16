from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator

from app.core.const import (
    INVESTMENT_AMOUNT_MIN,
    INVESTMENT_AMOUNT_MIN_LESS_THAN_MIN,
    MAX_STR_LENGTH,
    MIN_STR_LENGTH,
)


class CharityProjectBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    full_amount: Optional[int]

    class Config:
        extra = Extra.forbid
        min_anystr_length = MIN_STR_LENGTH


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(
        ..., min_length=MIN_STR_LENGTH, max_length=MAX_STR_LENGTH
    )
    description: str = Field(...)
    full_amount: int = Field(..., ge=MIN_STR_LENGTH)


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectUpdate(CharityProjectBase):
    @validator("full_amount")
    def full_amount_must_be_greater_than_zero(cls, value: str):
        if value < INVESTMENT_AMOUNT_MIN:
            raise ValueError(INVESTMENT_AMOUNT_MIN_LESS_THAN_MIN)
        return value
