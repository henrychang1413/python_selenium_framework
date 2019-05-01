# coding=utf-8
# author:  henry chang
# email : henrychang1413@gmail.com

class BinarytoDecimal:
    """ input binary , output is Decimal """
    def __init__(self, input_num):
        self.__input_num = input_num

    def covertx(self):
        total = 0
        num_list = list(str(self.__input_num))
        j = len(num_list)
        for x in num_list:
            total += int(x)*(2**(j-1))
            j -=1
        return total

class DecimalToBinary:
    """ input decimal , output is binary """
    def __init__(self, input_num):
        self.__input_num = input_num

    def covertx(self):
        div_int = int(self.__input_num/2)
        div_mod = self.__input_num%2
        bilist = [str(div_mod)]
        while div_int > 1 :
            div_mod = div_int%2
            div_int = int(div_int/2)
            bilist.append(str(div_mod))

        bilist.append(str(div_int))
        binum = "".join(reversed(bilist))
        return binum

class DecimalToHexadecimal :
    """ input decimal , output is Hexadecimal """

    def __init__(self, input_num):
        self.__input_num = input_num

    def __mapHex(self, dec):
        if dec == 10 :
            return "A"
        elif dec == 11 :
            return "B"
        elif dec == 12 :
            return "C"
        elif dec == 13 :
            return "D"
        elif dec == 14 :
            return "E"
        elif dec == 15 :
            return "F"

    def covertx(self):
        div_int = int(self.__input_num/16)
        div_mod = self.__input_num%16
        if div_mod > 9:
            bilist = [str(self.__mapHex(div_mod))]
        else:
            bilist = [str(div_mod)]

        while div_int > 15 :
            div_mod = div_int%16
            div_int = int(div_int/16)
            if div_mod > 9:
                bilist.append(str(self.__mapHex(div_mod)))
            else:
                bilist.append(str(div_mod))

        bilist.append(str(div_int))
        binum = "".join(reversed(bilist))
        return binum


class HexadecimalToDecimal:
    """ input  Hexadecimal, output is decimal """

    def __init__(self, input_num):
        self.__input_num = input_num

    def __CmapHex(self, dec):
        if dec == "0":
            return 0
        elif dec == "1":
            return 1
        elif dec == "2":
            return 2
        elif dec == "3":
            return 3
        elif dec == "4":
            return 4
        elif dec == "5":
            return 5
        elif dec == "6":
            return 6
        elif dec == "7":
            return 7
        elif dec == "8":
            return 8
        elif dec == "9":
            return 9
        elif dec == "A":
            return 10
        elif dec == "B":
            return 11
        elif dec == "C":
            return 12
        elif dec == "D":
            return 13
        elif dec == "E":
            return 14
        elif dec == "F":
            return 15

    def covertx(self):
        total = 0
        num_list = list(str(self.__input_num))
        j = len(num_list)
        for x in num_list:
            total += self.__CmapHex(x)*(16**(j-1))
            j -=1
        return total


# if __name__ == "__main__":
#     x = DecimalToHexadecimal(560)
#     print(x.covertx())

#     y = DecimalToBinary(88)
#     print(y.covertx())

#     z = HexadecimalToDecimal("1DFA")
#     print(z.covertx())

#     w = BinarytoDecimal(11010)
#     print(w.covertx())
