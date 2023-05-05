from django.shortcuts import render
from database.database_module import database_executor as db
from django.http import HttpResponse
import datetime

def return_page(request):
    if request.method == "GET":
        return render(request, "index.html")
    return HttpResponse(status=403)

def return_page2(request, resource):
    if request.method == "GET":
        return render(request, "index.html")
    return HttpResponse(status=403)

def get_start_page_data(request):
    if request.method == "GET":
        page =db.get_start_page_data()
        if len(page) != 0:
            return HttpResponse(page, status=200)
        else:
            return HttpResponse(status=204)
    return HttpResponse(status=403)


def find_books(request):
    if request.method == "GET":
        title = request.GET.get('title', None)
        genre = request.GET.get('genres', None)
        if genre is not None:
            temp = list(genre.split(','))
            if len(temp) > 0:
                genre = temp
        author = request.GET.get('author', None)
        author_firstname = author_surname = None
        if author is not None:
            author = list(author.split(' '))
            if len(author) == 2:
                author_firstname = author[0]
                author_surname = author[1]        
        publisher = request.GET.get('publisher', None)
        release_date = None
        temp_date = request.GET.get('releaseDate', None)
        if temp_date is not None:
            temp_date = list(temp_date.split(' '))
            if len(temp_date) == 6:
                temp_month = temp_date[1]
                datetime_object = datetime.datetime.strptime(temp_month, "%b")
                month_number = datetime_object.month
                temp_date2 = temp_date[3] + '-' + str(month_number) + '-' + temp_date[2]
                if len(temp_date2) <= 10:
                    release_date = temp_date2
        min_price = request.GET.get('minPrice', None)
        if min_price is not None:
            if float(min_price) < 0:
                min_price = None
        max_price = request.GET.get('maxPrice', None)
        if max_price is not None:
            if float(max_price) < 0:
                max_price = None
        resp = db.find_books( title, genre, author_firstname, author_surname, publisher, release_date, min_price, max_price)
        if len(resp) > 2:
            return HttpResponse(resp, status=200)
        else:
            return HttpResponse(status=204)
    return HttpResponse(status=403)


def get_book(request, id: int):
    if request.method == "GET":
        resp = db.get_book(id)
        if len(resp) != 0:
            return HttpResponse(resp, status=200)
        else:
            return HttpResponse(status=204)
    return HttpResponse(status=403)




