package pl.edu.pwr.ksiegarniainternetowa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.ReceiverDataEntity;

@Repository
public interface ReceiverDataRepository extends JpaRepository<ReceiverDataEntity, Long> {
}
