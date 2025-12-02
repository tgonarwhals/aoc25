def partone():
    total = 0
    file = open("input.txt","r")
    input = file.read()
    input = input.split(",")
    for rangeIn in input:
        rangeIn = rangeIn.split("-")
        # fun fact: range is NOT inclusive!
        for i in range(int(rangeIn[0]), int(rangeIn[1])+1):
            if (len(str(i)) % 2 != 0):
                # is not possible to be an invalid id (no middle of string), do nothing
                # print(str(i) + " is a valid ID")
                # i was gonna print all the valid ones but it takes too long
                pass
            else:
                # has potential to be an invalid id, split string in middle and check if equal
                midpoint = int(len(str(i))/2)
                numA = str(i)[:midpoint]
                numB = str(i)[midpoint:]
                if (numA == numB):
                    #invalid id, add to total
                    total += i
                    print(str(midpoint) + " " + str(numA) + " " + str(numB) + " | " + str(i) + " is an invalid ID")
                #else, valid id, do nothing
    print(total)

def parttwo():
    total = 0
    file = open("input.txt","r")
    input = file.read()
    input = input.split(",")
    for rangeIn in input:
        rangeIn = rangeIn.split("-")
        # fun fact: range is NOT inclusive!
        for i in range(int(rangeIn[0]), int(rangeIn[1])+1):
            #example: select the first number
            #if all of the next numbers match it, number is invalid, add to total
            #if not, select the first 2 numbers
            #if all next batches of 2 numbers match it, number is invalid, add to total
            #...
            #continue to check until n/2
            #????? dude what am i looking at here
            for j in range(1, int((len(str(i)))/2)+2):
                
                numRepeat = int(str(i)[:j])
                print (str(i) + " " + str(j) + " " + str(numRepeat))

    print(total)

if __name__ == "__main__":
    parttwo()