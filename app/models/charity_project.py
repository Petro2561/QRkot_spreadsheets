from sqlalchemy import Column, String, Text

from app.models.base import CommonFields


class CharityProject(CommonFields):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
