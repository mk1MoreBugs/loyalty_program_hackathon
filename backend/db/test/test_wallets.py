from db.crud.wallets import create_wallet, read_wallets, update_wallet


def test_create_and_read_wallet(db_session, wallet):
    create_wallet(
        db_session=db_session,
        amount_bonus=wallet.amount_bonus,
        user_id=wallet.user_id,
    )

    result = read_wallets(db_session)
    assert result[0].user_id == wallet.user_id
    assert result[0].amount_bonus == wallet.amount_bonus


def test_update_wallet(db_session, wallet):
    new_amount = wallet.amount_bonus + 100
    create_wallet(
        db_session=db_session,
        amount_bonus=wallet.amount_bonus,
        user_id=wallet.user_id,
    )

    update_wallet(
        db_session=db_session,
        user_id=wallet.user_id,
        new_amount=new_amount,
    )

    result = read_wallets(db_session)
    assert result[0].amount_bonus == new_amount
