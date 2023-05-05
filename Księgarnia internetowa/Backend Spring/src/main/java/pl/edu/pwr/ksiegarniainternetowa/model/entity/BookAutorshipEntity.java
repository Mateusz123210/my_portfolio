package pl.edu.pwr.ksiegarniainternetowa.model.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.*;

import javax.persistence.*;

@Builder
@Getter
@Setter
@Entity
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "BOOKAUTHORSHIPS")
public class BookAutorshipEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "book_author_id")
    private BookAuthorEntity author;

    @ManyToOne
    @JoinColumn(name = "book_id")
    private BookEntity bookEntity;
}
