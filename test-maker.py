from lxml import etree
from lxml import builder

# This program allows the user to build their own quiz. It asks the user what questions
# they want to have on the quiz, and it allows them to customize the number of options
# for each question. Once the quiz has been built successfully, the output is saved to
# an XML file.

def make_mc_question(root):
    # Builds multiple choice questions
    print("Making multiple choice question...")

    question = etree.SubElement(root, "question")
    type = etree.SubElement(question, "type")
    type.text = "multiple choice"

    q = etree.SubElement(question,"q")
    q.text = input("Enter the question you want to ask: ")

    c_limit = int(input("Enter the number of choices you want for this question: "))
    for num in range(c_limit):
        c = etree.SubElement(question,"c")
        c.text = input("Enter the choice letter (ex. A, B, C, etc) followed by the choice value: ")

    answer = etree.SubElement(question, "answer")
    answer.text = input("Enter the letter of the correct answer choice: ")

    return question

def make_tf_question(root):
    # Builds true false questions
    print("Making true false question...")

    question = etree.SubElement(root, "question")
    type = etree.SubElement(question, "type")
    type.text = "true false"

    q = etree.SubElement(question, "q")
    q.text = input("Enter the question you want to ask: ")

    c = etree.SubElement(question,"c")
    c.text = "True"
    c = etree.SubElement(question, "c")
    c.text = "False"

    answer = etree.SubElement(question, "answer")
    answer.text = input("Enter the correct answer ('true'/'false'): ")

    return question

def make_match_questions(root):
    # Builds matching question
    print("Making matching question...")

    question = etree.SubElement(root, "question")
    type = etree.SubElement(question, "type")
    type.text = "matching"

    q = etree.SubElement(question, "q")
    q.text = input("Enter the question you want to ask: ")

    c1_limit = int(input("How many terms do you want to be matched? "))
    for num in range(c_limit):
        c1 = etree.SubElement(question,"c1")
        c1.text = input("Enter the term: ")

    c2_limit = int(input("How many options do you want for people to choose to match with? "))
    for num in range(c2_limit):
        c2 = etree.SubElement(question,"c2")
        c2.text = input("Enter the option letter (ex. A, B, C, etc) followed by the option value: ")

    for num in range(c_limit):
        ans = etree.SubElement(question, "ans")
        ans.text = input("Enter the letter of the correct answer in the order that the terms were listed: ")

    return question

def file_namer():
    # Allows user to save their generated test under a name of their own choosing,
    # tests to make sure that the user's chosen file name is valid
    valid = True
    while valid:
        filename = input("Enter the name you'd like to save your quiz as (don't put the file extension): ")
        if ('.' in filename) or ('/' in filename):
            print("Sorry, that file name is invalid. Try again.")
        else:
            valid = False
    return filename

def main():

    print("Building your test...")
    test = etree.Element("test")

    mc_lim = int(input("How many multiple choice questions would you like? "))
    for num in range(mc_lim):
        mc_q = make_mc_question(test)

    tf_lim = int(input("How many true false questions would you like? "))
    for num in range(tf_lim):
        tf_q = make_tf_question(test)

    match_lim = int(input("How many matching questions would you like? "))
    for num in range(match_lim):
        match_q = make_match_questions(test)

    # This saves the user generated test into a tree structure
    test_content = (etree.tostring(test, pretty_print=True))

    filename = file_namer()
    with open(filename+".xml", "wb") as f:
        f.write(test_content)
        print("Test saved successfully as "+filename+'.xml')

main()
