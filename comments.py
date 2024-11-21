def check_valid_comment(comment):
    if len(comment) % 2 != 0:
        return False
    prev, open, close = '', 0, 0
    for i in range (0, len(comment),2):
        current = comment[i] + comment[i+1]
        if current == "*/": 
            close += 1
            if prev == "*/" or prev != "/*": return False
        elif current == "/*": 
            open += 1
            if prev == "/*": return False
        prev = current
    return True if open == close else False

def main():
    print(check_valid_comment("//////"))
    print(check_valid_comment("/**//**////**/"))
    print(check_valid_comment("///*/**/"))
    print(check_valid_comment("/////"))
main()