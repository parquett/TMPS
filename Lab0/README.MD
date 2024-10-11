# SOLID Implementation

### Author: Martiniuc Artiom

## Objectives:
- Implement 2 SOLID letters in a simple project.

## Design Patterns Used:

**1. Interface Segregation Principle (ISP)**  
The system adheres to ISP by defining separate interfaces for managing books (`BookManager`), listing books (`BookLister`), and notifying users (`UserNotifier`). This ensures that each class has specific responsibilities.

**2. Dependency Inversion Principle (DIP)**  
The `LibraryManager` class depends on abstractions (`BookStorage` and `UserNotifier`) rather than concrete implementations, promoting flexibility and scalability in the system.

## Implementation:

This system models a simple library management solution using design patterns and clean architecture principles. The system follows ISP by segregating responsibilities into different interfaces for adding/removing books, listing books, and notifying users. The DIP principle is implemented by making `LibraryManager` depend on abstract classes (`BookStorage` and `UserNotifier`), allowing for various storage and notification implementations.

### Key Features:
- **Book Management**: The `LibraryManager` allows adding and removing books to/from the library.
- **Listing Books**: The `LibraryManager` can list all books stored in the library.
- **User Notification**: The system notifies users via email when a book is added or removed, using the `UserNotifier` abstraction.

### Snippets from the Code:

```python
# Interface for managing books
class BookManager(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def remove_book(self, book):
        pass
```
```python
# Implementation of BookStorage that uses a list
class ListBookStorage(BookStorage):
    def __init__(self):
        self.books = []

    def save(self, book):
        self.books.append(book)

    def delete(self, book):
        self.books.remove(book)
```
```python
# Concrete implementation of BookStorage that uses a list
class ListBookStorage(BookStorage):
    def __init__(self):
        self.books = []

    def save(self, book):
        self.books.append(book)

    def delete(self, book):
        self.books.remove(book)
```
## Results:
After executing the code, two books are added to the library, and the notifications are sent.
The system then lists all books currently in the library.

```commandline
Email notification sent: Book '1984' by George Orwell added to the library.
Email notification sent: Book 'To Kill a Mockingbird' by Harper Lee added to the library.

All books in the library:
1984 by George Orwell
To Kill a Mockingbird by Harper Lee
```

## Conclusion:
This implementation effectively uses the ISP and DIP principles to create a flexible and maintainable library management system. By abstracting book storage and user notification, the system is easily extendable to other storage mechanisms (e.g., databases) and notification methods (e.g., SMS).
