import MySQLdb as mc
from database.models import *
from database.serializers import BooksSerializer,BooksSerializer2, BookAuthorshipsSerializer, BookCategoriesSerializer
import json
import datetime

def get_start_page_data():
    all_entries = Books.objects.filter(is_available = 1)
    list1 = []
    dict1 = {}
    serializer = BooksSerializer(all_entries, many = True)
    dict1["books"] = serializer.data
    list1.append(dict1)    
    dict2 = {}
    all_categories = BookCategories.objects.all()
    serializer = BookCategoriesSerializer(all_categories, many = True)
    dict2["categories"] = serializer.data
    list1.append(dict2)    
    ret = json.dumps(list1)
    return ret
   
def find_books(title1: str, genre1: list, author_firstname: str, author_surname:str, publisher1: str, release1: str, min1: str, max1: str):
    all_entries = None
    dict1 = {}
    dict1['is_available'] = 1
    if title1 is not None:
        dict1['title__icontains'] = title1
    if release1 is not None:
        format = '%Y-%m-%d'
        try:
            date = datetime.datetime.strptime(release1, format).date()
        except ValueError:
            return ""
        dict1['release_date__exact'] = date
    if min1 is not None:
        min2 = float(min1)
        dict1['price__gte'] = min2
    if max1 is not None:
        max2 = float(max1)
        dict1['price__lte'] = max2
    all_entries = Books.objects.filter(**dict1).select_related('book_category','publisher')
    list1 = []
    for i in all_entries:
        good = True
        if genre1 is not None:
            if i.book_category.name not in genre1:
                good = False
        if good is True and publisher1 is not None:
            if publisher1 != i.publisher.name:
                good = False
        if good is True:
            if author_firstname is not None:
                authors = BookAuthorships.objects.select_related('book_author').filter(book = i.id)
                contains = False
                for j in authors:
                    if j.book_author.firstname == author_firstname and j.book_author.surname == author_surname:
                        contains = True
                        break                
                if contains is True:
                    serializer = BooksSerializer(i)
                    list1.append(serializer.data)
            else:
                serializer = BooksSerializer(i)
                list1.append(serializer.data)
    return json.dumps(list1)

def get_book(id: int):
    all_entries = Books.objects.filter(is_available = 1, id = id).select_related('book_category','publisher','book_cover','language')
    if (not(all_entries is None)) and len(all_entries) > 0:
        dict1 = {}
        serializer = BooksSerializer2(all_entries[0])
        dict1["book"] = serializer.data
        authors = BookAuthorships.objects.select_related('book_author').filter(book = all_entries[0].id)
        serializer2 = BookAuthorshipsSerializer(authors, many = True)
        dict1["authors"] = serializer2.data
        ret = json.dumps(dict1)
        return ret
    return ""


