package pl.edu.pwr.internetprovider.service;

import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pl.edu.pwr.internetprovider.model.Installation;
import pl.edu.pwr.internetprovider.model.Payment;
import pl.edu.pwr.internetprovider.repository.PaymentRepository;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Service
public class PaymentServiceImpl implements PaymentService{
    private final PaymentRepository paymentRepository;
    private final InstallationServiceImpl installationServiceImpl;

    @Autowired
    public PaymentServiceImpl(PaymentRepository paymentRepository, InstallationServiceImpl installationServiceImpl) {
        this.paymentRepository = paymentRepository;
        this.installationServiceImpl = installationServiceImpl;
    }

    @Transactional
    @Override
    public List<Payment> getInstallationPayments(Integer installationId) {
        Optional<Installation> installationOptional = installationServiceImpl.getInstallation(installationId);
        if(installationOptional.isEmpty())
            return null;
        return paymentRepository.findByInstallationId(installationOptional.get());
    }

    @Transactional
    @Override
    public List<Payment> addInstallationPayment(LocalDate date, Float price, Integer installationId) {
        Optional<Installation> installation = installationServiceImpl.getInstallation(installationId);
        if(installation.isEmpty()) return null;
        Payment payment = Payment.builder().date(date).price(price).installationId(installation.get()).build();
        paymentRepository.save(payment);
        return getInstallationPayments(installationId);
    }

    @Transactional
    @Override
    public List<Payment> updatePayment(Integer paymentId, LocalDate date, Float price, Integer installationId) {
        Optional<Installation> installation = installationServiceImpl.getInstallation(installationId);
        if(installation.isEmpty()) return null;
        Optional<Payment> payment = paymentRepository.findById(paymentId);
        if(payment.isEmpty()) return null;
        Payment oldPayment = payment.get();
        oldPayment.setDate(date);
        oldPayment.setPrice(price);
        oldPayment.setInstallationId(installation.get());
        paymentRepository.save(oldPayment);
        return getInstallationPayments(installationId);
    }

    @Transactional
    @Override
    public List<Payment> deletePayment(Integer paymentId) {
        Optional<Payment> oldPayment = paymentRepository.findById(paymentId);
        if(oldPayment.isEmpty()) return null;
        Integer installationId = oldPayment.get().getInstallationId().getId();
        paymentRepository.deleteById(paymentId);
        return getInstallationPayments(installationId);
    }
}
