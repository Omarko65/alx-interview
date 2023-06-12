#!/usr/bin/env python3
''' a function that determines if the a given
    set of data is a a valid utf8 encoding
'''


def int_to_binary(value: int) -> str:
    ''' a function that converts values to binary form
        that is 8 bits long
    '''
    bin_format = bin(value)
    bin_format = bin_format[2:]
    if len(bin_format) != 8:
        bin_format = '0' + bin_format
    return bin_format


def check_byte(byte: str) -> int:
    '''
    a function that checks the byte of data
    returns 1 if it's 1 byte data
    2 if it's 2 bytes and so on
    returns 5 if it's a continuation
    and 0 if there's an error
    '''
    if byte[0] == '0':
        return 1
    elif byte[0] == '1':
        if byte[1] == '1':
            if byte[2] == '1':
                if byte[3] == '1':
                    return 4
                else:
                    return 3
            else:
                return 2
        else :
            return 5
    else:
        return 0


def validUTF8(data):
    '''
    function that validates data and confirm if it
    is a valid UTF8 encoding
    '''
    binary_list = []
    j = 0
    for i in data:
        binary_list.append(int_to_binary(i))

    while j < len(binary_list):
        curr_byte = check_byte(binary_list[j])
        if curr_byte == 1:
            j+=1
            continue

        elif curr_byte == 2:
            next_byte = check_byte(binary_list[j+1])
            if next_byte != 5:
                return False
            else:
                j+=2
                continue
        elif curr_byte == 3:
            next_byte = check_byte(binary_list[j+1])
            upper_byte = check_byte(binary_list[j+2])
            if next_byte != 5 and upper_byte != 5:
                return False
            else:
                j+=3
                continue
        elif curr_byte == 4:
            byte_a = check_byte(binary_list[j+1])
            byte_b = check_byte(binary_list[j+2])
            byte_c = check_byte(binary_list[j+3])
            if byte_a != 5 and byte_b != 5 and byte_c != 5:
                return False
            else:
                j+=4
                continue
        else:
            return False

    return True
