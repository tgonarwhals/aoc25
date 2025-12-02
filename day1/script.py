def partone():
    file = open("input.txt","r")
    dial = 50
    count = 0
    i = 0
    for line in file.readlines():
        i+=1
        if (line[0] == "L"):
            num = int("-" + line[1:])
        else:
            num = int(line[1:])
        dial += num
        while (dial < 0):
            dial += 100
        while (dial >= 100):
            dial -= 100
        print(str(i) + ": " + str(dial))
        if dial == 0:
            count += 1
    print(str(count) + " is the number maybe")



def parttwo():
    file = open("input.txt","r")
    dial = 50
    count = 0
    i = 0
    for line in file.readlines():
        i+=1
        #define the numbers, L is negative, R is positive, reformat numbers into machine format:
        if (line[0] == "L"):
            num = int("-" + line[1:])
        else:
            num = int(line[1:])

        #i saw something online and i want to try literally just brute forcing it lmfao
        while (num != 0):
            if (num < 0):
                dial -= 1
                num += 1
            if (num > 0):
                dial += 1
                num -= 1
            if (dial < 0):
                dial += 100
            elif (dial >= 100):
                dial -= 100
            if (dial == 0):
                count += 1
            
        
        print(str(i) + ": " + line[:-1] + " -> " + str(dial) + " | " + str(count))
        
        
    print(str(count))


if __name__ == "__main__":
    parttwo()