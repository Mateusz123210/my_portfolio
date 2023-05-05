package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.ClientEntity;
import pl.edu.pwr.ksiegarniainternetowa.repository.ClientRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.ClientService;

import java.util.Optional;

@Slf4j
@Service
@RequiredArgsConstructor
public class ClientServiceImpl implements ClientService {

    private final ClientRepository clientRepository;

    @Override
    public boolean existsById(Long id) {

        return clientRepository.existsById(id);
    }

    @Override
    public ClientEntity getById(Long id) throws EntityNotFoundException{

        Optional<ClientEntity> foundClientEntityOpt = clientRepository.findById(id);

        if(foundClientEntityOpt.isEmpty()){
            throw new EntityNotFoundException("Nie istnieje klient o takim id");
        }

        return foundClientEntityOpt.get();
    }

    @Override
    public ClientEntity getByUserId(Long userId){

        return clientRepository.getByUserEntityId(userId);
    }

    @Override
    public void save(ClientEntity clientEntity) {

    }
}
