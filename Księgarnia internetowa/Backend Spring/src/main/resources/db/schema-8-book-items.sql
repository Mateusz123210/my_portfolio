CREATE TABLE IF NOT EXISTS `bookitems` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` int(11) NOT NULL,
  `book_id` bigint(20) NOT NULL,
  `is_purchased` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `BookItems_book_id_11c410c6_fk_Books_id` (`book_id`),
  CONSTRAINT `BookItems_book_id_11c410c6_fk_Books_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;