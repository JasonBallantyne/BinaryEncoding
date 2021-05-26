def listToString(s):
    # Initialize an empty string
    listStr = ""

    # Traverse in the string
    for ele in s:
        listStr += ele

    # Return string
    return listStr


def isBinary(num):
    # Checking if the input is binary
    for i in str(num):
        # If digit is 1 or 0
        if i in '10':
            binary = True
        else:
            binary = False
            break
    return binary


def hammingEncode(binary):
    if not isBinary(binary):
        return "Error: Input must be binary!"
    else:
        return checkEncoding(binary)


def checkEncoding(checkNum):
    numList = []
    parity = 1
    y = 0
    location = 2
    checkList = list(checkNum)

    while (len(checkList) + y + 1) > 2 ** y:
        y += 1

    # Assigning placeholder values
    for i in range(len(checkList)):
        if i + 1 == parity:
            checkList.insert(parity - 1, 'y')
            parity *= 2
            numList.append(i)

    for x in numList:
        codeList = []
        for p in range(x, len(checkList), location):
            status = checkList[p:int(p + (location / 2))]
            for n in status:
                codeList.append(n)

        location *= 2
        # Counting occurance of 1, checking if even and assigning it 1 or 0
        numCounter = codeList.count('1')
        if numCounter % 2 == 0:
            checkList[x] = "0"
        else:
            checkList[x] = "1"

    return listToString(checkList)


print(hammingEncode("1100"))
