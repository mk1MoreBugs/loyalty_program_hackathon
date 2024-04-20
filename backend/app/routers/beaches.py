from typing import Annotated

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.dependencies import session_db
from app.schemas.beach import BreachOut, BaseBeach
from db.crud import beaches

router = APIRouter(
    prefix="/beaches",
    tags=["beaches"],
)


@router.get(
    "/",
    summary="Показать доступное количество лежаков на всех пляжах",
)
async def read_beaches(db_session: Session = Depends(session_db)) -> list[BreachOut]:
    return beaches.read_beaches(db_session)


@router.post(
    "/",
    summary="Создать новый пляж",
)
async def create_beach(
        db_session: Annotated[Session, Depends(session_db)],
        beach: BaseBeach,
):
    """
    - **name**: Название пляжа
    - **number_sunbeds_available**: Число свободных лежаков
    - **number_sunbeds**: Общее количество лежаков
    - **price_sunbeds**: Цена аренды 1 лежака
    """
    beaches.create_beach(db_session=db_session, **dict(beach))


@router.put(
    "/{beach_id}",
    summary="Обновить количество свободных лежаков",
)
async def update_beach(
        db_session: Annotated[Session, Depends(session_db)],
        beach_id: int,
        new_number_sunbeds_available: Annotated[int, Body()],
):
    """
    - **beach_id**: ID пляжа
    - **new_number_sunbeds_available**: Новое количество доступных лежаков
    """
    beaches.update_beach(
        db_session=db_session,
        beach_id=beach_id,
        new_number_sunbeds_available=new_number_sunbeds_available
    )
