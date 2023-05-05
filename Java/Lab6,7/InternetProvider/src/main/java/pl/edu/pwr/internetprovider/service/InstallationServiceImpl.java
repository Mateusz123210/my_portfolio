package pl.edu.pwr.internetprovider.service;


import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pl.edu.pwr.internetprovider.model.Charge;
import pl.edu.pwr.internetprovider.model.Client;
import pl.edu.pwr.internetprovider.model.Installation;
import pl.edu.pwr.internetprovider.model.Payment;
import pl.edu.pwr.internetprovider.repository.ChargeRepository;
import pl.edu.pwr.internetprovider.repository.InstallationRepository;
import pl.edu.pwr.internetprovider.repository.PaymentRepository;

import java.util.List;
import java.util.Optional;

@Service
public class InstallationServiceImpl implements InstallationService{
    private final InstallationRepository installationRepository;
    private final ClientServiceImpl clientServiceImpl;
    private final ServiceServiceImpl serviceServiceImpl;
    private final ChargeRepository chargeRepository;
    private final PaymentRepository paymentRepository;

    @Autowired
    public InstallationServiceImpl(InstallationRepository installationRepository,
                                   ClientServiceImpl clientServiceImpl,
                                   ServiceServiceImpl serviceServiceImpl, ChargeRepository chargeRepository,
                                   PaymentRepository paymentRepository){
        this.installationRepository = installationRepository;
        this.clientServiceImpl = clientServiceImpl;
        this.serviceServiceImpl = serviceServiceImpl;
        this.chargeRepository = chargeRepository;
        this.paymentRepository = paymentRepository;
        clientServiceImpl.setInstallation(this);
        serviceServiceImpl.setInstallation(this);
    }

    @Transactional
    @Override
    public List<Installation> getAll() {
        return installationRepository.findAll();
    }

    @Transactional
    @Override
    public List<Installation> getClientInstallations(Integer clientId) {
        Client client = clientServiceImpl.getById(clientId);
        if(client == null) return null;
        return installationRepository.findByClientId(client);
    }

    @Transactional
    @Override
    public Optional<Installation> getInstallation(Integer id) {
        return installationRepository.findById(id);
    }

    @Transactional
    @Override
    public List<Installation> addClientInstallations(String address, Integer routerNumber, Integer serviceId,
                                                     Integer clientId) {
        Client client = clientServiceImpl.getById(clientId);
        if(client == null) return null;
        pl.edu.pwr.internetprovider.model.Service service = serviceServiceImpl.getById(serviceId);
        if(service == null) return null;
        Installation installation = Installation.builder().address(address).routerNumber(routerNumber).
                serviceId(service).clientId(client).build();
        installationRepository.save(installation);
        return installationRepository.findByClientId(client);
    }

    @Transactional
    @Override
    public Installation updateInstallation(Integer id, String address, Integer routerNumber,
                                                 Integer serviceId, Integer clientId) {
        Client client = clientServiceImpl.getById(clientId);
        if(client == null) return null;
        pl.edu.pwr.internetprovider.model.Service service = serviceServiceImpl.getById(serviceId);
        if(service == null) return null;
        Optional<Installation> oldInstallation = installationRepository.findById(id);
        if(oldInstallation.isEmpty()){
            return null;
        }
        Installation old = oldInstallation.get();
        old.setAddress(address);
        old.setRouterNumber(routerNumber);
        old.setServiceId(service);
        old.setClientId(client);
        installationRepository.save(old);
        Optional<Installation> ins = installationRepository.findById(id);
        if(ins .isEmpty())
            return null;
        return ins.get();
    }

    @Transactional
    @Override
    public List<Installation> deleteInstallation(Integer id) {
        Optional<Installation> installation = installationRepository.findById(id);
        if(installation.isEmpty())
            return null;
        Integer clientId = installation.get().getClientId().getNumber();
        List<Charge> charges = chargeRepository.findByInstallationId(installation.get());
        if(charges != null){
            for(Charge c: charges){
                chargeRepository.deleteById(c.getId());
            }
        }
        List<Payment> payments = paymentRepository.findByInstallationId(installation.get());
        if(payments != null){
            for(Payment p: payments){
                paymentRepository.deleteById(p.getId());
            }
        }
        installationRepository.deleteById(id);
        return getClientInstallations(clientId);
    }

    @Transactional
    @Override
    public List<Installation> getServiceInstallations(Integer serviceId) {
        pl.edu.pwr.internetprovider.model.Service service = serviceServiceImpl.getById(serviceId);
        if(service == null) return null;
        return installationRepository.findByServiceId(service);
    }
}
