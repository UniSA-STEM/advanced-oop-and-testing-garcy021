'''
File: enclosure.py
Description:  Defines Enclosure class for the Zoo Management System.
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal


class Enclosure:

    def __init__(self, name, environment_type, size, cleanliness_level=100):
        # basic validation
        if type(name) != str or not name.strip():
            raise ValueError("Enclosure name must be a non-empty string.")
        if type(environment_type) != str or not environment_type.strip():
            raise ValueError("environment_type must be a non-empty string.")
        if type(size) != int or size <= 0:
            raise ValueError("size must be a positive integer.")
        if type(cleanliness_level) != int or cleanliness_level < 0 or cleanliness_level > 100:
            raise ValueError("cleanliness_level must be an int between 0 and 100.")

        self.__name = name.strip()
        self.__environment_type = environment_type.strip().lower()
        self.__size = size
        self.__cleanliness_level = cleanliness_level

        self.__animals = []
        self.__allowed_species = None  # set when first animal is added

    # Getters
    def get_name(self):
        return self.__name

    def get_environment_type(self):
        return self.__environment_type

    def get_size(self):
        return self.__size

    def get_cleanliness_level(self):
        return self.__cleanliness_level

    def get_allowed_species(self):
        return self.__allowed_species

    # -------------------------
    # Core Enclosure Behaviours
    # -------------------------
    def add_animal(self, animal):
        # Ensure it's an Animal object (basic safe check)
        if type(animal) == str or animal is None:
            raise ValueError("animal must be a valid Animal object.")

        # Capacity check
        if len(self.__animals) >= self.__size:
            raise ValueError("Enclosure is full.")

        # Under treatment check (assignment rule)
        if animal.has_active_health_issue():
            raise ValueError("Cannot move animal: under treatment.")

        # Environment compatibility check
        if animal.get_required_environment() != self.__environment_type:
            raise ValueError(
                f"{animal.get_name()} cannot be placed in a {self.__environment_type} enclosure."
            )

        # Single-species rule
        if self.__allowed_species is None:
            self.__allowed_species = animal.get_species()
        else:
            if animal.get_species() != self.__allowed_species:
                raise ValueError(
                    f"Incompatible species. This enclosure is for {self.__allowed_species} only."
                )

        self.__animals.append(animal)

    def remove_animal(self, animal):
        """Removes an animal from enclosure."""
        if animal not in self.__animals:
            raise ValueError("Animal not found in enclosure.")
        self.__animals.remove(animal)

        # If empty, reset allowed species
        if len(self.__animals) == 0:
            self.__allowed_species = None

    def list_animals(self):
        """Returns a list of animal names inside this enclosure."""
        names = []
        for a in self.__animals:
            names.append(a.get_name())
        return names

    def report_status(self):
        """Returns a short status report."""
        species_text = self.__allowed_species if self.__allowed_species else "None"
        return (
            f"Enclosure '{self.__name}' | env={self.__environment_type} | "
            f"species={species_text} | animals={len(self.__animals)}/{self.__size} | "
            f"cleanliness={self.__cleanliness_level}%"
        )
