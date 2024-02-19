import pytest
from student import *


@pytest.fixture
def time():
    return Time(0, 0, 0)


@pytest.mark.parametrize("hours", [0, 4, 23])
@pytest.mark.parametrize("minutes", [0, 12, 59])
@pytest.mark.parametrize("seconds", [0, 12, 59])
def test_constructor_valid_values(hours, minutes, seconds):
    time = Time(hours, minutes, seconds)

    assert time.hours == hours
    assert time.minutes == minutes
    assert time.seconds == seconds


@pytest.mark.parametrize("hours, minutes, seconds", [
    (-1, 0, 0),
    (24, 0, 0),
    (0, -1, 0),
    (0, 60, 0),
    (0, 0, -1),
    (0, 0, 60)
])
def test_constructor_invalid_values(hours, minutes, seconds):
    with pytest.raises(ValueError):
        Time(hours, minutes, seconds)



@pytest.mark.parametrize("hours", list(range(0, 24)))
def test_set_valid_hours(time, hours):
    time.hours = hours
    assert time.hours == hours


@pytest.mark.parametrize("minutes", list(range(0, 60)))
def test_set_valid_minutes(time, minutes):
    time.minutes = minutes
    assert time.minutes == minutes


@pytest.mark.parametrize("seconds", list(range(0, 60)))
def test_set_valid_seconds(time, seconds):
    time.seconds = seconds
    assert time.seconds == seconds


@pytest.mark.parametrize("hours", [-4, -1, 24, 29])
def test_set_invalid_hours(time, hours):
    with pytest.raises(ValueError):
        time.hours = hours

@pytest.mark.parametrize("minutes", [-4, -1, 60, 61])
def test_set_invalid_minutes(time, minutes):
    with pytest.raises(ValueError):
        time.minutes = minutes


@pytest.mark.parametrize("seconds", [-4, -1, 60, 61])
def test_set_invalid_seconds(time, seconds):
    with pytest.raises(ValueError):
        time.seconds = seconds
