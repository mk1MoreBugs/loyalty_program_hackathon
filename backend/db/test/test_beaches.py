from db import Beach
from db.crud.beaches import create_beach, read_beaches, update_beach


def test_create_and_read_beach(db_session, beach):
    create_beach(
        db_session=db_session,
        name=beach.name,
        number_sunbeds=beach.number_sunbeds,
        number_sunbeds_available=beach.number_sunbeds_available,
        price_sunbeds=beach.price_sunbeds,
    )

    result = read_beaches(db_session=db_session)
    assert result[0].name == beach.name
    assert result[0].number_sunbeds == beach.number_sunbeds
    assert result[0].number_sunbeds_available == beach.number_sunbeds_available
    assert result[0].price_sunbeds == beach.price_sunbeds


def test_update_number_sunbeds(db_session, beach):
    new_number_sunbeds = 10
    create_beach(
        db_session=db_session,
        name=beach.name,
        number_sunbeds=beach.number_sunbeds,
        number_sunbeds_available=beach.number_sunbeds_available,
        price_sunbeds=beach.price_sunbeds,
    )

    update_beach(
        db_session=db_session,
        beach_id=1,
        new_number_sunbeds_available=new_number_sunbeds
    )

    result = read_beaches(db_session=db_session)
    assert result[0].number_sunbeds_available == new_number_sunbeds

