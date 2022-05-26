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


roots_menu()
