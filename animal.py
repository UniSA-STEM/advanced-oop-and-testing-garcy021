'''
File: animal.py
Description: Defines Animal hierarchy and HealthRecord system for the Zoo Management System.
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod
from datetime import date


#Stores description, severity, treatment, notes, and resolution status.
# HealthRecord Class
class HealthRecord:

    def __init__(self, description, severity, treatment_plan="", notes=""):
        if type(description) != str or not description.strip():
            raise ValueError("HealthRecord description must be a non-empty string.")

        if type(severity) != int or severity < 1 or severity > 5:
            raise ValueError("Severity must be an integer between 1 and 5.")

        self.description = description.strip()
        self.severity = severity
        self.treatment_plan = treatment_plan.strip()
        self.notes = notes.strip()
        self.date_reported = date.today()
        self.resolved = False

# Marks the issue as resolved and optionally appends extra notes.
    def mark_resolved(self, notes=""):
        """Marks the issue as resolved."""
        self.resolved = True
        if notes:
            if self.notes:
                self.notes = self.notes + "\n" + notes
            else:
                self.notes = notes

# Returns a short text summary of this health record.
    def __str__(self):
        status = "Resolved" if self.resolved else "Active"
        return f"[{status}] {self.description} | severity={self.severity} | reported={self.date_reported}"


# ABSTRACT Animal Class
class Animal(ABC):

    def __init__(self, name, species, age, dietary_needs, required_environment):
        # Validation
        if type(name) != str or not name.strip():
            raise ValueError("name must be a non-empty string.")
        if type(species) != str or not species.strip():
            raise ValueError("species must be a non-empty string.")
        if type(dietary_needs) != str or not dietary_needs.strip():
            raise ValueError("dietary_needs must be a non-empty string.")
        if type(required_environment) != str or not required_environment.strip():
            raise ValueError("required_environment must be a non-empty string.")
        if type(age) != int or age < 0:
            raise ValueError("age must be a non-negative integer.")

        self.__name = name.strip()
        self.__species = species.strip()
        self.__age = age
        self.__dietary_needs = dietary_needs.strip()
        self.__required_environment = required_environment.strip().lower()
        self.__health_records = []

    # Encapsulated Getters
    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_dietary_needs(self):
        return self.__dietary_needs

    def get_required_environment(self):
        return self.__required_environment

    # Health Management
# Adds a HealthRecord to this animal.
    def add_health_record(self, record):
        if type(record) != HealthRecord:
            raise ValueError("record must be a HealthRecord instance.")
        self.__health_records.append(record)

#Returns a list of health records.
    def get_health_records(self, include_resolved=True):
        if include_resolved:
            return list(self.__health_records)

        unresolved = []
        for r in self.__health_records:
            if not r.resolved:
                unresolved.append(r)
        return unresolved

    def has_active_health_issue(self):
        for r in self.__health_records:
            if not r.resolved:
                return True
        return False

    def latest_health_issue(self):
        last = None
        for r in self.__health_records:
            if not r.resolved:
                last = r
        return last

    # Shared Behaviours
    def eat(self):
        return f"{self.__name} the {self.__species} is eating ({self.__dietary_needs})."

    def sleep(self):
        return f"{self.__name} the {self.__species} is sleeping."

    # Abstract Method (polymorphism)
    @abstractmethod
    def make_sound(self):
        pass

    def __str__(self):
        status = "UNDER TREATMENT" if self.has_active_health_issue() else "Healthy"
        return f"{self.__name} ({self.__species}), age {self.__age}, env={self.__required_environment}, status={status}"


# Category Classes
class Mammal(Animal):
    category = "mammal"

class Bird(Animal):
    category = "bird"

class Reptile(Animal):
    category = "reptile"

# These DO NOT restrict the zoo.
class Koala(Mammal):
    def __init__(self, name, age):
        super().__init__(name, "Koala", age, "Eucalyptus leaves", "forest")

    def make_sound(self):
        return self.get_name() + " grunts softly."

class Penguin(Bird):
    def __init__(self, name, age):
        super().__init__(name, "Penguin", age, "Fish", "aquatic")

    def make_sound(self):
        return self.get_name() + " squawks loudly."

class Snake(Reptile):
    def __init__(self, name, age):
        super().__init__(name, "Snake", age, "Rodents", "desert")

    def make_sound(self):
        return self.get_name() + " hisses."
