package pl.edu.pwr.internetprovider.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.internetprovider.model.Charge;
import pl.edu.pwr.internetprovider.model.Installation;

import java.util.List;

@Repository
public interface ChargeRepository extends JpaRepository<Charge, Integer> {
    List<Charge> findByInstallationId(Installation installation);
}
