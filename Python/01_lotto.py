import random

def generateSixNumbers():
    # erstelle leere Liste
    numbers = []

    while len(numbers) < 6:
        # eine Zufallszahl generieren
        z = random.randint(1,45)

        # überprüfe ob Zahl in Liste schon enthalten
        if z not in numbers:
            numbers.append(z)
    return numbers

def getNumbersFromUser():
    userinput = input("Bitte geben Sie Ihre Zahlen mit Leerzeichen getrennt ein:")
    usernumbers = userinput.split(" ")
    usernumbers_int = []
    for number in usernumbers:
        usernumbers_int.append(int(number))
    return usernumbers_int

def compareNumbers(numbers, usernumbers):
    correct_numbers = 0
    for number in numbers:
        if number in usernumbers:
            correct_numbers = correct_numbers + 1
    
    return correct_numbers
    

numbers = generateSixNumbers()
usernumbers = getNumbersFromUser()
correct = compareNumbers(numbers, usernumbers)

print(numbers)
print(usernumbers)
print(f"Es waren {correct} Zahlen richtig.")