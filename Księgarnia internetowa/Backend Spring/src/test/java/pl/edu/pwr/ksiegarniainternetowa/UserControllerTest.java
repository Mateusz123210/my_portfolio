package pl.edu.pwr.ksiegarniainternetowa;

import io.restassured.response.Response;
import lombok.RequiredArgsConstructor;
import org.apache.http.entity.ContentType;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpStatus;
import org.springframework.test.context.ActiveProfiles;
import pl.edu.pwr.ksiegarniainternetowa.model.api.request.RegistrationData;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookCategoryEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.UserEntity;
import pl.edu.pwr.ksiegarniainternetowa.repository.ClientRepository;
import pl.edu.pwr.ksiegarniainternetowa.repository.PersonalDataRepository;
import pl.edu.pwr.ksiegarniainternetowa.repository.UserRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.ClientService;

import java.util.ArrayList;
import java.util.List;

import static io.restassured.RestAssured.given;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@ActiveProfiles("test")
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.DEFINED_PORT)
@RequiredArgsConstructor
public class UserControllerTest {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PersonalDataRepository personalDataRepository;

    @Autowired
    private ClientRepository clientRepository;

    private List<UserEntity> userEntities = new ArrayList<>();

    private final String url = "http://localhost:9000/v1/user";

    @BeforeAll
    public void initAll() {

        for (int i=0; i < 6; i++){

            String str = String.valueOf(i);

            userEntities.add(
                UserEntity.builder()
                    .username("Username " + str)
                    .password(("Password " + str).toCharArray())
                    .isEmployee(i % 2 == 0)
                .build()
            );
        }

        userEntities = userRepository.saveAll(userEntities);
    }

    @Test
    public void shouldRegisterUser(){

        Response response = given()
            .when()
                .contentType(ContentType.APPLICATION_JSON.toString())
                .body(
                    RegistrationData.builder()
                        .username("kamil")
                        .password(("dywan").toCharArray())
                        .name("Kamil")
                        .surname("Dywan")
                        .email("kamil@mail.com")
                        .tel("000111222")
                    .build()
                )
            .post(url + "/register");

        assertTrue(userRepository.findById(7L).get().getUsername().equals("kamil"));
        assertTrue(personalDataRepository.findById(1L).get().getName().equals("Kamil"));
        assertTrue(clientRepository.findById(1L).get().getUserEntity().getUsername().equals("kamil"));
    }
}
