import random

numberOfStreaks = 0

def coinFlip():
    coin = random.randint(0, 1)
    return coin

for experimentNumber in range (10000):
    flipList = []
    streakFound = False

    count = 1

    for number in range(100):
        flipList.append(coinFlip())
    
    for i in range(1, len(flipList)):
        if flipList[i] == flipList[i - 1]:
            count += 1
        else:
            if count >= 6:
                streakFound = True
            count = 1
    
    if count >= 6:
        streakFound = True

    if streakFound:
        numberOfStreaks += 1

chanceOfStreaks = numberOfStreaks / 10000 * 100

# print(f"Chance of streaks per 100 flips: {numberOfStreaks/100}%")
print(f'Chance of streaks per 10,000: {chanceOfStreaks:.2f}%')


