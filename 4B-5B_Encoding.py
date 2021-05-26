def modulateInputs(data):
    block_coding = {'0000': '11110', '0001': '01001', '0010': '10100', '0011': '10101',
                      '0100': '01010', '0101': '01011', '0110': '01110', '0111': '01111',
                      '1000': '10010', '1001': '10011', '1010': '10110', '1011': '10111',
                      '1100': '11010', '1101': '11011', '1110': '11100', '1111': '11101'}

    result = ""
    # Checking each four bit binary
    for i in range(0, len(data), 4):
        four_bit = data[i:i+4]
        # Checking if binary exists in the dictionary & appending to string
        if four_bit in block_coding:
            result += block_coding[four_bit]
        else:
            print("Error: Input must be in 4 bit binary")
            break
    return result


print(modulateInputs("11110000"))