
#sort out this self business, cause it's getting on my nerves

class questionModel:
    questionType = None
    questions = None
    answers = None

    def __init__(self, questionBody, answers):
     self.questions = questionBody
     self.answers = answers
       

class matchingQuestionModel:
    questionType = "match"
    questions = None
    leftSide = None
    rightSide = None

    def __init__(self, questionBody, leftSide, rightSide):
     self.questions = questionBody
     self.leftSide = leftSide
     self.rightSide = rightSide




#works for multiple choice and T/F but we'll need a separate function for matching
# def askQuestions(questionDict):
#     for x in questionDict:
#         if(x.questionType != "match"):
#             print(x.questions)
#             for y in x.answers:
#                 print(y)
#             answer = input("Input here please: ")
#             print(questionDict[x])
#             if(answer.lower() != questionDict[x].lower()):
#                 print("incorrect")
#             else:
#                 print("correct")
#             print("")
#         else:
#             print("matching currently not handled")
#
#
# print("try this")
# q1 = questionModel("What is the 2nd thing in this list?", ["No","More","Heroes"])
# q2 = questionModel("This statement is true", ["True","False"])
# q3 = matchingQuestionModel("This is a matching",["Killer","High","Desolation"],["Queen","Voltage","Row"])
# thisDict = {
#     q1:"More",
#     q2:"True",
#     q3:["not","currently","implemented"]
# }
# askQuestions(thisDict)