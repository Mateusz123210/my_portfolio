package pl.edu.pwr.ksiegarniainternetowa.service;

import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderStatusEntity;

import java.util.List;

public interface OrderStatusService {

    boolean existsById(Long id);
    OrderStatusEntity getByName(String name);

    List<OrderStatusEntity> getAll();
}
