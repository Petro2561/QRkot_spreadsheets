from datetime import datetime

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, Integer

from app.core.db import Base


class CommonFields(Base):
    __abstract__ = True
    __table_args__ = (
        CheckConstraint("full_amount > 0", name="full_amount_is_positive"),
        CheckConstraint(
            "full_amount >= invested_amount",
            name="full_amount_ge_invested_amount",
        ),
    )
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, nullable=False, default=0)
    fully_invested = Column(Boolean, nullable=False, default=False)
    create_date = Column(DateTime, nullable=False, default=datetime.now)
    close_date = Column(DateTime, nullable=True)
