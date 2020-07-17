import sys

############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller,
                 ):
        """Initialize a melon."""
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(
        'yw', 'Yellow_watermelon', 2013, 'yellow', False, True)
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with:')

        for i, pairing in enumerate(melon.pairings):
            print(f'- {melon.pairings[i]}')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    dict_melon_codes = {}

    for melon in melon_types:
        dict_melon_codes[melon.code] = melon

    return dict_melon_codes


all_melon_types = make_melon_types()

# print_pairing_info(all_melon_types)
# print(make_melon_type_lookup(all_melon_types))

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvested_by):
        """Initialize a melon."""
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvested_by = harvested_by

    def is_sellable(self, color_rating, shape_rating, harvest_field):
        """Determine if a melon is sellable based on color and shape ratings"""

        if self.color_rating > 5 and self.shape_rating > 5 and harvest_field != 3:
            self.is_sellable = 'CAN BE SOLD'

        else:
            self.is_sellable = 'NOT SELLABLE'


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_harvested_melons = []

    melons_by_id = make_melon_type_lookup(all_melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_1.is_sellable(8, 7, 2)
    all_harvested_melons.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_2.is_sellable(3, 4, 2)
    all_harvested_melons.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_3.is_sellable(9, 8, 3)
    all_harvested_melons.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_4.is_sellable(10, 6, 35)
    all_harvested_melons.append(melon_4)

    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_5.is_sellable(8, 9, 35)
    all_harvested_melons.append(melon_5)

    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_6.is_sellable(8, 2, 35)
    all_harvested_melons.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_7.is_sellable(2, 3, 4)
    all_harvested_melons.append(melon_7)

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_8.is_sellable(6, 7, 4)
    all_harvested_melons.append(melon_8)

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')
    melon_9.is_sellable(7, 10, 3)
    all_harvested_melons.append(melon_9)

    return all_harvested_melons


def get_sellability_report(all_harvested_melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in all_harvested_melons:
        print(
            f'Harvsted by {melon.harvested_by} from Field {melon.harvest_field} ({melon.is_sellable})')


def melons_from_file(melon_types):
    """Reads in data from a file and returns a list of Melon objects."""

    all_melons_from_file = []

    melons_by_id = make_melon_type_lookup(all_melon_types)

    file = open(sys.argv[1])

    for i, line in enumerate(file):  # iterate over the entries in the data
        line = line.rstrip()  # remove trailing spaces from each line on the right
        data = line.split(" ")

        melon_shape = int(data[1])
        melon_color = int(data[3])
        melon_type = data[5]
        harvester = data[8]
        field = int(data[11])

        melon_i = Melon(melons_by_id[melon_type], melon_shape,
                        melon_color, field, data[8])
        melon_i.is_sellable(melon_shape, melon_color, field)
        all_melons_from_file.append(melon_i)

        print(
            f'Melon {i}, shape: {melon_shape}, color: {melon_color}, code: {melon_type}, harvested by: {data[8]} in field {field}, sellable state: {melon_i.is_sellable}')

    return all_melons_from_file


# print(melons_from_file(all_melon_types))
all_harvested_melons = make_melons(all_melon_types)
# print(make_melons(all_melon_types))
# get_sellability_report(all_harvested_melons)
print(melons_from_file(all_melon_types))
