package pl.edu.pwr.ksiegarniainternetowa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pl.edu.pwr.ksiegarniainternetowa.model.entity.BookItemEntity;

import java.util.List;

@Repository
public interface BookItemRepository extends JpaRepository<BookItemEntity, Long> {

    List<BookItemEntity> findFirst10ByBookEntityIdAndIsPurchased(Long bookId, Boolean isPurchased);
}
