package pl.edu.pwr.ksiegarniainternetowa;

import pl.edu.pwr.ksiegarniainternetowa.model.entity.*;
import pl.edu.pwr.ksiegarniainternetowa.repository.*;
import io.restassured.response.Response;
import lombok.RequiredArgsConstructor;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpStatus;
import org.springframework.test.context.ActiveProfiles;
import static io.restassured.RestAssured.given;
import static org.junit.jupiter.api.Assertions.*;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@ActiveProfiles("test")
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.DEFINED_PORT)
@RequiredArgsConstructor
public class BookControllerTest {

    @Autowired
    private BookAuthorRepository bookAuthorRepository;

    @Autowired
    private PublisherRepository publisherRepository;

    @Autowired
    private BookCategoryRepository bookCategoryRepository;

    @Autowired
    private LanguageRepository languageRepository;

    @Autowired
    private BookCoverRepository bookCoverRepository;

    @Autowired
    private BookRepository bookRepository;

    @Autowired
    private BookAuthorshipRepository bookAuthorshipRepository;

    private List<BookAuthorEntity> bookAuthorEntities = new ArrayList<>();
    private List<PublisherEntity> publisherEntities = new ArrayList<>();
    private List<BookCategoryEntity> bookCategoryEntities = new ArrayList<>();
    private List<LanguageEntity> languageEntities = new ArrayList<>();
    private List<BookCoverEntity> bookCoverEntities = new ArrayList<>();
    private List<BookEntity> bookEntities = new ArrayList<>();
    private List<BookAutorshipEntity> bookAutorshipEntities = new ArrayList<>();

    private final String url = "http://localhost:9000/v1";

    public void initBookAuthors(){

        for (int i=0; i < 5; i++){

            String str = String.valueOf(i);

            bookAuthorEntities.add(
                BookAuthorEntity.builder()
                    .firstname("Name " + str)
                    .surname("Surname " + str)
                .build()
            );
        }

        bookAuthorEntities = bookAuthorRepository.saveAll(bookAuthorEntities);
    }

    public void initPublishers(){

        for (int i=0; i < 5; i++){

            String str = String.valueOf(i);

            publisherEntities.add(
                PublisherEntity.builder()
                    .name("Publisher " + str)
                .build()
            );
        }

        publisherEntities = publisherRepository.saveAll(publisherEntities);
    }

    public void initBookCategories(){

        for (int i=0; i < 5; i++){

            String str = String.valueOf(i);

            bookCategoryEntities.add(
                BookCategoryEntity.builder()
                    .name("Category " + str)
                .build()
            );
        }

        bookCategoryEntities = bookCategoryRepository.saveAll(bookCategoryEntities);
    }

    public void initLanguages(){

        for (int i=0; i < 5; i++){

            String str = String.valueOf(i);

            languageEntities.add(
                LanguageEntity.builder()
                    .name("Language " + str)
                .build()
            );
        }

        languageEntities = languageRepository.saveAll(languageEntities);
    }

    public void initBookCovers(){

        for (int i=0; i < 5; i++){

            String str = String.valueOf(i);

            bookCoverEntities.add(
                BookCoverEntity.builder()
                    .name("Cover " + str)
                .build()
            );
        }

        bookCoverEntities = bookCoverRepository.saveAll(bookCoverEntities);
    }

    public void initBooks(){

        for (int i=0; i < 10; i++){

            String str = String.valueOf(i);

            bookEntities.add(
                BookEntity.builder()
                    .title("Title " + str)
                    .description("Desc " + str)
                    .isbn("Isbn " + str)
                    .releaseNumber(i)
                    .releaseDate(LocalDateTime.now())
                    .size(str + "x" + str + 2  + "x" + str + 4)
                    .price(BigDecimal.valueOf(i + i / 10))
                    .isAvailable(i % 5 == 0)
                    .numOfBookItems(0)
                    .numOfBookPages(str + 10)
                    .publisher(publisherEntities.get(i % 5))
                    .category(bookCategoryEntities.get(i % 5))
                    .language(languageEntities.get(i % 5))
                    .cover(bookCoverEntities.get(i % 5))
                .build()
            );
        }

        bookEntities = bookRepository.saveAll(bookEntities);
    }

    public void initBookAuthorships(){

        for (int i=0; i < 20; i++){

            bookAutorshipEntities.add(
                BookAutorshipEntity.builder()
                    .bookEntity(bookEntities.get(i % 10))
                    .author(bookAuthorEntities.get(i % 5))
                .build()
            );
        }

        bookAutorshipEntities = bookAuthorshipRepository.saveAll(bookAutorshipEntities);
    }

    @BeforeAll
    public void initAll() {

        initBookAuthors();
        initPublishers();
        initBookCategories();
        initLanguages();
        initBookCovers();
        initBooks();
        initBookAuthorships();
    }

    @Test
    public void shouldBookById(){

        BookEntity book = bookEntities.get(1);

        Response response = given()
            .when()
            .get(url + "/book/" + book.getId());

        response.then().statusCode(HttpStatus.OK.value());

        String responseStr = response.asString();

        //BookEntity gotBook = response.as(BookEntity.class);

        assertTrue(responseStr.contains("\"id\":" + book.getId()));
    }

    @Test
    public void shouldNotGetBookByNotExistingId(){

        Response response = given()
                .when()
                .get(url + "/book/20");

        response.then().statusCode(HttpStatus.NOT_FOUND.value());
    }

    @Test
    public void shouldNotGetBookByInvalidId(){

        Response response = given()
                .when()
                .get(url + "/book/a");

        response.then().statusCode(HttpStatus.BAD_REQUEST.value());
    }

    @Test
    public void shouldGetBooksWhichIdIsInIds(){

        Response response = given()
                .queryParam("bookIds", List.of(1, 2, 3))
            .when()
            .get(url + "/books/by-Ids");

        String strBooks = response.asString();

        System.out.println(strBooks);

        response.then().statusCode(HttpStatus.OK.value());

        assertTrue(strBooks.contains("\"id\":1"));
        assertTrue(strBooks.contains("\"id\":2"));
        assertTrue(strBooks.contains("\"id\":3"));
    }
}
