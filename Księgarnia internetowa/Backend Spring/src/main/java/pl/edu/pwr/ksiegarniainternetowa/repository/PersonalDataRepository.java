package pl.edu.pwr.ksiegarniainternetowa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.PersonalDataEntity;

import java.util.Optional;

@Repository
public interface PersonalDataRepository extends JpaRepository<PersonalDataEntity, Long> {
    
    Optional<PersonalDataEntity> findByNameAndSurnameAndEmailAndTel(
        String name, String surname, String email, String tel
    );
}
