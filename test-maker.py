from lxml import etree
from lxml import builder

# TODO: get rid of anything that's hard coded
# TODO: implement error handling

# This program allows the user to build their own quiz. It asks the user what questions
# they want to have on the quiz, and it allows them to customize the number of options
# for each question. Once the quiz has been built successfully, the output is saved to
# an XML file.

def make_mc_question(root):
    print("Making multiple choice question...") # this line is for testing purposes

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
    print("Making true false question...")  # this line is for testing purposes

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
    answer.text = input("Enter the correct answer: ")

    return question

def make_match_questions(root):
    print("Making matching question...")  # this line is for testing purposes

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

def main():

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

    # This part writes the question structure out into an xml file; the file name is
    # hard coded, but this will be changed later
    info = (etree.tostring(test, pretty_print=True))
    with open("test-file.xml", "wb") as f:
        f.write(info)

main()
