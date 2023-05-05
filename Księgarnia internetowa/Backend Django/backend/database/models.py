from django.db import models

class MyTypeField(models.Field):
    def db_type(self, connection):
        return 'CHAR'


class Languages(models.Model):
    name = models.CharField(max_length=32, unique=True)


    class Meta:
        db_table = "Languages"


class BookCovers(models.Model):
    name = models.CharField(max_length=20, unique=True)


    class Meta:
        db_table = "BookCovers"


class Publishers(models.Model):
    name= models.CharField(max_length=50, unique=True)


    class Meta:
        db_table = "Publishers"


class BookCategories(models.Model):
    name = models.CharField(max_length=22, unique=True)


    class Meta:
        db_table = "BookCategories"


class Books(models.Model):
    book_category = models.ForeignKey(BookCategories, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    book_cover = models.ForeignKey(BookCovers, on_delete=models.CASCADE)
    language= models.ForeignKey(Languages, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description= models.TextField(blank=True)
    isbn= models.CharField(max_length=20, unique=True, blank=True)
    release_number = models.IntegerField(blank=True)
    release_date = models.DateField()
    size = models.CharField(max_length=11)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    is_available = models.BooleanField()
    num_of_book_items = models.IntegerField()
    number_of_pages = models.CharField(max_length = 20)
    avatar = models.BinaryField()


    class Meta:
        db_table = "Books"


class BookAuthors(models.Model):
    firstname = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)


    class Meta:
        db_table = "BookAuthors"


class BookAuthorships(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    book_author = models.ForeignKey(BookAuthors, on_delete=models.CASCADE)


    class Meta:
        db_table = "BookAuthorships"


class BookItems(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    code = models.IntegerField()


    class Meta:
        db_table = "BookItems"

class PersonalData(models.Model):
    name= models.CharField(max_length=32)
    surname= models.CharField(max_length=32)
    email= models.CharField(max_length=164)
    tel= models.CharField(max_length=25)


    class Meta:
        db_table = "PersonalData"


class Users(models.Model):
    username = models.CharField(max_length=30)
    password = MyTypeField()
    is_employee = models.BooleanField()

    class Meta:
        db_table = "Users"


class Clients(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    personal_data = models.ForeignKey(PersonalData, on_delete=models.CASCADE)


    class Meta:
        db_table = "Clients"


class ReceiversData(models.Model):
    name= models.CharField(max_length=10)
    personal_data = models.ForeignKey(PersonalData, on_delete=models.CASCADE)


    class Meta:
        db_table = "ReceiversData"


class OrdersStatuses(models.Model):
    name= models.CharField(max_length=10)


    class Meta:
        db_table = "OrdersStatuses"


class Orders(models.Model):
    order_status = models.ForeignKey(OrdersStatuses, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    receivers_data = models.ForeignKey(ReceiversData, on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=6,decimal_places=2)


    class Meta:
        db_table = "Orders"


class OrdersItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    book_item = models.ForeignKey(BookItems, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6,decimal_places=2)


    class Meta:
        db_table = "OrdersItems"


    







