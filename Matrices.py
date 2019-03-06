import sys
from time import sleep
from math import e, sin, cos, tan, pi, log


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
        opcion = raw_input("Choose an option [a-e]: ")
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


matrices()
