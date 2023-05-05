import json

def solve_arithmetic_average(numbers: list, number_of_numbers):
    response = {}
    arithmetic_average = sum(numbers) / number_of_numbers
    response["solution"] = str(arithmetic_average).replace(".",",")
    hint = "Srednia arytmetyczna to suma liczb podzielona przez ich liczbę.\nWzór: (x1 + x2 + x3 + ... + xn) / n\nWynik: ("
    for a in numbers:
        hint = hint + str(a).replace(".",",") + " + "
    hint = hint[:-3] + ") / " + str(number_of_numbers) + " = " + str(arithmetic_average).replace(".",",")
    response["hint"] = hint
    return json.dumps(response)

def solve_weighted_average(numbers: list, wages: list, number_of_numbers):
    response = {}
    all_sum = 0.0
    wages_sum = sum(wages)
    for i in range(len(numbers)):
        if wages[i] < 0:
            return None
        all_sum += numbers[i] * wages[i]
    if wages_sum == 0.0:
        response["error"] = "Suma wag nie może być równa 0"
        return json.dumps(response)
    result = all_sum / wages_sum
    response["solution"] = str(result).replace(".", ",")
    hint = "Srednia ważona to suma liczb pomnożonych przez wagi tych liczb, podzielona przez sumę wag.\nWzór: (x1 * w1 + x2 * w2 + x3 * w3 + ... + xn * wn)"+\
        " / (w1 + w2 + w3 + ... + wn)\nWynik: ("
    for a in range(len(numbers)):
        hint = hint + str(numbers[a]).replace(".", ",") + " * " + str(wages[a]) + " + "
    hint = hint[:-3] + ") / ("
    for a in range(len(wages)):
        hint = hint + str(wages[a]).replace(".", ",") + " + "
    hint = hint[:-3] + ") = " + str(result).replace(".", ",")
    response["hint"] = hint
    return json.dumps(response)