from django.contrib import admin
from catalog.models import Genre,Book,BookInstance,Author

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Author)
# Register your models here.
