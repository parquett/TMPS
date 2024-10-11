from abc import ABC, abstractmethod

# Interface Segregation Principle (ISP)
# Define separate interfaces for different responsibilities


# Interface for managing books
class BookManager(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, book):
        pass


# Interface for listing books
class BookLister(ABC):
    @abstractmethod
    def list_books(self):
        pass


# Interface for notifying users when a book is added
class UserNotifier(ABC):
    @abstractmethod
    def notify_user(self, message):
        pass


class EmailNotifier(UserNotifier):
    def notify_user(self, message):
        print(f"Email notification sent: {message}")


# DIP: BookStorage abstraction
class BookStorage(ABC):
    @abstractmethod
    def save(self, book):
        pass

    @abstractmethod
    def delete(self, book):
        pass


# Concrete implementation of BookStorage that uses a list
class ListBookStorage(BookStorage):
    def __init__(self):
        self.books = []

    def save(self, book):
        self.books.append(book)

    def delete(self, book):
        self.books.remove(book)


# LibraryManager depends on abstractions (ISP, DIP)
class LibraryManager(BookManager, BookLister):
    def __init__(self, storage: BookStorage, notifier: UserNotifier):
        self.storage = storage
        self.notifier = notifier

    def add_book(self, book):
        self.storage.save(book)
        self.notifier.notify_user(f"Book '{book['title']}' by {book['author']} added to the library.")

    def remove_book(self, book):
        self.storage.delete(book)
        self.notifier.notify_user(f"Book '{book['title']}' by {book['author']} removed from the library.")

    def list_books(self):
        for book in self.storage.books:
            print(f"{book['title']} by {book['author']}")


storage = ListBookStorage()
notifier = EmailNotifier()
library = LibraryManager(storage, notifier)

book1 = {"title": "1984", "author": "George Orwell"}
book2 = {"title": "To Kill a Mockingbird", "author": "Harper Lee"}

library.add_book(book1)
library.add_book(book2)

print("\nAll books in the library:")
library.list_books()
