package pl.edu.pwr.internetprovider.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.internetprovider.model.Service;

@Repository
public interface ServiceRepository extends JpaRepository<Service, Integer> {

}
