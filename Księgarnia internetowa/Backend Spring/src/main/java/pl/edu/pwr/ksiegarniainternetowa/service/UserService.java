package pl.edu.pwr.ksiegarniainternetowa.service;

import pl.edu.pwr.ksiegarniainternetowa.model.entity.UserEntity;

public interface UserService {
    UserEntity getById(Long id);

    UserEntity getByUsername(String username);

    UserEntity save(UserEntity userEntity);
}