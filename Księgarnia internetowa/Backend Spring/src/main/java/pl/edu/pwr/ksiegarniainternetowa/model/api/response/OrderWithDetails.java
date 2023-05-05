package pl.edu.pwr.ksiegarniainternetowa.model.api.response;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderItemEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderStatusEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.PersonalDataEntity;

import javax.persistence.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.time.OffsetDateTime;
import java.util.List;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
public class OrderWithDetails {

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class OrderBookDetails {

        private BookEntity book;
        private Integer quantity;
    }

    private Long id;
    private OffsetDateTime creationDate;
    private OffsetDateTime fullfillmentDate;
    private BigDecimal totalPrice;
    private OrderStatusEntity status;
    private PersonalDataEntity receiverData;
    private List<OrderBookDetails> books;
}
