package pl.edu.pwr.internetprovider.service;


import pl.edu.pwr.internetprovider.model.Payment;

import java.time.LocalDate;
import java.util.List;

public interface PaymentService {
    List<Payment> getInstallationPayments(Integer installationId);
    List<Payment> addInstallationPayment(LocalDate date, Float price, Integer installationId);
    List<Payment> updatePayment(Integer paymentId, LocalDate date, Float price, Integer installationId);
    List<Payment> deletePayment(Integer paymentId);
}
