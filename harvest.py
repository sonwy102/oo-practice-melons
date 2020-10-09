############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon type."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing(['mint'])

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing(['strawberries','mint'])

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing(['proscuitto'])

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing(['ice cream'])

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f'- {pairing}')
        

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    for melon in melon_types:

        melon_dict[melon.code] = melon
        
        # # If melon.code doesn't exist as a key in melon_dict
        # if melon.code not in melon_dict:
        #     # Initialize key and add <melon object> as an element of the value (list)
        #     melon_dict[melon.code] = [melon]
        # else: 
        #     # add <melon object> into melon_dict[key]'s value (list)
        #     melon_dict[melon.code].append(melon)
           
    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        """Initialize a melon"""

        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        """Returns true if melon is sellable, false otherwise"""

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True 
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Create dictionary of {reporting code(str): MelonType (obj)}
    melons_by_id = make_melon_type_lookup(melon_types)

    # Instantiate melons 1 - 9
    melon1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    # Make a list of Melon objects
    melon_harvest = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]

    return melon_harvest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:

        # Set default state to NOT SELLABLE
        state = 'NOT SELLABLE'

        # if is_sellable returns True, change state to CAN BE SOLD
        if melon.is_sellable():
            state = 'CAN BE SOLD'

        print(f"Harvested by {melon.harvester} from Field {melon.field} ({state})")

def make_melon_obj(filename, melon_types):
    """Given a txtfile of melons harvested, return a dictionary of each Melon object"""

    # Open txtfile of melons and initialize variables
    harvest_data = open(filename)
    index = 1
    melon_obj_dict = {}

    # Create dictionary of {reporting code(str): MelonType (obj)}
    melons_by_id = make_melon_type_lookup(melon_types)

    # Iterate over each line of melon_file
    for line in harvest_data:

        # Process each line of data and add to melon_obj_dict
        line = line.split(' ')
        melon_obj_dict["melon" + str(index)] = Melon(melons_by_id[line[5]], line[1], line[3], line[11], line[8])
        index += 1
    
    # Close file
    harvest_data.close()

    return melon_obj_dict


