import xml_parser
import test_maker

def run_program():

    invalid_opt = True

    while invalid_opt:
        print("\nWould you like to take a test, or build your own?")
        test_choice = input("(Enter 't' for taking a test, or 'b' for building one): ")
        if test_choice is 't':
            xml_parser.main()
            invalid_opt = False
        elif test_choice is 'b':
            test_maker.main()
            invalid_opt = False
        else:
            print("Sorry, that option isn't recognized.")

def main():

    run_program()

    repeat = True
    while repeat:
        print("\nWould you like to run the program again?")
        repeat_choice = input("(Enter 'y' for yes, 'n' for no): ")
        if repeat_choice is 'y':
            run_program()
        elif repeat_choice is 'n':
            print("Exiting program...")
            repeat = False
        else:
            print("Sorry, that option is not recognized.")

main()