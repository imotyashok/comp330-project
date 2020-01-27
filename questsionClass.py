
#sort out this self buisness, cause it's getting on my nerves

class questionModel:
    questionType = None
    questions = None
    answers = None

    def __init__(self, questionBody, answers):
     self.questions = questionBody
     self.answers = answers
       

#works for multiple choice and T/F but we'll need a separate function for matching
def askQuestion(questionDict):
    for x in questionDict:
        print(x.questions)
        for y in x.answers:
            print(y)
        answer = input("Input here please: ")
        print(questionDict[x])
        if(answer.lower() != questionDict[x].lower()):
            print("incorrect")
        else:
            print("correct")
        print("")


print("try this")
q1 = questionModel("What is the 2nd thing in this list?", ["A.No","B.More","C.Heroes"])
q2 = questionModel("This statement is true", ["True","False"])
thisDict = {
    q1:"More",
    q2:"True"
}
askQuestion(thisDict)