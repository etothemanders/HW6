"""
melon_info.py - Prints out all the melons in our inventory

"""
from melons import melon_dict

class Inventory(object):
    
    def __init__(self):
        self.melons = []
        self.load_melons()
        
    def load_melons(self):
        for melon, attr in melon_dict.items():
            m = Melon(melon, attr['seedless'], attr['price'])
            self.melons.append(m)
            
    def print_melons(self):
        for melon in self.melons:
            print melon

class Melon(object):
    
    def __init__(self, name, seedless, price):
        self.name = name
        self.seedless = seedless
        self.price = price

    def __str__(self):
    	hashasnot = 'have'
    	if self.seedless:
    		hashasnot = 'do not have'
    	return "%ss %s seeds and are $%0.2f" % ( self.name, hashasnot, self.price)
    
if __name__ == '__main__':
    inv = Inventory()
    inv.print_melons()