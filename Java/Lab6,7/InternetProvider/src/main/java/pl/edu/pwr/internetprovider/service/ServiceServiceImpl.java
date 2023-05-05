package pl.edu.pwr.internetprovider.service;

import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pl.edu.pwr.internetprovider.model.Installation;
import pl.edu.pwr.internetprovider.repository.ServiceRepository;

import java.util.List;
import java.util.Optional;

@Service
public class ServiceServiceImpl implements ServiceService{
    private final ServiceRepository serviceRepository;
    private InstallationServiceImpl installationRef;

    public void setInstallation(InstallationServiceImpl installation) {
        installationRef = installation;
    }

    @Autowired
    public ServiceServiceImpl(ServiceRepository serviceRepository) {
        this.serviceRepository = serviceRepository;
    }

    @Transactional
    @Override
    public List<pl.edu.pwr.internetprovider.model.Service> getAllServices() {
        return serviceRepository.findAll();
    }

    @Transactional
    @Override
    public pl.edu.pwr.internetprovider.model.Service getById(Integer id) {
        Optional<pl.edu.pwr.internetprovider.model.Service> service = serviceRepository.findById(id);
        if(service.isEmpty()){
            return null;
        }
        return service.get();
    }

    @Transactional
    @Override
    public List<pl.edu.pwr.internetprovider.model.Service> addService(String type, Float price) {
        pl.edu.pwr.internetprovider.model.Service service = pl.edu.pwr.internetprovider.model.Service.builder().
                type(type).price(price).build();
        serviceRepository.save(service);
        return getAllServices();
    }

    @Transactional
    @Override
    public pl.edu.pwr.internetprovider.model.Service updateService(Integer id, String type, Float price) {
        Optional<pl.edu.pwr.internetprovider.model.Service> service = serviceRepository.findById(id);
        if(service.isEmpty()){
            return null;
        }
        pl.edu.pwr.internetprovider.model.Service old = service.get();
        old.setType(type);
        old.setPrice(price);
        serviceRepository.save(old);
        return getById(id);
    }

    @Transactional
    @Override
    public List<pl.edu.pwr.internetprovider.model.Service> deleteService(Integer id) {
        List<Installation> installations = installationRef.getServiceInstallations(id);
        if(installations != null){
            for(Installation i: installations){
                installationRef.deleteInstallation(i.getId());
            }
        }
        serviceRepository.deleteById(id);
        return getAllServices();
    }
}
