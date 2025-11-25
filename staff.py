'''
File: staff.py
Description: Defines ZooKeeper and Veterinarian staff roles for the Zoo Management System.
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''



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

    # ----- Assignments -----
    def assign_animal(self, animal):
        # Accept Animal and all subclasses
        if not is_animal_object(animal):
            raise ValueError("Assigned object must be an Animal.")
        self.__assigned_animals.append(animal)

    def assign_enclosure(self, enclosure):
        if type(enclosure) != Enclosure:
            raise ValueError("Assigned object must be an Enclosure.")
        self.__assigned_enclosures.append(enclosure)
