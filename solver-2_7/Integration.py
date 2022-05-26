import sys
from time import sleep
from math import e, sin, cos, tan, pi, log, log10


def func_keeper():
    print "\nGive me a function in python form."
    print "e.g. (x ** 2 + 1) / (1 - x) ** 2"
    func = raw_input("The function must be in terms of 'x': ")
    return func


def func_evaluator(func, to_plot):
    f = lambda x: eval(func)
    fx = f(to_plot)
    return fx


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
        opcion = raw_input("Choose an option [a-e]: ").lower()
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


num_integration()
