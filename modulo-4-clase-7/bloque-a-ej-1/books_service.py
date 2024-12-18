import re

books = [
	{
		"isbn": "19920043920-1",
		"name": "API Design Patterns",
		"publisher": "Talento Futuro",
		"year": "2024",
		"details": "The book provides a comprehensive introduction to the API design paterns that are industry-wide use these days."
	},
	{
		"isbn": "99293948392-1",
		"name": "Backend Software Engineering",
		"publisher": "Talento Futuro",
		"details": "This best-selling book on backend software development in the industry standard for guiding the development of such applications"
	}
]

def validate_isbn(isbn):
    """
    Valida el formato del ISBN.

    Args:
        isbn (str): El ISBN del libro a validar.

    Raises:
        ValueError: Si el ISBN no está presente o no es válido.

    Returns:
        None
    """
    if not isbn:
        raise ValueError("ISBN is required")
    # Compilamos una expresión regular para validar el formato del ISBN.
    # El formato esperado es de 10 a 13 dígitos seguidos de un guion y un dígito verificador.
    format_isbn = re.compile(r"^\d{10,13}-\d$")
    if not format_isbn.match(isbn):
        raise ValueError("ISBN is not valid")

def get_book_basic_data(isbn):
    """
    Obtiene los datos básicos de un libro dado su ISBN.

    Args:
        isbn (str): El ISBN del libro.

    Raises:
        ValueError: Si el ISBN no es válido.
        KeyError: Si no se encuentra un libro con el ISBN proporcionado.

    Returns:
        dict: Un diccionario con los datos básicos del libro (ISBN, nombre, editorial y año).
    """
    validate_isbn(isbn)
    for book in books:
        if book["isbn"] == isbn:
            return { 
                "isbn": book["isbn"], 
                "name": book["name"],
                "publisher": book["publisher"],
                "year": book["year"] 
            }
    raise KeyError("Book not found")

def get_a_book_details(isbn):
    """
    Obtiene los detalles de un libro dado su ISBN.

    Args:
        isbn (str): El ISBN del libro.

    Raises:
        ValueError: Si el ISBN no es válido.
        KeyError: Si no se encuentra un libro con el ISBN proporcionado.

    Returns:
        str: Los detalles del libro.
    """
    validate_isbn(isbn)
    for book in books:
        if book["isbn"] == isbn:
            return book["details"]
    raise KeyError("Book not found")