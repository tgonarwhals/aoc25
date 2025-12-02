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

        #spin the dial
        dial += num

        #correct back down to range 0-99, counting every 0 we pass along the way
        while (dial < 0):
            dial += 100
            count += 1
        while (dial >= 100):
            dial -= 100
            count += 1
        
        print(str(i) + ": " + line[:-1] + " -> " + str(dial) + " | " + str(count))
        
        
    print(str(count))


if __name__ == "__main__":
    parttwo()