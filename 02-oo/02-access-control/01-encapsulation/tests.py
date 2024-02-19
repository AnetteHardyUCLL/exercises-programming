from student import Wizard

def test_wizard_initialization():
    wizard = Wizard("Gandalf")
    assert wizard.name == "Gandalf"
    assert wizard._Wizard__mana == 45
    assert wizard._Wizard__health == 65

def test_wizard_get_mana():
    wizard = Wizard("Gandalf")
    assert wizard.get_mana() == 45

def test_wizard_get_health():
    wizard = Wizard("Gandalf")
    assert wizard.get_health() == 65

# Run the tests
test_wizard_initialization()
test_wizard_get_mana()
test_wizard_get_health()
