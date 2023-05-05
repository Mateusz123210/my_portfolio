package pl.edu.pwr.internetprovider.service;

import pl.edu.pwr.internetprovider.model.Charge;
import pl.edu.pwr.internetprovider.model.Installation;

import java.time.LocalDate;
import java.util.List;

public interface ChargeService {
    List<Charge> getInstallationCharges(Integer installationId);
    Charge addCharge(LocalDate paymentDeadline, Float amountToPay, Boolean paid, Integer installationId);
    void updateChargePaid(Integer id, LocalDate paymentDeadline, Float amountToPay, Boolean paid, Installation installationId);
}
