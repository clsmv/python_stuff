def get_hundreds(hundred):
    if(str(hundred)[1]=='0' and str(hundred)[2]=='0'): return get_units(int(str(hundred)[0])) + " " + "hundred"
    elif(str(hundred)[1]=='0'): return get_units(int(str(hundred)[0])) + " hundred " +  get_units(int(str(hundred)[2]))
    else: return get_units(int(str(hundred)[0])) + " hundred " +  get_tens(int(str(hundred)[1]+str(hundred)[2]))

def get_tens(ten):
    teen_list=["eleven","twelve","thirteen","fourteen",'fifteen']
    ten_list=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if (ten>=11 and ten<=15): return teen_list[ten-11]
    elif (ten>=16 and ten<=19): return get_units(int(str(ten)[1]))+"teen"
    else:
        if str(ten)[1]=='0': return ten_list[int(str(ten)[0])-1]
        else: return ten_list[int(str(ten)[0])-1] + ' ' + get_units(int(str(ten)[1]))

def get_units(unit):
    unit_list=["one","two","three","four","five","six","seven","eight","nine"]
    return unit_list[unit-1]

def num_to_english(num):
    if num!=0:
        if len(str(num)) == 1: return get_units(num)
        elif len(str(num)) == 2: return get_tens(num)
        elif len(str(num)) == 3: return get_hundreds(num)
        else: return "N/A"
    else: return "zero"

def main():
    for i in range(1000):
        print(i,'=',num_to_english(i))
main()
