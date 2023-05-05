package pl.edu.pwr.ksiegarniainternetowa.model.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.*;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Builder
@Getter
@Setter
@Entity
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "BOOKCOVERS")
public class BookCoverEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", length = 20, nullable = false)
    private String name;

    @JsonIgnore
    @OneToMany(mappedBy = "cover", fetch = FetchType.LAZY)
    private Set<BookEntity> bookEntities = new HashSet<>();
}
