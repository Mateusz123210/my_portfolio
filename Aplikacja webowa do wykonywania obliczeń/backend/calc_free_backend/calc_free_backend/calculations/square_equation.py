import re
import json
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('SVG')
import numpy as np
import io
import base64

def solve_square_equation(equation: str, matplotlib_lock):
    equation = equation.replace(" ","").replace(",", ".")
    if len(equation) < 3:
        return None
    matcher = re.compile(r'^(-?(\d+(\.\d+)?)?)?x\^2(([+-](\d+(\.\d+)?)?)?x)?([+-]\d+(\.\d+)?)?$')
    matches = matcher.match(equation)
    if matches is None:
        return None
    response = {}
    if matches.group(1) is None:
        a = 1.0
    elif len(matches.group(1)) == 0:
        a = 1.0
    elif matches.group(1) == '-':
        a = -1.0
    else:
        try:
            a = float(matches.group(1))
        except ValueError:
            return None
        if a == 0:
            return None
    if matches.group(4) is None:
        b = 0.0
    elif matches.group(4) == '-' or matches.group(4) == '-x':
        b = -1.0
    elif matches.group(4) == '+' or matches.group(4) == '+x':
        b = 1.0
    elif matches.group(4) == '':
        b = 0.0
    else:
        try:
            b = float(matches.group(5))
        except ValueError:
            return None
    if matches.group(8) is None:
        c = 0.0
    else:
        try: 
            c = float(matches.group(8))
        except ValueError:
            return None
    delta = b**2 - 4*a*c
    response["hint"] = "Obliczamy deltę ze wzoru delta = b^2 - 4 * a * c.\ndelta = " + str(b).replace(".", ",") + "^2 - 4 * "+ str(a).replace(".", ",") + \
    " * " + str(c).replace(".", ",") + " = " + str(delta).replace(".", ",") + "\n"
    if delta < 0:
        response["solution"] = "Brak rozwiązań"     
        response["hint"] = response["hint"] +"delta < 0, więc brak rozwiązań"
        variant = 1
    elif delta == 0:
        x0 = -b/(2*a)
        response["solution"] = "x0 = " + str(x0)
        response["hint"] = response["hint"] + "delta = 0, zatem istnieje jedno rozwiązanie\nWzór: x0 = (-b) / (2 * a)\nWynik: x0 = "
        response["hint"] = response["hint"] + str(-1.0 * b).replace(".", ",") + " / (2 * "
        if a < 0:
            response["hint"] = response["hint"] + "(" + str(a).replace(".", ",") + ")"
        else:
            response["hint"] = response["hint"] + str(a).replace(".", ",") 
        response["hint"] = response["hint"] + ") = " + str(x0).replace(".", ",")
        variant = 2
    elif delta > 0:
        x1 = (-b - delta**0.5)/(2*a)
        x2 = (-b + delta**0.5)/(2*a)
        response["solution"] = "x1 = " + str(x1).replace(".", ",") + "\n" + "x2 = " + str(x2).replace(".", ",") 
        response["hint"] = response["hint"] + "delta > 0, zatem istnieją dwa rozwiązania\nWzory:\nx1 = (-b - delta^(1/2)) / (2 * a)\nx2 = (-b + delta^(1/2)) / (2 * a)\nWynik:\nx1 = ("
        response["hint"] = response["hint"] + str(-1.0 * b).replace(".", ",") +" - " + str(delta).replace(".", ",") + "^(1/2)) / (2 * "
        if a < 0:
            response["hint"] = response["hint"] + "(" + str(a).replace(".", ",") + ")"
        else:
            response["hint"] = response["hint"] + str(a).replace(".", ",") 
        response["hint"] = response["hint"] + ") = " + str(x1).replace(".", ",") + "\nx2 = ("
        response["hint"] = response["hint"] + str(-1.0 * b).replace(".", ",") +" + " + str(delta).replace(".", ",") + "^(1/2)) / (2 * "   
        if a < 0:
            response["hint"] = response["hint"] + "(" + str(a).replace(".", ",") + ")"
        else:
            response["hint"] = response["hint"] + str(a) 
        response["hint"] = response["hint"] + ") = " + str(x2).replace(".", ",")
        variant =3

    eq = equation
    result = -b/(2*a)
    if variant == 1:
        if result == -5 or result == 5:
            x = np.linspace(result-5.3, result+5.3, 100)
        else:
            x = np.linspace(result-5, result+5, 100)
    elif variant == 2:
        if result == -5 or result == 5:
            x = np.linspace(result-5.3, result+5.3, 100)
        else:
            x = np.linspace(result-5, result+5, 100)
        
    elif variant == 3:
        temp = abs(result-x1)
        x = np.linspace(result-temp -5.0, result + temp+ 5.0, 100)

    if b < 0:
        if c < 0:
            y = eval(str(a) + "*x**2" + str(b) + "*x" + str(c))
        else:
            y = eval(str(a) + "*x**2" + str(b) + "*x+"+ str(c))
        
    else:
        if c < 0:
            y = eval(str(a)+"*x**2+"+str(b) + "*x" + str(c))
        else:
            y = eval(str(a) + "*x**2+" + str(b) + "*x+" + str(c))
    matplotlib_lock.acquire()

    if result >= -5 and result <= 5:
        plt.axvline(0, color='#86bbd8')
    plt.plot(x, y, color='#d64550', label='y = '+eq.replace(".", ","))
    plt.title("Wykres funkcji")
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')  
    plt.legend(loc='upper left')  
    plt.locator_params(nbins=12)
    plt.grid(True)
    if variant == 1:
        q = -delta /(4*a)
        if abs(q) < 150.00:
            plt.axhline(0, color='#86bbd8')
    elif variant == 2:
        plt.axhline(0, color='#86bbd8')
        plt.scatter(x0, 0.0, color='#d64550')
        new_x0 = round(x0, 5)
        if a >=0:
            plt.annotate("  (" + str(new_x0).replace(".", ",") + ";0,0)",(x0+ 0.2, -0.1), fontsize = 11, verticalalignment='top')
        else:
            plt.annotate("  (" + str(new_x0).replace(".", ",") + ";0,0)",(x0+ 0.2, 0.1), fontsize = 11, verticalalignment='bottom')
    elif variant == 3:
        plt.axhline(0, color='#86bbd8')
        plt.scatter(x1, 0.0, color='#d64550')
        plt.scatter(x2, 0.0, color='#d64550')
        new_x1 = round(x1, 5)
        new_x2= round(x2, 5)
        if a >=0:
            plt.annotate("  (" + str(new_x1).replace(".", ",") + ";0,0)",(x1 - 0.2, -0.1), fontsize = 11, verticalalignment='top', horizontalalignment= "right")
            plt.annotate("  (" + str(new_x2).replace(".", ",") + ";0,0)",(x2+ 0.2, -0.1), fontsize = 11, verticalalignment='top')
        else:
            plt.annotate("  (" + str(new_x1).replace(".", ",") + ";0,0)",(x2- 0.2, 0.1), fontsize = 11, verticalalignment='bottom', horizontalalignment= "right")
            plt.annotate("  (" + str(new_x2).replace(".", ",") + ";0,.0)",(x2+ 0.2,-0.1), fontsize = 11, verticalalignment='top')
    fig = plt.gcf()
    img_data = io.BytesIO()
    fig.savefig(img_data, format = 'png')
    plt.clf()
    matplotlib_lock.release()
    img_data.seek(0)
    image_bytes = base64.b64encode(img_data.read())
    response["graph"] = image_bytes.decode("raw-unicode-escape")
















    return json.dumps(response)


    