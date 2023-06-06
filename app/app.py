# programing languages project
# project name : calculator
# porject craetor : parvin akbari

# change below string to calculate(like 2*34 or 2222/2)
string = "1+2"
print()

# check the str is correct
def strCheck(str):
    error = False
    try:
        # str must start whit number character
        int(str[0])

        # str must end with number character
        int(str[-1])
    except:
        print("Syntax error!!!")
        error = True

    # in the str must exist one mark
    numberOfMarks = 0
    for char in str:
        try:
            int(char)
        except:
            numberOfMarks+=1
    if numberOfMarks != 1:
        print("Syntax error!!!")
        error = True  

    # marks must be from {"+", "-", "*", "/"}
    for char in str:
        try:
            int(char)
        except:
            if char not in ["+", "-", "*", "/"]:
                print("Syntax error!!!")
                error = True
    return error

# calculating str
def calculator(str):
    # Separate numbers and mark
    num1 = ""
    num2 = ""
    markFlag = True

    for char in str:
        try:
            int(char)

            if markFlag:
                num1+=char
            else:
                num2+=char
        except:
            mark = char
            markFlag = False

    # convert str to int
    num1 = int(num1)
    num2 = int(num2)

    # calculate answer
    if mark == "+":
        return num1 + num2
    
    elif mark == "-":
        return num1 - num2
    
    elif mark == "*":
        return num1 * num2
    
    else:
        return num1 / num2
    
# give answer
if not strCheck(string):
    print(f"=> {calculator(string)}\n")

