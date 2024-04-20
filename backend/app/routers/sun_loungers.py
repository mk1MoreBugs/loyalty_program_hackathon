from fastapi import APIRouter

router = APIRouter(
    prefix="/sun-longers",
    tags=["sun longers"]
)


@router.get(
    path="/total-sun-loungers",
    summary="Количество свободных шезлонгов",
)
async def read_total_sun_loungers():
    pass
