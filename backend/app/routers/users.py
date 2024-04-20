from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from app.dependencies import session_db
from app.schemas.user import UserOut, BaseUser
from db.crud import users

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/")
async def read_users(db_session: Session = Depends(session_db)) -> list[UserOut]:
    return users.read_users(db_session)


@router.post("/")
async def create_user(
        user: BaseUser,
        db_session: Session = Depends(session_db),
):
    users.create_user(
        db_session=db_session,
        last_name=user.last_name,
        first_name=user.first_name,
        middle_name=user.middle_name,
        phone_number=user.phone_number,
        cashback_amount=user.cashback_amount,
        role=user.role,
    )
