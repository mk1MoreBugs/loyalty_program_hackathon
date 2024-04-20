from db.crud.users import create_user, read_user
from db.models.user import User


def test_create_and_read_user_without_middle_name(db_session):
    user = User(
        id=1,
        last_name="Foo",
        first_name="Bar",
        phone_number="+79000000000",
        cashback_amount=0,
    )
    create_user(
        db_session=db_session,
        last_name=user.last_name,
        first_name=user.first_name,
        phone_number=user.phone_number,
        cashback_amount=user.cashback_amount,
    )

    result = read_user(db_session=db_session)
    assert result[0].id == user.id
    assert result[0].last_name == user.last_name
    assert result[0].first_name == user.first_name
    assert result[0].phone_number == user.phone_number
    assert result[0].cashback_amount == user.cashback_amount
