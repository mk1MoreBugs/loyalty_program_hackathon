from pydantic import BaseModel


class WalletOut(BaseModel):
    id: int
    user_id: int
    amount_bonus: int
