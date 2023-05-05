package pl.edu.pwr.ksiegarniainternetowa.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookEntity;
import pl.edu.pwr.ksiegarniainternetowa.service.BookService;

import java.util.List;

@RestController
@CrossOrigin(origins = {"http://localhost:3000", "http://localhost:8000", "https://booksshop-dr.azurewebsites.net"})
@RequestMapping(value = "/v1")
@RequiredArgsConstructor
public class BookController {

    private final BookService bookService;

    @GetMapping(value = "/book/{id}")
    public ResponseEntity getBookById(@PathVariable("id") String bookIdStr) {

        Long bookId;

        try{
            bookId = Long.valueOf(bookIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Podano nieprawidłowe id książki");
        }

        BookEntity bookEntity;

        try{
            bookEntity = bookService.getBookById(bookId);
        }
        catch(EntityNotFoundException e){
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(e.getMessage());
        }

        return ResponseEntity.ok(bookEntity);
    }

    @GetMapping(value = "/books/by-Ids")
    public ResponseEntity<List<BookEntity>> getBooksByIds(@RequestParam("bookIds") List<Long> bookIds){

        List<BookEntity> foundBooks = bookService.getByIdList(bookIds);

        return ResponseEntity.ok(foundBooks);
    }
}
