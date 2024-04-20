from db.crud.users import create_user, read_users
from db.crud.wallets import read_wallets
from db.models.user import User


def test_create_and_read_user_without_middle_name(db_session):
    user = User(
        id=1,
        last_name="Foo",
        first_name="Bar",
        phone_number="+79000000000",
        cashback_amount=0,
        role="Местный",
    )
    create_user(
        db_session=db_session,
        last_name=user.last_name,
        first_name=user.first_name,
        phone_number=user.phone_number,
        cashback_amount=user.cashback_amount,
        role=user.role,
    )

    result_user = read_users(db_session=db_session)
    result_wallet = read_wallets(db_session=db_session)
    assert result_user[0].id == user.id
    assert result_user[0].last_name == user.last_name
    assert result_user[0].first_name == user.first_name
    assert result_user[0].phone_number == user.phone_number
    assert result_user[0].cashback_amount == user.cashback_amount

    assert result_wallet[0].user_id == 1
    assert result_wallet[0].amount_bonus == 0

