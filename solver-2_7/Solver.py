import sys
from time import sleep
from math import e, sin, cos, tan, pi, log


print "\nNUMERICAL METHODS SOLVER"
print "NEW in v.3.2.9: \nAdded Numerical Integration!"
print "Now you can reuse the values written on a system of equations."
print "In interpolation, tables will be sorted automatically."
print "Few other bugs squished."
print "More updates coming soon!\n"


def func_keeper():
    print "\nGive me a function in python form."
    print "e.g. (x ** 2 + 1) / (1 - x) ** 2"
    func = raw_input("The function must be in terms of 'x': ")
    return func


def func_evaluator(func, to_plot):
    f = lambda x: eval(func)
    fx = f(to_plot)
    return fx


def fill_matrix(a, b):
    for x in range(0, len(a)):
        print ""
        for y in range(0, len(a) + 1):
            if y < len(a):
                print "Please provide only the coefficients of your linear equations (in order): "
                a[x][y] = float(input("Row %d, column %d: " % ((x + 1), (y + 1))))
            else:
                sleep(.2)
                print "\nNOW the constant of that equation: "
                b[x] = float(input("Row %d, {B}: " % (x + 1)))


def print_matrix(mat, unk, r):
    print ""
    for i in range(len(mat)):
        for j in range(len(mat) + 1):
            if j < len(mat):
                print '{:^9.4}'.format(mat[i][j]),  # .format replaces % format (BEFORE '{:<14 .2f}')
            else:
                print '{} | {:.5}'.format(unk[i], r[i]),  # < aligns to the left
        print


def print_answers(array):
    for i in range(0, len(array)):
        if i != (len(array) - 1):
            print "[{:^7.4}],".format(array[i]),
        else:
            print "and [{:^7.4}].".format(array[i])


def scale(start, a, b):
    print "\n Scaling with pivot {:.5} in [{},{}]".format(a[start][start], start, start)
    divisor = a[start][start]
    temp = 0
    for coef in a[start]:
        coef = coef / divisor
        a[start][temp] = coef
        temp += 1
    b[start] /= divisor


def forw_elim(start, a, b):
    print "\n Forward Elimination"
    sleep(.4)
    for k in range(start, len(a)):
        for i in range(k + 1, len(a)):
            factor = (a[i][k] * a[k][k])
            for j in range(k, len(a)):
                a[i][j] -= (factor * a[k][j])
            b[i] -= (factor * b[k])


def back_subs(a, b, x):
    print "\n Backward Substitution"
    sleep(.4)
    last = len(a) - 1
    x[last] = b[last] / a[last][last]
    for i in range(last, -1, -1):
        suma = b[i]
        for j in range(i + 1, len(a)):
            suma -= (a[i][j] * x[j])
        x[i] = suma / a[i][i]


def sort_lists(list1, list2):
    print "\nTable will be sorted automatically"
    sleep(1.5)
    list1, list2 = zip(*sorted(zip(list1, list2)))
    list1, list2 = (list(t) for t in zip(*sorted(zip(list1, list2))))
    return list1, list2


def create_table():
    tam = float(input("How many items will be on your list?: "))
    tam = int(tam)

    repeat = True
    while repeat:
        x = []
        y = []

        print "Fill the values of your table, starting with all of the 'x' values and then the 'y' values:"

        print "\nX table:"
        for i in range(0, tam):
            x.append(float(input("P{}: ".format(i))))
            i += 1

        print "\nY table:"
        for j in range(0, tam):
            y.append(float(input("P{}: ".format(j))))
            j += 1

        x, y = sort_lists(x, y)

        display_table(x, y, tam)

        err = True
        while err:
            ans = raw_input("\nIs this correct? [Y/N]: ").upper()
            if ans == "Y":
                err = False
                repeat = False
            elif ans == "N":
                err = False
                repeat = False
            else:
                print "Invalid answer. Choose between [Y/N]."
                err = True

    return x, y, tam


def display_table(list1, list2, tam):
    print ""
    print "{:^6}| {:^6}".format("X", "Y")
    print("{:-^14s}".format(""))  # makes a lot of lines with "" in middle
    for cont in range(0, tam):
        print "{:^6.4}| {:^6.6}".format(list1[cont], list2[cont])


def main_menu():
    print "\nNUMERICAL METHODS SOLVER"
    sel_menu = True
    las_opciones = "\n MENU\n"
    las_opciones += "\t1.- Non-linear equations\n"
    las_opciones += "\t2.- System of linear equations\n"
    las_opciones += "\t3.- Interpolation and Curve Fitting\n"
    las_opciones += "\t4.- Regression\n"
    las_opciones += "\t5.- Numerical Integration\n"
    las_opciones += "\t6.- Runge-Kutta Methods (Under Construction...) \n"
    las_opciones += "\t 7.- Exit\n\n"
    print las_opciones

    while sel_menu:
        opcion = raw_input("Choose an option [1-6]: ")
        if opcion == "1":
            roots_menu()
            sel_menu = False
        elif opcion == "2":
            matrices()
            sel_menu = False
        elif opcion == "3":
            interpolation()
            sel_menu = False
        elif opcion == "4":
            regression()
            sel_menu = False
        elif opcion == "5":
            num_integration()
            sel_menu = False
        elif opcion == "6":
            runge_kutta()
            sel_menu = False
        elif opcion == "7":
            print "Exiting..."
            sleep(1.5)
            sel_menu = False
        else:
            print "Option not available."
            sel_menu = True


def roots_menu():
    sel_menu = True
    las_opciones = "\n NON-LINEAR EQUATIONS\n\n"
    las_opciones += "Closed Methods (assure convergence) [slower]\n"
    las_opciones += "\ta.- Bolzano/Bisection\n"
    las_opciones += "\tb.- False-Position\n"
    las_opciones += "\nOpen Methods (may diverge) [faster]\n"
    las_opciones += "\tc.- Newton-Raphson\n"
    las_opciones += "\td.- Secant\n"
    las_opciones += "\te.- Fixed point Iteration\n\n"
    las_opciones += "\t  f.- Main Menu\n"
    las_opciones += "\t  g.- EXIT\n\n"
    print las_opciones

    while sel_menu:
        opcion = raw_input("Choose an option [a-g]: ").lower()
        if opcion[0] == "a":
            bisection()
            sel_menu = False
        elif opcion[0] == "b":
            false_p()
            sel_menu = False
        elif opcion[0] == "c":
            newton()
            sel_menu = False
        elif opcion[0] == "d":
            secant()
            sel_menu = False
        elif opcion[0] == "e":
            fixed_p()
            sel_menu = False
        elif opcion[0] == "f":
            print "Returning to menu..."
            sleep(1)
            sel_menu = False
            main_menu()
        elif opcion[0] == "g":
            print "Exiting..."
            sleep(1.3)
            sys.exit()
        else:
            print "Option not available."
            sel_menu = True


def bisection():
    print "\n Bisection Method\n"

    current_iter = -1
    a, fa, b, fb, c, fc, ans = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    tolerance = float(input("What is your output tolerance?: "))
    max_it = float(input("What is your max number of iterations?: "))
    max_it = int(max_it)
    print "You can copy this: (9000 / x) * (1 - (1 / (1 + x) ** 24)) - 179000" \
          "\n as your function or type your own."
    func = func_keeper()

    print "What will be your 'a'?"
    err = True
    while err:
        a = float(input("Remember that evaluated, it should be on the upper interval of the x-axis: "))
        fa = func_evaluator(func, a)
        print "Your point is currently at %f.\n" % fa
        if fa < 0:
            print "f(a) is not in the upper interval. Try another value for 'a'."
            err = True
        elif abs(fa) < tolerance:
            ans = a
            print "You hit the answer: %f." % ans
            print "Returning to menu."
            sleep(1)
            roots_menu()
        else:
            err = False

    print "What will be your 'b'?"
    err = True
    while err:
        b = float(input("Remember that evaluated, it should be on the lower interval of the x-axis: "))
        fb = func_evaluator(func, b)
        print "Your point is currently at %f\n" % fa
        if fb > 0:
            print "f(b) is not in the lower interval. Try another value for 'b'."
            err = True
        elif abs(fb) < tolerance:
            ans = b
            print "You hit the answer: %f." % ans
            print "Returning to menu."
            sleep(1)
            roots_menu()
        else:
            err = False

    max_reached = False
    while not max_reached:
        current_iter += 1
        print "Current Iteration: %d." % current_iter
        c = (a + b) / 2
        fc = func_evaluator(func, c)
        print "'c' is now: %f. f(c) is %f. \n" % (c, fc)
        if current_iter >= max_it:
            print "Max iteration reached. Terminating."
            ans = c
            break
        if 0 > fc and abs(fc) > tolerance:
            print "Changing 'b'\n"
            b = c
            max_reached = False
        elif fc > 0 and abs(fc) > tolerance:
            print "Changing 'a'\n"
            a = c
            max_reached = False
        else:
            print "Tolerance reached."
            ans = c
            max_reached = True
    print "\n The root is close to %f." % ans
    print "Returning to menu."
    sleep(1)
    roots_menu()


def false_p():
    print "\n False-position Method\n"
    current_iter = -1
    a_cont, b_cont = 0, 0
    a, fa, b, fb, c, fc, ans = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    tolerance = float(input("What is your output tolerance?: "))
    max_it = float(input("What is your max number of iterations?: "))
    max_it = int(max_it)
    print "You can copy this: (9000 / x) * (1 - (1 / (1 + x) ** 24)) - 179000" \
          "\n as your function or type your own."
    func = func_keeper()

    print "What will be your 'a'?"
    err = True
    while err:
        a = float(input("Remember that evaluated, it should be on the upper interval of the x-axis: "))
        fa = func_evaluator(func, a)
        print "Your point is currently at %f.\n" % fa
        if fa < 0:
            print "f(a) is not in the upper interval. Try another value for 'a'."
            err = True
        elif abs(fa) < tolerance:
            ans = a
            print "You hit the answer: %f." % ans
            print "Returning to menu."
            sleep(1)
            roots_menu()
        else:
            err = False

    print "What will be your 'b'?"
    err = True
    while err:
        b = float(input("Remember that evaluated, it should be on the lower interval of the x-axis: "))
        fb = func_evaluator(func, b)
        print "Your point is currently at %f\n" % fb
        if fb > 0:
            print "f(b) is not in the lower interval. Try another value for 'b'."
            err = True
        elif abs(fb) < tolerance:
            ans = b
            print "You hit the answer: %f." % ans
            print "Returning to menu."
            sleep(1)
            roots_menu()
        else:
            err = False

    max_reached = False
    while not max_reached:
        current_iter += 1
        print "Current Iteration: %d." % current_iter
        c = b - (fb * (a - b) / (fa - fb))
        fc = func_evaluator(func, c)
        print "'c' is now: %f. f(c) is %f\n" % (c, fc)
        if current_iter >= max_it:
            print "Max iteration reached. Terminating."
            ans = c
            break
        elif abs(fc) <= tolerance:
            print "Tolerance reached."
            ans = c
            break
        else:
            temp = fa * fc
            if temp > 0:
                a = c
                fa = func_evaluator(func, a)
                a_cont = 0
                b_cont += 1
                if b_cont >= 2:
                    print "Modifying f(b) to improve convergence.\n"
                    fb = fb / 2
            else:
                b = c
                fb = func_evaluator(func, b)
                b_cont = 0
                a_cont += 1
                if a_cont >= 2:
                    print "Modifying f(a) to improve convergence.\n"
                    fa = fa / 2
    print "The root is close to %f" % ans
    print "Returning to menu."
    sleep(1)
    roots_menu()


def newton():
    print "\n Newton-Raphson Method\n"
    current_iter = -1
    x_i, x_nexti, ans = 0.0, 0.0, 0.0
    tolerance = float(input("What is your output tolerance?: "))
    max_it = float(input("What is your max number of iterations?: "))
    max_it = int(max_it)
    print "\nFor your function you can use this: (e ** (-x)) - x or type your own."
    func = func_keeper()
    print "\nNow the derivative of your function." \
          "\nIf you used the given function one, use: (-e ** (-x)) - 1"
    derivative = func_keeper()

    x_i = float(input("What will be your initial value?: "))

    max_reached = False
    while not max_reached:
        f_i = func_evaluator(func, x_i)
        d_i = func_evaluator(derivative, x_i)
        print "\n f(xi) is now: %f and f'(xi) is: %f." % (f_i, d_i)
        current_iter += 1
        print "\nCurrent Iteration: %d" % current_iter
        x_nexti = (x_i - (f_i / d_i))
        print "'xi+1' is now %f." % x_nexti
        if current_iter >= max_it:
            print "Max iteration reached. Terminating."
            ans = x_nexti
            break
        elif abs(f_i) <= tolerance:
            print "Tolerance reached."
            ans = x_nexti
            break
        else:
            x_i = x_nexti
            max_reached = False
    print "\nThe root is close to %f" % ans
    roots_menu()


def secant():
    print "\n Secant Method\n"
    current_iter = -1
    x_o, x_i, x_nexti, ans = 0.0, 0.0, 0.0, 0.0
    tolerance = float(input("What is your output tolerance?: "))
    max_it = float(input("What is your max number of iterations?: "))
    max_it = int(max_it)
    print "You can copy this: (e ** (-x)) - x as your function or type your own."
    func = func_keeper()

    x_o = float(input("What will be your initial value?: "))
    x_i = x_o + 0.001

    max_reached = False
    while not max_reached:
        f_i = func_evaluator(func, x_i)
        f_o = func_evaluator(func, x_o)
        current_iter += 1
        print "\nCurrent Iteration: %d" % current_iter
        x_nexti = (x_i - ((f_i * (x_o - x_i)) / (f_o - f_i)))
        print "'xi+1' is now %f" % x_nexti
        if current_iter >= max_it:
            print "Max iteration reached. Terminating."
            ans = x_nexti
            break
        elif abs(f_i) <= tolerance:
            print "Tolerance reached."
            ans = x_nexti
            break
        else:
            x_o = x_i
            x_i = x_nexti
            max_reached = False
    print "The root is close to %f" % ans
    roots_menu()


def fixed_p():
    print "\n Fixed-point Iteration Method\n"
    current_iter = -1
    x_i, x_nexti, ans = 0.0, 0.0, 0.0
    print "What is your relative error tolerance in %?"
    tolerance = float(input("Don't type the '%' symbol: "))
    max_it = float(input("What is your max number of iterations?: "))
    max_it = int(max_it)
    print "Remember that for Fixed-point, the function must be x = g(x)." \
          "\nYou can copy this: (e ** (-x)) as your function or type yur own."
    func = func_keeper()

    x_i = float(input("What will be your initial value?: "))
    max_reached = False
    while not max_reached:
        f_i = func_evaluator(func, x_i)
        current_iter += 1
        print "\nCurrent Iteration: %d" % current_iter
        x_nexti = f_i
        print "'xi+1' is now %f" % x_nexti
        if current_iter >= max_it:
            print "Max iteration reached. Terminating."
            ans = x_nexti
            break
        elif abs((x_nexti - x_i) / x_nexti) <= tolerance:
            print "Tolerance reached."
            ans = x_nexti
            break
        else:
            x_i = x_nexti
            max_reached = False
    print "The root is close to %f" % ans
    roots_menu()


"""BEGINS MATRICES"""


def matrices():
    results_vector = [2.0, -22.0, -7.0]
    unk_vector = ["x1", "x2", "x3"]
    matrix = [[6.0, 3.0, -2.0], [-1.0, 7.0, -3.0], [2.5, .5, 3.5]]
    size = len(matrix)

    print "\n\nA matrix has been created in case you want to use it:"
    print_matrix(matrix, unk_vector, results_vector)
    sleep(1)
    matrices_menu(matrix, unk_vector, results_vector, size)


def matrices_menu(matrix, unk_vec, res_vec, size):
    sel_menu = True
    las_opciones = "\n SOLVING SYSTEM OF EQUATIONS\n\n"
    las_opciones += "Direct Methods (Operate Directly on Matrix)\n"
    las_opciones += "\ta.- Gaussian Elimination\n"
    las_opciones += "\tb.- LU Decomposition\n"
    las_opciones += "\nIterative Methods (Start with initial vector; assume initial value)\n"
    las_opciones += "\tc.- Gauss-Seidel\n\n"
    las_opciones += "\t  d.- Main Menu\n"
    las_opciones += "\t  e.- EXIT\n\n"
    print las_opciones

    while sel_menu:
        opcion = raw_input("Choose an option [a-g]: ")
        if opcion[0].lower() == "a":
            gauss_el(matrix, unk_vec, res_vec, size)
            sel_menu = False
        elif opcion[0].lower() == "b":
            lu_decomp(matrix, unk_vec, res_vec, size)
            sel_menu = False
        elif opcion[0].lower() == "c":
            seidel(matrix, unk_vec, res_vec, size)
            sel_menu = False
        elif opcion[0].lower() == "d":
            print "Returning to menu..."
            sleep(1)
            sel_menu = False
            main_menu()
        elif opcion[0].lower() == "e":
            print "Exiting..."
            sleep(1.3)
            sys.exit()
        else:
            print "Option not available."
            sel_menu = True


def gauss_el(a, unk_vec, b, size):
    print "Gauss Elimination:\n"

    err = True
    while err:
        print "Continue with same matrix?"
        print_matrix(a, unk_vec, b)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            x = [0.0 for col in range(size)]
            ux = []
            for i in range(0, size):
                ux.append("{x" + str(i) + "}")
            err = False
        elif y_n == "N":
            size = float(input("How many unknowns do you have?: "))
            size = int(size)
            a = [[0.0 for col in range(size)] for row in range(size)]
            x = [0.0 for col in range(size)]
            ux = []
            for i in range(0, size):
                ux.append("{x" + str(i) + "}")
            b = [0.0 for col in range(size)]
            fill_matrix(a, b)
            print_matrix(a, ux, b)
            err = False
        else:
            print "Option not available."
            err = True

    a_copy = [0.0 for col in range(size)]
    for i in range(0, len(a)):
        a_copy[i] = list(a[i])

    b_copy = b[:]
    cont = -1
    for array in range(0, len(a)):
        cont += 1
        if array < (len(a) - 1):
            scale(array, a_copy, b_copy)
            print_matrix(a_copy, ux, b_copy)
            forw_elim(cont, a_copy, b_copy)
            print_matrix(a_copy, ux, b_copy)
        else:
            scale(array, a_copy, b_copy)
            print_matrix(a_copy, ux, b_copy)

    back_subs(a_copy, b_copy, x)
    print_matrix(a_copy, ux, b_copy)
    sleep(.7)

    print "The answers are:",
    print_answers(x)
    print "\nReturning to menu..."
    sleep(1)
    matrices_menu(a, ux, b, size)


def lu_decomp(a, ux, b, size):
    print "L-U Decomposition:\n"

    err = True
    while err:
        print "Continue with same matrix?"
        print_matrix(a, ux, b)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            l = [x[:] for x in a]
            x = list(b)
            uy = []
            for i in range(0, size):
                uy.append("{y" + str(i) + "}")
            err = False
        elif y_n == "N":
            size = float(input("How many unknowns do you have?: "))
            size = int(size)
            a = [[0.0 for col in range(size)] for row in range(size)]
            l = [x[:] for x in a]

            ux = []
            for i in range(0, size):
                ux.append("{x" + str(i) + "}")

            uy = []
            for i in range(0, size):
                uy.append("{y" + str(i) + "}")

            b = [0.0 for col in range(size)]

            x = list(b)
            fill_matrix(a, b)
            print_matrix(a, ux, b)
            err = False
        else:
            print "Option not available."
            err = True

    print "\nForward Elimination to get L-U:"
    todo = True
    while todo:
        l_copy = list(x[:] for x in l)

        u = [0.0 for col in range(size)]
        for i in range(0, size):
            u[i] = list(a[i])

        for i in range(0, len(l)):
            l_copy[i][i] = 1.0

        sleep(.3)
        y = list(b)
        for k in range(0, size):
            for i in range(k + 1, size):
                factor = (u[i][k] / u[k][k])
                l_copy[i][k] = factor
                for j in range(k, size):
                    u[i][j] -= (factor * u[k][j])
                y[i] -= (factor * y[k])

        print '\n"L" Matrix:'
        print_matrix(l_copy, uy, b)

        print "\nValues for {Y}:",
        print_answers(y)
        print '\n"U" Matrix:'
        print_matrix(u, ux, y)

        print "\nBackward Substitution to get {x}"
        sleep(.4)
        last = size - 1
        x[last] = y[last] / u[last][last]
        for i in range(last, -1, -1):
            suma = y[i]
            for j in range(i + 1, size):
                suma -= (u[i][j] * x[j])
            x[i] = suma / u[i][i]

        sleep(.7)
        print "The answers are:",
        print_answers(x)

        err = True
        while err:
            ans = raw_input("\nWould you like to solve with new B's? [Y/N]: ").upper()
            print ""
            if ans == "Y":
                for i in range(0, size):
                    print "Provide constant to equation: {}.".format(a[i]),
                    b[i] = float(input("B{}: ".format(i)))
                err = False
            elif ans == "N":
                err = False
                todo = False
            else:
                print "Answer not available. Choose between 'Y' or 'N'."
                err = True
    print "\nReturning to menu..."
    sleep(1)
    matrices_menu(a, ux, b, size)


def seidel_op(a, b, x):
    err_tol = float(input("\nWhat will be your error tolerance percentage?: "))
    max_it = float(input("What will be your max number of iterations?: "))
    max_it = int(max_it)

    while True:
        ans = raw_input("Do you want to use relaxation? [Y/N]: ").upper()
        if ans == "Y":
            relax_coef = float(input("Give me the value for lambda: "))
            break
        elif ans == "N":
            relax_coef = 1.0
            break
        else:
            print "Invalid answer. Choose between [Y/N]"

    for i in range(0, len(a)):
        dummy = a[i][i]
        for j in range(0, len(a)):
            a[i][j] = a[i][j] / dummy
        b[i] = b[i] / dummy
    for i in range(0, len(a)):
        sum = b[i]
        for j in range(0, len(a)):
            if i != j:
                sum -= a[i][j] * x[j]
        x[i] = sum
    iter = 1
    while True:
        print "\nIteration number: {}".format(iter)
        sentinel = 1
        for i in range(0, len(a)):
            old = x[i]
            sum = b[i]
            for j in range(0, len(a)):
                if i != j:
                    sum -= a[i][j] * x[j]
            x[i] = relax_coef * sum + (1.0 - relax_coef) * old
            if sentinel == 1 and x[i] != 0.0:
                aprox_err = abs((x[i] - old) / x[i]) * 100
                if aprox_err > err_tol:
                    print "Current error: {:.6}%".format(aprox_err)
                    sentinel = 0
        iter += 1
        if sentinel == 1 or iter >= max_it:
            print "\nFinal error: {:.6}%".format(aprox_err)
            break


def seidel(a, ux, b, size):
    print "Gauss-Seidel\n"

    err = True
    while err:
        print "Continue with same matrix?"
        print_matrix(a, ux, b)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            x = [0 for col in range(size)]
            err = False
        elif y_n == "N":
            size = float(input("How many unknowns do you have?: "))
            size = int(size)
            a = [[0 for col in range(size)] for row in range(size)]
            x = [0 for col in range(size)]
            ux = []
            for i in range(0, size):
                ux.append("{x" + str(i) + "}")
            b = [0 for col in range(size)]
            fill_matrix(a, b)
            print_matrix(a, ux, b)
            err = False
        else:
            print "Option not available."
            err = True

    a_copy = [0.0 for col in range(size)]
    for i in range(0, len(a)):
        a_copy[i] = list(a[i])

    b_copy = list(b)

    seidel_op(a_copy, b_copy, x)

    print_matrix(a_copy, ux, b_copy)
    print "The answers are:",
    print_answers(x)

    print "\nReturning to menu"
    sleep(1)
    matrices_menu(a, ux, b, size)


"""BEGINS INTERPOLATION"""


def interpolation():
    x = [0.5, 1.0, 3.0, 4.0, 7.0]
    b = [log(.5), log(1), log(3), log(4), log(7)]
    y = ["ln(.5)", "ln(1)", "ln(3)", "ln(4)", "ln(7)"]
    size = 5

    print "\n\nA Table has been created in case you want to use it:"
    display_table(x, y, size)
    sleep(1)
    interpolation_menu(x, b, size)


def interpolation_menu(x, b, size):
    sel_menu = True
    las_opciones = "\n INTERPOLATION\n\n"
    las_opciones += "a.- Lagrange\n"
    las_opciones += "b.- Newton's Divided Differences\n"
    las_opciones += "c.- Power Series\n"
    las_opciones += "\t  d.- Main Menu\n"
    las_opciones += "\t  e.- EXIT\n"
    las_opciones += ""

    print las_opciones

    while sel_menu:
        opcion = raw_input("Choose an option [a-e]: ").lower()
        if opcion[0] == "a":
            lagrange(x, b, size)
            sel_menu = False
        elif opcion[0] == "b":
            newton_dd(x, b, size)
            sel_menu = False
        elif opcion[0] == "c":
            power_series(x, b, size)
            sel_menu = False
        elif opcion[0] == "d":
            print "Returning to menu..."
            sleep(1)
            sel_menu = False
            main_menu()
        elif opcion[0] == "e":
            print "Exiting..."
            sleep(1.3)
            sys.exit()
        else:
            print "Option not available."
            sel_menu = True


def proterm(i, val, x):
    pro = 1
    for j in range(0, i):
        pro *= (val - x[j])
    return pro


def lagrange(x, b, size):
    err = True
    while err:
        print "Continue with same data?"
        display_table(x, b, size)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            x, y, size = create_table()
            err = False
        else:
            print "Option not available."
            err = True
    todo = True
    while todo:
        x_copy = list(x)
        b_copy = list(b)

        while True:
            to_find = float(input("\nWhat value of 'x' would you like to find 'y'?: "))
            if (to_find > x_copy[0]) and (to_find < x_copy[size - 1]):
                break
            else:
                print "Answer not between poles. Choose between {} and {}".format(x_copy[0], x_copy[size - 1])

        suma = 0
        for i in range(0, size):
            product = b_copy[i]
            for j in range(0, size):
                if i != j:
                    product *= (to_find - x_copy[j]) / (x_copy[i] - x_copy[j])
            suma += product
        lagrng = suma

        print "The value for {} is {}.".format(to_find, lagrng)

        append = True
        while append:
            print "\nAppend data to table for future use? [Y/N]: ",
            y_n = raw_input().upper()
            if y_n == "Y":
                x.append(to_find)
                b.append(lagrng)
                x, b = sort_lists(x, b)
                print "This point has been added to the list."
                size += 1
                display_table(x, b, size)
                append = False
            elif y_n == "N":
                append = False
            else:
                print "Option not available."
                append = True

        resp = True
        while resp:
            ans = raw_input("Would you like to find another point? [Y/N]: ").upper()
            if ans == "Y":
                resp = False
            elif ans == "N":
                resp = False
                todo = False
            else:
                print "Invalid answer. Choose either 'Y' OR 'N'."

    print "\nReturning to menu"
    sleep(1)
    interpolation_menu(x, b, size)


def print_table(mesa):
    print "\nDivided differences table"
    for i in range(0, len(mesa)):
        for j in range(0, len(mesa[i])):
            print "{:^7.4}| ".format(mesa[i][j]),
            j += 1
        print ""
    print ""


def apply_formula(size, value, x, dd):
    suma = dd[0][0]
    for i in range(1, size):
        suma += (proterm(i, value, x) * dd[i][0])
    return suma


def newton_dd(x, b, size):
    err = True
    while err:
        print "Continue with same data?"
        display_table(x, b, size)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            x, y, tam = create_table()
            err = False
        else:
            print "Option not available."
            err = True

    todo = True
    while todo:
        x_copy = list(x)
        b_copy = list(b)

        dd = [[] for col in range(size)]
        table = [[] for col in range(size - 1)]
        temp = size

        for i in range(0, size):
            dd[0].append(b_copy[i])

        for cont2 in range(1, size):
            temp -= 1
            for cont in range(temp - 1, - 1, -1):
                num = (dd[cont2 - 1][cont + 1] - dd[cont2 - 1][cont])
                den = (x_copy[cont + cont2] - x[cont])
                dd[cont2].insert(0, (num / den))
                cont += 1

        for i in range(1, size):
            for j in range(0, len(dd[i])):
                table[i - 1].append(dd[j + 1][i - 1])

        print_table(table)

        while True:
            to_find = float(input("\nWhat value of 'x' would you like to find 'y'?: "))
            if (to_find > x_copy[0]) and (to_find < x_copy[size - 1]):
                break
            else:
                print "Answer not between poles. Choose between {} and {}".format(x_copy[0], x_copy[size - 1])

        found = apply_formula(size, to_find, x_copy, dd)
        print "The value for {} is: {}".format(to_find, found)

        append = True
        while append:
            print "\nAppend data to table for future use? [Y/N]: ",
            y_n = raw_input().upper()
            if y_n == "Y":
                x.append(to_find)
                b.append(found)
                x, b = sort_lists(x, b)
                print "This point has been added to the list."
                size += 1
                display_table(x, b, size)
                append = False
            elif y_n == "N":
                append = False
            else:
                print "Option not available."
                append = True

        resp = True
        while resp:
            ans = raw_input("Would you like to find another point? [Y/N]: ").upper()
            if ans == "Y":
                resp = False
            elif ans == "N":
                resp = False
                todo = False
            else:
                print "Invalid answer. Choose either 'Y' OR 'N'."

    print "\nReturning to menu"
    sleep(1)
    interpolation_menu(x, b, size)


def power_series(x, b, size):
    err = True
    while err:
        print "Continue with same data?"
        display_table(x, b, size)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            x, y, tam = create_table()
            err = False
        else:
            print "Option not available."
            err = True

    todo = True
    while todo:
        x_copy = list(x)
        b_copy = list(b)

        while True:
            to_find = float(input("\nWhat value of 'x' would you like to find 'y'?: "))
            if (to_find > x_copy[0]) and (to_find < x_copy[size - 1]):
                break
            else:
                print "Answer not between poles. Choose between {} and {}".format(x_copy[0], x_copy[size - 1])

        mat = [[0.0 for col in range(size)] for row in range(size)]

        for i in range(0, size):
            mat[i][0] = 1.0

        for j in range(0, size):
            for k in range(1, size):
                mat[j][k] = x_copy[j] ** k

        ux = []
        for i in range(0, size):
            ux.append("{a" + str(i) + "}")
        print_matrix(mat, ux, b)

        l = [[0.0 for col in range(size)] for row in range(size)]
        foundw_back = [0.0 for col in range(size)]
        foundw_forw = [0.0 for col in range(size)]

        for i in range(0, len(mat)):
            l[i][i] = 1.0

        for k in range(0, len(mat)):
            for i in range(k + 1, len(mat)):
                factor = (mat[i][k] / mat[k][k])
                l[i][k] = factor
                for j in range(k, len(mat)):
                    mat[i][j] -= (factor * mat[k][j])
                b_copy[i] -= (factor * b_copy[k])

        foundw_forw[0] = b_copy[0] / l[0][0]
        for i in range(0, len(l)):
            suma = b_copy[i]
            for j in range(i + 1, len(l)):
                suma -= (l[i][j] * foundw_forw[j])
            foundw_forw[i] = suma / l[i][i]

        last = len(mat) - 1
        foundw_back[last] = foundw_forw[last] / mat[last][last]
        for i in range(last, -1, -1):
            suma = foundw_forw[i]
            for j in range(i + 1, len(mat)):
                suma -= (mat[i][j] * foundw_back[j])
            foundw_back[i] = suma / mat[i][i]

        print "\nUsing LU Decomposition, the coefficients are: ",
        print_answers(foundw_back)

        total = 0
        for z in range(0, size):
            total += foundw_back[z] * (to_find ** z)

        print "The value for {} is: {:.6}".format(to_find, total)

        append = True
        while append:
            print "\nAppend data to table for future use? [Y/N]: ",
            y_n = raw_input().upper()
            if y_n == "Y":
                x.append(to_find)
                b.append(total)
                x, b = sort_lists(x, b)
                print "This point has been added to the list."
                size += 1
                display_table(x, b, size)
                append = False
            elif y_n == "N":
                append = False
            else:
                print "Option not available."
                append = True

        resp = True
        while resp:
            ans = raw_input("Would you like to find another point? [Y/N]: ").upper()
            if ans == "Y":
                resp = False
            elif ans == "N":
                resp = False
                todo = False
            else:
                print "Invalid answer. Choose either 'Y' OR 'N'."

    print "Returning to menu"
    sleep(1)
    interpolation_menu(x, b, size)


"""BEGINS REGRESSION"""


def regression():
    x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]
    tam = 6

    print "\n\nA Table has been created in case you want to use it:"
    display_table(x, y, tam)
    sleep(1)
    regression_menu(x, y, tam)


def regression_menu(x, y, tam):
    sel_menu = True
    las_opciones = "\n What method would you like to use?\n\n"
    las_opciones += "\ta.- Linear\n"
    las_opciones += "\tb.- Polynomial\n"
    las_opciones += "\tc.- Exponential\n"
    las_opciones += "\td.- Logarithmic\n\n"
    las_opciones += "\t  e.- Main Menu\n"
    las_opciones += "\t  f.- EXIT\n\n"
    print las_opciones

    while sel_menu:
        opcion = raw_input("Choose an option [a-f]: ")
        if opcion[0].lower() == "a":
            linear(x, y, tam)
            sel_menu = False
        elif opcion[0].lower() == "b":
            poly(x, y, tam)
            sel_menu = False
        elif opcion[0].lower() == "c":
            expo(x, y, tam)
            sel_menu = False
        elif opcion[0].lower() == "d":
            loga(x, y, tam)
            sel_menu = False
        elif opcion[0].lower() == "e":
            print "Returning to menu..."
            sleep(1)
            sel_menu = False
            main_menu()
        elif opcion[0].lower() == "f":
            print "Exiting..."
            sleep(1.3)
            sys.exit()
        else:
            print "Option not available."
            sel_menu = True


def linear(x, y, tam):
    err = True
    while err:
        print "Continue with same data?"
        display_table(x, y, tam)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            x, y, tam = create_table()
            err = False
        else:
            print "Option not available."
            err = True
    sumx = 0.0
    sumxy = 0.0
    sumy = 0.0
    st = 0.0
    sumx2 = 0.0
    sr = 0.0

    for i in range(0, tam):
        sumx += x[i]
        sumy += y[i]
        sumxy += x[i] * y[i]
        sumx2 += (x[i]) ** 2

    xm = sumx / tam
    ym = sumy / tam

    a1 = (tam * sumxy - sumx * sumy) / (tam * sumx2 - (sumx ** 2))
    a0 = ym - a1 * xm

    for i in range(0, tam):
        st += (y[i] - ym) ** 2
        sr += (y[i] - a1 * x[i] - a0) ** 2
    syx = (sr / (tam - 2)) ** 0.5
    r = ((st - sr) / st) ** 0.5

    func = a0.__str__() + "+" + a1.__str__() + "* x"
    print "\nThe linear regression for this table would be: y = {:.5} + {:.5}x".format(a0, a1)
    print "Correlation Factor of: {:.5}".format(r)
    plot = True
    while plot:
        ans = raw_input("Would you like to plot a value? [Y/N]: ").upper()
        if ans == "Y":
            to_plot = float(input("Type a value for x: "))
            print "The value is: {}".format(func_evaluator(func, to_plot))
            plot = True
        elif ans == "N":
            plot = False
        else:
            print "Option not available."
            plot = True

    regression_menu(x, y, tam)


def poly(x, y, tam):
    err = True
    while err:
        print "Continue with same data?"
        display_table(x, y, tam)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            x, y, tam = create_table()
            err = False
        else:
            print "Option not available."
            err = True

    degree = True
    while degree:
        m = int(input("\nWhat will the order of the polynomial be?: "))
        if len(x) < m + 1:
            print "There are too few data points in your table for that order. Try another."
            degree = True
        elif len(x) > m + 1:
            degree = False
        else:
            "Answer does not make sense. Answer with a round number."
            degree = True

    sum_x = [0.0 for col in range(2 * m)]
    sum_xy = [0.0 for col in range(m + 1)]
    coeffs = [0.0 for col in range(m + 1)]
    unk_coeffs = []

    for i in range(0, m + 1):
        unk_coeffs.append("{A" + str(i) + "}")

    for i in range(0, 2 * m):
        for j in range(0, tam):
            if i == 0:
                sum_x[i] += x[j]
                sum_xy[i] += y[j]
            elif 0 < i < (m + 1):
                sum_x[i] += x[j] ** (i + 1)
                sum_xy[i] += x[j] ** i * y[j]
            else:
                sum_x[i] += x[j] ** (i + 1)

    matrix = [[0.0 for col in range(m + 1)] for row in range(m + 1)]

    for cont in range(0, m + 1):
        if cont == 0:
            matrix[0][cont] = float(tam)
        else:
            matrix[0][cont] = float(sum_x[cont - 1])

    for cont2 in range(1, m + 1):
        for cont3 in range(0, m + 1):
            matrix[cont2][cont3] = sum_x[(cont2 - 1) + cont3]

    cont = -1
    for array in range(0, len(matrix)):
        cont += 1
        if array < (len(matrix) - 1):
            scale(array, matrix, sum_xy)
            forw_elim(cont, matrix, sum_xy)
        else:
            scale(array, matrix, sum_xy)

    back_subs(matrix, sum_xy, coeffs)
    print_matrix(matrix, unk_coeffs, sum_xy)
    sleep(.7)

    print "The answers are:",
    print_answers(coeffs)

    plot = True
    while plot:
        ans = raw_input("Would you like to plot a value? [Y/N]: ").upper()
        if ans == "Y":
            to_plot = float(input("Type a value for x: "))
            polyplotted = 0
            for i in range(0, m + 1):
                polyplotted += coeffs[i] * to_plot ** i
            print "The value is: {:.5}".format(polyplotted)
            plot = True
        elif ans == "N":
            plot = False
        else:
            print "Option not available."
            plot = True

    print "Returning to menu."
    sleep(1)
    regression_menu(x, y, tam)


def expo(x, y, tam):
    err = True
    while err:
        print "Continue with same data?"
        display_table(x, y, tam)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            x, y, tam = create_table()
            err = False
        else:
            print "Option not available."
            err = True

    print "Under construction...\n Update coming soon!"
    print "Returning to menu"
    sleep(1)
    regression_menu(x, y, tam)


def loga(x, y, tam):
    err = True
    while err:
        print "Continue with same data?"
        display_table(x, y, tam)
        y_n = raw_input("[Y/N]: ").upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            x, y, tam = create_table()
            err = False
        else:
            print "Option not available."
            err = True

    print "Under construction...\n Update coming soon!"
    print "Returning to menu"
    sleep(1)
    regression_menu(x, y, tam)


"""BEGINS NUMERICAL INTEGRATION"""


def num_integration():
    to_int = "4 * x ** 2 - x ** 3 + 8"
    from_a = 0.0
    to_b = 5.0

    print "\n\nA matrix has been created in case you want to use it:"
    print "4x^2 - x^3 + 8; from 0.0 to 5.0"
    sleep(1)
    int_menu(to_int, from_a, to_b)


def int_menu(to_int, from_a, to_b):
    sel_menu = True
    las_opciones = "\n What method would you like to \n\n"
    las_opciones += "\ta.- Trapezoidal\n"
    las_opciones += "\tb.- Simpson's 1/3\n"
    las_opciones += "\tc.- Simpson's 3/8\n\n"
    las_opciones += "\t  d.- Main Menu\n"
    las_opciones += "\t  e.- EXIT\n\n"
    print las_opciones

    while sel_menu:
        opcion = raw_input("Choose an option [a-g]: ").lower()
        if opcion[0] == "a":
            trap(to_int, from_a, to_b)
            sel_menu = False
        elif opcion[0] == "b":
            simp13(to_int, from_a, to_b)
            sel_menu = False
        elif opcion[0] == "c":
            simp38(to_int, from_a, to_b)
            sel_menu = False
        elif opcion[0] == "d":
            print "Returning to menu..."
            sleep(1)
            sel_menu = False
            main_menu()
        elif opcion[0] == "e":
            print "Exiting..."
            sleep(1.3)
            sys.exit()
        else:
            print "Option not available."
            sel_menu = True


def trap(a_integrar, from_a, to_b):
    err = True
    while err:
        y_n = raw_input("Continue with same function? f(x) = {}\n [Y/N]: ".format(a_integrar)).upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            a_integrar = func_keeper()
            from_a = float(input("From here would you like to start the integral?: "))
            to_b = float(input("To which point would you like the integral to go?: "))
            err = False
        else:
            print "Option not available."
            err = True

    n = input("In how many points do you want to divide your interval?: ")
    n = int(n - 1)
    h = (to_b - from_a) / n
    f_a = func_evaluator(a_integrar, from_a)
    f_b = func_evaluator(a_integrar, to_b)
    integrated = h * (f_a + f_b) / 2
    print "Applying the formula: h * (f_a + f_b) / 2"
    print "The integral evaluated gives the approximation of {}\n".format(integrated)
    int_menu(a_integrar, from_a, to_b)


def simp13(a_integrar, from_a, to_b):
    err = True
    while err:
        y_n = raw_input("Continue with same function? f(x) = {}\n [Y/N]: ".format(a_integrar)).upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            a_integrar = func_keeper()
            from_a = float(input("From here would you like to start the integral?: "))
            to_b = float(input("To which point would you like the integral to go?: "))
            err = False
        else:
            print "Option not available."
            err = True

    even = True
    while even:
        n = input("\nIn how many points do you want to divide your interval? (Must be an odd number): ")
        n = int(n) - 1
        if n % 2 == 0:
            even = False
        else:
            print "\nNumber is not odd, please try again."
            even = True

    h = (to_b - from_a) / n
    f_a = func_evaluator(a_integrar, from_a)
    suma = f_a
    for i in range(1, n - 1, 2):
        suma += 4 * func_evaluator(a_integrar, from_a + i * h) + 2 * func_evaluator(a_integrar, from_a + (i + 1) * h)
    suma += 4 * func_evaluator(a_integrar, from_a + (n - 1) * h) + func_evaluator(a_integrar, from_a + n * h)
    integrated = h * suma / 3

    print "The integral evaluated gives the approximation of {}\n".format(integrated)
    int_menu(a_integrar, from_a, to_b)


def simp38(a_integrar, from_a, to_b):
    err = True
    while err:
        y_n = raw_input("Continue with same function? f(x) = {}\n [Y/N]: ".format(a_integrar)).upper()
        if y_n == "Y":
            err = False
        elif y_n == "N":
            a_integrar = func_keeper()
            from_a = float(input("From here would you like to start the integral?: "))
            to_b = float(input("To which point would you like the integral to go?: "))
            err = False
        else:
            print "Option not available."
            err = True

    odd = True
    while odd:
        n = input("\nIn how many points do you want to divide your interval?\n"
                  "(Must begin in 4, and advance in 3's. [4, 7, 10...]): ")
        if n % 3 == 1:
            odd = False
        else:
            print "\nThat number wont work with Simposon 3/8, please try another."
            odd = True
        n = int(n) - 1

    h = (to_b - from_a) / n
    f_a = func_evaluator(a_integrar, from_a)
    suma = f_a
    for i in range(1, n - 2, 3):
        suma += 3 * (func_evaluator(a_integrar, from_a + i * h) + 3 * func_evaluator(a_integrar, from_a + (i + 1) * h))
    suma += 3 * func_evaluator(a_integrar, from_a + (n - 2) * h) + 3 * func_evaluator(a_integrar, from_a + (n - 1) * h) + func_evaluator(a_integrar, from_a + n * h)
    integrated = 3 * h * suma / 8

    print "The integral evaluated gives the approximation of {}\n".format(integrated)
    int_menu(a_integrar, from_a, to_b)


"""BEGINS RUNGE-KUTTA"""


def runge_kutta():
    print "Under construction..."
    print "Returning to menu"
    sleep(1)
    main_menu()


main_menu()
