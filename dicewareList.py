import json
import os

inputPath = os.path.join(os.getcwd(),'Input')

for file in os.listdir(inputPath):
    dicewareDict = {}
    with open(os.path.join(inputPath, file), 'r', encoding='utf-8') as content:
        for line in content:
            lineElements = line.split()
            dicewareDict[lineElements[0]] = lineElements[1]
    try:
        outputName = f'{os.path.splitext(file)[0]}.json'
        with open(f'./Output/{outputName}','w') as outfile:
            json.dump(dicewareDict,outfile)
        print(f'{outputName} created')
    except error:
        print(error)
