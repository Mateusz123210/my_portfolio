package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.repository.BookCoverRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.BookCoverService;

@Service
@RequiredArgsConstructor
public class BookCoverServiceImpl implements BookCoverService {

    private final BookCoverRepository bookCoverRepository;

}
