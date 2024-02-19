from student import Archer

def test_archer_constructor():
    name = "Legolas"
    health = 10
    num_arrows = 20
    archer = Archer(name, health, num_arrows)
    assert archer.name == name
    assert archer.health == health
    assert archer.num_arrows == num_arrows

def test_archer_get_shot():
    archer = Archer("Legolas", 10, 20)
    archer.get_shot()
    assert archer.health == 9  # Health should be reduced by 1

def test_archer_get_shot_exception():
    archer = Archer("Legolas", 1, 20)
    try:
        archer.get_shot()
    except ValueError as e:
        assert str(e) == "Legolas is dead"  # Exception should be raised

def test_archer_shoot():
    legolas = Archer("Legolas", 10, 20)
    target = Archer("Enemy", 10, 20)
    legolas.shoot(target)
    assert target.health == 9  # Target's health should be reduced by 1
    assert legolas.num_arrows == 19  # Legolas' num_arrows should be reduced by 1

def test_archer_shoot_exception():
    legolas = Archer("Legolas", 10, 0)
    target = Archer("Enemy", 10, 20)
    try:
        legolas.shoot(target)
    except ValueError as e:
        assert str(e) == "Legolas can't shoot"  # Exception should be raised

# Run the tests
test_archer_constructor()
test_archer_get_shot()
test_archer_get_shot_exception()
test_archer_shoot()
test_archer_shoot_exception()
