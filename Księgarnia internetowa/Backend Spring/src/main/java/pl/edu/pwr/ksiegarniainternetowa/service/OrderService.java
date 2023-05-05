package pl.edu.pwr.ksiegarniainternetowa.service;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.model.api.request.CreateOrder;
import pl.edu.pwr.ksiegarniainternetowa.model.api.request.OrderSearchCriteria;
import pl.edu.pwr.ksiegarniainternetowa.model.api.response.OrderWithDetails;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderStatusEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.PersonalDataEntity;

import javax.transaction.Transactional;
import java.util.List;

public interface OrderService {

    OrderWithDetails getById(Long orderId) throws EntityNotFoundException;

    List<OrderWithDetails> getOrdersByClientId(Long clientId);

    Page<OrderWithDetails> searchOrdersByCriteria(OrderSearchCriteria orderSearchCriteria, Pageable pageable);
    void checkOrder(Long clientId, PersonalDataEntity personalData, List<CreateOrder.BasketItem> basketItemList);

    Long placeOrder(Long clientId, PersonalDataEntity personalData, List<CreateOrder.BasketItem> basketItemList);

    OrderEntity changeOrderStatus(Long orderId, OrderStatusEntity orderStatusEntity);
}
