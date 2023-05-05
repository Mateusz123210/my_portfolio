export interface Author {
    author_name: string,
    author_surname: string
}

export default interface Book{
    id: number
    title: string,
    authors: Author[],
    book_category: string,
    publisher: string,
    book_cover: string,
    language: string,
    avatar?: string,
    description?: string,
    isbn?: string,
    release_number?: number,
    release_date?: Date,
    size: string,
    number_of_pages: string,
    price: number
}