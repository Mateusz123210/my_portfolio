package pl.edu.pwr.ksiegarniainternetowa.model.api.response;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
public class LoggedUserDetails {

    private String accessToken;
    private Long userId;
    private Long clientId;
}
