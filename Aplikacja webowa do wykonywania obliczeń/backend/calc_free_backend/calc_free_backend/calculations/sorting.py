import json

def bubble_sort(numbers, ascending):
    numbers_length = len(numbers)
    response = {}
    response["hint"] = "Sortowanie bąbelkowe polega na cyklicznej zamianie dwóch sąsiadujących elementów, jeżeli" + \
        " nie są ułożone w kolejności, w której sortujemy. Przebieg sortowania:\n"
    change_counter = 0
    if ascending == "yes":
        for i in range(numbers_length-1):
            change = False
            for j in range(numbers_length - i - 1):
                if numbers[j+1] < numbers[j]:
                    (numbers[j], numbers[j+1]) = (numbers[j+1], numbers[j])
                    response["hint"] = response["hint"] + "Zamiana elementów (nr iteracji pętli zewnętrznej: " + \
                        str(i+1) + ", nr iteracji pętli wewnętrznej: " + str(j+1) + ")\nStan po zamianie: " + \
                            str(numbers).replace(",", ";").replace(".", ",") + "\n"
                    change = True
                    change_counter += 1
            if change is False:
                break
    else:
        for i in range(numbers_length-1):
            change = False
            for j in range(numbers_length - i - 1):
                if numbers[j+1] > numbers[j]:
                    (numbers[j], numbers[j+1]) = (numbers[j+1], numbers[j])
                    response["hint"] = response["hint"] + "Zamiana elementów (nr iteracji pętli zewnętrznej: " + \
                        str(i+1) + ", nr iteracji pętli wewnętrznej: " + str(j+1) + ")\nStan po zamianie: " + \
                            str(numbers).replace(",", ";").replace(".", ",") + "\n"
                    change = True
                    change_counter += 1
            if change is False:
                break
    response_solution = ""
    for i in numbers:
        response_solution += str(i) + ";"
    response_solution = response_solution[:-1]
    response["solution"] = response_solution.replace(".", ",")
    response["hint"] = response["hint"] + "\nLiczba wykonanych zamian: " + str(change_counter) + "."
    return json.dumps(response)

    
def quick_sort(numbers, ascending):
    response = {}
    response["hint"] = "Sortowanie szybkie (quicksort) polega na wybraniu pewnej liczby z sortowanych liczb oraz " + \
        "podziale elementów na dwie grupy. W jednej umieszczamy liczby mniejsze od wybranej wartości, a w drugiej większe lub równe. " + \
            "Procedurę należy powtórzyć rekurencyjnie dla obu grup.\n"
    response["operations"] = 0
    if ascending == "yes":
        quicksort_algorithm_ascending(numbers, 0, len(numbers) - 1, response)
    else:
        quicksort_algorithm_descending(numbers, 0, len(numbers) - 1, response)
    solution = ""
    for a in numbers:
        solution += str(a)+";"
    solution = solution[:-1]
    all_operations = response["operations"]
    response["hint"] = response["hint"] + "\nLiczba wykonanych zamian: " + str(all_operations) + "."
    response["solution"] = solution.replace(".", ",")

    return json.dumps(response)

def partition_ascending(numbers_list, first, last, response):
    pivot = numbers_list[last]
    response["hint"] = response["hint"] +"================\n" + "Oś: " + str(pivot).replace(".", ",") + "\nStan początkowy:\n"
    response["hint"] = response["hint"] + str(numbers_list).replace(",", ";").replace(".", ",") + "\nZamiany: \n"
    i = first -1
    for j in range(first, last):
        if numbers_list[j] <= pivot:
            i = i + 1
            response["operations"] += 1
            (numbers_list[i], numbers_list[j]) = (numbers_list[j], numbers_list[i])
            response["hint"] = response["hint"] + str(numbers_list[first: last+1]).replace(",", ";").replace(".", ",") + "\n"
    (numbers_list[i+1], numbers_list[last]) = (numbers_list[last], numbers_list[i+1])
    response["operations"] += 1
    response["hint"] = response["hint"] + str(numbers_list[first: last+1]).replace(",", ";").replace(".", ",") + "\n"
    response["hint"] = response["hint"] +"Stan końcowy:\n" + str(numbers_list).replace(",", ";").replace(".", ",") + "\n"
    return i+1

def quicksort_algorithm_ascending(numbers_list, first, last, response):
    if first < last:
        position = partition_ascending(numbers_list, first, last, response)
        quicksort_algorithm_ascending(numbers_list, first, position - 1, response)
        quicksort_algorithm_ascending(numbers_list, position + 1, last, response)


def partition_descending(numbers_list, first, last, response):
    pivot = numbers_list[last]
    response["hint"] = response["hint"] +"================\n" + "Oś: " + str(pivot).replace(".", ",") + "\nStan początkowy:\n"
    response["hint"] = response["hint"] + str(numbers_list).replace(",", ";").replace(".", ",") + "\nZamiany: \n"
    i = first -1
    for j in range(first, last):
        if numbers_list[j] >= pivot:
            i = i + 1
            response["operations"] += 1
            (numbers_list[i], numbers_list[j]) = (numbers_list[j], numbers_list[i])
            response["hint"] = response["hint"] + str(numbers_list[first: last+1]).replace(",", ";").replace(".", ",") + "\n"
    (numbers_list[i+1], numbers_list[last]) = (numbers_list[last], numbers_list[i+1])
    response["operations"] += 1
    response["hint"] = response["hint"] + str(numbers_list[first: last+1]).replace(",", ";").replace(".", ",") + "\n"
    response["hint"] = response["hint"] +"Stan końcowy:\n" + str(numbers_list).replace(",", ";").replace(".", ",") + "\n"
    return i+1

def quicksort_algorithm_descending(numbers_list, first, last, response):
    if first < last:
        position = partition_descending(numbers_list, first, last, response)
        quicksort_algorithm_descending(numbers_list, first, position - 1, response)
        quicksort_algorithm_descending(numbers_list, position + 1, last, response)