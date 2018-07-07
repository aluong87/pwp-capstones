class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The user's email, {email}, has been updated.".format(email=self.email))

    def __repr__(self):
        print("User {name}, email: {email}, books read: {books}".format(name=self.name, email=self.email, books=str(len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        average = 0
        rating = 0
        for values in self.books.values():
            if value:
                average += values
                rating += 1
        average = average/rating
        return average

class Book:

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.new_isbn = isbn
        print("The book's ISBN has been updated to {isbn}.".format{isbn=str(self.new_isbn)})

    def add_rating(self, rating):
        if rating and rating > 0 and rating <= 4:
            self.ratings.append(rating)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.title == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        average = 0
        for value in self.ratings:
            average += value
        average = average/len(self.ratings)
        return average

class Fiction(Book):

    def __init__(self, author):
        super(Fiction, self).__init__()
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):

    def __init__(self, subject, level):
        super(Non_Fiction, self).__init__()
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater:

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Book(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Book(title, subject, level, isbn)
        return new_none_fiction

    def get_user_average_rating(self, email):
        user = self.users.get(email, None)
        if user:
            return user.get_average_rating()
        else:
            return "No such user!"

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, None)
        if user:
            user.read_book(book, rating)
            if book not in self.books:
                self.books[book] = 0
            self.books[book] += 1
            book.add_rating(rating)
        else:
            print("No user with email {email}!".format(email=self.email))

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        max_read = float("-inf")
        most_read = new_none_fiction
        for book in self.books:
            num_read = self.books[book]
            if num_read > max_read:
                max_read = num_read
                most_read = book
        return most_read

    def highest_rated_book(self):
        highest_rating = float("-inf")
        best_book = none
        for book in self.books:
            average = book.get_average_rating()
            if average > highest_rating:
                highest_rating = average
                best_book = book
        return best_book

    def most_positive_user(self):
        highest_rating = float("-inf")
        nicest_user = None
        for user in self.users.values():
            average = user.get_average_rating()
            if average > highest_rating:
                highest_rating = average
                nicest_user = user
        return nicest_user
