# Debugger Workshop
In this workshop you will gain familiarity with the VS Code built in debugger!



## Part 1 - Hello World
In this section you will gain familiarity with the basic tools of the debugger. Go to the `hello.py`  and click the run and debug button in the sidebar. This will run the code in the debugger and an error will be thrown, fix this error before proceeding.

After the error is fixed add a breakpoint to your code somewhere before line 10.
>### Breakpoints
> Break points are places in the code you tell the debugger to stop so you can look at everything that is happening at the exact instant when the code stops. You can place a break point by clicking to the left of any line number in the code. This will make a red circle appear designating the start of that line as a breakpoint

After placing the breakpoint re-run the debugger. When the debugger stops at your break points there is now a pannel to the left containing sections for variables, watch, call stack, and breakpoints.

In variables pannel you should see the greeting variable that we have initilized with its value `hello`, you can change this value for the remainder of this iteration of the code by double clicking on it and entering a new value. Try changing the vairable by and seeing how it affects the two print statements

Naviage through the rest of the code using the buttons that appeared at the top of the screen.
>### Navigation
>There are 6 navigation buttons, in order they are:
>* Continue: The code resumes running as norma until the next breakpoint
>* Step over: Executes the next method as a single command without inspecting or following its component steps.
>* Step into: Enter the next method to follow its execution line-by-line.
>* Step out: When inside a method or function finishes executing the remainder of that code
>* Restart: Terminates the current debugging session and starts a new one from the beggining of the code
>* Stop: terminates the debugging session

Try placing different breakpoints, changing vairables and different navigations until you have an understanding.

## Part 2 - Insertion Sort

