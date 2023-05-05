package pl.edu.pwr.ksiegarniainternetowa.specification;

import org.springframework.data.jpa.domain.Specification;
import pl.edu.pwr.ksiegarniainternetowa.model.api.request.OrderSearchCriteria;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.*;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import javax.persistence.criteria.*;

/*
    private String name;
    private String surname;
    private String email;
    private String tel;
    private OffsetDateTime creationDateFrom;
    private OffsetDateTime creationDateTo;
    private OrderStatusEntity status;
    private BigDecimal priceFrom;
    private BigDecimal priceTo;
 */

public class OrderSpecification {

    public static Specification<OrderEntity> searchByCriteria(OrderSearchCriteria orderSearchCriteria) {
        return (root, query, cb) -> {

            List<Predicate> predicates = new ArrayList<>();

            if(orderSearchCriteria.getName() != null){
                predicates.add(
                    cb.like(
                        cb.lower(
                            root.get(OrderEntity_.CLIENT_ENTITY).get(ClientEntity_.PERSONAL_DATA_ENTITY).get(PersonalDataEntity_.NAME)
                        ),
                        "%" + orderSearchCriteria.getName()
                    )
                );
            }

            if(orderSearchCriteria.getSurname() != null){
                predicates.add(
                    cb.like(
                        cb.lower(
                            root.get(OrderEntity_.CLIENT_ENTITY).get(ClientEntity_.PERSONAL_DATA_ENTITY).get(PersonalDataEntity_.SURNAME)
                        ),
                        "%" + orderSearchCriteria.getSurname()
                    )
                );
            }

            if(orderSearchCriteria.getEmail() != null){
                predicates.add(
                    cb.like(
                        cb.lower(
                            root.get(OrderEntity_.CLIENT_ENTITY).get(ClientEntity_.PERSONAL_DATA_ENTITY).get(PersonalDataEntity_.EMAIL)
                        ),
                        "%" + orderSearchCriteria.getEmail()
                    )
                );
            }

            if(orderSearchCriteria.getTel() != null){
                predicates.add(
                    cb.like(
                        cb.lower(
                            root.get(OrderEntity_.CLIENT_ENTITY).get(ClientEntity_.PERSONAL_DATA_ENTITY).get(PersonalDataEntity_.TEL)
                        ),
                        "%" + orderSearchCriteria.getTel()
                    )
                );
            }

            if(orderSearchCriteria.getCreationDateFrom() != null){
                predicates.add(
                    cb.greaterThanOrEqualTo(
                        root.get(OrderEntity_.CREATION_DATE),
                        LocalDateTime.parse(orderSearchCriteria.getCreationDateFrom())
                    )
                );
            }

            if(orderSearchCriteria.getCreationDateTo() != null){
                predicates.add(
                    cb.lessThanOrEqualTo(
                        root.get(OrderEntity_.CREATION_DATE),
                        LocalDateTime.parse(orderSearchCriteria.getCreationDateTo())
                    )
                );
            }

            if(orderSearchCriteria.getStatusId() != null){
                predicates.add(
                    cb.equal(
                        root.get(OrderEntity_.ORDER_STATUS_ENTITY).get(OrderStatusEntity_.ID),
                        orderSearchCriteria.getStatusId()
                    )
                );
            }

            if(orderSearchCriteria.getPriceFrom() != null) {
                predicates.add(
                    cb.greaterThanOrEqualTo(
                        root.get(OrderEntity_.TOTAL_PRICE), orderSearchCriteria.getPriceFrom()
                    )
                );
            }

            if(orderSearchCriteria.getPriceTo() != null){
                predicates.add(
                    cb.greaterThanOrEqualTo(
                        root.get(OrderEntity_.TOTAL_PRICE), orderSearchCriteria.getPriceTo()
                    )
                );
            }

            Predicate[] predicatesArr = predicates.toArray(new Predicate[0]);

            return cb.and(predicatesArr);
        };
    }
}
