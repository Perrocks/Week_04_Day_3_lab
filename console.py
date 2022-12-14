import pdb

from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


author_1 = Author("Harper Lee")
author_repository.save(author_1)

book_1 = Book ("To Kill a Mockingbird", author_1, "murder mystery")
book_repository.save(book_1)
