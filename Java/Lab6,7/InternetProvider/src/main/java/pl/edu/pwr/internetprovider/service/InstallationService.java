package pl.edu.pwr.internetprovider.service;

import pl.edu.pwr.internetprovider.model.Installation;

import java.util.List;
import java.util.Optional;

public interface InstallationService {
    List<Installation> getAll();
    List<Installation> getClientInstallations(Integer clientId);
    Optional<Installation> getInstallation(Integer id);
    List<Installation> addClientInstallations(String address, Integer routerNumber, Integer serviceId,
                                              Integer clientId);
    Installation updateInstallation(Integer id, String address, Integer routerNumber,
                                          Integer serviceId, Integer clientId);
    List<Installation> deleteInstallation(Integer id);
    List<Installation> getServiceInstallations(Integer serviceId);
}
