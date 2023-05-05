package pl.edu.pwr.ksiegarniainternetowa.service;

import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookItemEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderItemEntity;

import java.math.BigDecimal;

public interface OrderItemService {

    boolean isBookItemPurchasedByBookItemId(Long bookItemId);
    void create(OrderEntity orderEntity, BookItemEntity bookItemEntity, BigDecimal price);
}
