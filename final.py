#create functions that return variables to a main
#have them create breakpoints in the fucntions to stop it from reaching a certain point
#then live change a variable so the return is a certain thing
#using conditional breakpoints

def function_1(x: int) -> int: #using breakpoints and log points modify x in this function to return the correct number 
    i: int = 0
    while(i <= 5000):
        x += 3
        if(x % 66 == 0):
            i = i /3
            return i
        i += 6
    return 0

def function_2(y: str) -> str: #using breakpoints and logpoints change the letter variable 6 times to spell out a new message
    new: str = ""
    for letter in y:
        new += letter
    return new

def main() -> None:
    x: int = 0
    x = function_1(x)
    if(x != 10):
        print("Try again :(")
        return
    y = "Lou shaved the poodles"
    y = function_2(y)
    print(y) #Lou shaved the poodles -> You solved the problem


if __name__ == '__main__':
    main()