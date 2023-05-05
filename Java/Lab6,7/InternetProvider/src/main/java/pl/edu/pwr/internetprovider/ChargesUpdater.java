package pl.edu.pwr.internetprovider;

import jakarta.transaction.Transactional;
import pl.edu.pwr.internetprovider.model.Charge;
import pl.edu.pwr.internetprovider.model.Installation;
import pl.edu.pwr.internetprovider.model.Payment;
import pl.edu.pwr.internetprovider.service.ChargeServiceImpl;
import pl.edu.pwr.internetprovider.service.InstallationServiceImpl;
import pl.edu.pwr.internetprovider.service.PaymentServiceImpl;

import java.io.IOException;
import java.time.LocalDate;
import java.util.List;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class ChargesUpdater implements Runnable{
    private final ChargeServiceImpl chargeServiceImpl;
    private final InstallationServiceImpl installationServiceImpl;
    private final PaymentServiceImpl paymentServiceImpl;
    private Boolean end = false;
    private Logger logger, notPaidLogger;

    public ChargesUpdater(ChargeServiceImpl chargeServiceImpl, InstallationServiceImpl installationServiceImpl,
                          PaymentServiceImpl paymentServiceImpl){
        this.chargeServiceImpl = chargeServiceImpl;
        this.installationServiceImpl = installationServiceImpl;
        this.paymentServiceImpl = paymentServiceImpl;
        logger = Logger.getLogger("ToPayLogs");
        try {
            FileHandler fh = new FileHandler(System.getProperty("user.dir") + "\\ToPayLogs.log");
            logger.addHandler(fh);
            SimpleFormatter formatter = new SimpleFormatter();
            fh.setFormatter(formatter);
        } catch (SecurityException | IOException e) {
        }
        notPaidLogger = Logger.getLogger("NotPaidLogs");
        try {
            FileHandler fh = new FileHandler(System.getProperty("user.dir") + "\\NotPaidLogs.log");
            notPaidLogger.addHandler(fh);
            SimpleFormatter formatter = new SimpleFormatter();
            fh.setFormatter(formatter);
        } catch (SecurityException | IOException e) {
        }
    }

    public void destroy(){
        end = true;
    };

    @Transactional
    private void update(){
        StringBuilder toPay = new StringBuilder("Charges to pay:\n");
        StringBuilder notPaid = new StringBuilder("Charges not paid in time:\n");
        try {
            List<Installation> installations = installationServiceImpl.getAll();
            for (Installation i : installations) {
                List<Charge> charges = chargeServiceImpl.getInstallationCharges(i.getId());
                if (charges == null || charges.isEmpty()) {
                    Charge c1 = chargeServiceImpl.addCharge(LocalDate.now().plusMonths(1), i.getServiceId().getPrice(),
                            false, i.getId());
                    toPay.append(c1.toString() + "\n");
                } else {
                    Charge charge = charges.get(0);
                    for (int j = 0; j < charges.size(); j++) {
                        if (charges.get(j).getPaymentDeadline().isAfter(charge.getPaymentDeadline()))
                            charge = charges.get(j);
                    }
                    Charge c1 = chargeServiceImpl.addCharge(charge.getPaymentDeadline().plusMonths(1),
                            i.getServiceId().getPrice(), false, i.getId());
                    toPay.append(c1.toString() + "\n");
                }
                List<Payment> payments = paymentServiceImpl.getInstallationPayments(i.getId());
                if(payments == null){
                    for(Charge c: charges){
                        if(!c.getPaid())
                            notPaid.append(c.toString());
                    }
                }else{
                    Float paymentsSum = 0.0f;
                    Float paidChargesSum = 0.0f;
                    Float minimum = Float.MAX_VALUE;
                    for(Charge c: charges){
                        if(c.getPaid()) paidChargesSum += c.getAmountToPay();
                    }
                    for(Payment p: payments){
                        paymentsSum += p.getPrice();
                    }
                    Float difference = paymentsSum - paidChargesSum;
                    if(difference >= 0.0f) {
                        for (Charge c : charges) {
                            if (!c.getPaid() && difference >= c.getAmountToPay()) {
                                difference -= c.getAmountToPay();
                                chargeServiceImpl.updateChargePaid(c.getId(), c.getPaymentDeadline(), c.getAmountToPay(),
                                        true, c.getInstallationId());
                                c.setPaid(true);
                            }
                        }
                    }
                    for(Charge c: charges){
                        if(!c.getPaid())
                            notPaid.append(c.toString() + "\n");
                    }
                }
            }
        }catch(Exception e){
        }
        logger.info(toPay.toString());
        notPaidLogger.info(notPaid.toString());
    }

    @Override
    public void run() {
        while(true){
            try {
                for(int i = 0; i < 5000; i++){
                    if(end) return;
                    Thread.sleep(2);
                }
            } catch (InterruptedException e) {
            }
            update();
        }
    }
}
