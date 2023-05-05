package pl.edu.pwr.ksiegarniainternetowa.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.ClientEntity;

public interface ClientService {

    boolean existsById(Long id);
    ClientEntity getById(Long id);

    ClientEntity getByUserId(Long userId);

    void save(ClientEntity clientEntity);
}
