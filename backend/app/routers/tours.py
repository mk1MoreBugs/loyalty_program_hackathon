from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from app.dependencies import session_db
from app.schemas.tour import TourOut, BaseTour
from db.crud import tours

router = APIRouter(
    prefix="/tours",
    tags=["tours"]
)


@router.get("/")
async def read_tours(db_session: Session = Depends(session_db)) -> list[TourOut]:
    return tours.read_tours(db_session=db_session)


@router.post("/")
async def create_tour(
        tour: BaseTour,
        db_session: Session = Depends(session_db),
):
    tours.create_tour(
        db_session=db_session,
        **dict(tour),
    )
