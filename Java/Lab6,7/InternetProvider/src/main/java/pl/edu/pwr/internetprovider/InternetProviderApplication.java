package pl.edu.pwr.internetprovider;

import jakarta.annotation.PreDestroy;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.core.task.TaskExecutor;
import pl.edu.pwr.internetprovider.service.ChargeServiceImpl;
import pl.edu.pwr.internetprovider.service.InstallationServiceImpl;
import pl.edu.pwr.internetprovider.service.PaymentServiceImpl;

@SpringBootApplication
public class InternetProviderApplication {

    private final ChargeServiceImpl chargeServiceImpl;
    private final InstallationServiceImpl installationServiceImpl;
    private final PaymentServiceImpl paymentServiceImpl;

    @Autowired
    public InternetProviderApplication(ChargeServiceImpl chargeServiceImpl,
                                       InstallationServiceImpl installationServiceImpl,
                                       PaymentServiceImpl paymentServiceImpl) {
        this.chargeServiceImpl = chargeServiceImpl;
        this.installationServiceImpl = installationServiceImpl;
        this.paymentServiceImpl = paymentServiceImpl;
    }

    @Bean()
    public CommandLineRunner chargesRunner(TaskExecutor executor){

        return new CommandLineRunner() {
            private ChargesUpdater chargesUpdater;
            @PreDestroy
            public void destroy(){
                chargesUpdater.destroy();
            };
            @Override
            public void run(String... args) {
                chargesUpdater = new ChargesUpdater(chargeServiceImpl, installationServiceImpl,
                        paymentServiceImpl);
                executor.execute(chargesUpdater);
            }
        };
    }

    public static void main(String[] args) {
        SpringApplication.run(InternetProviderApplication.class, args);
    }
}
