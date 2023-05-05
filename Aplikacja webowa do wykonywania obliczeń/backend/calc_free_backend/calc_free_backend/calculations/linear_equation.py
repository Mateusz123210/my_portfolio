import re
import json
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('SVG')
import numpy as np
import io
import base64

def solve_linear_equation(equation, matplotlib_lock):
    equation = equation.replace(" ","").replace(",", ".")
    if len(equation) < 1:
        return None
    matcher = re.compile(r'^(-?(\d+(\.\d+)?)?)?x([+-]\d+(\.\d+)?)?$')
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
        b = -0.0
    else:
        try:
            b = float(matches.group(4))
        except ValueError:
            return None
    result = -1 * b / a
    response["solution"] = "x = " + str(result).replace(".", ",")
    hint = "Wynik równania ax + b = 0 obliczamy, przekształcając równanie.\n" + \
        "Wzór: x = -b / a\nWynik: x = " + str(-b).replace(".", ",") + " / "
    if a < 0:
        hint = hint + "(" + str(a).replace(".", ",") + ")"
    else:
        hint = hint + str(a).replace(".", ",")
    hint = hint + " = " + str(result).replace(".", ",")
    response["hint"] = hint
    eq = equation
    if result == -5 or result == 5:
        x = np.linspace(result-5.3, result+5.3, 100)
    else:
        x = np.linspace(result-5, result+5, 100)
    if b < 0:
        y = eval(str(a)+"*x"+str(b))
    else:
        y = eval(str(a)+"*x+"+str(b))
    matplotlib_lock.acquire()
    plt.axhline(0, color='#86bbd8')
    if result >= -5 and result <= 5:
        plt.axvline(0, color='#86bbd8')
    plt.plot(x, y, color='#d64550', label='y = '+eq.replace(".", ","))
    plt.title("Wykres funkcji")
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')  
    plt.legend(loc='upper left')  
    plt.locator_params(nbins=12)
    plt.grid(True)
    plt.scatter(result, 0, color='#d64550')
    if a >=0:
        plt.annotate("  (" + str(result).replace(".", ",") + ";0,0)",(result + 0.2,-0.1), fontsize = 11, verticalalignment='top')
    else:
        plt.annotate("  (" + str(result).replace(".", ",") + ";0,0)",(result + 0.2,0.1), fontsize = 11, verticalalignment='bottom')
    fig = plt.gcf()
    img_data = io.BytesIO()
    fig.savefig(img_data, format = 'png')
    plt.clf()
    matplotlib_lock.release()
    img_data.seek(0)
    image_bytes = base64.b64encode(img_data.read())
    response["graph"] = image_bytes.decode("raw-unicode-escape")
    return json.dumps(response)