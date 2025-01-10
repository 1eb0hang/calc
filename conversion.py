from mode import Mode

def convert(string:str, input:Mode, output:Mode):
    val = ""
    match input:
        case Mode.HEX:
            match output:
                case Mode.DEC:
                    val = HEX.to_dec(string)

                case Mode.OCT:
                    val = HEX.to_oct(string)

                case Mode.BIN:
                    val = HEX.to_bin(string)

        case Mode.DEC:
            match output:
                case Mode.HEX:
                    val = DEC.to_hex(string)

                case Mode.OCT:
                    val = DEC.to_oct(string)

                case Mode.BIN:
                    val = DEC.to_bin(string)

        case Mode.OCT:
            match output:
                case Mode.HEX:
                    val = OCT.to_hex(string)

                case Mode.DEC:
                    val = OCT.to_dec(string)

                case Mode.BIN:
                    val = OCT.to_bin(string)

        case Mode.BIN:
            match output:
                case Mode.HEX:
                    val = BIN.to_hex(string)

                case Mode.DEC:
                    val = BIN.to_dec(string)

                case Mode.OCT:
                    val = BIN.to_oct(string)
    return val

class HEX:
    def __new__(cls):
        return None

    def to_dec(string:str):
        val = int(string, 16)
        return str(val)

    def to_bin(string:str):
        val = bin(int(string, 16))[2:]
        return val

    def to_oct(string:str):
        val = oct(int(string, 16))[2:]
        return val

class DEC:
    def __new__(cls):
        return None

    def to_hex(string:str):
        val = int(string)
        val = hex(val)[2:]
        return str(val)

    def to_bin(string:str):
        val = bin(int(string))[2:]
        return val

    def to_oct(string:str):
        val = oct(int(string))[2:]
        return val

class OCT:
    def __new__(cls):
        return None

    def to_dec(string:str):
        val = int(string, 8)
        return val
\
    def to_bin(string:str):
        val = int(string, 8)
        return val

    def to_hex(string:str):
        val = hex(int(string, 8))[2:]
        return val

class BIN:
    def __new__(cls):
        return None

    def to_dec(string:str):
        val = int(string, 2)
        return val

    def to_hex(string:str):
        val = hex(int(string, 2))[2:]
        return val

    def to_oct(string:str):
        val = oct(int(string, 2))[2:]
        return val


"""
def convert_number(value, from_base, to_base):
    \"""
    Converts a number between various bases.

    Parameters:
    - value: The number as a string (for bases > 10).
    - from_base: Base of the input number (e.g., 2, 8, 10, 16).
    - to_base: Desired base of the output number (e.g., 2, 8, 10, 16).

    Returns:
    - The converted number as a string.
    \"""
    # Convert to decimal first
    decimal_value = int(value, from_base)

    # Convert from decimal to the desired base
    if to_base == 2:
        return bin(decimal_value)[2:]
    elif to_base == 8:
        return oct(decimal_value)[2:]
    elif to_base == 10:
        return str(decimal_value)
    elif to_base == 16:
        return hex(decimal_value)[2:]
    else:
        raise ValueError("Unsupported base!")

# Examples
print(convert_number("1f", 16, 8))  # Hex to Oct
print(convert_number("1f", 16, 2))  # Hex to Bin
print(convert_number("31", 10, 8))  # Dec to Oct
print(convert_number("11111", 2, 10))  # Bin to Dec
"""
