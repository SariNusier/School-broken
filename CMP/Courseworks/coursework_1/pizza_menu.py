
# coding: utf-8

# In[1]:

import xml.etree.ElementTree as et


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
    print("# %s\n"%getChildByTag("shopname", root).text)

    print("## Sizes")
    for size in getChildByTag("sizes", root):
        print("- %s"%size.text)
        
    print("\n## Toppings")
    for topping in getChildByTag("toppings", root):
        print("- %s"%topping.text)

    print("\n## Crusts")
    for crust in getChildByTag("crusts", root):
        print("- %s"%crust.text)
except IOError as ioe:
    print("I/O Error: %s" % ioe)


# In[4]:




# In[ ]:



