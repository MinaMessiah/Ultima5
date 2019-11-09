'''
This module contains all character related functions
and also items, reagents, armaments, spells, & equipment
'''

import binascii

import OffsetDict
import FileUtility

# Read the contents of the "SAVED.GAM" file
file = FileUtility.read_file()
SEPARATOR = "________________________________"


# A function that validates the character name
def name_check(name):
    if name.isalpha() and len(name) <= 9: return True
    else: return False


# A function that reads the character name
def read_name(rng):
    rng = [int(n) for n in rng.split("-")]
    name = file[rng[0]:rng[1]]
    name = b''.join(name)
    name = binascii.unhexlify(name).decode()
    return name


# A function that edits the character name
def edit_name(new_name, rng):
    rng = [int(n) for n in rng.split("-")]
    new_name = binascii.hexlify(new_name.encode())
    new_name = new_name.ljust(20, b'0')
    new_name = [(new_name[i:i + 2]) for i in range(0, len(new_name), 2)]
    FileUtility.change_value(new_name, rng, value_flag=1)


# A function that reads an attribute that is 8 bits or less
def read_single_attr(rng):
    attr = str(int(file[int(rng)], 16))
    return attr


# A function that edits an attribute that is 8 bits or less
def edit_single_attr(new_attr, rng):
    rng = int(rng)
    new_attr = hex(int(new_attr)).split('x')
    new_attr = new_attr[1].encode().zfill(2)
    FileUtility.change_value(new_attr, rng)


# A function that reads an attribute that is 16 to 8 bits
def read_double_attr(rng):
    rng = [int(n) for n in rng.split("-")]
    remainder = file[rng[0]]
    multiplier = file[rng[1]]
    attr = (int(multiplier, 16) * 256) + int(remainder, 16)
    attr = str(attr)
    return attr


# A function that edits an attribute that is 16 to 8 bits
def edit_double_attr(new_attr, rng):
    rng = [int(n) for n in rng.split("-")]
    remainder = new_attr % 256
    multiplier = new_attr // 256
    new_attr = remainder + (256 * multiplier)
    new_attr = hex(new_attr).encode().split(b'x')
    new_attr = new_attr[1].zfill(4)
    new_attr = [(new_attr[i:i + 2]) for i in range(0, len(new_attr), 2)]
    FileUtility.change_value(new_attr, rng)


# A function that returns the names of all characters
def get_all_characters():
    character_names = []
    for character in OffsetDict.Characters[0:-1]:
        for k, v in character.items():
            if k == "Name":
                character_names.append(read_name(v))
    return character_names


# A function that reads a character attributes given its number
def read_character_attr(char_number):
    for k, v in OffsetDict.Characters[char_number-1].items():
        if k == "Name":
            v = read_name(v)
        elif v.find("-") > 0:
            v = read_double_attr(v)
        else:
            v = read_single_attr(v)
        print(k + " = " + v)
    print(SEPARATOR)


# A function that edits a character attributes given its number and the new attributes
def edit_character_attr(char_number, new_attrs):
    for k, v in OffsetDict.Characters[char_number-1].items():
        if k == "Name":
            if k in new_attrs.keys(): edit_name(new_attrs["Name"], v)
            else: continue
        elif v.find("-") > 0:
            edit_double_attr(new_attrs[k], v)
        else:
            edit_single_attr(new_attrs[k], v)


# A function that reads a character attributes into a dictionary given its number
def read_character_dict(char_number):
    new_dict = dict()
    for k, v in OffsetDict.Characters[char_number-1].items():
        if k == "Name":
            new_dict[k] = read_name(v)
        elif v.find("-") > 0:
            new_dict[k] = int(read_double_attr(v))
        else:
            new_dict[k] = int(read_single_attr(v))
    return new_dict


# A function that reads all characters attributes
def read_all_character_attr():
    for i in range(1, len(OffsetDict.Characters)-1):
        read_character_attr(i)


# A function that edits all characters attributes
def edit_all_character_attr(new_attrs):
    for i in range(1, len(OffsetDict.Characters[0:-1])):
        edit_character_attr(i, new_attrs)


# A function that prints the names of the enabled characters in their order
def read_enabled_characters():
    num_of_characters_enabled = int(read_single_attr(OffsetDict.Characters[-1]))
    all_characters = get_all_characters()
    print("The following {} characters are enabled:".format(num_of_characters_enabled))
    for i in range(num_of_characters_enabled):
        print("{}. {}".format(i+1, all_characters[i]))


# A function that changes the number of the enabled characters
def edit_enabled_characters(new_num):
    num_of_characters_enabled = int(read_single_attr(OffsetDict.Characters[-1]))
    if num_of_characters_enabled == new_num:
        print("Number of enabled characters is already set to {}".format(num_of_characters_enabled))
        raise ValueError
    edit_single_attr(new_num, OffsetDict.Characters[-1])
    print("Changing number of enabled characters from {} to {}".format(num_of_characters_enabled, new_num))


# A function that swaps the position of the characters
def swap_enabled_characters():
    positions_used = []
    for i in range(1,17):
        if i in positions_used: continue
        while 1:
            try:
                order = validate_choice(int(input("Enter character number for position {}: ".format(i))), 16)[0]
                if not order: raise ValueError
                if order in positions_used: raise FileExistsError
                else: positions_used.append(order)
                temp = read_character_dict(i)
                ordr = read_character_dict(order)

                edit_character_attr(i, ordr)
                edit_character_attr(order, temp)

                print("Character {} swapped with character {}".format(order, i))
                break
            except ValueError: print("Unknown character number. Enter a value between 1-16")
            except FileExistsError: print("Player at position {} already swapped".format(order))


# A function that reads the equipment
def read_equipment():
    for k, v in OffsetDict.Equipment.items():
        if v.find("-") > 0:
            v = read_double_attr(v)
        else:
            v = read_single_attr(v)
        print(k + " = " + v)


# A function that edits the equipment
def edit_equipment(new_equipment_dict):
    for k, v in OffsetDict.Equipment.items():
        if v.find("-") > 0:
            edit_double_attr(new_equipment_dict[k], v)
        else:
            edit_single_attr(new_equipment_dict[k], v)


# A function that reads the items
def read_items():
    for k, v in OffsetDict.Items.items():
        v = read_single_attr(v)
        print(k + " = " + v)


# A function that edits the items
def edit_items(new_items):
    for k, v in OffsetDict.Items.items():
        edit_single_attr(new_items[k], v)


# A function that reads the reagents
def read_reagents():
    for k, v in OffsetDict.Reagents.items():
        v = read_single_attr(v)
        print(k + " = " + v)


# A function that edits the equipment
def edit_reagents(new_reagents):
    for k, v in OffsetDict.Reagents.items():
        edit_single_attr(new_reagents[k], v)


# A function that reads the armaments
def read_armaments():
    for k, v in OffsetDict.Armaments.items():
        v = read_single_attr(v)
        print(k + " = " + v)


# A function that edits the equipment
def edit_armaments(new_armaments):
    for k, v in OffsetDict.Armaments.items():
        edit_single_attr(new_armaments[k], v)


# A function that reads the spells
def read_spells():
    for k, v in OffsetDict.Spells.items():
        v = read_single_attr(v)
        print(k + " = " + v)


# A function that edits the spells
def edit_spells(new_spells):
    for k, v in OffsetDict.Spells.items():
        edit_single_attr(new_spells[k], v)


# A function that reads the assignment required values
def read_assignment_values():
    for k, v in OffsetDict.Assignment.items():
        v = read_single_attr(v)
        print(k + " = " + v)


# A function that edits the assignment required values
def edit_assignment_values(new_attrs):
    for k, v in OffsetDict.Assignment.items():
        edit_single_attr(new_attrs[k], v)


# A function that prints the character names
def print_character_names():
    character_list = get_all_characters()
    for i in range(len(character_list)):
        print("{0}. {1}".format(i+1, character_list[i]))


# A function that builds a new attributes dictionary from user input and validates it
def build_new_attrs_dict(all=1):
    new_attrs = dict()
    if all > 0:
        while 1:
            name = input("Enter new name: ")
            if name_check(name):
                new_attrs["Name"] = name
                break
            else: print("Name shouldn't exceed 8 characters and should contain only letters")

    new_attrs["Str"] = validate_choice(int(input("Enter new str value (0-99): ")), 99)[0]
    new_attrs["Int"] = validate_choice(int(input("Enter new int value (0-99): ")), 99)[0]
    new_attrs["Dex"] = validate_choice(int(input("Enter new dex value (0-99): ")), 99)[0]
    new_attrs["HP"] = validate_choice(int(input("Enter new HP value (0-999): ")), 999)[0]
    new_attrs["HM"] = validate_choice(int(input("Enter new HM value (0-999): ")), 999)[0]
    new_attrs["Ex"] = validate_choice(int(input("Enter new exp value (0-9999): ")), 9999)[0]
    new_attrs["Magic"] = validate_choice(int(input("Enter new magic value (0-99): ")), 99)[0]
    return new_attrs


# A function that builds a new attributes dictionary from user input and validates it
def build_new_equipment_dict():
    new_eqp = dict()
    new_eqp["Food"] = validate_choice(int(input("Enter new food value (0-9999): ")), 9999)[0]
    new_eqp["Gold"] = validate_choice(int(input("Enter new gold value (0-9999): ")), 9999)[0]
    new_eqp["Keys"] = validate_choice(int(input("Enter new keys value (0-99): ")), 99)[0]
    new_eqp["Gems"] = validate_choice(int(input("Enter new gems value (0-99): ")), 99)[0]
    new_eqp["Torches"] = validate_choice(int(input("Enter new torches value (0-99): ")), 99)[0]
    return new_eqp


# A function that builds a new items dictionary from user input and validates it
def build_new_items_dict():
    new_items = dict()
    for k, v in OffsetDict.Items.items():
        new_items[k] = validate_choice(int(input("Enter new {} value (0-99): ".format(k.lower()))), 99)[0]
    return new_items


# A function that builds a new reagents dictionary from user input and validates it
def build_new_reagents_dict():
    new_reagents = dict()
    for k, v in OffsetDict.Reagents.items():
        new_reagents[k] = validate_choice(int(input("Enter new {} value (0-99): ".format(k.lower()))), 99)[0]
    return new_reagents


# A function that builds a new armaments dictionary from user input and validates it
def build_new_armaments_dict():
    new_armaments = dict()
    for k, v in OffsetDict.Armaments.items():
        new_armaments[k] = validate_choice(int(input("Enter new {} value (0-99): ".format(k.lower()))), 99)[0]
    return new_armaments


# A function that builds a new spells dictionary from user input and validates it
def build_new_spells_dict():
    new_spells = dict()
    for k, v in OffsetDict.Spells.items():
        new_spells[k] = validate_choice(int(input("Enter new {} value (0-99): ".format(k.lower()))), 99)[0]
    return new_spells


# A function that builds a new dictionary for the assignment required values from user input and validates it
def build_new_assignment_dict():
    new_assg = dict()
    new_assg["Keys"] = validate_choice(int(input("Enter new keys value (0-100): ")), 100)[0]
    new_assg["Skull Keys"] = validate_choice(int(input("Enter new skull keys value (0-100): ")), 100)[0]
    new_assg["Gems"] = validate_choice(int(input("Enter new gems value (0-100): ")), 100)[0]
    new_assg["Black Badge"] = validate_choice(int(input("Enter new black badge value (0-100): ")), 100)[0]
    new_assg["Magic Carpet"] = validate_choice(int(input("Enter new magic carpet value (0-100): ")), 100)[0]
    new_assg["Magic Axe"] = validate_choice(int(input("Enter new magic axe value (0-100): ")), 100)[0]
    return new_assg


# A function that validates the choice from the user input
def validate_choice(choice, bound, save=False):
    try:
        choice = int(choice)
        if choice not in range(0, bound + 1): raise ValueError
    except ValueError:
        if isinstance(choice, str) and choice.upper() == 'S' and bound <= 11:
            FileUtility.write_file()
            save = True
            print("File Saved")
        elif isinstance(choice, str) and bound > 50:
            print("Non-numeric value entered")
            raise ValueError
        elif isinstance(choice, int) and choice > bound:
            print("Value entered is out of bounds")
            raise ValueError
        else:
            print("Unknown command")
            return -1, save
    return choice, save
