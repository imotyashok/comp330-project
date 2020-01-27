import xml.etree.ElementTree as ET

# This function parses our XML file into a tree structure
tree = ET.parse('questions-template.xml')
test = tree.getroot()

print(test.tag)

# Test function to print out what our XML file looks like; this information
# can later be stored into a dictionary or some other data structure

xml_arr =[]
q_arr = []
choice_arr = []

for question in test:
    print('\n')
    for choice in question:
        print(choice.tag+": "+choice.text)
        choice_arr.append(choice.tag+": "+choice.text)



