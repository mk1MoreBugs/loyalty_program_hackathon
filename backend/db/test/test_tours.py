from db.crud.tours import create_tour, read_tour
from db.models.tour import Tour


def test_create_and_read_user_without_middle_name(db_session):
    tour = Tour(
        id=1,
        name="Foo",
        price=100,
        cashback_percent=10,
    )
    create_tour(
        db_session=db_session,
        name=tour.name,
        price=tour.price,
        cashback_percent=tour.cashback_percent,
    )

    result = read_tour(db_session=db_session)
    assert result[0].id == tour.id
    assert result[0].name == tour.name
    assert result[0].price == tour.price
    assert result[0].cashback_percent == tour.cashback_percent
