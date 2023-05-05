package pl.edu.pwr.ksiegarniainternetowa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderStatusEntity;

import java.util.Optional;

@Repository
public interface OrderStatusRepository extends JpaRepository<OrderStatusEntity, Long> {

    Optional<OrderStatusEntity> findByName(String name);
}
