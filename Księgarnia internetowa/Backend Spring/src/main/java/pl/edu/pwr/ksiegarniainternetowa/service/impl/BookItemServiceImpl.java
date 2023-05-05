package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookItemEntity;
import pl.edu.pwr.ksiegarniainternetowa.repository.BookItemRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.BookItemService;
import pl.edu.pwr.ksiegarniainternetowa.service.BookService;

import java.util.List;

@Slf4j
@Service
@RequiredArgsConstructor
public class BookItemServiceImpl implements BookItemService {

    private final BookItemRepository bookItemRepository;
    private final BookService bookService;

    @Override
    public boolean existsById(Long id) {

        return bookItemRepository.existsById(id);
    }

    public List<BookItemEntity> getAvailableBookItemsByBookId(Long bookId) throws EntityNotFoundException {

        if(!bookService.existsById(bookId)){
            throw new EntityNotFoundException("Nie istnieje książka o takim id");
        }

        return bookItemRepository.findFirst10ByBookEntityIdAndIsPurchased(bookId, false);
    }
}
