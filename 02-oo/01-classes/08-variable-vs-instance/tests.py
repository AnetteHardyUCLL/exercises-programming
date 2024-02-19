from student import Dragon

def test_dragon_init():
    first_dragon = Dragon("fire")
    assert first_dragon.element == "fire"

    second_dragon = Dragon("ice")
    assert second_dragon.element == "ice"

def test_dragon_breath_damage():
    fire_dragon = Dragon("fire")
    assert fire_dragon.get_breath_damage() == 300

    ice_dragon = Dragon("ice")
    assert ice_dragon.get_breath_damage() == 150

    unknown_dragon = Dragon("unknown")
    assert unknown_dragon.get_breath_damage() == 0

# Run the tests
test_dragon_init()
test_dragon_breath_damage()
