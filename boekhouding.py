from helper import *


inkomsten = {
    "Aardbeien-ij-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

def som(dictionary):
    return sum(dictionary.values())

print(decoreer(som(inkomsten)))


