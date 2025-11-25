'''
File: staff.py
Description: Defines ZooKeeper and Veterinarian staff roles for the Zoo Management System.
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal, HealthRecord
from enclosure import Enclosure

# Helper: Detect Animal subclasses
#Returns True if obj is an instance of Animal or a subclass of Animal, using only type() and __bases__ (no isinstance()).
def is_animal_object(obj):
    current_class = type(obj)

    while current_class != object:
        if current_class == Animal:
            return True

        bases = current_class.__bases__
        if len(bases) == 0:
            current_class = object
        else:
            current_class = bases[0]

    return False

# Base Staff Class
class Staff:

    def __init__(self, name, role):
        if type(name) != str or not name.strip():
            raise ValueError("Staff name must be a non-empty string.")
        if type(role) != str or not role.strip():
            raise ValueError("role must be a non-empty string.")

        self.__name = name.strip()
        self.__role = role.strip()
        self.__assigned_animals = []
        self.__assigned_enclosures = []

    # ----- Getters -----
    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def get_assigned_animals(self):
        return list(self.__assigned_animals)

    def get_assigned_enclosures(self):
        return list(self.__assigned_enclosures)


    def assign_animal(self, animal):
        # Accept Animal and all subclasses
        if not is_animal_object(animal):
            raise ValueError("Assigned object must be an Animal.")
        self.__assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        if type(enclosure) != Enclosure:
            raise ValueError("Assigned object must be an Enclosure.")
        self.__assigned_enclosures.append(enclosure)

# ZooKeeper Role
class ZooKeeper(Staff):

    def __init__(self, name):
        super().__init__(name, "ZooKeeper")

    def feed_animal(self, animal):
        if animal not in self.get_assigned_animals():
            raise ValueError("ZooKeeper cannot feed unassigned animal.")
        return animal.eat()

    def clean_enclosure(self, enclosure):
        if enclosure not in self.get_assigned_enclosures():
            raise ValueError("ZooKeeper cannot clean unassigned enclosure.")
        enclosure.clean()
        return f"{self.get_name()} cleaned enclosure {enclosure.get_name()}."

# Veterinarian Role
#   Veterinarian staff member
class Veterinarian(Staff):

    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def perform_health_check(self, animal, description, severity, treatment=""):
        if animal not in self.get_assigned_animals():
            raise ValueError("Veterinarian cannot check an unassigned animal.")

        record = HealthRecord(description, severity, treatment)
        animal.add_health_record(record)
        return f"{self.get_name()} recorded a health issue for {animal.get_name()}."

    def mark_resolved(self, animal, notes=""):
        if animal not in self.get_assigned_animals():
            raise ValueError("Veterinarian cannot update unassigned animal.")

        issue = animal.latest_health_issue()
        if issue is None:
            raise ValueError("Animal has no active health issues.")

        issue.mark_resolved(notes)
        return f"{self.get_name()} resolved health issue for {animal.get_name()}."