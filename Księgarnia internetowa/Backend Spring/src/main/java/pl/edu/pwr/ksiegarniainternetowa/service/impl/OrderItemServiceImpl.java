package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookItemEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderItemEntity;
import pl.edu.pwr.ksiegarniainternetowa.repository.OrderItemRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.BookItemService;
import pl.edu.pwr.ksiegarniainternetowa.service.OrderItemService;
import pl.edu.pwr.ksiegarniainternetowa.service.OrderStatusService;

import java.math.BigDecimal;

@Slf4j
@Service
@RequiredArgsConstructor
public class OrderItemServiceImpl implements OrderItemService {

    private final OrderItemRepository orderItemRepository;
    private final OrderStatusService orderStatusService;
    private final BookItemService bookItemService;

    @Override
    public boolean isBookItemPurchasedByBookItemId(Long bookItemId) {

        if(!bookItemService.existsById(bookItemId)){
            throw new EntityNotFoundException("Nie istnieje egzemplarz książki o takim id");
        }

        return orderItemRepository.existsByOrderEntityOrderStatusEntityIdNotAndBookItemEntityId(
            orderStatusService.getByName("Wycofane").getId(),
            bookItemId
        );
    }

    @Override
    public void create(OrderEntity orderEntity, BookItemEntity bookItemEntity, BigDecimal price) {

        OrderItemEntity newOrderItemEntity = OrderItemEntity.builder()
            .orderEntity(orderEntity)
            .bookItemEntity(bookItemEntity)
            .price(price)
        .build();

        orderItemRepository.save(newOrderItemEntity);
    }
}
