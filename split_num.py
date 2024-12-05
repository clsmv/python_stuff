def split_num(num):
    result = []
    abs_num=abs(num)
    while abs_num > 0:
        result.append(abs_num%10)
        abs_num//=10
    result.reverse()
    return [i * -1 for i in result] if num < 0 else result

def main():
    print(split_num(-904309834))
main()