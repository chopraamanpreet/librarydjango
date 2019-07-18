from django.contrib import admin
from catalog.models import Genre,Book,BookInstance,Author

#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Genre)
#admin.site.register(Author)

#To change how a model is displayed in the admin interface you define a ModelAdmin class

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name','date_of_birth','date_of_death')


#register the admin class with model
admin.site.register(Author,AuthorAdmin)


#using @register decorater to register the model

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(BookInstanceAdmin)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
