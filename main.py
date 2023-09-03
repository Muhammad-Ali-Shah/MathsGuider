from tkinter import *

# creates new full screen window
window = Tk()

window.geometry("960x480")
window.title("MathsGuider")

steps = [  # initializes the 2D array containing the steps
    ["Use the following index law:\nx^a + x^b = x^(a+b)"],  # index laws (x^a * x^b)

    ["Use the following index law:\nx^a - x^b = x^(a-b)"],  # index laws (x^a / x^b)

    ["Use the following index law:\n(x^a)^b = x^(a*b)"],  # index laws ((x^a)^b)

    [
        "When inputting the final answer separate with a space if applicable\n\nThe above equation is in the format ax^2 + bx + c\n\nWhat two numbers add together to make b and multiply to make c (separate these with a space)",
        "Let's call these numbers p and q. This means the above expression can be factorized as (x+p) (x+q).\nThe final answer is -p and -q.\nSeparate these numbers with a space"],
    # solving quadratic equations (when a = 1)
    ["What numbers add together to make b and multiply to make c/a",
     "Let's call these numbers p and q. Express the problem as ax^2 + px + qc.",
     "What does ax^2 + px factorize to?",
     "What does qx + c factorize to?", "What is the common factor between both",
     "Let the factors that aren't common be p and q. We can re-express the expression in the form (common factor) "
     "(px + q)",
     "Set each factor to equal 0. This will allow you to find two solutions for x. Find these and separate them with a "
     "space when inputting your answer"],
    # solving quadratic equations (when a!=1)

    ["What can you multiply each of the equations by to make the Coefficients (numbers in front of variables) of either"
     " x or y equal. \n(separate these numbers with a space if you need to multiply both equations)",
     "Either add or subtract both equations from each other to form a new equation",
     "Find the value of the unknown variable in this equation",
     "Use this value and substitute it into one of the equations to find the value of the other unknown"],
    # Simultaneous equations

    ["Pythagoras' Theorem is 'a^2 + b^2 = c^2' where C is the hypotenuse (the longest length in the triangle) and a and"
     " b are other side lengths.\nUse this equation with the known side lengths to find the unknown side length"],
    # finding a side length in a right-angle triangle given 2 lengths
    ["Area = 1/2 * base * height. Both side lengths (that aren't the hypotenuse) are the base and height as this is"
     " a right-angle triangle. \nSubstitute both side lengths for the answer"],
    # area of right-angled triangle
]


def intCheck(x):  # Checks whether a string can be converted to an integer
    try:
        int(x)
    except:
        return False  # if not an integer, False is returned
    else:
        return True  # if an integer, True is returned


def floatCheck(x):  # Checks whether a string can be converted to a float
    try:
        float(x)
    except:
        return False  # If not a float, False is returned
    else:
        return True  # If a float, True is returned


beginningMenuScreen = Frame(window)
# This is the frame that contains the group of widgets in the beginning menu screen

stepsScreen = Frame(window)
# Creates the frame for the steps screen widgets

problemTypes = [
    "Index laws",
    "Solving quadratic equations",
    "Simultaneous equations",
]  # list of problem types


def loadBeginningMenuScreen():
    beginningMenuScreen = Frame(window)
    beginningMenuScreen.pack(expand=True, fill="both")

    ProblemChoice = StringVar()
    # variable introduced to keep track of the choice selected in the option menu

    ProblemSelectorMenu = OptionMenu(beginningMenuScreen, ProblemChoice, *problemTypes)
    ProblemSelectorMenu.place(x=0, y=50)

    inputLabelText = StringVar()
    inputLabelText.set("Select an option from the problem selector menu")

    def problemInput():
        inputText1 = ProblemChoice.get()
        # this variable has been introduced to change the label text depending on the option selected (if any)

        # changes variable containing the label text depending on choice of problem from selector menu
        if ProblemChoice.get() == "Index laws":
            inputText1 = "Enter in form 'x^a (* or / ) x^b'"
        elif ProblemChoice.get() == "Factorisation":
            inputText1 = "Enter in form 'ax*b + cx*d + ...'"
        elif ProblemChoice.get() == "Rationalisation":
            inputText1 = "Enter in form 'a/bsqrt(c)'"
        elif (ProblemChoice.get() == "Solving quadratic equations"
              or ProblemChoice.get() == "Completing the square" or
              ProblemChoice.get() == "Solving quadratic equations by completing the square"):
            inputText1 = "Enter in form 'ax^2 + bx + c' and make sure the input is equal to 0"
        elif ProblemChoice.get() == "Finding the inverse of functions":
            inputText1 = "Enter f(x) in a linear or quadratic form"
        elif ProblemChoice.get() == "Simultaneous equations":
            inputText1 = "Enter both equations in both input boxes in the form 'ax + by = c'"
        elif ProblemChoice.get() == "Finding equations of circles from midpoint and radius":
            inputText1 = "Enter midpoint in the first box in the form (a,b), then enter radius in second box"
        elif ProblemChoice.get() == "Finding midpoint and radius from circle equations":
            inputText1 = "Enter equation in following form '(x-a)^2 + (y-b)^2 = c'"
        elif (ProblemChoice.get() == "Finding a side length in a right-angle triangle given two lengths" or
              ProblemChoice.get() == "Area of right-angled triangle"):
            inputText1 = "Enter the 2 shortest side lengths in both input boxes"
        inputLabelText.set(inputText1)  # sets the label text as above

    def querybox2():  # this function will either add or remove box2 depending on the problem type selected
        if (ProblemChoice.get() == "Simultaneous equations"
                or ProblemChoice.get() == "Finding equations of circles from midpoint and radius"
                or ProblemChoice.get() == "Finding a side length in a right-angle triangle given two lengths"
                or ProblemChoice.get() == "Area of right-angled triangle"):
            box2.place(x=500, y=420)
        else:
            box2.place_forget()
        box2.delete(0, 'end')

    SelectionButton = Button(
        beginningMenuScreen,
        text="Click once problem selected",
        command=lambda: [problemInput(), querybox2()]
    )

    SelectionButton.place(x=102, y=82)

    # button that executes the problemInput command to change the label text depending on the selected problem type,
    # as well either add or remove box2 depending on whether it is require

    InputLabel = Label(beginningMenuScreen, textvariable=inputLabelText).place(x=490, y=370)
    # This adds text that accompanies the input box

    box1 = Entry(beginningMenuScreen)
    box1.place(x=500, y=395)
    # This creates the (first) input box

    box2 = Entry(beginningMenuScreen)

    # If it is required, the second input box is also added

    def firstStepClicked():  # this command contains all the code that will execute once the "first step" button is clicked
        input1 = box1.get() + "                        "
        input2 = box2.get() + "                        "

        # Sets the two variables to the inputs into the input boxes

        def inputCheck(input1, input2):
            # function containing input checking algorithms. Returns True if input is valid
            # , and False otherwise

            # See design for all input checking algorithms
            if ProblemChoice.get() == "Index laws":  # Input check for index laws
                if (
                        input1[0] == 'x'
                        and input1[1] == '^'
                        and intCheck(input1[2]) == True
                        and (input1[4] == '*' or input1[4] == '/')
                        and input1[6] == 'x' and input1[7] == '^' and intCheck(input1[8])):
                    return True

                elif (
                        input1[0] == '('
                        and input1[1] == 'x'
                        and input1[2] == '^'
                        and intCheck(input1[3]) == True
                        and input1[4] == ")"
                        and input1[5] == '*'
                        and intCheck(input1[6])):
                    return True

                else:
                    return False

            elif ProblemChoice.get() == "Solving quadratic equations":  # Input check for solving quadratic equations
                i = 0
                if intCheck(input1[0]):
                    i = 1
                if (
                        input1[i] == 'x'
                        and input1[i + 1] == '^'
                        and input1[i + 2] == '2'
                        and (input1[i + 4] == '+' or input1[i + 4] == '-')
                ):
                    if intCheck(input1[i + 6]):
                        i = i + 1

                    if (
                            input1[i + 6] == 'x'
                            and (input1[i + 8] == '+' or input1[i + 8] == '-')
                            and intCheck(input1[i + 10])):
                        return True
                    else:
                        return False
                else:
                    return False

            elif ProblemChoice.get() == "Simultaneous equations":  # Input check for simultaneous equations
                def validSimultaneousEquation(x):
                    i = 0
                    if intCheck(x[0]) == True:
                        i = 1

                    if x[i] == 'x' and (x[i + 2] == '+' or x[i + 2] == '-'):
                        if intCheck(x[i + 4]):
                            i = i + 1

                        if x[i + 4] == 'y' and x[i + 6] == '=' and intCheck(x[i + 8]):
                            return True
                        else:
                            return False
                    else:
                        return False

                return validSimultaneousEquation(input1) and validSimultaneousEquation(input2)

            elif (ProblemChoice.get() == "Finding a side length in a right-angle triangle given two lengths"
                  or ProblemChoice.get() == "Area of right-angled triangle"):
                # input check for right-angle triangle related types
                if floatCheck(input1) and floatCheck(input2):
                    return True
                else:
                    return False

        if inputCheck(input1, input2):
            beginningMenuScreen.destroy()
            loadStepsScreen(input1, input2)  # the steps screen will load if the input is valid
        else:
            invalidInputLabel = Label(beginningMenuScreen, fg="red",
                                      text="Invalid input. Read the text on top of the input box carefully")
            invalidInputLabel.place(x=500, y=455)

    FirstStepButton = Button(beginningMenuScreen, text="First step", command=firstStepClicked).place(x=700, y=395)
    # Displays "First step" button. Upon clicking it will execute the firstStepClicked function

    ShowPreviousQuestionsButton = Button(beginningMenuScreen, text="Show previous questions").place(x=10, y=445)
    # Displays "Show previous questions" button

    SaveProblemButton = Button(beginningMenuScreen, text="Save problem").place(x=688, y=425)

    # Displays "Save problem" button

    def loadStepsScreen(input1, input2):  # essentially displays all the widgets in the steps screen
        stepsScreen = Frame(window)
        stepsScreen.pack(expand=True, fill="both")

        def backToStart():
            stepsScreen.destroy()
            loadBeginningMenuScreen()  # if the back to start button is clicked, this function will be called that destroy the steps screen calls the loadBeginningMenuScreen function

        backToStartButton = Button(stepsScreen, text="Back to start", command=backToStart).place(x=3, y=1)
        # Button that returns the user to the beginning menu screen

        inputText = StringVar()
        if input2 == "                        ":
            inputText.set(
                input1[:-20])  # If box2 is empty, the text displaying the input will output only the text in boxl
        else:
            inputText.set(input1[:-20] + "\n" + input2[
                                                :-20])  # if box 2 isn't empty, the text displaying the output will output both the text in boxl and box2(on separate lines

        solvedSteps = 0  # this counts how many steps have been completed
        stepInput = None

        # below are the variables used for validation
        if ProblemChoice.get() == "Simultaneous equations":
            a1 = 0
            a2 = 0
            b1 = 0
            b2 = 0
            c1 = 0
            c2 = 0
            x = 0
            y = 0


        elif ProblemChoice.get() == "Solving quadratic equations":
            p = 0
            q = 0

        def stepProcess(input1, input2):
            stepAnswer = None
            finalAnswer = None
            finalAnswer1 = None
            finalAnswer2 = None
            # the above has been added to make the answer validate against all 3 final answer varaibles
            # this means that less code has to be written (eg. determining a variable is empty)
            nonlocal solvedSteps
            nonlocal stepInput
            # the above two variables aren't local to the function, but are required by it nonetheless

            if ProblemChoice.get() == "Index laws":
                if input1[0] == '(':
                    a = int(input1[3])
                    b = int(input1[6])  # a and b are defined such that inputl = (x%a)*b
                    finalAnswer = "x^" + str(a * b)  # applies index law to input

                else:
                    a = int(input1[2])
                    operator = input1[4]
                    b = int(input1[8])

                    # a, operator and b are defined such that inputl = 'x%a (operator) x*b

                    if operator == '*':
                        finalAnswer = 'x^' + str(a + b)  # if operator = '*', the final answer will be x (a+b)
                    else:
                        finalAnswer = 'x^' + str(a - b)  # otheruise, the final answer will be x*(a-b)
                    # index law applied to input

            elif ProblemChoice.get() == "Solving quadratic equations":
                if solvedSteps == 0:
                    # This part below finds the coefficient of each terr
                    a = 1
                    if intCheck(input1[6]) == True:
                        b = int(input1[4] + input1[6])
                        c = int(input1[9] + input1[11:12])
                    else:
                        b = int(input1[4] + "1")
                        c = int(input1[8] + input1[10:11])
                    # variables a, b and c are assigned in the form
                    # if there is no coefficient before any of the 3

                    nonlocal p
                    nonlocal q
                    # these are the global variables used

                    # This part searches for solutions
                    solutionsFound = False  # this is a flag for whether :
                    i = 1  # this index is incremented by 1 until reaching

                    while i != abs(c) + 1 and solutionsFound == False:
                        if (c % i == 0) and (i + (c / i) == b):
                            p = -int(i)
                            q = -int(c / i)
                            solutionsFound = True

                        else:
                            i = i - 1
                    if solutionsFound == False:  # if no solutions
                        finalAnswer1 = "NO SOLUTIONS"
                        finalAnswer2 = ""
                    else:  # otherwise, there are two possible fine
                        finalAnswer1 = str(p) + " " + str(q)
                        if p == q:  # If both solutions are equival
                            finalAnswer2 = p
                        else:
                            finalAnswer2 = str(q) + " " + str(p)

            elif ProblemChoice.get() == "Simultaneous equations":  # B:
                nonlocal a1
                nonlocal a2
                nonlocal b1
                nonlocal b2
                nonlocal c1
                nonlocal c2
                nonlocal x
                nonlocal y
                # this is required so that these global variables can be accessed and modified

                if solvedSteps == 0:
                    def equationExtract(equation):  # this function th;
                        if intCheck(equation[0]) == True:
                            ae = int(equation[0])
                            i = 1  # this index is so that if a number is at the start, it will run from the next index

                        else:
                            i = 0
                            ae = 1
                        if intCheck(equation[i + 4]) == True:
                            be = int(equation[i + 2] + equation[i + 4])
                            i = i + 1
                        else:
                            be = int(equation[i + 2] + '1')
                        try:  # this checks whether c has two digits
                            int(equation[i + 9])
                        except:
                            ce = int(equation[i + 8])  # if c doesn't have two digits, it is counted individually
                        else:
                            ce = int(equation[i + 8] + equation[i + 9])
                        return ae, be, ce  # an array is returned. ae, be, ce

                    equation1 = equationExtract(input1)
                    equation2 = equationExtract(input2)
                    a1 = equation1[0]
                    b1 = equation1[1]
                    c1 = equation1[2]
                    a2 = equation2[0]
                    b2 = equation2[1]
                    c2 = equation2[2]

                    if (a1 == a2) or (b1 == b2):  # if two of
                        a = a1 - a2
                        b = b1 - b2
                        c = c1 - c2

                    else:  # otherwise, equation 2 will be
                        a3 = a2 * (a1 / a2)
                        b3 = b2 * (a1 / a2)
                        c3 = c2 * (a1 / a2)
                        # as a3 and al are equal, al, bl
                        a = a3 - a1
                        b = b3 - b1
                        c = c3 - c1

                    if a == 0:
                        # either a or b is equal to zero
                        # if a is equal to 0, y=c/b and x=(c
                        y = int(c / b)
                        x = int((c1 - b1 * y) / a1)
                    else:
                        # otherwise, x=c/a and y=(cl-al*x)/b
                        x = int(c / a)
                        y = int((c1 - a1 * x) / b1)
                    finalAnswer = str(x) + " " + str(y)

                if solvedSteps == 1:
                    stepInput = stepAnswerBox.get()

                    if intCheck(stepInput) == True:  # if the step input comprises of one nu
                        # below one of the equations(a, b or c¢ for one equation) will be r
                        if int(stepInput) == abs(a1 / a2) or int(stepInput) == abs(b1 / b2):
                            a2 = a2 * int(stepInput)
                            b2 = b2 * int(stepInput)
                            c2 = c2 * int(stepInput)
                        else:
                            a1 = a1 * int(stepInput)
                            b1 = b1 * int(stepInput)
                            c1 = c1 * int(stepInput)

                    else:
                        a1 = a1 * int(stepInput[0])
                        b1 = a1 * int(stepInput[0])
                        c1 = a1 * int(stepInput[0])
                        a2 = a1 * int(stepInput[2])
                        b2 = a1 * int(stepInput[2])
                        c2 = a1 * int(stepInput[2])

                    if a1 == -a2 or b1 == -b2:  # if both a or b terms are negatives of each
                        try:
                            a = int(a1 + a2)
                            b = int(b1 + b2)
                            c = int(c1 + c2)
                        except:
                            a = a1 + a2
                            b = b1 + b2
                            c = c1 + c2

                        if a == 0:  # the answer to this step depends on which of a or b 1s equal to zero
                            stepAnswer = str(b) + 'y = ' + str(c)
                        else:
                            stepAnswer = str(a) + 'x = ' + str(c)

                    else:
                        stepAnswer = None

                if solvedSteps == 3:
                    stepInput = stepAnswerBox.get()
                    if int(stepInput) == x:
                        stepAnswer = y
                    else:
                        stepAnswer = x

            return stepAnswer, finalAnswer, finalAnswer1, finalAnswer2

        incorrectStepInputLabel = Label(stepsScreen, text="Incorrect. Go through carefully.", fg="red")

        def checkStepAnswer():
            nonlocal solvedSteps
            nonlocal input1
            nonlocal input2
            nonlocal answers
            stepAnswer = answers[0]
            finalAnswer = answers[1]
            finalAnswer1 = answers[2]
            finalAnswer2 = answers[3]
            stepInput = stepAnswerBox.get()
            if stepInput == "":
                return

            try:
                stepInput = int(stepInput)  # if stepInput is an integer but stored
            except:
                pass

            if stepInput == stepAnswer:
                solvedSteps += 1  # if stepInput = stepAnswer, the solvedSteps count
                try:
                    stepText.set(stepText.get() + "\n\n" + steps[5][solvedSteps])
                    answers = stepProcess(input1, input2)
                except:
                    stepsScreen.destroy()
                    loadBeginningMenuScreen()  # if the step is out of range, the st
                else:
                    incorrectStepInputLabel.place_forget()  # if the user is correct



            elif ProblemChoice.get() == "Solving quadratic equations":
                nonlocal p
                nonlocal q
                if solvedSteps == 0:  # the code below will only execute if this is
                    if intCheck(stepInput) != True:  # if stepInput was an integer
                        try:
                            int(stepInput[1])
                        except:
                            u = int(stepInput[0])
                            i = 0
                        else:
                            u = int(stepInput[0] + stepInput[1])
                            i = 1

                        try:
                            int(stepInput[i + 3])
                        except:
                            v = int(stepInput[i + 2])
                        else:
                            v = int(stepInput[i + 2] + stepInput[i + 3])

                        if (u == -p and v == -q) or (u == -q and v == -p):
                            stepText.set(stepText.get() + "\n\n" + steps[3][1])  #
                            solvedSteps = 1
                            stepAnswer = None
                            incorrectStepInputLabel.place_forget()

                        else:
                            incorrectStepInputLabel.place(x=40, y=425, anchor=W)

                    else:
                        incorrectStepInputLabel.place(x=40, y=425, anchor=W)

            elif ProblemChoice.get() == "Simultaneous equations":  # this parti.

                if solvedSteps == 0:  # checks if multiplied number is equal on
                    if (stepInput == abs(a1 / a2)
                            or stepInput == abs(b1 / b2)
                            or stepInput == abs(a2 / a1)
                            or stepInput == abs(b2 / b1)):
                        solvedSteps = 1
                        stepText.set(stepText.get() + "\n\n" + steps[5][1])
                        answers = stepProcess(input1, input2)
                        incorrectStepInputLabel.place_forget()  # if the user i

                    else:
                        incorrectStepInputLabel.place(x=40, y=425, anchor=W)
                elif solvedSteps == 1:
                    if intCheck(stepInput[0]) == False:

                        # if the first character in stepInput is either 'x' o
                        # the index i also equals -1 so that one position to

                        p = 1
                        i = -1
                    else:
                        p = int(stepInput[0])  # creates two variables, p and gq
                        i = 0
                        if intCheck(stepInput[1]) == True:
                            # this checks if the first number has two digits
                            # if this is the case, p is stored as the two dig
                            p = int(stepInput[0] + stepInput[1])
                            i = 1

                    q = int(stepInput[i + 5])
                    try:
                        int(stepInput[i + 6])
                    except:
                        pass
                    else:
                        q = int(stepInput[i + 5] + stepInput[i + 6])  # again, it
                    if (((p == a1 - a2 or p == b1 - b2) and q == c1 - c2)  # this
                            or ((p == a2 - a1 or p == b2 - b1) and q == c2 - c1)):
                        solvedSteps = 2
                        stepText.set(stepText.get() + "\n\n" + steps[5][2])  #
                        answers = stepProcess(input1, input2)
                        incorrectStepInputLabel.place_forget()  # if the user i
                    else:
                        incorrectStepInputLabel.place(x=40, y=425, anchor=W)
                elif solvedSteps == 2:
                    if int(stepInput) == x or int(stepInput) == y:  # here we a
                        solvedSteps = 3
                        stepText.set(stepText.get() + "\n\n" + steps[5][2])
                        answers = stepProcess(input1, input2)
                        incorrectStepInputLabel.place_forget()  # if the user i
                    else:
                        incorrectStepInputLabel.place(x=40, y=425, anchor=W)
                elif solvedSteps == 3:
                    incorrectStepInputLabel.place(x=40, y=425, anchor=W)

            else:
                incorrectStepInputLabel.place(x=40, y=425, anchor=W)

            if stepInput == finalAnswer or stepInput == finalAnswer1 or stepInput == finalAnswer2:
                stepsScreen.destroy()
                loadBeginningMenuScreen()

        answers = stepProcess(input1, input2)

        problemLabel = Label(stepsScreen, textvariable=inputText, borderwidth=5, relief='solid', padx=5, pady=5)
        problemLabel.place(anchor=N, x=426, y=10)

        stepAnswerBox = Entry(stepsScreen, width=20)
        stepAnswerBox.place(x=40, y=450, anchor=W)

        checkStepAnswerButton = Button(stepsScreen, text="Check step answer", command=checkStepAnswer).place(anchor=W,x=170,y=450)

        stepText = StringVar()

        if ProblemChoice.get() == "Index laws":
            if input1[4] == '*':
                stepText.set(steps[0][0])  # The instruction at (0,0) in the steps array is displayed becat
            elif input1[4] == '/':
                stepText.set(steps[1][0])  # The instruction at (1,0) in the steps array is displayed becat
            else:
                stepText.set(steps[2][0])  # The instruction at (2,0) in the steps array is displayed becat

        elif ProblemChoice.get() == "Solving quadratic equations":
            if input1[0] == 'x':
                stepText.set(steps[3][0])  # The instruction at (4,0) in the steps array is displayed becat
            else:
                stepText.set(steps[4][0])  # The instruction at (4,0) in the steps array is displayed becal

        elif ProblemChoice.get() == "Simultaneous equations":
            stepText.set(steps[5][0])

        elif ProblemChoice.get() == "Finding a side length in a right-angle triangle given two lengths":
            stepText.set(steps[6][0])

        elif ProblemChoice.get() == "Area of right-angled triangle":
            stepText.set(steps[7][0])

        stepTextLabel = Label(stepsScreen, textvariable=stepText).place(anchor=N, x=426, y=100)

        def checkFinalAnswer():
            nonlocal answers
            finalAnswer = str(answers[1])
            finalAnswer1 = str(answers[2])
            finalAnswer2 = str(answers[3])
            # all possible final answers are assigned as such from the answers array that this has prev
            finalInput = finalAnswerBox.get()  # a variable called finallnput is instantiated
            if finalInput == finalAnswer or finalInput == finalAnswer1 or finalInput == finalAnswer2:
                stepsScreen.destroy()
                loadBeginningMenuScreen()
            else:
                incorrectStepInputLabel.place(x=40, y=425, anchor=W)  # otherwise, the incorrect label wi

        finalAnswerBox = Entry(stepsScreen)
        finalAnswerBox.place(anchor=W, x=450, y=450)

        CheckFinalAnswerButton = Button(stepsScreen, text="Check final answer", command=checkFinalAnswer).place(anchor=W, x=580, y=450)
        incorrectStepInputLabel.place_forget()


loadBeginningMenuScreen()
window.mainloop()
