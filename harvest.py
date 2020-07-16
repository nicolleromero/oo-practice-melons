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
print_pairing_info(all_melon_types)
print(make_melon_type_lookup(all_melon_types))

############
# Part 2   #
############


# class Melon(object):
#     """A melon in a melon harvest."""

#     # Fill in the rest
#     # Needs __init__ and is_sellable methods


# def make_melons(melon_types):
#     """Returns a list of Melon objects."""

#     # Fill in the rest


# def get_sellability_report(melons):
#     """Given a list of melon object, prints whether each one is sellable."""

#     # Fill in the rest
