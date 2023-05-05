from django.shortcuts import render
from django.http import HttpResponse
from django_ratelimit.decorators import ratelimit
from calc_free_backend.calculations import linear_equation, square_equation, averages, points_on_surface, sorting, triangle
from threading import Lock
matplotlib_lock= Lock()

@ratelimit(key='get:q',rate='10000000/s')
def return_page(request):
    if request.method=="GET":
        return render(request, "index.html")
    return HttpResponse(status=403)

@ratelimit(key='get:q',rate='10000000/s')
def return_page2(request, resource):
    return return_page(request)

@ratelimit(key='get:q',rate='1000000/s')
def solve_linear_equation(request):
    if request.method=="GET":
        equation = request.GET.get('equation', None)
        if equation is None:
            return HttpResponse(status=400)
        response = linear_equation.solve_linear_equation(equation, matplotlib_lock)
        if response is None:
            return HttpResponse(status=400)
        return HttpResponse(response, status=200)
    return HttpResponse(status=403)

@ratelimit(key='get:q',rate='1000000/s')
def solve_square_equation(request):
    if request.method=="GET":
        equation = request.GET.get('equation', None)
        if equation is None:
            return HttpResponse(status=400)
        response = square_equation.solve_square_equation(equation, matplotlib_lock)
        if response is None:
            return HttpResponse(status=400)
        return HttpResponse(response, status=200)
    return HttpResponse(status=403)

@ratelimit(key='get:q',rate='1000000/s')
def arithmetic_average(request):
    if request.method=="GET":
        numbers = request.GET.get('numbers', None)
        if numbers is None:
            return HttpResponse(status=400)
        numbers = list(numbers.split(";"))
        number_of_numbers = len(numbers)
        if number_of_numbers == 0:
            return HttpResponse(status=400)
        try:
            numbers = [float(x.replace(",",".")) for x in numbers]
        except ValueError:
            return HttpResponse(status=400)
        response = averages.solve_arithmetic_average(numbers, number_of_numbers)
        if response is None:
            return HttpResponse(status=400)
        return HttpResponse(response, status=200)
    return HttpResponse(status=403)

@ratelimit(key='get:q',rate='1000000/s')
def weighted_average(request):
    if request.method=="GET":
        numbers = request.GET.get('numbers', None)
        wages = request.GET.get('wages', None)
        if numbers is None or wages is None:
            return HttpResponse(status=400)
        numbers = list(numbers.split(";"))
        wages= list(wages.split(";"))
        number_of_numbers = len(numbers)
        if number_of_numbers == 0 or len(wages) != number_of_numbers:
            return HttpResponse(status=400)
        try:
            numbers = [float(x.replace(",",".")) for x in numbers]
            wages = [float(x.replace(",",".")) for x in wages]
        except ValueError:
            return HttpResponse(status=400)
        response = averages.solve_weighted_average(numbers, wages, number_of_numbers)
        if response is None:
            return HttpResponse(status=400)
        return HttpResponse(response, status=200)
    return HttpResponse(status=403)

@ratelimit(key='get:q',rate='1000000/s')
def distance_between_points(request):
    if request.method=="GET":
        first = request.GET.get('firstPoint', None)
        second = request.GET.get('secondPoint', None)
        if first is None or second is None:
            return HttpResponse(status=400)
        first = list(first.split(";"))
        second= list(second.split(";"))
        if len(first) !=2 or len(second) != 2:
            return HttpResponse(status=400)
        first[0] = first[0].replace(",", ".")
        first[1] = first[1].replace(",", ".")
        second[0] = second[0].replace(",", ".")
        second[1] = second[1].replace(",", ".")
        try:
            first = [float(x) for x in first]
            second = [float(x) for x in second]
        except ValueError:
            return HttpResponse(status=400)
        response = points_on_surface.find_distance_between_points(first,second, matplotlib_lock)
        if response is None:
            return HttpResponse(status=400)
        return HttpResponse(response, status=200)
    return HttpResponse(status=403)

@ratelimit(key='get:q',rate='1000000/s')
def bubble_sort(request):
    if request.method=="GET":
        numbers = request.GET.get('numbers', None)
        ascending = request.GET.get('ascending', None)
        if numbers is None or ascending is None:
            return HttpResponse(status=400)
        numbers = list(numbers.split(";"))
        number_of_numbers = len(numbers)
        if number_of_numbers == 0 or number_of_numbers > 30:
            return HttpResponse(status=400)
        try:
            numbers = [float(x.replace(",", ".")) for x in numbers]
        except ValueError:
            return HttpResponse(status=400)
        response = sorting.bubble_sort(numbers, ascending)
        if response is None:
            return HttpResponse(status=400)
        return HttpResponse(response, status=200)
    return HttpResponse(status=403)

@ratelimit(key='get:q',rate='1000000/s')
def quick_sort(request):
    if request.method=="GET":
        numbers = request.GET.get('numbers', None)
        ascending = request.GET.get('ascending', None)
        if numbers is None or ascending is None:
            return HttpResponse(status=400)
        numbers = list(numbers.split(";"))
        number_of_numbers = len(numbers)
        if number_of_numbers == 0 or number_of_numbers > 30:
            return HttpResponse(status=400)
        try:
            numbers = [float(x.replace(",", ".")) for x in numbers]
        except ValueError:
            return HttpResponse(status=400)
        response = sorting.quick_sort(numbers, ascending)
        if response is None:
            return HttpResponse(status=400)
        return HttpResponse(response, status=200)
    return HttpResponse(status=403)

@ratelimit(key='get:q',rate='1000000/s')
def calculate_triangle_properties(request):
    if request.method=="GET":
        first_side = request.GET.get('firstSide', None)
        second_side = request.GET.get('secondSide', None)
        hypotenuse = request.GET.get('hypotenuse', None)
        if first_side is not None:
            first_side = first_side.replace(",", ".")
        if second_side is not None:
            second_side = second_side.replace(",", ".")
        if hypotenuse is not None:
            hypotenuse = hypotenuse.replace(",", ".")
        try:
            if first_side is None:
                if second_side is None or hypotenuse is None:
                    return HttpResponse(status=400)
                second_side = float(second_side)
                hypotenuse = float(hypotenuse)
            else:
                if second_side is None:
                    if hypotenuse is None:
                        return HttpResponse(status=400)
                    first_side = float(first_side)
                    hypotenuse = float(hypotenuse)
                else:
                    first_side = float(first_side)
                    second_side = float(second_side)
                    if hypotenuse is not None:
                        hypotenuse = float(hypotenuse)
        except ValueError:
            return HttpResponse(status=400)
        response = triangle.calculate_triangle_properties(first_side, second_side, hypotenuse)
        if response is None:
            return HttpResponse(status=400)
        return HttpResponse(response, status=200)
    return HttpResponse(status=403)
