package pl.edu.pwr.internetprovider.service;

import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pl.edu.pwr.internetprovider.model.Charge;
import pl.edu.pwr.internetprovider.model.Installation;
import pl.edu.pwr.internetprovider.repository.ChargeRepository;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Service
public class ChargeServiceImpl implements ChargeService{

    private final ChargeRepository chargeRepository;
    private final InstallationService installationService;

    @Autowired
    public ChargeServiceImpl(ChargeRepository chargeRepository,
                             InstallationService installationService) {
        this.chargeRepository = chargeRepository;
        this.installationService = installationService;
    }

    @Transactional
    @Override
    public List<Charge> getInstallationCharges(Integer installationId) {
        Optional<Installation> installationOptional = installationService.getInstallation(installationId);
        if(installationOptional.isEmpty())
            return null;
        return chargeRepository.findByInstallationId(installationOptional.get());
    }

    @Transactional
    @Override
    public Charge addCharge(LocalDate paymentDeadline, Float amountToPay, Boolean paid, Integer installationId) {
        Optional<Installation> installation = installationService.getInstallation(installationId);
        if(installation.isEmpty()) return null;
        Charge charge = Charge.builder().paymentDeadline(paymentDeadline).amountToPay(amountToPay).
                paid(paid).installationId(installation.get()).build();
        chargeRepository.save(charge);
        return charge;
    }

    @Transactional
    @Override
    public void updateChargePaid(Integer id, LocalDate paymentDeadline, Float amountToPay, Boolean paid, Installation installationId) {
        Charge newCharge = Charge.builder().id(id).paymentDeadline(paymentDeadline).
                amountToPay(amountToPay).paid(true).
                installationId(installationId).build();
        chargeRepository.save(newCharge);
    }
}
