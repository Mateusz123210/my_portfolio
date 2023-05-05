package pl.edu.pwr.ksiegarniainternetowa.model.api.request;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderStatusEntity;

import java.math.BigDecimal;
import java.time.OffsetDateTime;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
public class OrderSearchCriteria {

    private String name;
    private String surname;
    private String email;
    private String tel;
    private String creationDateFrom;
    private String creationDateTo;
    private Long statusId;
    private BigDecimal priceFrom;
    private BigDecimal priceTo;
}
