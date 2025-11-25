'''
File: test_animal.py
Description: Unit tests for animal.py
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import HealthRecord, Koala, Penguin, Snake

# HealthRecord Tests
def test_health_record_valid_creation():
    r = HealthRecord("Scratch", 2, "Rest")
    assert r.description == "Scratch"
    assert r.severity == 2
    assert r.resolved is False

def test_health_record_invalid_description():
    error_raised = False
    try:
        HealthRecord("", 3)
    except ValueError:
        error_raised = True
    assert error_raised is True

def test_health_record_invalid_severity():
    error_raised_low = False
    try:
        HealthRecord("Cold", 0)
    except ValueError:
        error_raised_low = True
    assert error_raised_low is True

    error_raised_high = False
    try:
        HealthRecord("Cold", 6)
    except ValueError:
        error_raised_high = True
    assert error_raised_high is True

def test_mark_resolved_sets_flag():
    r = HealthRecord("Injury", 4)
    r.mark_resolved("Recovered")
    assert r.resolved is True
    assert "Recovered" in r.notes

# Animal / Subclass Tests
def test_animal_subclass_creation():
    k = Koala("Koko", 4)
    assert k.get_name() == "Koko"
    assert k.get_species() == "Koala"
    assert k.get_age() == 4
    assert k.get_required_environment() == "forest"

def test_animal_invalid_age():
    error_raised = False
    try:
        Koala("BadKoala", -1)
    except ValueError:
        error_raised = True
    assert error_raised is True

def test_add_health_record_and_active_issue():
    k = Koala("Koko", 4)
    r = HealthRecord("Paw injury", 3)

    k.add_health_record(r)
    assert k.has_active_health_issue() is True
    assert len(k.get_health_records()) == 1

def test_get_unresolved_records_only():
    k = Koala("Koko", 4)
    r1 = HealthRecord("Injury", 3)
    r2 = HealthRecord("Cold", 2)

    k.add_health_record(r1)
    k.add_health_record(r2)

    r1.mark_resolved()
    unresolved = k.get_health_records(include_resolved=False)

    assert len(unresolved) == 1
    assert unresolved[0].description == "Cold"

def test_latest_health_issue():
    k = Koala("Koko", 4)
    r1 = HealthRecord("Injury", 3)
    r2 = HealthRecord("Cold", 2)

    k.add_health_record(r1)
    k.add_health_record(r2)
    r1.mark_resolved()

    latest = k.latest_health_issue()
    assert latest.description == "Cold"

def test_make_sound_polymorphism():
    k = Koala("Koko", 4)
    p = Penguin("Pingu", 3)
    s = Snake("Sly", 5)
    assert "grunts" in k.make_sound()
    assert "squawks" in p.make_sound()
    assert "hisses" in s.make_sound()
