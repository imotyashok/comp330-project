import xml.etree.ElementTree as ET
import questionClass

# This function parses our XML file into a tree structure
tree = ET.parse('questions-template.xml')
test = tree.getroot()

print(test.tag)

# Test function to print out what our XML file looks like; this information
# can later be stored into a dictionary or some other data structure

for question in test:
    print('\n')
    for choice in question:
<<<<<<< HEAD
        print(choice.tag+": "+choice.text)
        choice_arr.append(choice.tag+": "+choice.text)

q1 = questionModel("hello", [1,2])

=======
        print(choice.tag + ": " + choice.text)
        for c in choice:
            print(c.tag+": "+c.text)
>>>>>>> 97b278635119f981af22c844239a7c5aea5b5026
