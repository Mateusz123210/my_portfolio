package pl.edu.pwr.ksiegarniainternetowa.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderStatusEntity;
import pl.edu.pwr.ksiegarniainternetowa.service.OrderStatusService;

import java.util.List;

@RestController
@CrossOrigin(origins = {"http://localhost:3000", "http://localhost:8000", "https://booksshop-dr.azurewebsites.net"})
@RequestMapping(value = "/v1")
@RequiredArgsConstructor
public class OrderStatusController {

    private final OrderStatusService orderStatusService;

    @GetMapping(value = "/order-statuses")
    public ResponseEntity<List<OrderStatusEntity>> orderStatusEntities(){

        List<OrderStatusEntity> foundOrderStatuses = orderStatusService.getAll();

        return ResponseEntity.ok(foundOrderStatuses);
    }
}
