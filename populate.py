import os
import django
import random
from faker import Faker
from applications.books.models import Book
from applications.loans.models import Loan
from applications.users.models import UserProfile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system_project.settings.local')
django.setup()

fake = Faker()

def populate_users(n=10):
    for _ in range(n):
        fake_name = fake.name()
        fake_email = fake.email()
        fake_date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
        UserProfile.objects.create(
            name=fake_name,
            email=fake_email,
            date_of_birth=fake_date_of_birth,
        )

def populate_books(n=10):
    for _ in range(n):
        fake_title = fake.sentence(nb_words=3)
        fake_author = fake.name()
        fake_isbn = fake.isbn13(separator="")
        fake_copies = random.randint(1, 10)
        Book.objects.create(
            title=fake_title,
            author=fake_author,
            isbn=fake_isbn,
            available_copies=fake_copies,
        )

def populate_loans(n=10):
    users = list(UserProfile.objects.all())
    books = list(Book.objects.all())
    for _ in range(n):
        loan_user = random.choice(users)
        loan_book = random.choice(books)
        Loan.objects.create(
            user=loan_user,
            book=loan_book,
            return_date=fake.date_between(start_date='-1y', end_date='today')
        )

print("Populate script started...")
populate_users(10)
populate_books(10)
populate_loans(20)
print("Populate script finished.")
