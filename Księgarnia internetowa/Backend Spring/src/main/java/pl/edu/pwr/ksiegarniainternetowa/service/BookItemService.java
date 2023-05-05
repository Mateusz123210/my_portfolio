package pl.edu.pwr.ksiegarniainternetowa.service;

import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookItemEntity;

import java.util.List;

public interface BookItemService {

    boolean existsById(Long id);
    List<BookItemEntity> getAvailableBookItemsByBookId(Long bookId);
}
