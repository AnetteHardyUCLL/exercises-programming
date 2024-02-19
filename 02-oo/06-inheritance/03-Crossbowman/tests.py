from student import Human, Archer, Crossbowman
import pytest

def test_human_initialization():
    human = Human("John")
    assert human.get_name() == "John"

def test_archer_initialization():
    archer = Archer("Legolas", 20)
    assert archer.get_name() == "Legolas"
    assert archer.get_num_arrows() == 20

def test_archer_use_arrows_successful():
    archer = Archer("Legolas", 20)
    archer.use_arrows(10)
    assert archer.get_num_arrows() == 10

def test_archer_use_arrows_insufficient():
    archer = Archer("Legolas", 5)
    with pytest.raises(Exception) as exc_info:
        archer.use_arrows(10)
    assert str(exc_info.value) == "Not enough arrows"

def test_crossbowman_initialization():
    crossbowman = Crossbowman("Bran", 30)
    assert crossbowman.get_name() == "Bran"
    assert crossbowman.get_num_arrows() == 30

def test_crossbowman_triple_shot_successful():
    crossbowman = Crossbowman("Bran", 10)
    result = crossbowman.triple_shot("target")
    assert result == "target was shot by 3 crossbow bolts"
    assert crossbowman.get_num_arrows() == 7

def test_crossbowman_triple_shot_insufficient_arrows():
    crossbowman = Crossbowman("Bran", 2)
    with pytest.raises(Exception) as exc_info:
        crossbowman.triple_shot("target")
    assert str(exc_info.value) == "Not enough arrows"

# Run the tests
if __name__ == "__main__":
    pytest.main()
