package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.PersonalDataEntity;
import pl.edu.pwr.ksiegarniainternetowa.repository.PersonalDataRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.PersonalDataService;

import java.util.Optional;

@Slf4j
@Service
@RequiredArgsConstructor
public class PersonalDataServiceImpl implements PersonalDataService {

    private final PersonalDataRepository personalDataRepository;

    @Override
    public PersonalDataEntity getById(Long id) throws EntityNotFoundException {

        Optional<PersonalDataEntity> foundPersonalDataOpt = personalDataRepository.findById(id);

        if(foundPersonalDataOpt.isEmpty()){
            throw new EntityNotFoundException("Nie istnieją dane personalne o takim id");
        }

        return foundPersonalDataOpt.get();
    }

    @Override
    public Long create(PersonalDataEntity personalDataEntity) {

        Optional<PersonalDataEntity> foundPersonalDataEntity =
            personalDataRepository.findByNameAndSurnameAndEmailAndTel(
                personalDataEntity.getName(),
                personalDataEntity.getSurname(),
                personalDataEntity.getEmail(),
                personalDataEntity.getTel()
            );

        if(foundPersonalDataEntity.isPresent()){
            return foundPersonalDataEntity.get().getId();
        }

        PersonalDataEntity newPersonalDataEntity = PersonalDataEntity.builder()
            .name(personalDataEntity.getName())
            .surname(personalDataEntity.getSurname())
            .email(personalDataEntity.getEmail())
            .tel(personalDataEntity.getTel())
        .build();

        return personalDataRepository.save(newPersonalDataEntity).getId();
    }

    @Override
    public PersonalDataEntity save(PersonalDataEntity personalDataEntity) {
        return null;
    }
}
