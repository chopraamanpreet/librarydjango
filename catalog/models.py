from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    """A typical class defining a model, derived from the Model class."""
    name=models.CharField(max_length=200,help_text='Enter book genre')

    def __str__(self):
        """String for representing the Genre object (in Admin site etc.)."""
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary=models.CharField(max_length=1000, help_text='Brief about the book')
    isbn=models.CharField('ISBN',max_length=13,help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre=models.ManyToManyField(Genre,help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])
    
class BookInstance(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4,help_text='unique id')
    book=models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)

    LOAN_STATUS=(
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','available'),
        ('r','reversed'),
    )

    status=models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability'
    )

    class Meta:
        ordering=['due_back']

    def __str__(self):
        return f'{self.id}({self.book.title})'


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'