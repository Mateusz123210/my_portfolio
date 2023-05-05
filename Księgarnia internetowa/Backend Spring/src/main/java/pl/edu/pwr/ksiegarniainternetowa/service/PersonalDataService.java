package pl.edu.pwr.ksiegarniainternetowa.service;

import pl.edu.pwr.ksiegarniainternetowa.model.entity.PersonalDataEntity;

public interface PersonalDataService {

    PersonalDataEntity getById(Long id);
    Long create(PersonalDataEntity personalDataEntity);

    PersonalDataEntity save(PersonalDataEntity personalDataEntity);
}
