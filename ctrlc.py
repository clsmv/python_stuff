def keyboard_shortcut(text):
    clipboard, copied_text, i = [], '', 0
    words = text.split()
    while i < len(words):
        current_word = words[i]
        command = ''.join(words[i:i+3])
        if command == "Ctrl+C": 
            copied_text = ' '.join(clipboard)
            i += 3
        elif command == "Ctrl+V": 
            clipboard += copied_text.split()
            i += 3
        else: 
            clipboard.append(current_word)
            i += 1
    return ' '.join(clipboard)

def main():
    text1 = "the egg and Ctrl + C Ctrl + V the spoon"
    text2 = "WARNING Ctrl + V Ctrl + C Ctrl + V"
    text3 = "The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V"
    print(keyboard_shortcut(text1)) # "the egg and the egg and the spoon"
    print(keyboard_shortcut(text2)) # "WARNING WARNING"
    print(keyboard_shortcut(text3)) # "The The Town The The Town"

if __name__ == "__main__":
    main()