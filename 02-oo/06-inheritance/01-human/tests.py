from student import Human, Archer

def test_human_initialization():
    human = Human("John")
    assert human.get_name() == "John"

def test_archer_initialization():
    archer = Archer("Legolas", 20)
    assert archer.get_name() == "Legolas"
    assert archer.get_num_arrows() == 20

def test_archer_inherited_attributes():
    archer = Archer("Legolas", 20)
    assert hasattr(archer, "_Human__name")  # Check if the Human's private attribute is accessible

# Run the tests
if __name__ == "__main__":
    test_human_initialization()
    test_archer_initialization()
    test_archer_inherited_attributes()
