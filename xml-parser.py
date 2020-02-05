import xml.etree.ElementTree as ET
#import questionClass
from questionClass import questionModel
from questionClass import matchingQuestionModel
from questionClass import askQuestions

# This function parses our XML file into a tree structure
tree = ET.parse('questions-template.xml')
test = tree.getroot()

#print(test.tag)

# Test function to print out what our XML file looks like; this information
# can later be stored into a dictionary or some other data structure

questionDictionary = {}

choice_arr = []

for question in test:
    print('\n')
    toAdd = []
    toAddL = []
    toAddR = []
    panswers = []
    qType = None
    for choice in question:
        if (choice.tag == 'type') and (choice.text == "matching"):
            qType = 'matching'
            toAdd.append("matching")
        if(choice.tag == 'type') and (choice.text != "matching"):
            toAdd.append("none")
        if (choice.tag == 'q'):
            toAdd.append(choice.text)
        if(choice.tag == 'c'):
            panswers.append(choice.text)
        if(choice.tag == 'answer'):
            toAdd.append(choice.text)
        if(choice.tag == 'ans'):
            panswers.append(choice.text)
        if(choice.tag == 'c1'):
            toAddL.append(choice.text)
        if(choice.tag == 'c2'):
            toAddR.append(choice.text)
            
            
            
    if qType != 'matching':        
        questionDictionary[questionModel(toAdd[1],panswers)] =toAdd[2]
    else:
        questionDictionary[matchingQuestionModel(toAdd[1],toAddL ,toAddR)] = panswers 
        
        
        
print(questionDictionary)
askQuestions(questionDictionary)

#print(questionDictionary)
q5 = questionModel("hello", ["1","2"])

q6 = matchingQuestionModel("helllooo", [2,3], [4,5])



