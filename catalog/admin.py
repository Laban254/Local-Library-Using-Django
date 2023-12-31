from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     list_display= ('title', 'author', 'display_genre')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth',
                     'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth',
                                           'date_of_death')]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
     list_display = ('status', 'due_back')
