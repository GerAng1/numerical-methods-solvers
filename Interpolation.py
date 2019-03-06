import sys
from time import sleep
from math import e, sin, cos, tan, pi, log


def print_answers(array):
    for i in range(0, len(array)):
        if i != (len(array) - 1):
            print "[{:^7.4}],".format(array[i]),
        else:
            print "and [{:^7.4}].".format(array[i])


def print_matrix(mat, unk, r):
    print ""
    for i in range(len(mat)):
        for j in range(len(mat) + 1):
            if j < len(mat):
                print '{:^9.4}'.format(mat[i][j]),  # .format replaces % format (BEFORE '{:<14 .2f}')
            else:
                print '{} | {:.5}'.format(unk[i], r[i]),  # < aligns to the left
        print


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


def print_table(mesa):
    print "\nDivided differences table"
    for i in range(0, len(mesa)):
        for j in range(0, len(mesa[i])):
            print "{:^7.4}| ".format(mesa[i][j]),
            j += 1
        print ""
    print ""


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


interpolation()
