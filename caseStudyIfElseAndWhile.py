# David Bowman
# caseStudyIfElseAndWhile.py
# This program will ask the user for their name and GPA and then decide if they are on the Dean's list or Honor Roll.
# 11/3/2023

name = input("Enter your last name: ")

if name == 'ZZZ':
    quit()
else:
    GPA = float(input("Enter your GPA: "))

    if GPA >= 3.5:
        print(name, "you are on the Dean's list.")
    elif GPA > 3.25:
        print(name, "you are on the Honor Roll.")
    else:
        print(name, "you are not on the Honor Roll or Dean's list.")