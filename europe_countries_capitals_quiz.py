from time import sleep as slp
import os


def next():
    slp(0.2)
    os.system('cls')

def slow_next():
    slp(1)
    os.system('cls')

def rly_slow():
    slp(7)
    os.system('cls')

def load():
    print("*..")
    next()
    print(".*.")
    next()
    print("..*")
    next()

print("Loading...")
slow_next()
for i in range(7):
    load()
if __name__ == '__main__':
    print("Successfully Loaded!")
    slow_next()
else:
    print("Loading failed...\nTry Again")
    slow_next()

print("Welcome to the Europe countries and capitals quiz!")
slow_next()
os.system('cls')
hello = str(input("What is your name?: "))
print("Hello "+hello)
slow_next()
print("I will list a country and you will tell me the capital of that country! Let's get started!")
slow_next()

for i in range(3):
    load()


score = 0

question1 = str(input("Spain: "))
question1A = "Madrid"
if question1 == question1A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question1A+". You said "+question1+".")
    slow_next()
    
question2 = str(input("Portugal: "))
question2A = "Lisbon"
if question2 == question2A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question2A+". You said "+question2+".")
    slow_next()

question3 = str(input("Andorra: "))
question3A = "Andorra la Vella"
if question3 == question3A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question3A+". You said "+question3+".")
    slow_next()

question4 = str(input("France: "))
question4A = "Paris"
if question4 == question4A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question4A+". You said "+question4+".")
    slow_next()

question5 = str(input("Ireland: "))
question5A = "Dublin"
if question5 == question5A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question5A+". You said "+question5+".")
    slow_next()

question6 = str(input("United Kingdom: "))
question6A = "London"
if question6 == question6A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question6A+". You said "+question6+".")
    slow_next()

question7 = str(input("Iceland: "))
question7A = "Reykjavik"
if question7 == question7A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question7A+". You said "+question7+".")
    slow_next()

question8 = str(input("Belgium: "))
question8A = "Brussels"
if question8 == question8A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question8A+". You said "+question8+".")
    slow_next()

question9 = str(input("Netherlands: "))
question9A = "Amsterdam"
if question9 == question9A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question9A+". You said "+question9+".")
    slow_next()

question10 = str(input("Switzerland: "))
question10A = "Bern"
if question10 == question10A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question10A+". You said "+question10+".")
    slow_next()

question11 = str(input("Germany: "))
question11A = "Berlin"
if question11 == question11A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question11A+". You said "+question11+".")
    slow_next()

question12 = str(input("Denmark: "))
question12A = "Copenhagen"
if question12 == question12A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question12A+". You said "+question12+".")
    slow_next()

question13 = str(input("Sweden: "))
question13A = "Stockholm"
if question13 == question13A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question13A+". You said "+question13+".")
    slow_next()

question14 = str(input("Finland: "))
question14A = "Helsinki"
if question14 == question14A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question14A+". You said "+question14+".")
    slow_next()

question15 = str(input("Austria: "))
question15A = "Vienna"
if question15 == question15A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question15A+". You said "+question15+".")
    slow_next()

question16 = str(input("Norway: "))
question16A = "Oslo"
if question16 == question16A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question16A+". You said "+question16+".")
    slow_next()

question17 = str(input("Italy: "))
question17A = "Rome"
if question17 == question17A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question17A+". You said "+question17+".")
    slow_next()

question18 = str(input("San Marino: "))
question18A = "San Marino"
if question18 == question18A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question18A+". You said "+question18+".")
    slow_next()

question19 = str(input("Vatican City: "))
question19A = "Vatican City"
if question19 == question19A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question19A+". You said "+question19+".")
    slow_next()

question20 = str(input("Malta: "))
question20A = "Valletta"
if question20 == question20A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question20A+". You said "+question20+".")
    slow_next()

question21 = str(input("Czechia: "))
question21A = "Prague"
if question21 == question21A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question21A+". You said "+question21+".")
    slow_next()

question22 = str(input("Estonia: "))
question22A = "Tallinn"
if question22 == question22A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question22A+". You said "+question22+".")
    slow_next()

question23 = str(input("Latvia: "))
question23A = "Riga"
if question23 == question23A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question23A+". You said "+question23+".")
    slow_next()

question24 = str(input("Lituania: "))
question24A = "Vilnius"
if question24 == question24A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question24A+". You said "+question24+".")
    slow_next()

question25 = str(input("Luxembourg: "))
question25A = "Luxembourg"
if question25 == question25A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question25A+". You said "+question25+".")
    slow_next()

question26 = str(input("Slovakia: "))
question26A = "Bratislava"
if question26 == question26A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question26A+". You said "+question26+".")
    slow_next()

question27 = str(input("Hungary: "))
question27A = "Budapest"
if question27 == question27A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question27A+". You said "+question27+".")
    slow_next()

question28 = str(input("Slovenia: "))
question28A = "Ljubljiana"
if question28 == question28A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question28A+". You said "+question28+".")
    slow_next()

question29 = str(input("Croatia: "))
question29A = "Zagreb"
if question29 == question29A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question29A+". You said "+question29+".")
    slow_next()

question30 = str(input("Bosnia and Herzegovina: "))
question30A = "Sarajevo"
if question30 == question30A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question30A+". You said "+question30+".")
    slow_next()

question31 = str(input("Serbia: "))
question31A = "Belgrade"
if question31 == question31A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question31A+". You said "+question31+".")
    slow_next()

question32 = str(input("Montenegro: "))
question32A = "Podgorica"
if question32 == question32A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question32A+". You said "+question32+".")
    slow_next()

question33 = str(input("Albania: "))
question33A = "Tirana"
if question33 == question33A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question33A+". You said "+question33+".")
    slow_next()

question34 = str(input("Kosovo: "))
question34A = "Pristina"
if question34 == question34A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question34A+". You said "+question34+".")
    slow_next()

question35 = str(input("North Macedonia: "))
question35A = "Skopje"
if question35 == question35A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question35A+". You said "+question35+".")
    slow_next()

question36 = str(input("Greece: "))
question36A = "Athens"
if question36 == question36A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question36A+". You said "+question36+".")
    slow_next()

question37 = str(input("Bulgaria: "))
question37A = "Sofia"
if question37 == question37A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question37A+". You said "+question37+".")
    slow_next()

question38 = str(input("Romania: "))
question38A = "Bucharest"
if question38 == question38A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question38A+". You said "+question38+".")
    slow_next()

question39 = str(input("Moldova: "))
question39A = "Chisinau"
if question39 == question39A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question39A+". You said "+question39+".")
    slow_next()

question40 = str(input("Ukraine: "))
question40A = "Kiev"
if question40 == question40A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question40A+". You said "+question40+".")
    slow_next()

question41 = str(input("Poland: "))
question41A = "Warsaw"
if question41 == question41A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question41A+". You said "+question41+".")
    slow_next()

question42 = str(input("Belarus: "))
question42A = "Minsk"
if question42 == question42A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question42A+". You said "+question42+".")
    slow_next()

question43 = str(input("Liechtenstein: "))
question43A = "Vaduz"
if question43 == question43A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question43A+". You said "+question43+".")
    slow_next()

question44 = str(input("Russia: "))
question44A = "Moscow"
if question44 == question44A:
    print("Correct!")
    score += 1
    slow_next()
else:
    print("Incorrect! The correct answer was "+question44A+". You said "+question44+".")
    slow_next()



print("Your score is "+str(score)+"/44.  That's  good!")