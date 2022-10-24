from random import choices

def Choices():
    print('temp')
    print('')
    print('')
    print('')
    print('')

    answer1 = input()

    if answer1 == 'A' or answer1 == 'a':
        path1()
    elif answer1 == 'B' or answer1 == 'b':
        print('Persoonlijk niet de grootste fan van brood als ontbijt')
    elif answer1 == 'C' or answer1 == 'c':
        print('Ik zou tenminste wel iets eten')
    else: print('Je kan alleen met A, B of C antwoorden')

    print('Wil je nog een keer?')
    print('Ja of Nee?')
    retry = input()

    if retry == 'Ja' or retry == 'ja':
        Choices()
    else: print('Goodbye!')
Choices()

def path1():
    answer1 = input()

    if answer1 == 'A' or answer1 == 'a':
        path1()
    elif answer1 == 'B' or answer1 == 'b':
        print('Persoonlijk niet de grootste fan van brood als ontbijt')
    elif answer1 == 'C' or answer1 == 'c':
        print('Ik zou tenminste wel iets eten')
    else: print('Je kan alleen met A, B of C antwoorden')