# Create empty string accumulator
# for each word in phrase
#    get 1st letter of word
#    turn letter into upper case
#    append it to end of string accumulator
# print out acronym abbreviation

def acronymBuilder():
    print("This program builds acronym abbreviations")
    print()
    phrase = input("Enter your phrase here: ")
    acronym = ""

    for word in phrase.split():
        acronym = acronym + word[0]
    acronym = acronym.upper()

    print("The acronym word is: ", acronym)

acronymBuilder()

