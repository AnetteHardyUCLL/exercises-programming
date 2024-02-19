from student import Wizard

def test_wizard_get_fireballed():
    wizard = Wizard("Gandalf")
    initial_health = wizard.get_health()
    wizard.get_fireballed()
    assert wizard.get_health() == initial_health - 30  # Fireball damage is 30

def test_wizard_drink_mana_potion():
    wizard = Wizard("Gandalf")
    initial_mana = wizard.get_mana()
    wizard.drink_mana_potion()
    assert wizard.get_mana() == initial_mana + 40  # Mana potion adds 40 mana

# Run the tests
test_wizard_get_fireballed()
test_wizard_drink_mana_potion()
