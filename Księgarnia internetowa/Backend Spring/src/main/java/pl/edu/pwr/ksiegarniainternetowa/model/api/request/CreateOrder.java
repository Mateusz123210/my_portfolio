package pl.edu.pwr.ksiegarniainternetowa.model.api.request;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderItemEntity;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.PersonalDataEntity;

import java.util.List;
import java.util.Map;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
public class CreateOrder {

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    public static class BasketItem{

        private Long bookId;
        private Integer quantity;
    }

    private Long clientId;
    private PersonalDataEntity receiverData;
    private List<BasketItem> basketItems;
}
