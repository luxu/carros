from pathlib import Path

import pytest

from core.models import Car, Manufacturer

TERMS_LIST = [
  [[4, 3], [-2, 1]],
  [[-4, 3], [-2, 1]]
]

def load_json_in_the_cars():
    # filename = "cars.json"
    # local_filename_json = Path.joinpath(Path.home(), Path('desktop'), filename)
    # with open(local_filename_json, "r", encoding="utf8") as _file:
    #     texto = _file.read()
    # return texto
    yield from ["2022-02-12", "2022-01-12", "2020-02-12"]

@pytest.fixture
def manufacturer(db):
    return Manufacturer.objects.create(
        name='FIAT'
    )

@pytest.fixture
def car(manufacturer):
    return Car.objects.create(
        price=3.00,
        year=2023,
        manufacturer=manufacturer
    )


def test_car(car):
    assert car.name == 'Doblô'
