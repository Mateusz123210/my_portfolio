CREATE TABLE IF NOT EXISTS `bookauthorships` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `book_author_id` bigint(20) NOT NULL,
  `book_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `database_bookauthorships_book_id_0142b746_fk_database_books_id` (`book_id`),
  KEY `database_bookauthors_book_author_id_1f689a2c_fk_database_` (`book_author_id`),
  CONSTRAINT `database_bookauthors_book_author_id_1f689a2c_fk_database_` FOREIGN KEY (`book_author_id`) REFERENCES `bookauthors` (`id`),
  CONSTRAINT `database_bookauthorships_book_id_0142b746_fk_database_books_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;