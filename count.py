import sys


string = ""
qwerty = wasd = zxcv = 0

for line in sys.stdin:
    string = line
    for i in range(len(string)):
        if((string[i] >= 'a' and string[i] <= 'z') or (string[i] >= 'A' and string[i] <= 'Z')): 
            qwerty = qwerty + 1 
        elif(string[i] >= '0' and string[i] <= '9'):
        elif(string[i] >= '0' and string[i] <= '9'):
            wasd = wasd + 1
        else:
            zxcv = zxcv + 1

sys.stdout.write("Total angka: " + str(wasd))
sys.stdout.write('\n')
sys.stdout.write("Total huruf: " + str(qwerty))
sys.stdout.write('\n')
sys.stdout.write("Total symbol: " + str(zxcv))
sys.stdout.write('\n')
