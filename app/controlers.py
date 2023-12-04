from litestar import Controller, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData
from fastapi import HTTPException, Query
from sqlalchemy.orm import Session

from app.dtos import BookReadDTO, BookWriteDTO
from app.models import Book, Loan
from app.repositories import BookRepository, LoanRepository, provide_books_repo, provide_loan_repo
from app.database import SessionLocal

class BookController(Controller):
    path = "/books"
    tags = ["books"]
    return_dto = BookReadDTO
    dependencies = {"books_repo": Provide(provide_books_repo), "loan_repo": Provide(provide_loan_repo)}

    @get()
    async def list_books(self, books_repo: BookRepository) -> list[Book]:
        return books_repo.list()

    @post(dto=BookWriteDTO)
    async def create_book(self, data: Book, books_repo: BookRepository) -> Book:
        return books_repo.add(data)

    @get("/{book_id:int}", return_dto=BookReadDTO)
    async def get_book(self, book_id: int, books_repo: BookRepository) -> Book:
        book = books_repo.get_by_id(book_id) 
        if not book:
            raise HTTPException(status_code=404, detail="No se encontró el libro")
        return book

    @patch("/{book_id:int}", dto=BookWriteDTO)
    async def update_book(
        self, book_id: int, data: DTOData[Book], books_repo: BookRepository
    ) -> Book:
        book = books_repo.get_by_id(book_id) 
        if not book:
            raise HTTPException(status_code=404, detail="No se encontró el libro")
        book = data.update_instance(book)
        return books_repo.update(book)

    @post("/{book_id:int}/loan")
    async def create_loan(self, book_id: int, loan_repo: LoanRepository, books_repo: BookRepository = Provide(provide_books_repo)) -> Loan:
        book = books_repo.get_by_id(book_id)

        if not book:
            raise HTTPException(status_code=404, detail="No se encontró el libro")
        
        # Agrega lógica adicional según tus requerimientos (verificación de disponibilidad, fechas, etc.)
        
        # Crea un nuevo préstamo
        loan = loan_repo.create_loan(book_id)
        return loan

    @get("/search")
    async def search_books_by_title(
        self, title: str = Query(..., title="nombre del libro"), books_repo: BookRepository = Provide(provide_books_repo)
    ) -> list[Book]:
        books = books_repo.search_by_title(title)
        return books