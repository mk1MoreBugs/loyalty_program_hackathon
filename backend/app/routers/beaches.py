from typing import Annotated

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.dependencies import session_db
from app.schemas.beach import BreachOut, BaseBeach
from db.crud import beaches

router = APIRouter(
    prefix="/beaches",
    tags=["beaches"]
)


@router.get("/")
async def read_beaches(db_session: Session = Depends(session_db)) -> list[BreachOut]:
    return beaches.read_beaches(db_session)


@router.post("/")
async def create_beach(
        db_session: Annotated[Session, Depends(session_db)],
        beach: BaseBeach,
):
    beaches.create_beach(db_session=db_session, **dict(beach))


@router.put("/{beach_id}")
async def update_beach(
        db_session: Annotated[Session, Depends(session_db)],
        beach_id: int,
        new_number_sunbeds: Annotated[int, Body()],
):
    beaches.update_beach(
        db_session=db_session,
        beach_id=beach_id,
        new_number_sunbeds=new_number_sunbeds
    )
