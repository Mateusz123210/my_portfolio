package pl.edu.pwr.internetprovider.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Builder
@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "Installations")
public class Installation {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "address", length = 50, nullable = false)
    private String address;

    @Column(name = "routerNumber", nullable = false)
    private Integer routerNumber;

    @ManyToOne
    @JoinColumn(name = "clientId", nullable = false)
    private Client clientId;

    @ManyToOne
    @JoinColumn(name = "serviceId", nullable = false)
    private Service serviceId;
}
