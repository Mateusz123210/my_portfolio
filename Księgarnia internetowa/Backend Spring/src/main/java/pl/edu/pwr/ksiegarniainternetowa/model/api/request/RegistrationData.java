package pl.edu.pwr.ksiegarniainternetowa.model.api.request;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
public class RegistrationData {

    private String username;
    private char[] password;
    private String name;
    private String surname;
    private String email;
    private String tel;

}