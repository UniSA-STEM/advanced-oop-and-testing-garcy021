'''
File: animal.py
Description:  Defines Animal hierarchy and HealthRecord system for the Zoo Management System.
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC,
from datetime import date

# HealthRecord Class
class HealthRecord:
    """
    Represents a health issue for an animal.
    """

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

    def mark_resolved(self, notes=""):
        """Marks the issue as resolved."""
        self.resolved = True
        if notes:
            if self.notes:
                self.notes = self.notes + "\n" + notes
            else:
                self.notes = notes

    def __str__(self):
        status = "Resolved" if self.resolved else "Active"
        return f"[{status}] {self.description} | severity={self.severity} | reported={self.date_reported}"

# Animal
class Animal(ABC):
    """
    Abstract Animal class with fully encapsulated attributes.
    """

    def __init__(self, name, species, age, dietary_needs, required_environment):
        self.__validate_str(name, "name")
        self.__validate_str(species, "species")
        self.__validate_str(dietary_needs, "dietary_needs")
        self.__validate_str(required_environment, "required_environment")

        if type(age) != int or age < 0:
            raise ValueError("age must be a non-negative integer.")

        self.__name = name.strip()
        self.__species = species.strip()
        self.__age = age
        self.__dietary_needs = dietary_needs.strip()
        self.__required_environment = required_environment.strip().lower()

        self.__health_records = []


    # Validation
    def __validate_str(self, value, field):
        """Ensures a string value is non-empty."""
        if type(value) != str or not value.strip():
            raise ValueError(field + " must be a non-empty string.")