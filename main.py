'''
File: main.py
Description: It shows how main system works.
Author: Chirag Garg
ID: 110395864
Username: garcy021
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Koala, Penguin, Snake
from enclosure import Enclosure
from staff import ZooKeeper, Veterinarian

def print_heading(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

def main():
    # 1) Create Animals
    print_heading("1) Creating Animals")

    koala1 = Koala("Koko", 4)
    koala2 = Koala("Luna", 2)
    penguin1 = Penguin("Pingu", 3)
    snake1 = Snake("Sly", 5)

    print(koala1)
    print(koala2)
    print(penguin1)
    print(snake1)

    print(koala1.make_sound())
    print(penguin1.make_sound())
    print(snake1.make_sound())

    # 2) Create Enclosures
    print_heading("2) Creating Enclosures")

    forest_enclosure = Enclosure("Forest Zone", "forest", 2)
    aquatic_enclosure = Enclosure("Aquatic Zone", "aquatic", 3)
    desert_enclosure = Enclosure("Desert Zone", "desert", 1)

    print(forest_enclosure.report_status())
    print(aquatic_enclosure.report_status())
    print(desert_enclosure.report_status())

    # 3) Add animals to enclosures
    print_heading("3) Adding Animals to Enclosures")

    forest_enclosure.add_animal(koala1)
    forest_enclosure.add_animal(koala2)
    aquatic_enclosure.add_animal(penguin1)
    desert_enclosure.add_animal(snake1)

    print(forest_enclosure.report_status())
    print("Forest animals:", forest_enclosure.list_animals())

    print(aquatic_enclosure.report_status())
    print("Aquatic animals:", aquatic_enclosure.list_animals())

    print(desert_enclosure.report_status())
    print("Desert animals:", desert_enclosure.list_animals())

    print("\nTrying to add penguin to forest enclosure (should fail):")
    try:
        forest_enclosure.add_animal(penguin1)
    except ValueError as e:
        print("Error:", e)

    # 4) Create Staff
    print_heading("4) Creating Staff")

    keeper = ZooKeeper("Ava")
    vet = Veterinarian("Dr Sam")

    print("Keeper:", keeper.get_name(), "-", keeper.get_role())
    print("Vet:", vet.get_name(), "-", vet.get_role())

    # 5) Assign staff
    print_heading("5) Assigning Staff")

    keeper.assign_enclosure(forest_enclosure)
    keeper.assign_enclosure(aquatic_enclosure)

    keeper.assign_animal(koala1)
    keeper.assign_animal(koala2)
    keeper.assign_animal(penguin1)

    vet.assign_animal(koala1)
    vet.assign_animal(snake1)

    print("Keeper assigned enclosures:")
    for e in keeper.get_assigned_enclosures():
        print(" -", e.get_name())

    print("Keeper assigned animals:")
    for a in keeper.get_assigned_animals():
        print(" -", a.get_name())

    print("Vet assigned animals:")
    for a in vet.get_assigned_animals():
        print(" -", a.get_name())

    # 6) Daily routine
    print_heading("6) Daily Routine Demo")

    print("Feeding animals:")
    for a in keeper.get_assigned_animals():
        print(keeper.feed_animal(a))

    print("\nSoiling and cleaning enclosures:")
    forest_enclosure.soil(30)
    aquatic_enclosure.soil(50)

    print(forest_enclosure.report_status())
    print(aquatic_enclosure.report_status())

    print(keeper.clean_enclosure(forest_enclosure))
    print(keeper.clean_enclosure(aquatic_enclosure))

    print(forest_enclosure.report_status())
    print(aquatic_enclosure.report_status())

    # 7) Health system
    print_heading("7) Health System Demo")

    print("Vet checks koala1:")
    print(vet.perform_health_check(koala1, "Scratched paw", 3, "Rest and ointment"))

    # Create a second forest enclosure (empty) for movement demo
    forest_enclosure_2 = Enclosure("Forest Zone 2", "forest", 2)

    print("\nTrying to move koala1 to another forest enclosure while under treatment:")
    try:
        forest_enclosure_2.add_animal(koala1)
    except ValueError as e:
        print("Error:", e)

    print("\nVet resolves issue:")
    print(vet.mark_resolved(koala1, "Healed well."))

    print("\nTrying to move koala1 again after treatment:")
    try:
        forest_enclosure_2.add_animal(koala1)
        print("Move successful.")
    except ValueError as e:
        print("Error:", e)

    # 8) Reports
    print_heading("8) Final Enclosure Reports")

    print(forest_enclosure.report_status())
    print(aquatic_enclosure.report_status())
    print(desert_enclosure.report_status())

main()
