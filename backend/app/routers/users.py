from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Path

from app.dependencies import session_db
from app.schemas.user import UserOut, BaseUser
from db.crud import users

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get(
    "/",
    summary="Показать всех пользователей",
)
async def read_users(db_session: Session = Depends(session_db)) -> list[UserOut]:
    return users.read_users(db_session)


@router.post(
    "/",
    summary="Создать нового пользователя",

)
async def create_user(
        user: BaseUser,
        db_session: Session = Depends(session_db),
):
    """
    - **last_name**: Фамилия
    - **first_name**: Имя
    - **middle_name**: Отчество
    - **phone_number**: Номер телефона
    - **cashback_amount**: Количество бонусных баллов
    - **role**: Роль пользователя: *Местный* или *Турист*

    При создании нового пользователя также создается бонусный счет
    """
    users.create_user(
        db_session=db_session,
        last_name=user.last_name,
        first_name=user.first_name,
        middle_name=user.middle_name,
        phone_number=user.phone_number,
        cashback_amount=user.cashback_amount,
        role=user.role,
    )


@router.delete(
    "/{user_id}",
    summary="Удалить пользователя",
)
async def delete_user(
        db_session: Annotated[Session, Depends(session_db)],
        user_id: Annotated[int, Path(title="Id пользователя, которого нужно удалить")],
):
    """
          - **user_id**: ID пользователя
       """
    pass
