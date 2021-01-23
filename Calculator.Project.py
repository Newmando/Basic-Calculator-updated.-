print('Hello user welcome to the calculator')

while True:
# This is the first entry for the user and can only be entered in numbers or resets.   
    while True:
        try:
            Num1 = float(input('Enter first number:  '))
            break
        except ValueError:
            print('Please only use numbers in the calculator')
            continue

# Operator code limits user to only certain keys and 1 Character. 
    def getChar():
        Op = input('Please enter an operator out of the following {+ Add - Subtract / Divied * Multiply } ')# Operator.
        allowedChars = '+-/*'
        while(len(Op)!= 1 or Op not in allowedChars):
            Op = input('Enter character any of the following {+ Add - Subtract / Divied * Multiply } ')
        return Op
    

    Op = getChar()
    print(Op)

    

#Second Number input with same entry requirements.
    while True:
        try:
            Num2 = float(input('Enter second number '))
            break
        except ValueError:
            print('Please only use numbers in the calculator')
            continue

        
    Fin = ('Your answer is ') # A neatier input than typing out each print statment.
    

#If elif statement with all different outcomes for the operator input.         
    if Op == '+':
        print((Fin) + str((Num1)+ (Num2)))
    elif Op == '-':
         print ((Fin) + str((Num1) - (Num2)))
    elif Op == '*':
        print((Fin) + str((Num1) * (Num2)))
    elif Op == '/':
        print ((Fin) + str((Num1)/ (Num2)))
    print('Thank you for using calculator')
    continue



                 
                 

    
      
                
