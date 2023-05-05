package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.mapper.DateTimeMapper;
import pl.edu.pwr.ksiegarniainternetowa.model.api.request.CreateOrder;
import pl.edu.pwr.ksiegarniainternetowa.model.api.request.OrderSearchCriteria;
import pl.edu.pwr.ksiegarniainternetowa.model.api.response.OrderWithDetails;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.*;
import pl.edu.pwr.ksiegarniainternetowa.repository.OrderRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.*;
import pl.edu.pwr.ksiegarniainternetowa.specification.OrderSpecification;

import javax.persistence.criteria.CriteriaBuilder;
import javax.transaction.Transactional;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDateTime;
import java.time.OffsetDateTime;
import java.util.*;
import java.util.stream.Collectors;

@Slf4j
@Service
@RequiredArgsConstructor
public class OrderServiceImpl implements OrderService {

    private final OrderRepository orderRepository;
    private final ClientService clientService;
    private final BookItemService bookItemService;
    private final BookService bookService;
    private final PersonalDataService personalDataService;
    private final ReceiverDataService receiverDataService;
    private final OrderStatusService orderStatusService;
    private final OrderItemService orderItemService;

    private final DateTimeMapper dateTimeMapper = DateTimeMapper.INSTANCE;

    @Override
    public OrderWithDetails getById(Long orderId) throws EntityNotFoundException{

        Optional<OrderEntity> foundOrderEntityOpt = orderRepository.findById(orderId);

        if(foundOrderEntityOpt.isEmpty()){
            throw new EntityNotFoundException("Nie istnieje zamówienie o takim id");
        }

        OrderEntity orderEntity = foundOrderEntityOpt.get();

        OffsetDateTime offsetCreationDateTime = dateTimeMapper.localDateTimeToOffsetDateTime(
                orderEntity.getCreationDate()
        );

        OffsetDateTime fullFillmentDate = null;

        if(orderEntity.getFullfillmentDate() != null){
            fullFillmentDate = dateTimeMapper.localDateTimeToOffsetDateTime(
                    orderEntity.getFullfillmentDate()
            );
        }

        PersonalDataEntity receiverData;

        if(orderEntity.getReceiverDataEntity() != null){
            receiverData = orderEntity.getReceiverDataEntity().getPersonalDataEntity();
        }
        else{
            receiverData = orderEntity.getClientEntity().getPersonalDataEntity();
        }

        Map<Long, OrderWithDetails.OrderBookDetails> booksQuantities = new HashMap();

        orderEntity.getOrderItemEntityList().stream().forEach(orderItemEntity -> {
            Long bookId = orderItemEntity.getBookItemEntity().getBookEntity().getId();

            if(booksQuantities.containsKey(bookId)) {
                OrderWithDetails.OrderBookDetails orderBookEntity = booksQuantities.get(bookId);
                orderBookEntity.setQuantity(orderBookEntity.getQuantity() + 1);
            }
            else {
                booksQuantities.put(
                    bookId,
                    new OrderWithDetails.OrderBookDetails(
                            orderItemEntity.getBookItemEntity().getBookEntity(),
                            1
                    )
                );
            }
        });

        return OrderWithDetails.builder()
            .id(orderEntity.getId())
            .creationDate(offsetCreationDateTime)
            .fullfillmentDate(fullFillmentDate)
            .totalPrice(orderEntity.getTotalPrice())
            .status(orderEntity.getOrderStatusEntity())
            .receiverData(receiverData)
            .books(new ArrayList<>(booksQuantities.values()))
            .build();
    }

    @Override
    public List<OrderWithDetails> getOrdersByClientId(Long clientId) throws EntityNotFoundException{

        if(!clientService.existsById(clientId)){
            throw new EntityNotFoundException("Nie istnieje klient o takim id");
        }

        List<OrderEntity> foundOrders = orderRepository.findAllByClientEntityId(clientId);

        return foundOrders.stream()
            .map(orderEntity ->
                getById(orderEntity.getId())
            )
            .collect(Collectors.toList());
    }

    @Override
    public Page<OrderWithDetails> searchOrdersByCriteria(
        OrderSearchCriteria orderSearchCriteria, Pageable pageable
    ) {
        Page<OrderWithDetails> foundOrdersWithDetailsPage = orderRepository.findAll(
            OrderSpecification.searchByCriteria(
                orderSearchCriteria
            ),
            pageable != null ? pageable : Pageable.unpaged()
        ).map(obj -> {
            OrderEntity orderEntity = (OrderEntity) obj;
            return getById(orderEntity.getId());
        });

        return foundOrdersWithDetailsPage;
    }

    @Override
    public void checkOrder(
        Long clientId,  PersonalDataEntity personalData, List<CreateOrder.BasketItem> basketItemList
    ){
        if(basketItemList == null || basketItemList.isEmpty()){
            throw new IllegalStateException("Koszyk jest pusty");
        }

        for(CreateOrder.BasketItem basketItem : basketItemList) {

            Long bookId = basketItem.getBookId();
            Integer quantity = basketItem.getQuantity();

            BookEntity foundBook = bookService.getBookById(bookId);

            if (!foundBook.getIsAvailable()) {
                throw new IllegalStateException(
                        "Książka o tytule " + foundBook.getTitle() + " jest niedostępna"
                );
            }

            int quantityDiff = quantity - foundBook.getNumOfBookItems();

            if (quantityDiff > 0) {
                throw new IllegalStateException(
                        "Nie ma na stanie odpowiedniej liczby książek dla tytułu " + foundBook.getTitle() +
                                " brakuje " + quantityDiff + " sztuk"
                );
            }
        }
    }

    @Transactional
    @Override
    public Long placeOrder(Long clientId, PersonalDataEntity receiverData, List<CreateOrder.BasketItem> basketItemList)
        throws EntityNotFoundException, IllegalStateException
    {
        if(basketItemList == null || basketItemList.isEmpty()){
            throw new IllegalStateException("Koszyk jest pusty");
        }

        BigDecimal totalPrice = BigDecimal.valueOf(0);

        List<BookItemEntity> foundAvailableBookItems = new ArrayList<>();

        for(CreateOrder.BasketItem basketItem : basketItemList){

            Long bookId = basketItem.getBookId();
            Integer quantity = basketItem.getQuantity();

            BookEntity foundBook = bookService.getBookById(bookId);

            if(!foundBook.getIsAvailable()){
                throw new IllegalStateException(
                    "Książka o tytule " + foundBook.getTitle() + " jest niedostępna"
                );
            }

            int quantityDiff = quantity - foundBook.getNumOfBookItems();

            if(quantityDiff > 0){
                throw new IllegalStateException(
                    "Nie ma na stanie odpowiedniej liczby książek dla tytułu " + foundBook.getTitle() +
                    " brakuje " + quantityDiff + " sztuk"
                );
            }

            foundAvailableBookItems.addAll(
                bookItemService.getAvailableBookItemsByBookId(bookId).stream()
                    .limit(quantity)
                .collect(Collectors.toList())
            );

            totalPrice = totalPrice.add(foundBook.getPrice());
        }

        OrderStatusEntity orderStatus = orderStatusService.getByName("Utworzone");
        ClientEntity foundClientEntity = clientService.getById(clientId);

        ReceiverDataEntity receiverDataEntity = null;

        if(receiverData != null){
            Long personalDataId = personalDataService.create(receiverData);

            receiverDataEntity = receiverDataService.create(personalDataId);
        }

        totalPrice = totalPrice.setScale(2, RoundingMode.HALF_EVEN);

        OrderEntity placedOrder = OrderEntity.builder()
            .orderStatusEntity(orderStatus)
            .clientEntity(foundClientEntity)
            .receiverDataEntity(receiverDataEntity)
            .creationDate(LocalDateTime.now())
            .totalPrice(totalPrice)
        .build();

        OrderEntity createdOrder = orderRepository.save(placedOrder);

        foundAvailableBookItems.forEach(bookItemEntity -> {
            bookItemEntity.setIsPurchased(true);

            orderItemService.create(createdOrder, bookItemEntity, bookItemEntity.getBookEntity().getPrice());

            int numOfBookItems = bookItemEntity.getBookEntity().getNumOfBookItems();
            bookItemEntity.getBookEntity().setNumOfBookItems(numOfBookItems - 1);
        });

        return orderRepository.save(placedOrder).getId();
    }

    @Transactional
    @Override
    public OrderEntity changeOrderStatus(Long orderId, OrderStatusEntity orderStatusEntity)
        throws EntityNotFoundException, IllegalStateException
    {
        Optional<OrderEntity> foundOrderEntityOpt = orderRepository.findById(orderId);

        if(foundOrderEntityOpt.isEmpty()){
            throw new EntityNotFoundException("Nie istnieje zamówienie o takim id");
        }

        if(!orderStatusService.existsById(orderStatusEntity.getId())){
            throw new EntityNotFoundException("Nie istnieje status zamówienia o takim id");
        }

        OrderEntity orderEntity = foundOrderEntityOpt.get();

        if(orderEntity.getOrderStatusEntity().getName().equals("Odebrane") ||
            orderEntity.getOrderStatusEntity().getName().equals("Wycofane")
        ){
            throw new IllegalStateException("Nie można zmienić stanu tego zamówienia");
        }

        if(orderStatusEntity.getName().equals("Odebrane")){
            orderEntity.setFullfillmentDate(LocalDateTime.now());
        }
        else{
            orderEntity.setFullfillmentDate(null);
            orderEntity.setOrderStatusEntity(orderStatusEntity);
        }

        if(orderStatusEntity.getName().equals("Wycofane")){
            orderEntity.getOrderItemEntityList().stream().forEach(orderItemEntity -> {
                BookItemEntity bookItemEntity =  orderItemEntity.getBookItemEntity();
                bookItemEntity.setIsPurchased(false);

                BookEntity bookEntity = bookItemEntity.getBookEntity();
                bookEntity.setNumOfBookItems(bookEntity.getNumOfBookItems() + 1);
            });
        }

        return orderEntity;
    }
}
