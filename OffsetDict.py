'''
This module contains the dictionary of attributes
and their corresponding offsets
'''


# A function that generates the offsets dictionary for all the characters
def build_characters_dict(char_dict):
    Characters = []
    for i in range(16):
        charDict = {}
        for attr, rng in Character.items():
            if rng.find("-"):
                nRng = rng.split("-")
                nRng = [str(int(x)+(32*i)) for x in nRng]
                nRng = "-".join(nRng)
                charDict[attr] = nRng
            else:
                nRng = str(int(rng)+(32*i))
                charDict[attr] = nRng
        Characters.append(charDict)
    Characters.append("693")
    return Characters


Character = { "Name":  "2-11", "Str":   "14", "Int":   "16", "Dex":   "15", 
        "HP":    "18-19", "HM":    "20-21", "Ex":    "22-23", "Magic": "17"}

# A list that contains a dictionary of attributes and their offsets for each character
Characters = build_characters_dict(Character)

# A dictionary that contains items and their corresponding offsets
Items = {
    "Item1":    "634",
    "Item2":    "635",
    "Item3":    "636",
    "Item4":    "637",
    "Item5":    "638",
    "Item6":    "639",
    "Item7":    "640",
    "Item8":    "641",
    "Blue":     "642",
    "Yellow":   "643",
    "Red":      "644",
    "Green":    "645",
    "Orange":   "646",
    "Purple":   "647",
    "Black":    "648",
    "White":    "649",
    "Magic Carpet": "672",
    "Skull Keys": "673",
    "Amulet": "674",
    "Crown": "675",
    "Spectre": "676",
    "Black Badge": "677"
}

# A dictionary that contains reagents and their corresponding offsets
Reagents = {
    "Sulfur Ash": "682",
    "Ginseng": "683",
    "Garlic": "684",
    "Sp. Silk": "685",
    "Blood Moss": "686",
    "Blk. Pearl": "687",
    "Nightshade": "688",
    "Mandrake": "689"
}

# A dictionary that contains armaments and their corresponding offsets
Armaments = {
    "Leath Helm": "538",
    "Chain Coif": "539",
    "Iron Helm": "540",
    "Spkd. Helm": "541",
    "Sm. Shield": "542",
    "Lg. Shield": "543",
    "Spkd. Shld": "544",
    "Mag. Shld": "545",
    "Jewel Shld": "546",
    "Cloth": "547",
    "Leather": "548",
    "Ring Mail": "549",
    "Scale": "550",
    "Chain": "551",
    "Plate": "552",
    "Myst. Armr": "553",
    "Dagger": "554",
    "Sling": "555",
    "Club": "556",
    "Flame Oil": "557",
    "Main Gauch": "558",
    "Spear": "559",
    "Thrwn Axe": "560",
    "Sht. Sword": "561",
    "Mace": "562",
    "Morn. Star": "563",
    "Bow": "564",
    "Arrows": "565",
    "Crossbow": "566",
    "Quarrels": "567",
    "Long Sword": "568",
    "2H Hammer": "569",
    "2H Axe": "570",
    "2H Sword": "571",
    "Halberd": "572",
    "Chaos Swrd": "573",
    "Magic Bow": "574",
    "Silver Swd": "575",
    "Magic Axe": "576",
    "Glass Swrd": "577",
    "Jewel Swrd": "578",
    "Myst. Swrd": "579",
    "Inv. Ring": "580",
    "Prot. Ring": "581",
    "Regen Ring": "582",
    "Am/Turning": "583",
    "Sp. Collar": "584",
    "Ankh": "585"
}

# A dictionary that contains spells and their corresponding offsets
Spells = {
    "In Lor": "586",
    "Grav Por": "587",
    "An Zi": "588",
    "An Nox": "589",
    "Mani": "590",
    "An Ylem": "591",
    "An Sanct": "592",
    "An Xen Cor": "593",
    "Rel Hur": "594",
    "In Wis": "595",
    "Kal Xen": "596",
    "In Xen Man": "597",
    "Vas Lor": "598",
    "Vas Flam": "599",
    "In Flam Gr": "600",
    "In Nox Gr": "601",
    "In Zu Grav": "602",
    "In Por": "603",
    "An Grav": "604",
    "In Sanct": "605",
    "In Sanct G": "606",
    "Uus Por": "607",
    "Des Por": "608",
    "Wis Quas": "609",
    "In Bet Xen": "610",
    "An Ex Por": "611",
    "In Ex Por": "612",
    "Vas Mani": "613",
    "In Zy": "614",
    "Rel Tym": "615",
    "In Vas P Y": "616",
    "Quas An Wi": "617",
    "In An": "618",
    "Wis An Yle": "619",
    "An Xen Ex": "620",
    "Rel Xen Be": "621",
    "Sanct Lo": "622",
    "Xen Corp": "623",
    "In Quas Xe": "624",
    "In Quas Wi": "625",
    "In Nox Hur": "626",
    "In Quas Co": "627",
    "In Mani Co": "628",
    "Kal Xen Co": "629",
    "In Vas G C": "630",
    "In Flam Hu": "631",
    "Vas Rel Po": "632",
    "An Tym": "633"
}

# A dictionary that contains equipment and their corresponding offsets
Equipment = {
    "Food": "514-515",
    "Gold": "516-517",
    "Keys": "518",
    "Gems": "519",
    "Torches": "520"
}

# A dictionary that contains assigment required attributes and their corresponding offsets
Assignment = {
    "Keys": "518",
    "Skull Keys": "523",
    "Gems": "519",
    "Black Badge": "536",
    "Magic Carpet": "522",
    "Magic Axe": "576",
}