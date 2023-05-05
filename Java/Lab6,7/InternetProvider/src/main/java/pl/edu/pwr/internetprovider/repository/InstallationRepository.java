package pl.edu.pwr.internetprovider.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.internetprovider.model.Client;
import pl.edu.pwr.internetprovider.model.Installation;
import pl.edu.pwr.internetprovider.model.Service;

import java.util.List;

@Repository
public interface InstallationRepository extends JpaRepository<Installation, Integer> {
    List<Installation> findByClientId(Client client);
    List<Installation> findByServiceId(Service service);
}
