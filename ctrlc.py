def keyboard_shortcut(text):
    clipboard, copied_text, i = [], '', 0
    while i < len(text.split()):
        current_word = text.split()[i]
        if i != len(text.split())-1 and current_word == "Ctrl":
            command = ''.join(text.split()[i:i+3])
            if command == "Ctrl+C" or command == "Ctrl+V":
                if command == "Ctrl+C": 
                    copied_text = ' '.join(clipboard)
                elif command == "Ctrl+V": 
                    clipboard += copied_text.split()
            i += 3
        else: 
            clipboard.append(current_word)
            i += 1
    return ' '.join(clipboard)

def main():
    text = "The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V"
    print(keyboard_shortcut(text))
main()

#the egg and the egg and the spoon