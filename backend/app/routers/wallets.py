from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Query

from app.dependencies import session_db
from app.schemas.wallet import WalletOut
from db.crud import wallets

router = APIRouter(
    prefix="/wallets",
    tags=["wallets"]
)


@router.get("/")
async def read_wallets(db_session: Session = Depends(session_db)) -> list[WalletOut]:
    return wallets.read_wallets(db_session)


@router.get("/{user_id}")
async def read_wallets_by_id(
        db_session: Annotated[Session, Depends(session_db)],
        user_id: int,
) -> WalletOut:
    pass


@router.get("/{user_id}")
async def create_wallet(
       db_session: Annotated[Session, Depends(session_db)],
        user_id: int,
        amount_bonus: Annotated[int, Query(alias="amount-bonus")] = 0,
):
    wallets.create_wallet(
        db_session=db_session,
        amount_bonus=amount_bonus,
        user_id=user_id,
    )


@router.put("/")
async def update_wallet(
        db_session: Annotated[Session, Depends(session_db)],
        user_id: int,
        new_amount: int,
):
    wallets.update_wallet(
        db_session=db_session,
        user_id=user_id,
        new_amount=new_amount,
    )
