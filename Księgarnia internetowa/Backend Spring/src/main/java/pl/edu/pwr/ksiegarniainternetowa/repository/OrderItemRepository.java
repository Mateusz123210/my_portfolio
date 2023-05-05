package pl.edu.pwr.ksiegarniainternetowa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderItemEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderStatusEntity;

@Repository
public interface OrderItemRepository extends JpaRepository<OrderItemEntity, Long> {

    boolean existsByOrderEntityOrderStatusEntityIdNotAndBookItemEntityId(Long orderStatusId, Long bookItemId);
}
