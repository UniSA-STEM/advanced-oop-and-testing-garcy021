'''
File: test_staff.py
Description: Unit tests for staff.py
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''
from staff import ZooKeeper, Veterinarian
from enclosure import Enclosure
from animal import Koala, Snake

def test_staff_validation():
    error_raised = False
    try:
        ZooKeeper("")
    except ValueError:
        error_raised = True
    assert error_raised is True

    error_raised = False
    try:
        Veterinarian("")
    except ValueError:
        error_raised = True
    assert error_raised is True

def test_assign_animal_accepts_subclass():
    keeper = ZooKeeper("Ava")
    koala = Koala("Koko", 3)

    keeper.assign_animal(koala)
    animals = keeper.get_assigned_animals()
    assert koala in animals

def test_assign_enclosure():
    keeper = ZooKeeper("Ava")
    forest = Enclosure("Forest", "forest", 2)

    keeper.assign_enclosure(forest)
    enclosures = keeper.get_assigned_enclosures()
    assert forest in enclosures

def test_zookeeper_feed_unassigned_raises():
    keeper = ZooKeeper("Ava")
    koala = Koala("Koko", 3)

    error_raised = False
    try:
        keeper.feed_animal(koala)
    except ValueError:
        error_raised = True
    assert error_raised is True

def test_vet_health_check_adds_record():
    vet = Veterinarian("Dr Sam")
    koala = Koala("Koko", 3)

    vet.assign_animal(koala)
    vet.perform_health_check(koala, "Paw injury", 3, "Rest")

    assert koala.has_active_health_issue() is True
    assert len(koala.get_health_records()) == 1

def test_vet_resolves_issue():
    vet = Veterinarian("Dr Sam")
    snake = Snake("Sly", 5)

    vet.assign_animal(snake)
    vet.perform_health_check(snake, "Cold", 2, "Heat lamp")

    assert snake.has_active_health_issue() is True

    vet.mark_resolved(snake, "Recovered")
    assert snake.has_active_health_issue() is False