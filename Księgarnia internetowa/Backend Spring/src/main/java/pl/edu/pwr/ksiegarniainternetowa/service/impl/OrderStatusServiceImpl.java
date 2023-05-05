package pl.edu.pwr.ksiegarniainternetowa.service.impl;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import pl.edu.pwr.ksiegarniainternetowa.exception.EntityNotFoundException;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.OrderStatusEntity;
import pl.edu.pwr.ksiegarniainternetowa.repository.OrderStatusRepository;
import pl.edu.pwr.ksiegarniainternetowa.service.OrderStatusService;

import java.util.List;
import java.util.Optional;

@Slf4j
@Service
@RequiredArgsConstructor
public class OrderStatusServiceImpl implements OrderStatusService {

    private final OrderStatusRepository orderStatusRepository;

    @Override
    public boolean existsById(Long id) {

        return orderStatusRepository.existsById(id);
    }

    @Override
    public OrderStatusEntity getByName(String name) throws EntityNotFoundException {

        Optional<OrderStatusEntity> foundOrderStatus = orderStatusRepository.findByName(name);

        if(foundOrderStatus.isEmpty()){
            throw new EntityNotFoundException("Nie znaleziono statusu zamówienia o takim id");
        }
        
        return foundOrderStatus.get();
    }

    @Override
    public List<OrderStatusEntity> getAll(){

        return orderStatusRepository.findAll();
    }
}
