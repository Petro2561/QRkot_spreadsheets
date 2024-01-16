from datetime import datetime

from app.models.charity_project import CommonFields


async def investing_logic(crud_obj, new_obj: CommonFields, session):
    spisok = await crud_obj.get_avaliable_sourses(session)
    for source in spisok:
        avaliable = source.full_amount - source.invested_amount
        needed = new_obj.full_amount - new_obj.invested_amount
        new_obj.invested_amount += min(avaliable, needed)
        source.invested_amount += min(avaliable, needed)
        close(new_obj)
        close(source)
    await session.commit()
    await session.refresh(new_obj)


def close(obj):
    if obj.full_amount == obj.invested_amount:
        obj.fully_invested = True
        obj.close_date = datetime.now()
