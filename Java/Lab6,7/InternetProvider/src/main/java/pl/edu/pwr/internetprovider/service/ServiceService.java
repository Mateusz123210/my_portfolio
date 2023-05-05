package pl.edu.pwr.internetprovider.service;

import pl.edu.pwr.internetprovider.model.Service;

import java.util.List;

public interface ServiceService {
    List<Service> getAllServices();
    Service getById(Integer id);
    List<Service> addService(String type, Float price);
    Service updateService(Integer id, String type, Float price);
    List<Service> deleteService(Integer id);
}
