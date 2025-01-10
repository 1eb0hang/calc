from conversion import *


def eval_sum(string:str, mode:Mode)->str:
    pass

def separate(string:str):
    return get_numbers(string), get_symbols(string)

def combine(lst1:list, lst2:list)->str:
    val = ""
    for i in range(len(lst2)):
        val += lst1[i] + lst2[i]
    val += lst1[-1]
    return val



def get_symbols(string:str):
    val = ""
    for char in list(string):
        val+=char if char in ["+","-", "x", "÷"] else ""
    return list(val)

def get_numbers(string:str):
    return [l for i in string.split('+') for j in i.split('-')
        for k in j.split('x') for l in k.split('÷')]

def is_number(string:str, mode:Mode = Mode.DEC)->bool:
    val = True
    match mode:
        case Mode.HEX:
            val = is_num_hex(string)

        case Mode.DEC:
            val = is_num_dec(string)

        case Mode.OCT:
            val = is_num_oct(string)

        case Mode.BIN:
            val = is_num_bin(string)

        case _:
            val = False

    return val

def is_num_hex(string):
    dec_count = 0

    for char in list(string):
        if char == ".":
            dec_count +=1

        if dec_count>1:
            return False

        if not char.isnumeric() and char != ".":
            if (ord(char) < 65 and ord(char) > 71) or (ord(char) <97 and ord(char) > 102):
                if (list(string).index(char)) == 0:
                    if (char != "-"):
                        print("wron leter")
                        return False
                else:
                    return False
    return True

def is_num_dec(string):
    dec_count = 0

    for char in list(string):
        if char == ".":
            dec_count +=1

        if dec_count>1:
            return False

        if not char.isnumeric() and char != ".":
            if list(string).index(char) == 0:
                if((char != "-")):
                    return False
            else:
                return False
    return True

def is_num_oct(string):
    dec_count = 0

    for char in list(string):
        if char == ".":
            dec_count +=1

        if dec_count>1:
            return False

        if (ord(char)<48 or ord(char)>55) and char != ".":
            if list(string).index(char) == 0:
                if((char != "-")):
                    return False
            else:
                return False
    return True

def is_num_bin(string):
    dec_count = 0

    for char in list(string):
        if char == ".":
            dec_count +=1

        if dec_count>1:
            return False

        if (char != "0" and char!= "1") and char != ".":
            if list(string).index(char) == 0:
                if((char != "-")):
                    return False
            else:
                return False
    return True
