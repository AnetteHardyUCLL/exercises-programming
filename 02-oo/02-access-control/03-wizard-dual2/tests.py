from student import Wizard

def test_wizard_cast_fireball_successful():
    # Create a wizard and a target
    wizard = Wizard("Gandalf")
    target = Wizard("Saruman")

    # Ensure that the wizard has enough mana to cast fireball
    wizard._Wizard__mana = 25

    # Cast fireball
    result = wizard.cast_fireball(target)

    # Check if the fireball was cast successfully
    assert result == "Gandalf casts fireball at Saruman"

    # Check if the wizard's mana is deducted correctly
    assert wizard.get_mana() == 5

    # Check if the target's health is reduced by 30
    assert target.get_health() == 35

def test_wizard_cast_fireball_insufficient_mana():
    # Create a wizard and a target
    wizard = Wizard("Gandalf")
    target = Wizard("Saruman")

    # Ensure that the wizard has insufficient mana to cast fireball
    wizard._Wizard__mana = 15

    # Try casting fireball and ensure it raises an exception
    try:
        wizard.cast_fireball(target)
    except Exception as e:
        assert str(e) == "Gandalf cannot cast fireball"

# Run the tests
test_wizard_cast_fireball_successful()
test_wizard_cast_fireball_insufficient_mana()
