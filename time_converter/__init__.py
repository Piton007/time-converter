import re

SECOND = 1000
MINUTE = SECOND * 60
HOUR = MINUTE * 60



formats = {
    "s":SECOND,
    "m":MINUTE,
    "h":HOUR
}

REGX_PATTERN = r"^([0-9]*)\w$"

def calculateMilis(time):
     """
     calculate milis with various time formats 
     Xh : Xhours
     Xs : Xseconds
     Xm : Xminutes
    """
    try:
        match = re.search(REGX_PATTERN,time)
        general_group = match.group(0)
        cant = match.group(1)
        return  -1 if formats.get(general_group[-1]) is None else int(cant) * formats.get(general_group[-1])  
    except :
        return -1
   


if __name__ == "__main__":

    def input_text_doesnt_match():
        time ="hellom"
        result = -1
        assert calculateMilis(time) == result

    def time_suffix_is_invalid():
        time = "25b"
        result = -1
        assert calculateMilis(time) == result
    def integer_part_is_negative():
        time = "-25m"
        result = 25 * MINUTE
        assert calculateMilis(time)
    def time_suffix_is_valid():
        time = "20m"
        result = 20*MINUTE
        assert calculateMilis(time) == result

    input_text_doesnt_match()
    integer_part_is_negative()
    time_suffix_is_valid()
    time_suffix_is_invalid()
    
    