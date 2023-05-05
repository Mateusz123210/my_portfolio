package pl.edu.pwr.internetprovider.service;


import pl.edu.pwr.internetprovider.model.Client;

import java.util.List;

public interface ClientService {
    List<Client> getAll();
    Client getById(Integer id);
    List<Client> addClient(String name, String surname);
    Client updateClient(Integer number,String name, String surname);
    List<Client> deleteClient(Integer clientId);
}
