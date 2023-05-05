package pl.edu.pwr.ksiegarniainternetowa.service;

import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookEntity;

import java.util.List;

public interface BookService {

    boolean existsById(Long bookId);
    BookEntity getBookById(Long bookId);
    List<BookEntity> getByIdList(List<Long> ids);
}
