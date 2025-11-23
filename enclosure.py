'''
File: enclosure.py
Description:  Defines Enclosure class for the Zoo Management System.
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''


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
