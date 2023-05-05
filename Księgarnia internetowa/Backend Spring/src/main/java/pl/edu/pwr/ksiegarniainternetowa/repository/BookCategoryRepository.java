package pl.edu.pwr.ksiegarniainternetowa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookCategoryEntity;

@Repository
public interface BookCategoryRepository extends JpaRepository<BookCategoryEntity, Long> {
}
