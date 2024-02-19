import pytest
from student import MusicalNote



def test_getting_name():
    name = 'a4'
    pitch = 440
    note = MusicalNote(name, pitch)
    assert note.name == name


def test_getting_pitch():
    name = 'a4'
    pitch = 440
    note = MusicalNote(name, pitch)
    assert note.pitch == pitch


def test_setting_name():
    note = MusicalNote('a4', 440)
    with pytest.raises(AttributeError):
        note.name = 'b5'


def test_setting_pitch():
    note = MusicalNote('a4', 440)
    with pytest.raises(AttributeError):
        note.pitch = 500
