from app.models.donation import Donation

from .base import CRUDBase


class CRUDDonation(CRUDBase):
    pass


donation_crud = CRUDDonation(Donation)
