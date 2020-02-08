import xml.etree.ElementTree as ET
from questionClass import questionModel
from questionClass import matchingQuestionModel
from questionClass import askQuestions

# This function parses our XML file into a tree structure
tree = ET.parse('questions-template.xml')
test = tree.getroot()


questionDictionary = {}

for question in test:
    print('\n')
    toAdd = []
    toAddL = []
    toAddR = []
    possible_ans = []
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
            possible_ans.append(choice.text)
        if(choice.tag == 'answer'):
            toAdd.append(choice.text)
        if(choice.tag == 'ans'):
            possible_ans.append(choice.text)
        if(choice.tag == 'c1'):
            toAddL.append(choice.text)
        if(choice.tag == 'c2'):
            toAddR.append(choice.text)
            

    if qType != 'matching':        
        questionDictionary[questionModel(toAdd[1], possible_ans)] =toAdd[2]
    else:
        questionDictionary[matchingQuestionModel(toAdd[1],toAddL ,toAddR)] = possible_ans
        
        
        
print(questionDictionary)
askQuestions(questionDictionary)




