import random

#generate_command() will receive a command_number (to know in which instruction we're at),
#and will return the first part of the command. 
def generate_command(command_number):
    #names[] is a list that contains names that are similar to Simon.
    names = ['Saemon says','Simn says','Samuel says','Susan says','Saul says','Steven says','Simeon says','Spencer says']
    #I also created this operations list.
    operations = ['add','subtract','multiply by']
    
    #The name will be set as 'Simon says' by default.
    name = 'Simon says'
    #The program picks a random number from 1 to 10. If the number's even, the name or the instruction will change. 
    #There's always a 50% chance that the command will change it's name or action. 
    if (random.randint(1,10)%2==0):
        if command_number==0:
            #This is exclusive for the first instruction. It follows the same rule as before.
            #For this instruction, the names can be substituted with the word 'Firstly'. 
            if (random.randint(1,10)%2==0): name = "Firstly,"
            #In case the random number is odd, the program will pick a random name from the list of names.
            else: name = random.choice(names)
        else:
            #For the rest of instructions, the names of the list can be substituted with the word 'then'.
            #This works just as the previous lines of code. 
            if (random.randint(1,10)%2==0): name = "Then"
            else: name = random.choice(names)

    #Once the name or action is obtained, the program picks a random operation from the list operations[]. 
    operation = random.choice(operations)
    #Finally, everything is concatenated and returned in one string
    command = name + ' ' + operation
    return command

#simon_says() will return the output
def simon_says():
    #the acum variable will store the result of the operations. 
    acum = 0
    #This program will randomly iterate from 2 to 6 times.
    for i in range (0,random.randint(1,5)):
        #A random number from 1 to 10 is generated and the concatenated to the first part of the command.
        number = random.randint(1,10)
        command = generate_command(i) + ' ' + str(number)
        print(command)
        #The split() method is used to re-store the name and the operation of the command. 
        name = command.split()[0]
        operation = command.split()[2]
        #If he name is Simon, then the program will do the operation. Otherwise, acum will remain as 0
        if name == 'Simon':
            if (operation == 'add'): acum += number
            elif (operation == 'subtract'): acum -= number
            else: acum *= number
    return acum

#It's really important to point out that the first operation will always be againts 0. 
#If the first operation is a multiplication, even if the command says 'Simon says', the output will remain 0. 
#Also, this program also considers negative numbers.

#Finally, the main method will call simon_says() and will print the output.
def main():
    out = simon_says()
    print('output:',out)

if __name__ == '__main__':
    main()