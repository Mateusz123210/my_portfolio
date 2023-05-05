import json

def calculate_triangle_properties(first_side, second_side, hypotenuse):
    result = hypotenuse
    response = {}
    if first_side is None:
        if second_side <= 0 or hypotenuse <= 0 or second_side >= hypotenuse:
            response["error"] = "Trójkąt prostokątny o podanych długościach boków nie istnieje!"
            return json.dumps(response)
        first_side = (hypotenuse ** 2 - second_side ** 2) ** 0.5
        response["firstSide"] = str(first_side).replace(".",",")
        first_hint = "==========\nBok a:\nDługość przyprostokątnej obliczamy z twierdzenia Pitagorasa.\n" + \
            "Wzór: a = (c^2 - b^2)^(1 / 2)\nWynik: a = (" + str(hypotenuse).replace(".",",") + "^2 - " + \
                str(second_side).replace(".",",") + "^2)^(1 / 2) = "+ str(first_side).replace(".",",") + "\n"
        response["hint"] = first_hint
    elif second_side is None:
        if first_side <= 0 or hypotenuse <= 0 or first_side >= hypotenuse:
            response["error"] = "Trójkąt prostokątny o podanych długościach boków nie istnieje!"
            return json.dumps(response)
        second_side = (hypotenuse ** 2 - first_side ** 2) ** 0.5
        response["secondSide"] = str(second_side).replace(".",",")
        second_hint = "==========\nBok b:\nDługość przyprostokątnej obliczamy z twierdzenia Pitagorasa.\n" + \
            "Wzór: b = (c^2 - a^2)^(1 / 2)\nWynik: b = (" + str(hypotenuse).replace(".",",") + "^2 - " + \
                str(first_side).replace(".",",") + "^2)^(1 / 2) = "+ str(second_side).replace(".",",") + "\n"
        response["hint"] = second_hint
    elif hypotenuse is None:
        if first_side <= 0 or second_side <= 0:
            response["error"] = "Trójkąt prostokątny o podanych długościach boków nie istnieje!"
            return json.dumps(response)
        result = (first_side ** 2 + second_side ** 2) ** 0.5
        response["hypotenuse"] = str(result).replace(".",",")
        hypotenuse_hint = "==========\nBok c:\nDługość przeciwprostokątnej obliczamy z twierdzenia Pitagorasa.\n" + \
            "Wzór: c = (a^2 + b^2)^(1 / 2)\nWynik: c = (" + str(first_side).replace(".",",") + "^2 + " + \
                str(second_side).replace(".",",") + "^2)^(1 / 2) = "+ str(result).replace(".",",") + "\n"
        response["hint"] = hypotenuse_hint 
    else:
        if first_side <= 0 or second_side <= 0:
            response["error"] = "Trójkąt prostokątny o podanych długościach boków nie istnieje!"
            return json.dumps(response)
        result = (first_side ** 2 + second_side ** 2) ** 0.5
        if abs(result - hypotenuse) > 0.000001:
            response["error"] = "Trójkąt prostokątny o podanych długościach boków nie istnieje!"
            return json.dumps(response) 
        response["hint"] = ""
    sinus = second_side/result
    response["sinL"] = str(sinus).replace(".",",")
    response["hint"] = response["hint"] + "==========\nsin(L):\nSinus kąta jest równy stosunkowi długości przyprostokątnej leżącej na przeciwko kąta do " + \
        "długości przeciwprostokątnej.\nWzór: sin(L) = b / c\nWynik: sin(L) = " + str(second_side).replace(".",",")+ " / " + str(result).replace(".",",") + \
            " = "+str(sinus).replace(".",",") + "\n"
    cosinus = first_side/result
    response["cosL"] = str(cosinus).replace(".",",")
    response["hint"] =  response["hint"] + "==========\ncos(L):\nCosinus kąta jest równy stosunkowi długości przyprostokątnej leżącej przy kącie do " + \
        "długości przeciwprostokątnej.\nWzór: cos(L) = a / c\nWynik: cos(L) = " + str(first_side).replace(".",",")+ " / " + str(result).replace(".",",") + \
            " = "+str(cosinus).replace(".",",") + "\n" 
    tangens = second_side/first_side
    response["tgL"] = str(tangens).replace(".",",")
    response["hint"] = response["hint"] + "==========\ntg(L):\nTangens kąta jest równy stosunkowi długości przyprostokątnej leżącej na przeciwko kąta do " + \
        "długości przyprostokątnej leżącej przy kącie.\nWzór: tg(L) = b / a\nWynik: tg(L) = " + str(second_side).replace(".",",")+ " / " + \
             str(first_side).replace(".",",") + \
            " = "+str(tangens).replace(".",",") + "\n" 
    cotangens = first_side/second_side
    response["ctgL"] = str(cotangens).replace(".",",")
    response["hint"] =  response["hint"] + "==========\nctg(L):\nCotangens kąta jest równy stosunkowi długości przyprostokątnej leżącej przy kącie do " + \
        "długości przyprostokątnej leżącej na przeciwko kąta.\nWzór: ctg(L) = a / b\nWynik: ctg(L) = " + str(first_side).replace(".",",")+ " / " + \
             str(second_side).replace(".",",") + \
            " = "+str(cotangens).replace(".",",") + "\n" 
    response["hint"] =  response["hint"] + "==========\nsin(B):\nSinus kąta jest równy stosunkowi długości przyprostokątnej leżącej na przeciwko kąta do " + \
        "długości przeciwprostokątnej.\nWzór: sin(B) = a / c\nWynik: sin(B) = " + str(first_side).replace(".",",")+ " / " + str(result).replace(".",",") + \
            " = "+str(cosinus).replace(".",",") + "\n" 
    response["hint"] =  response["hint"] + "==========\ncos(B):\nCosinus kąta jest równy stosunkowi długości przyprostokątnej leżącej przy kącie do " + \
        "długości przeciwprostokątnej.\nWzór: cos(B) = b / c\nWynik: cos(B) = " + str(second_side).replace(".",",")+ " / " + str(result).replace(".",",") + \
            " = "+str(sinus).replace(".",",") + "\n"
    response["hint"] =response["hint"] + "==========\ntg(B):\nTangens kąta jest równy stosunkowi długości przyprostokątnej leżącej na przeciwko kąta do " + \
        "długości przyprostokątnej leżącej przy kącie.\nWzór: tg(B) = a / b\nWynik: tg(B) = " + str(first_side).replace(".",",")+ " / " + \
             str(second_side).replace(".",",") + \
            " = "+str(cotangens).replace(".",",") + "\n" 
    response["hint"] = response["hint"] + "==========\nctg(B):\nCotangens kąta jest równy stosunkowi długości przyprostokątnej leżącej przy kącie do " + \
        "długości przyprostokątnej leżącej na przeciwko kąta.\nWzór: ctg(B) = b / a\nWynik: ctg(B) = " + str(second_side).replace(".",",")+ " / " + \
             str(first_side).replace(".",",") + \
            " = "+str(tangens).replace(".",",") + "\n"
    return json.dumps(response)