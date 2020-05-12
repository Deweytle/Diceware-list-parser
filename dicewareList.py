import json
dicewareList = []

file = open('eff_large_wordlist.txt', 'r', encoding='utf-8')
for line in file:
    lineElements = line.split()
    lineDictionnary = {
        'dices': lineElements[0],
        'value': lineElements[1]
    }
    dicewareList.append(lineDictionnary)

try:
    with open('eff_large_wordlist.json','w') as outfile:
        json.dump(dicewareList,outfile)
except error:
    print(error)

#Cleanup
file.close()
