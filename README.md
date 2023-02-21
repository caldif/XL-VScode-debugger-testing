# Debugger Workshop
In this workshop you will gain familiarity with the VS Code built in debugger!



## Part 1 - Hello World
In this section you will gain familiarity with the basic tools of the debugger. Go to the `hello.py`  and click the run and debug button in the sidebar. This will run the code in the debugger and an error will be thrown, fix this error before proceeding.

After the error is fixed add a breakpoint to your code somewhere on line 7.
>### Breakpoints
> Break points are places in the code you tell the debugger to stop so you can look at everything that is happening at the exact instant when the code stops. You can place a break point by clicking to the left of any line number in the code. This will make a red circle appear designating the start of that line as a breakpoint

After placing the breakpoint re-run the debugger. When the debugger stops at your break points there is now a pannel to the left containing sections for variables, watch, call stack, and breakpoints.

In variables pannel you should see the greeting variable that we have initilized with its value `"hello"`, you can change this value for the remainder of this iteration of the code by double clicking on it and entering a new value. Try changing the vairable by and seeing how it affects the two print statements

Naviage through the rest of the code using the buttons that appeared at the top of the screen.
>### Navigation
>There are 6 navigation buttons, in order they are:
>* Continue: The code resumes running as norma until the next breakpoint
>* Step over: Executes the next function as a single command without inspecting or following its component steps.
>* Step into: Enter the next method to follow its execution line-by-line.
>* Step out: When inside a function finishes executing the remainder of that code
>* Restart: Terminates the current debugging session and starts a new one from the beggining of the code
>* Stop: terminates the debugging session

Try placing different breakpoints, changing vairables and different navigations until you have an understanding.

## Part 2 - Insertion Sort

Open the `insertion.py` file. this is a sorting algorithm that puts a list in order. Add a breakpoint on line 10. You can see the array chaning every time the breakpoint is hit in the loop as it sorts.

Now we are going to try adding a conditional breakpoint to the loop.
> ### Conditional Breakpoints
> Conditional breakpoints have the debugger halt only under certain circumstances as opposed to a normal breakpoint which stops the debugger no matter what. There are two types of conditional breakpoints hit, and expression. 
>
> Hit breakpoints halt the debugger after that breakpoint has been passed a certain number of times. Expression breakpoints stop the debugger if a certain equation that you specify is met.

You add these breakpoints by right clicking instead of left clicking when going to add a breakpoint and selecting `conditional breakpoint`. Try adding a breakpoint on line 15 that halts the debugger every 3 times it is hit. Experiment with hit counts of different numbers.

Now try adding an expression breakpoint that will stop the code when the third number is in it's correct, sorted place in the given list in main.

If you want to keep track of the array being sorted without halting the debugger you can try adding a log point.
>### Log points
>Log points function similar to print statements without cluttering up your code. They print whatever is specified in the expression out to the debug console. If you wish to print variable contents you simply need to surround the variable name with {}

## Part 3 - Challenge
Use what you have learned about breakpoints, log points, and variable changing to solve the puzzle in `final.py`. You are only allowed to place breakpints in the functions, not in main, for the purposes of this puzzle. There are two functions to work with.

In function one you are only allowed to modify the x variable. Use breakpoints and logpoints to stop the program at the right time so that modifying x will result in the correct return value.

In function two you are only allowed to modify the letters variable, you are allowed to change this variable exactly 6 times. By changing the letter variable transformed the passed string into a hidden message. The correct message is in the solutions.txt file.
