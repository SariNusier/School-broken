
# coding: utf-8

# In[10]:

import xml.etree.ElementTree as et
import csv


# In[ ]:




# In[ ]:




# In[15]:

def getChildByTag(tag, root):
    for child in root:
        if child.tag == tag:
            return child
        
        
def formatStringToPrint(name, size, toppings, crust):
    
    allToppings = ""
    for topping in toppings:
        allToppings += topping + " and "
    return "%s: %s Pizza with %s%s"%(name, size, allToppings, crust)


def getToppings(toppingCodes, toppingString):
    toppings = []
    for c in range(0, len(toppingString)):
        toppings.append(toppingCodes[toppingString[c]])
    return toppings


# In[16]:

# Reading the file
try:
    tree = et.ElementTree(file='data/pizza.xml')
    root = tree.getroot()
    sizeCodes = {}
    toppingCodes = {}
    crustCodes = {}
    
    for size in getChildByTag("sizes", root):
        sizeCodes[size.attrib["code"]] = size.text
    #print(sizeCodes)
    
    for topping in getChildByTag("toppings", root):
        toppingCodes[topping.attrib["code"]] = topping.text
    #print(toppingCodes)
    
    for crust in getChildByTag("crusts", root):
        crustCodes[crust.attrib["code"]] = crust.text
        
    with open("data/pizza_specials.csv", "r") as csvFile:
        csvSpecials = csv.DictReader(csvFile)
        for special in csvSpecials:
            print(formatStringToPrint(special["name"],
                               sizeCodes[special["size"]],
                               getToppings(toppingCodes, special["toppings"]),
                               crustCodes[special["crust"]]))
            
except IOError as ioe:
    print("I/O Error: %s" % ioe)


# In[ ]:



