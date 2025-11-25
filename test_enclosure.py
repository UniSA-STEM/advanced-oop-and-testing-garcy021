'''
File: test_enclosure.py
Description: Unit tests for enclosure.py
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''
from enclosure import Enclosure
from animal import Koala, Penguin, HealthRecord

def test_enclosure_valid_creation():
    e = Enclosure("Forest", "forest", 2)
    assert e.get_name() == "Forest"
    assert e.get_environment_type() == "forest"
    assert e.get_size() == 2
    assert e.get_cleanliness_level() == 100

def test_enclosure_invalid_inputs():
    # empty name
    error_raised = False
    try:
        Enclosure("", "forest", 2)
    except ValueError:
        error_raised = True
    assert error_raised is True
    # empty environment
    error_raised = False
    try:
        Enclosure("E1", "", 2)
    except ValueError:
        error_raised = True
    assert error_raised is True

    # invalid size
    error_raised = False
    try:
        Enclosure("E1", "forest", 0)
    except ValueError:
        error_raised = True
    assert error_raised is True

    # invalid cleanliness
    error_raised = False
    try:
        Enclosure("E1", "forest", 2, 101)
    except ValueError:
        error_raised = True
    assert error_raised is True

def test_add_animal_environment_rule():
    forest = Enclosure("Forest", "forest", 2)
    penguin = Penguin("Pingu", 2)

    error_raised = False
    try:
        forest.add_animal(penguin)
    except ValueError:
        error_raised = True
    assert error_raised is True

def test_add_animal_single_species_rule():
    forest = Enclosure("Forest", "forest", 2)
    koala = Koala("Koko", 3)
    penguin = Penguin("Pingu", 2)

    forest.add_animal(koala)

    error_raised = False
    try:
        forest.add_animal(penguin)
    except ValueError:
        error_raised = True
    assert error_raised is True

def test_add_animal_capacity_rule():
    forest = Enclosure("Forest", "forest", 1)
    koala1 = Koala("Koko", 3)
    koala2 = Koala("Luna", 2)

    forest.add_animal(koala1)

    error_raised = False
    try:
        forest.add_animal(koala2)
    except ValueError:
        error_raised = True
    assert error_raised is True

def test_under_treatment_rule_blocks_move():
    forest = Enclosure("Forest", "forest", 2)
    desert = Enclosure("Desert", "desert", 2)

    koala = Koala("Koko", 3)

    # add first while healthy
    forest.add_animal(koala)

    # now add health issue
    record = HealthRecord("Injury", 3)
    koala.add_health_record(record)

    # moving should be blocked
    error_raised = False
    try:
        desert.add_animal(koala)
    except ValueError:
        error_raised = True
    assert error_raised is True

def test_clean_and_soil_behavior():
    forest = Enclosure("Forest", "forest", 2)

    forest.soil(30)
    assert forest.get_cleanliness_level() == 70

    forest.clean()
    assert forest.get_cleanliness_level() == 100

    forest.soil(200)
    assert forest.get_cleanliness_level() == 0