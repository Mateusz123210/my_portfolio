package pl.edu.pwr.internetprovider.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.internetprovider.model.Client;

@Repository
public interface ClientRepository extends JpaRepository<Client, Integer> {

}
