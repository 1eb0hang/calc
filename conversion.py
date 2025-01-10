from mode import Mode

def convert(string:str, input:Mode, output:Mode):
    val = ""
    match input:
        case Mode.HEX:
            match output:
                case Mode.DEC:
                    val = HEX.to_dec(text)

                case Mode.OCT:
                    val = HEX.to_oct(text)

                case Mode.BIN:
                    val = HEX.to_bin(text)

        case Mode.DEC:
            match mode:
                case Mode.HEX:
                    val = DEC.to_hex(text)

                case Mode.OCT:
                    val = DEC.to_oct(text)

                case Mode.BIN:
                    val = DEC.to_bin(text)

        case Mode.OCT:
            match mode:
                case Mode.HEX:
                    val = OCT.to_hex(text)

                case Mode.DEC:
                    val = OCT.to_dec(text)

                case Mode.BIN:
                    val = OCT.to_bin(text)

        case Mode.BIN:
            match mode:
                case Mode.HEX:
                    val = BIN.to_hex(text)

                case Mode.DEC:
                    val = BIN.to_dec(text)

                case Mode.OCT:
                    val = BIN.to_oct(text)
    return val

class HEX:
    def __new__(cls):
        return None

    def to_dec(string:str):
        val = int(string, 16)
        val = hex(val)
        return str(val)

    def to_bin(string:str):
        pass

    def to_oct(string:str):
        pass

class DEC:
    def __new__(cls):
        return None

    def to_hex(string:str):
        val = int(string)
        val = hex(val)
        return str(val)

    def to_bin(string:str):
        pass

    def to_oct(string:str):
        pass

class OCT:
    def __new__(cls):
        return None

    def to_dec(string:str):
        pass

    def to_bin(string:str):
        pass

    def to_hex(string:str):
        pass

class BIN:
    def __new__(cls):
        return None

    def to_dec(string:str):
        pass

    def to_hex(string:str):
        pass

    def to_oct(string:str):
        pass
