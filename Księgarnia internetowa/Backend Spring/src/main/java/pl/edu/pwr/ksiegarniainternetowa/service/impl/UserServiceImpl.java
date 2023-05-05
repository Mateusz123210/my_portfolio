package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityConflictException;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.UserEntity;
import pl.edu.pwr.ksiegarniainternetowa.repository.UserRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.UserService;

import java.util.Optional;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;

    @Override
    public UserEntity getById(Long id) {

        Optional<UserEntity> foundUserEntityOpt = userRepository.findById(id);

        if(foundUserEntityOpt.isEmpty()){
            throw new EntityNotFoundException("Nie istnieje użytkownik o takim id");
        }

        return foundUserEntityOpt.get();
    }

    @Override
    public UserEntity getByUsername(String username){

        return userRepository.getByUsername(username);
    }

    public UserEntity save(UserEntity userEntity) throws EntityConflictException {

        if(userRepository.existsByUsername(userEntity.getUsername())){
            throw new EntityConflictException("Istnieje już użytkownik o takiej nazwie użytkownika");
        }

        return userRepository.save(userEntity);
    }
}