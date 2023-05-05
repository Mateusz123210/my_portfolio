package pl.edu.pwr.internetprovider.service;

import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pl.edu.pwr.internetprovider.model.Client;
import pl.edu.pwr.internetprovider.model.Installation;
import pl.edu.pwr.internetprovider.repository.ClientRepository;
import java.util.List;
import java.util.Optional;

@Service
public class ClientServiceImpl implements ClientService{
    private final ClientRepository clientRepository;
    private InstallationServiceImpl installationRef;

    public void setInstallation(InstallationServiceImpl installation) {
        installationRef = installation;
    }

    @Autowired
    public ClientServiceImpl(ClientRepository clientRepository) {
        this.clientRepository = clientRepository;
    }

    @Transactional
    @Override
    public List<Client> getAll() {
        return clientRepository.findAll();
    }

    @Transactional
    @Override
    public Client getById(Integer id) {
        Optional<Client> client = clientRepository.findById(id);
        if(client.isEmpty()){
            return null;
        }
        return clientRepository.findById(id).get();
    }

    @Transactional
    @Override
    public List<Client> addClient(String name, String surname) {
        Client client = Client.builder().name(name).surname(surname).build();
        clientRepository.save(client);
        return getAll();
    }

    @Transactional
    @Override
    public Client updateClient(Integer number, String name, String surname) {
        Optional<Client> client = clientRepository.findById(number);
        if(client.isEmpty()){
            return null;
        }
        Client old = client.get();
        old.setName(name);
        old.setSurname(surname);
        clientRepository.save(old);
        return getById(number);
    }

    @Transactional
    @Override
    public List<Client> deleteClient(Integer clientId) {
        List<Installation> installations = installationRef.getClientInstallations(clientId);
        if(installations != null){
            for(Installation i: installations){
                installationRef.deleteInstallation(i.getId());
            }
        }
        clientRepository.deleteById(clientId);
        return getAll();
    }
}
