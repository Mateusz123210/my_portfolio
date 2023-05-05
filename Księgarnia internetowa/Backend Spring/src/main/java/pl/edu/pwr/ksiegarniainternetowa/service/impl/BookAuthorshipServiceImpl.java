package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.repository.BookAuthorshipRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.BookAuthorshipService;

@Service
@RequiredArgsConstructor
public class BookAuthorshipServiceImpl implements BookAuthorshipService {

    private final BookAuthorshipRepository bookAuthorshipRepository;

}
