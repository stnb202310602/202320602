prices = [1000, 2000, 3000, 2000, 3000]
length = len(prices)
holding_seconds = []

for i in range(length):
    seconds = 0
    for x in range(i + 1, length):
        seconds += 1
        if prices[i] > prices[x]:
            break
    holding_seconds.append(seconds)

print(holding_seconds)