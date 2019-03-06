import sys
from time import sleep
from math import e, sin, cos, tan, pi, log


def print_answers(array):
    for i in range(0, len(array)):
        if i != (len(array) - 1):
            print "[{:^7.4}],".format(array[i]),
        else:
            print "and [{:^7.4}].\n".format(array[i])


def print_matrix(mat, unk, r):
    print ""
    for i in range(len(mat)):
        for j in range(len(mat) + 1):
            if j < len(mat):
                print '{:^9.4}'.format(mat[i][j]),  # .format replaces % format (BEFORE '{:<14 .2f}')
            else:
                print '{} | {:.5}'.format(unk[i], r[i]),  # < aligns to the left
        print


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


def func_evaluator(func, to_plot):
    f = lambda x: eval(func)
    fx = f(to_plot)
    return fx


def sort_lists(list1, list2):
    print "\nTable will be sorted automatically"
    sleep(1)
    list1, list2 = zip(*sorted(zip(list1, list2)))
    list1, list2 = (list(t) for t in zip(*sorted(zip(list1, list2))))
    return list1, list2


def display_table(list1, list2, tam):
    print ""
    print "{:^6}| {:^6}".format("X", "Y")
    print("{:-^14s}".format(""))  # makes a lot of lines with "" in middle
    for cont in range(0, tam):
        print "{:^6.4}| {:^6.6}".format(list1[cont], list2[cont])


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

        while True:
            ans = raw_input("\nIs this correct? [Y/N]: ").upper()
            if ans == "Y":
                repeat = False
                break
            elif ans == "N":
                break
            else:
                print "Invalid answer. Choose between [Y/N]"

    return x, y, tam


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


regression()
