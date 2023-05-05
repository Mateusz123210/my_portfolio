package pl.edu.pwr.internetprovider.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;


@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "Charges")
public class Charge {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "paymentDeadline")
    private LocalDate paymentDeadline;

    @Column(name = "amountToPay", nullable = false)
    private Float amountToPay;

    @Column(name = "paid", nullable = false)
    private Boolean paid;

    @ManyToOne
    @JoinColumn(name = "installationId", nullable = false)
    private Installation installationId;
}
