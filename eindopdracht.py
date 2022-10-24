from random import choices

def Choices():
    print('Beantwoord deze met A, B of C.')
    print('Wat wil je als ontbijt?')
    print('A) Muesli')
    print('B) Brood')
    print('C) Niks')

    answer1 = input()

    if answer1 == 'A' or answer1 == 'a':
        print('Goede keus')
    elif answer1 == 'B' or answer1 == 'b':
        print('Persoonlijk niet de grootste fan van brood als ontbijt')
    elif answer1 == 'C' or answer1 == 'c':
        print('Ik zou tenminste wel iets eten')
    else: print('Je kan alleen met A, B of C antwoorden')

    print('Volgende vraag')
    print('Wat neem je voor drinken?')
    print('A) Water')
    print('B) Melk')
    print('C) Cola')

    answer2 = input()

    if answer2 == 'A' or answer2 == 'a':
        print('Goede keus zou ik ook doen')
    elif answer2 == 'B' or answer2 == 'b':
        print('Verstandig')
    elif answer2 == 'C' or answer2 == 'c':
        print('Cola met ontbijt???')
    else: print('Je kan alleen met A, B of C antwoorden')

    print('Oke volgende')
    print('Wil je een douche nemen?')
    print('A) Ja')
    print('B) Nee')
    print('C) Douche?')

    answer3 = input()

    if answer3 == 'A' or answer3 == 'a':
        print('Maak het niet langer dan 5 minutes')
    elif answer3 == 'B' or answer3 == 'b':
        print('Dan niet')
    elif answer3 == 'C' or answer3 == 'c':
        print('uh')
    else: print('Je kan alleen met A, B of C antwoorden')

    print('Oke laatste')
    print('Wat wil je nu gaan doen?')
    print('A) Gamen')
    print('B) Video editen')
    print('C) School werk')

    answer4 = input()

    if answer4 == 'A' or answer4 == 'a':
        print('Vergeet je huiswerk niet')
    elif answer4 == 'B' or answer4 == 'b':
        print('Succes')
    elif answer4 == 'C' or answer4 == 'c':
        print('Verstandig')
    else: print('Je kan alleen met A, B of C antwoorden')

    print('Wil je nog een keer?')
    print('Ja of Nee?')
    retry = input()

    if retry == 'Ja' or retry == 'ja':
        Choices()
    else: print('Goodbye!')

Choices()