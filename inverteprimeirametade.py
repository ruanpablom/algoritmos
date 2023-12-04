string = input()

posMetade = int(len(string)/2)

string = (string[:posMetade])[::-1] + string[posMetade:]

print(string)