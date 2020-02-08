import xml.etree.ElementTree as ET
from questionClass import questionModel
from questionClass import matchingQuestionModel
from questionClass import askQuestions

def parser_func(tree):
    # This function parses our XML file into a tree structure
   # tree = ET.parse('questions-template.xml')
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

    return questionDictionary

def valid_name():
    # Tests to make sure that the entered file name is valid
    not_valid = True
    while not_valid:
        filename = input("Enter the name of your test file (do not include the '.xml' extension): ")
        try:
            f = open(filename+'.xml')
            not_valid = False
        except FileNotFoundError:
            print("Sorry, '"+filename+".xml' does not exist! Try again.")

    return filename

def main():
    print("Would you like to take a pre-built exam, or an exam that you built?")

    invalid_opt = True
    while invalid_opt:
        exam_choice = input("(Enter 'p' for pre-built, or 'e' for your own exam): ")
        if exam_choice is 'p':
            tree = ET.parse('questions-template.xml')
            invalid_opt = False
        elif exam_choice is 'e':
            f_name = valid_name()
            tree = ET.parse(f_name+".xml")
            invalid_opt = False
        else:
            print("That is an invalid option.")


    q_dict = parser_func(tree)
    print(q_dict)
    askQuestions(q_dict)

if __name__ == "__main__":
    main()
# main()



