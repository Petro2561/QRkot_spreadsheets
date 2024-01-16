from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import CommonFields


class Donation(CommonFields):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text)
