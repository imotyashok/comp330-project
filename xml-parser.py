import xml.etree.ElementTree as ET
#import questionClass
from questionClass import questionModel
from questionClass import matchingQuestionModel

# This function parses our XML file into a tree structure
tree = ET.parse('questions-template.xml')
test = tree.getroot()

print(test.tag)

# Test function to print out what our XML file looks like; this information
# can later be stored into a dictionary or some other data structure

questionDictionary = {}

choice_arr = []
for question in test:
    print('\n')
    for choice in question:
            print(choice.tag+": "+choice.text)
            #choice_arr.append(choice.tag+": "+choice.text)

q5 = questionModel("hello", ["1","2"])

q6 = matchingQuestionModel("helllooo", [2,3], [4,5])

print(q5.questions)
print(q5.answers)
print(q6.questions)

#
#questoinObject:answers
#for each in test:
#if question.tpye = match
#questiondict.add(matchquestionobject(x,y):z)
#else
#questiondict.add(questionmodel)
#askquestions(questiondict)
#


