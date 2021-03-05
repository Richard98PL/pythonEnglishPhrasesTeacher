import random
import time
from os import system, name 
  
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def sleeper(number):
    for i in range(number):
        #print(str(number-i) + '...')
        time.sleep(0.1)
    clear()

file = open('file.txt','r',encoding='utf-8')
lines = file.read().splitlines()
random.shuffle(lines)
count = 0
phrasesDict = {}
singlePhrases = []
for line in lines:
    count += 1
    line = line.lower()
    if line.strip():
        #print("Line{}: {}".format(count, line.strip()))
        if "-" in line:
            splitted = line.split("-")
            print(splitted)
            phrasesDict[splitted[1].strip()] = splitted[0].strip()
        else:
            singlePhrases.append(line)
            print(line)
print('Intialization finished succesfully.')
print(str(len(phrasesDict)) + ' phrases loaded.')

cont = 'n'
while cont != 'y':
    print('continue? y/n')
    cont = input().lower()
clear()

score = 0

for key in phrasesDict:
    print(bcolors.OKBLUE + 'current score: ' + str(score) + '/' + str(len(phrasesDict)) + bcolors.ENDC)
    print('-> ' + bcolors.WARNING + key + bcolors.ENDC)
    correctAnswer = phrasesDict[key]
    answers = [correctAnswer]
    for i in range(3):
        answers.append(random.choice(list(phrasesDict.values())))

    letters = ['a','b','c','d']
    answersDict = {}
    for letter in letters:
        selection = random.randint(0, len(answers)-1)
        drawnPhrase = answers.pop(selection)
        answersDict[letter] = drawnPhrase
        print(bcolors.BOLD + letter + bcolors.ENDC + ': ' + drawnPhrase)

    answer = 'e'
    wasAnsweredGood = False

    while not wasAnsweredGood:
        while answer not in ['a','b','c','d']:
            print(bcolors.HEADER + "answer: " + bcolors.ENDC,end='')
            answer = input()

        if answersDict[answer] is correctAnswer:
            print(bcolors.OKGREEN + 'good answer!\n' + bcolors.ENDC)
            score += 1
            wasAnsweredGood = True
        else:
            print(bcolors.FAIL + 'bad answer.\n' + bcolors.ENDC)
            score -= 1
        
        answer = 'e'

    sleeper(3)

print('your score is ' + str(score) + '/' + str(len(phrasesDict)))