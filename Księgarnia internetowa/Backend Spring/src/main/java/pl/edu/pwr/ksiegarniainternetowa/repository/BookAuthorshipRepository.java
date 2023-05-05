package pl.edu.pwr.ksiegarniainternetowa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookAutorshipEntity;

@Repository
public interface BookAuthorshipRepository extends JpaRepository<BookAutorshipEntity, Long> {
}
