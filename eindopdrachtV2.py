from random import choices
import sys
import time

# slowprint function
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

# auto route
def path22():
    slowprint('Je vertrekt met de auto en komt in het land van bestemming aan.')
    slowprint('Je krijgt de kans om te werken als supermarktmedewerker of te helpen als een docent op een school, wat kies je? Supermarkt of docent?')

    answer1 = input()

    if answer1 == 'supermarkt' or answer1 == 'Supermarkt':
        slowprint('Je wordt supermarktmedewerker en gaat bij de jumbo werken.')
        slowprint('Helaas verdient dit niet genoeg en lukt het niet meer om iets beters te vinden, je kan geen verblijvings vergunning krijgen en moet helaas weer terug naar huis.')
    elif answer1 == 'docent' or answer1 == 'Docent':
        slowprint('Je gaat samenwerken met een docent engels')
        slowprint('Je krijgt later je eigen klas en wordt meer betaalt. Je kan een verblijfsvergunning krijgen om hier te blijven werken.')
    else: print('dit is geen geldig antwoord')
# boot route
def path12():
    slowprint('Je neemt de boot tocht richting europa wat heel spannend blijkt maar wel goed afloopt.')
    slowprint('Je moet wachten in een asielzoekerscentrum en begint met het doen van vrijwilligerswerk in de tussentijd.')
    slowprint('Er wordt je aangeboden om naar een gastgezin te gaan, wil je dit?')

    answer1 = input()

    if answer1 == 'ja' or answer1 == 'Ja':
         slowprint('Je komt in een gastgezin terecht.')
         slowprint('Je krijgt de kans om naar een opleiding te gaan en maakt deze af. Vervolgens vind je een goede baan en kan je op jezelf gaan wonen.')
    elif answer1 == 'nee' or answer1 == 'Nee':
         slowprint('Je besluit niet naar het gastgezin te gaan.')
         slowprint('Je blijft langer bij het asielzoekerscentrum waar dingen zo lang blijken te duren dat je zelf begint met nederlands te leren en hierin gaat les geven aan mensen die hier ook vastzitten. Tot de dag van vandaag lukt het nog steeds niet om een verblijfsvergunning te krijgen.')
    else: print('dit is geen geldig antwoord')
# vliegtuig route
def path11():
    slowprint('Je vertrekt met het vliegtuig richting europa en alles verloopt vrij soepel')
    slowprint('Je krijgt de kans om mee te werken met een engels docent of om eerst een cursus te volgen voor mogelijk een betere baan, wat doe je? Naar de cursus of docent?')

    answer1 = input()

    if answer1 == 'cursus' or answer1 == 'Cursus':
        slowprint('Je volgt een extra cursus waardoor je mogelijk een betere baan kunt krijgen.')
        slowprint('Maar dit blijkt helaas vrij lastig te zijn en te lang te duren, je kunt geen geschikte baan vinden en moet helaas weer terug naar huis.')
    elif answer1 == 'docent' or answer1 == 'Docent':
        slowprint('Je gaat samenwerken met een docent engels')
        slowprint('Je krijgt later je eigen klas en wordt meer betaalt. Je kan een verblijfsvergunning krijgen om hier te blijven werken.')
    else: print('dit is geen geldig antwoord')
# werk route
def path2():
    slowprint('Er is niet genoeg kans op goed betaalt werk in je land meer en je moet dus vertrekken om iets beters te vinden')
    slowprint('Hoe ga je het land verlaten? Met het vliegtuig of de auto?')

    answer1 = input()

    if answer1 == 'vliegtuig' or answer1 == 'Vliegtuig':
        path11()
    elif answer1 == 'auto' or answer1 == 'de auto':
        path22()
    else: print('dit is geen geldig antwoord')
# oorlog route
def path1():
    slowprint('Het is niet veilig in je land meer, je moet zo snel mogelijk het land verlaten')
    slowprint('Hoe ga je het land verlaten? Vertrek je met het vliegtuig of met de boot?')

    answer1 = input()

    if answer1 == 'vliegtuig' or answer1 == 'Vliegtuig':
        path11()
    elif answer1 == 'boot' or answer1 == 'Boot':
        path12()
    else: print('dit is geen geldig antwoord')

def Choices():
    slowprint('Hallo, wat is je naam ook alweer?')

    name = input()

    slowprint('Hallo ' + name + ', ik heb vernomen dat je het land moet verlaten')
    slowprint('Wat is hier ook alweer de reden van? Kwam het door oorlog of omdat je werk moet zoeken?')

    answer = input()

    if answer == 'oorlog' or answer == 'Oorlog':
        path1()
    elif answer == 'werk' or answer == 'werk zoeken':
        path2()
    else: print('dit is geen geldig antwoord')
Choices()