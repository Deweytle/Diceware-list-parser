import json
import os

inputPath = os.path.join(os.getcwd(),'Input')

for file in os.listdir(inputPath):
    dicewareList = []
    with open(os.path.join(inputPath, file), 'r', encoding='utf-8') as content:
        for line in content:
            lineElements = line.split()
            lineDictionnary = {
                'dices': lineElements[0],
                'value': lineElements[1]
            }
            dicewareList.append(lineDictionnary)
    try:
        outputName = f'{os.path.splitext(file)[0]}.json'
        with open(f'./Output/{outputName}','w') as outfile:
            json.dump(dicewareList,outfile)
        print(f'{outputName} created')
    except error:
        print(error)
