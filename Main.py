'''
The main script that contains the CLI of the program
'''

import CharacterUtility as CU

SEPARATOR = "_____________________________________________________________________________________"
save_status = True

print("Welcome to Ultima 5 Hacking Tool. Select one of the following options:")

# Enter main loop
while 1:
    # Display menu
    print(SEPARATOR)
    print("1. View current characters stats")
    print("2. Edit characters stats")
    print("3. View assignment required values")
    print("4. Edit assignment required values")
    print("5. More options")
    print("0. Exit")
    print("S. Save")

    # User input validation
    try: choice, save_status = CU.validate_choice(input(), 5, save=save_status)
    except ValueError: continue

    # User selects to exit
    if choice == 0:
        # Checks if file is saved before exiting
        if save_status: break
        else:
            print("WARNING: Changes not saved. Exit again to force exit.")
            save_status = True

    # User selects to view characters
    elif choice == 1:
        # Prints menu with all character names and options
        print("Select the desired character")
        CU.print_character_names()
        print("Or enter 0 to view all characters")

        # Reads the character attributes
        choice = int(input())
        if choice: CU.read_character_attr(choice)
        else: CU.read_all_character_attr()

    # User selects to edit characters
    elif choice == 2:
        # Prints menu with all character names and options
        print("Select the desired character")
        CU.print_character_names()
        print("Or enter 0 to edit all characters (Note: All characters will have the same stats)")

        # Validates user selection
        try:
            choice = int(input())
            new_attrs = CU.build_new_attrs_dict(all=choice)
        except ValueError:
            continue

        # Edits the character attributes
        if choice: CU.edit_character_attr(choice, new_attrs)
        else: CU.edit_all_character_attr(new_attrs)
        save_status = False

    # User selects to view values required for the assignment
    elif choice == 3:
        print("Current assignment required values:")
        # Reads the values required for the assignment
        CU.read_assignment_values()

    # User selects to edit values required for the assignment
    elif choice == 4:
        # Prompts user for new values and validates them
        try: new_attrs = CU.build_new_assignment_dict()
        except ValueError: continue
        # Edits the values required for the assignment
        CU.edit_assignment_values(new_attrs)
        save_status = False

    # User selects the "More options" from the main menu
    elif choice == 5:
        # Prints the "More options" menu
        while 1:
            print(SEPARATOR)
            print("1. View current items")
            print("2. Edit items")
            print("3. View current reagents")
            print("4. Edit reagents")
            print("5. View current spells")
            print("6. Edit spells")
            print("7. View current equipment")
            print("8. Edit equipment")
            print("9. View enabled characters")
            print("10. Edit enabled characters")
            print("11. Swap enabled characters")
            print("0. Main menu")
            print("S. Save")

            # User input validation
            try: choice, save_status = CU.validate_choice(input(), 11, save=save_status)
            except ValueError: continue

            # Returns to "Main Menu" if user entered 0
            if choice == 0: break

            # User selects to view currents items
            elif choice == 1:
                print("Current items values:")
                # Prints current items and their values
                CU.read_items()

            # User selects to edit current items
            elif choice == 2:
                # Prompts user for new items values and validates them
                try: new_items = CU.build_new_items_dict()
                except ValueError: continue
                # Edits the items and their values
                CU.edit_items(new_items)
                save_status = False

            # User selects to view reagents items
            elif choice == 3:
                print("Current reagents values:")
                # Prints current reagents and their values
                CU.read_reagents()

            # User selects to edit current reagents
            elif choice == 4:
                # Prompts user for new items reagents and validates them
                try: new_reagents = CU.build_new_reagents_dict()
                except ValueError: continue
                # Edits the reagents and their values
                CU.edit_reagents(new_reagents)
                save_status = False

            # User selects to view spells items
            elif choice == 5:
                print("Current spells values:")
                # Prints current spells and their values
                CU.read_spells()

            # User selects to edit current spells
            elif choice == 6:
                # Prompts user for new items spells and validates them
                try: new_spells = CU.build_new_spells_dict()
                except ValueError: continue
                # Edits the spells and their values
                CU.edit_spells(new_spells)
                save_status = False

            # User selects to view equipment items
            elif choice == 7:
                print("Current equipment values:")
                # Prints current equipment and their values
                CU.read_equipment()

            # User selects to edit current equipment
            elif choice == 8:
                # Prompts user for new items equipment and validates them
                try: new_eqp = CU.build_new_equipment_dict()
                except ValueError: continue
                # Edits the equipment and their values
                CU.edit_equipment(new_eqp)
                save_status = False

            # User selects to view the enabled characters
            elif choice == 9:
                # Prints a list of enabled characters
                CU.read_enabled_characters()

            # User selects to change the number of enabled characters
            elif choice == 10:
                # Prompts user for number of characters to be enabled
                try:
                    num_of_enabled_chars = CU.validate_choice(input("Enter number of characters to be enabled (1-16): "), 16)[0]
                    if num_of_enabled_chars <= 0:
                        print("Value entered is out of bounds")
                        raise ValueError
                except ValueError: continue
                try: 
                    CU.edit_enabled_characters(num_of_enabled_chars)
                    save_status = False
                except ValueError: continue

            # User selects to change characters order
            elif choice == 11:
                # Prints all character names and their positions
                print("Current character order: ")
                CU.print_character_names()
                # Changes the character positions
                CU.swap_enabled_characters()
                save_status = False

    else: continue
