package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookEntity;
import pl.edu.pwr.ksiegarniainternetowa.repository.BookRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.BookService;

import javax.transaction.Transactional;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class BookServiceImpl implements BookService {

    private final BookRepository bookRepository;

    @Override
    public boolean existsById(Long bookId) {

        return bookRepository.existsById(bookId);
    }

    @Override
    public BookEntity getBookById(Long bookId) {
        Optional<BookEntity> bookEntityOpt = bookRepository.findById(bookId);

        if(bookEntityOpt.isEmpty()){
            throw new EntityNotFoundException("Nie istnieje książka o takim id");
        }
        // Optional, zeby mozna bylo ewentualnie wyrzucac wyjatki

        return bookEntityOpt.get();
    }

    @Override
    public List<BookEntity> getByIdList(List<Long> ids) {

        return bookRepository.findAllById(ids);
    }
}
