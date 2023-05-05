package pl.edu.pwr.ksiegarniainternetowa.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.User;
import org.springframework.web.bind.annotation.*;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityConflictException;
import pl.edu.pwr.ksiegarniainternetowa.model.api.request.RegistrationData;
import pl.edu.pwr.ksiegarniainternetowa.model.api.response.LoggedUserDetails;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.ClientEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.PersonalDataEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.UserEntity;
import pl.edu.pwr.ksiegarniainternetowa.repository.UserRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.ClientService;
import pl.edu.pwr.ksiegarniainternetowa.service.PersonalDataService;
import pl.edu.pwr.ksiegarniainternetowa.service.TokenService;
import pl.edu.pwr.ksiegarniainternetowa.service.UserService;

import java.security.Principal;

@RestController
@CrossOrigin(origins = {"http://localhost:3000", "http://localhost:8000", "https://booksshop-dr.azurewebsites.net"})
@RequestMapping(value = "/v1/user")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;
    private final PersonalDataService personalDataService;
    private final ClientService clientService;
    private final UserRepository userRepository;

    private final TokenService tokenService;

    @PostMapping(value = "/register")
    public ResponseEntity<String> registerUser(@RequestBody RegistrationData registrationData) {

        UserEntity userEntity = UserEntity.builder()
                .username(registrationData.getUsername())
                .password(registrationData.getPassword())
                .isEmployee(false)
                .build();

        try{
            userEntity = userService.save(userEntity);
        }
        catch(EntityConflictException e){
            return ResponseEntity.status(HttpStatus.CONFLICT).body(e.getMessage());
        }

        PersonalDataEntity personalDataEntity = PersonalDataEntity.builder()
                .name(registrationData.getName())
                .surname(registrationData.getSurname())
                .email(registrationData.getEmail())
                .tel(registrationData.getTel())
                .build();
        personalDataEntity = personalDataService.save(personalDataEntity);
        ClientEntity clientEntity = ClientEntity.builder()
                .userEntity(userEntity)
                .personalDataEntity(personalDataEntity)
                .build();
        clientService.save(clientEntity);
        return new ResponseEntity<>("Registration completed successfully", HttpStatus.OK);
    }

    @PostMapping("/token")
    public ResponseEntity token(Authentication authentication) {

        String token = tokenService.generateToken(authentication);

        User userInfo = (User) authentication.getPrincipal();

        String username = userInfo.getUsername();

        UserEntity userEntity = userService.getByUsername(username);

        Long clientId = null;

        if(!userEntity.getIsEmployee()){

            clientId = clientService.getByUserId(userEntity.getId()).getId();
        }

        LoggedUserDetails loggedUserDetails = LoggedUserDetails.builder()
                .accessToken(token)
                .userId(userEntity.getId())
                .clientId(clientId)
            .build();

        return ResponseEntity.ok(loggedUserDetails);
    }
}