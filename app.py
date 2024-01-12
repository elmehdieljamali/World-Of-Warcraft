import database
import sqlite3
import subprocess
import main

MENU_PROMPT = """ Welcome to World Of Warcraft!

Please choose an option to start the game
1) Insert a character.
2) Insert an arm.
3) Insert a shield.
4) Insert food.
5) View all characters.
6) View all arms.
7) View all shields.
8) View all food.
9) Start the Game.
10) Exit the Game.
"""
def phrase_generator(choice):
    if choice == "1":
        return "Character added successfully."
    elif choice == "2":
        return "Arm added successfully."
    elif choice == "3":
        return "Shield added successfully."
    elif choice == "4":
        return "Food added successfully."
    elif choice == "5":
        return "Viewing all characters."
    elif choice == "6":
        return "Viewing all arms."
    elif choice == "7":
        return "Viewing all shields."
    elif choice == "8":
        return "Viewing all food."
    elif choice == "9":
        return "Starting the game."
    elif choice == "10":
        return "Exiting the game."
    else:
        return "Unknown choice. Please try again."

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "10":

        if user_input == "1":
            print(phrase_generator(user_input))
            name = input("Enter character name: ")
            life_score = int(input("Enter the life score: "))
            arm = input("Enter arm name: ")
            type = input("Enter type name: ")

            database.add_character(connection, (name, life_score, arm, type))
            print("Character added successfully")

        elif user_input == "2":
            print(phrase_generator(user_input))
            name = input("Enter arm name: ")
            power = int(input("Enter the arm power points: "))
            length = int(input("Enter arm length: "))
            weight = int(input("Enter type weight: "))

            database.add_arm(connection, (name, power, length, weight))
            print("Arm added successfully")

        elif user_input == "3":
            print(phrase_generator(user_input))
            name = input("Enter shield name: ")
            defense_power = int(input("Enter the shield defense power: "))
            weight = int(input("Enter shield weight: "))

            database.add_shield(connection, (name, defense_power, weight))
            print("Shield added successfully")

        elif user_input == "4":
            print(phrase_generator(user_input))
            name = input("Enter food name: ")
            life_score = int(input("Enter the food life score: "))
            energy_points = int(input("Enter food energy points: "))
            weight = int(input("Enter food weight: "))

            database.add_food(connection, (name, life_score, energy_points, weight))
            print("Food added successfully")

        elif user_input == "5":
            print(phrase_generator(user_input))
            row = database.select_all_characters(connection)
            for line in row:
                print(line)

        elif user_input == "6":
            print(phrase_generator(user_input))
            row = database.select_all_arms(connection)
            for line in row:
                print(line)

        elif user_input == "7":
            print(phrase_generator(user_input))
            row = database.select_all_shields(connection)
            for line in row:
                print(line)

        elif user_input == "8":
            print(phrase_generator(user_input))
            row = database.select_all_food(connection)
            for line in row:
                print(line)

        elif user_input == "9":
            print(phrase_generator(user_input))
            subprocess.run(["python", "main.py"])

        else:
            print("Your request is unknown, please try again")

menu()
