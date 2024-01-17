from datetime import datetime
from typing import Dict, Optional

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.core.const import FORMAT

SHEET_RANGE = "A1:E30"

TABLE_VALUES = [
    ["Отчет от"],
    ["Топ проектов по скорости закрытия"],
    ["Название проекта", "Время сбора", "Описание"],
]

REPORT_NAME = 'Отчет от {current_date_time}'
SHEETS_LOCALE = 'ru_RU'
SHEETS_TITLE = 'Лист1'
SHEETS_TYPE = 'GRID'

SHEETS_COLUMNS_NUMBER = 5
SHEETS_ROWS_NUMBER = 100

SHEETS_PROPERTIES = dict(
    sheetType=SHEETS_TYPE,
    sheetId=0,
    title=SHEETS_TITLE,
    gridProperties=dict(
        rowCount=SHEETS_ROWS_NUMBER,
        columnCount=SHEETS_COLUMNS_NUMBER,
    )
)

SPREADSHEET_BODY = dict(
    properties=dict(
        title=REPORT_NAME,
        locale=SHEETS_LOCALE
    ),
    sheets=[dict(
        properties=SHEETS_PROPERTIES
    )]
)


async def spreadsheet_create(
    wrapper_services: Aiogoogle, spreadsheet_body: Optional[Dict] = None
) -> str:
    service = await wrapper_services.discover("sheets", "v4")
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=SPREADSHEET_BODY)
    )
    return response["spreadsheetId"]


async def set_user_permissions(
    spreadsheet_id: str, wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        "type": "user",
        "role": "writer",
        "emailAddress": settings.email,
    }
    service = await wrapper_services.discover("drive", "v3")
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id",
        )
    )


async def spreadsheets_update_value(
    wrapper_services: Aiogoogle, spreadsheet_id: str, projects: list
) -> None:
    service = await wrapper_services.discover("sheets", "v4")
    TABLE_VALUES[0].append(datetime.now().strftime(FORMAT))
    for project in projects:
        project["duration"] = str((project["duration"]))
        TABLE_VALUES.append(list(project.values()))
    update_body = {"majorDimension": "ROWS", "values": TABLE_VALUES}

    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=SHEET_RANGE,
            valueInputOption="USER_ENTERED",
            json=update_body,
        )
    )
