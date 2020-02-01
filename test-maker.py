import lxml.etree
import lxml.builder

EM = lxml.builder.ElementMaker()
TEST = EM.root
QUESTION = EM.question
TYPE = EM.type
Q = EM.q
C = EM.c
C2 = EM.c2
ANSWER = EM.answer

def main():

    ## Hard-coding what's written to the new XML file for testing purposes
    new_test_doc = TEST(
        QUESTION(
            TYPE("true false"),
            Q("Humans can eat uranium for a healthy snack."),
            C("True"),
            C("False"),
            ANSWER("True")
        )
    )

    print(lxml.etree.tostring(new_test_doc, pretty_print=True))

main()
