
# coding: utf-8

# In[1]:

import xml.etree.ElementTree as et
import csv


# In[ ]:




# In[ ]:




# In[2]:

def getChildByTag(tag, root):
    for child in root:
        if child.tag == tag:
            return child


# In[3]:

# Reading the file
try:
    tree = et.ElementTree(file='data/pizza.xml')
    root = tree.getroot()
    result = {}
    
    result["sizes"] = len(getChildByTag("sizes", root))   
    result["toppings"] = len(getChildByTag("toppings", root)) 
    result["crusts"] = len(getChildByTag("crusts", root)) 
    result["total_combo"] = result["sizes"]*(2**result["toppings"])*result["crusts"]
    with open("data/pizza_report.csv", "w") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=['sizes','toppings','crusts','total_combo'])
        writer.writeheader()
        writer.writerow(result)
except IOError as ioe:
    print("I/O Error: %s" % ioe)


# In[ ]:



