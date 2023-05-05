CREATE TABLE IF NOT EXISTS `bookauthors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  `surname` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `bookcovers` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `BookCovers_name_a7dfcaa3_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `publishers` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Publishers_name_3e3c67b3_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `languages` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Languages_name_afabad0b_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `bookcategories` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(22) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `BookCategories_name_5f91d8d9_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `books` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf8_polish_ci NOT NULL,
  `description` longtext COLLATE utf8_polish_ci NOT NULL,
  `isbn` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `release_number` int(11) NOT NULL,
  `release_date` date NOT NULL,
  `size` varchar(11) COLLATE utf8_polish_ci NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `is_available` tinyint(1) NOT NULL,
  `num_of_book_items` int(11) NOT NULL,
  `number_of_pages` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  `avatar` longblob NOT NULL,
  `book_category_id` bigint(20) NOT NULL,
  `book_cover_id` bigint(20) NOT NULL,
  `language_id` bigint(20) NOT NULL,
  `publisher_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Books_isbn_0774ed7a_uniq` (`isbn`),
  KEY `database_books_book_category_id_bedcd30f_fk_database_` (`book_category_id`),
  KEY `database_books_book_cover_id_265f41a2_fk_database_bookcovers_id` (`book_cover_id`),
  KEY `database_books_language_id_4e92e52a_fk_database_languages_id` (`language_id`),
  KEY `database_books_publisher_id_d3e22786_fk_database_publishers_id` (`publisher_id`),
  CONSTRAINT `database_books_book_category_id_bedcd30f_fk_database_` FOREIGN KEY (`book_category_id`) REFERENCES `bookcategories` (`id`),
  CONSTRAINT `database_books_book_cover_id_265f41a2_fk_database_bookcovers_id` FOREIGN KEY (`book_cover_id`) REFERENCES `bookcovers` (`id`),
  CONSTRAINT `database_books_language_id_4e92e52a_fk_database_languages_id` FOREIGN KEY (`language_id`) REFERENCES `languages` (`id`),
  CONSTRAINT `database_books_publisher_id_d3e22786_fk_database_publishers_id` FOREIGN KEY (`publisher_id`) REFERENCES `publishers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
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
CREATE TABLE IF NOT EXISTS `bookitems` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` int(11) NOT NULL,
  `book_id` bigint(20) NOT NULL,
  `is_purchased` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `BookItems_book_id_11c410c6_fk_Books_id` (`book_id`),
  CONSTRAINT `BookItems_book_id_11c410c6_fk_Books_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `password` varchar(256) COLLATE utf8_polish_ci NOT NULL,
  `is_employee` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `personaldata` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  `surname` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  `email` varchar(64) COLLATE utf8_polish_ci NOT NULL,
  `tel` varchar(25) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `clients` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `personal_data_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Clients_personal_data_id_9da9bd5e_fk_PersonalData_id` (`personal_data_id`),
  KEY `Clients_user_id_4c87af95_fk_Users_id` (`user_id`),
  CONSTRAINT `Clients_personal_data_id_9da9bd5e_fk_PersonalData_id` FOREIGN KEY (`personal_data_id`) REFERENCES `personaldata` (`id`),
  CONSTRAINT `Clients_user_id_4c87af95_fk_Users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `receiversdata` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `personal_data_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ReceiversData_personal_data_id_ee868a30_fk_PersonalData_id` (`personal_data_id`),
  CONSTRAINT `ReceiversData_personal_data_id_ee868a30_fk_PersonalData_id` FOREIGN KEY (`personal_data_id`) REFERENCES `personaldata` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `ordersstatuses` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(12) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `orders` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creation_date` datetime(6) NOT NULL,
  `fullfillment_date` datetime(6),
  `total_price` decimal(6,2) NOT NULL,
  `client_id` bigint(20) NOT NULL,
  `order_status_id` bigint(20) NOT NULL,
  `receivers_data_id` bigint(20),
  PRIMARY KEY (`id`),
  KEY `Orders_order_status_id_7f631565_fk_OrdersStatuses_id` (`order_status_id`),
  KEY `Orders_receivers_data_id_c7eeb7e1_fk_ReceiversData_id` (`receivers_data_id`),
  KEY `Orders_client_id_71fdbbc0_fk_Clients_id` (`client_id`),
  CONSTRAINT `Orders_client_id_71fdbbc0_fk_Clients_id` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`),
  CONSTRAINT `Orders_order_status_id_7f631565_fk_OrdersStatuses_id` FOREIGN KEY (`order_status_id`) REFERENCES `ordersstatuses` (`id`),
  CONSTRAINT `Orders_receivers_data_id_c7eeb7e1_fk_ReceiversData_id` FOREIGN KEY (`receivers_data_id`) REFERENCES `receiversdata` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
CREATE TABLE IF NOT EXISTS `ordersitems` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `price` decimal(6,2) NOT NULL,
  `book_item_id` bigint(20) NOT NULL,
  `order_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `OrdersItems_book_item_id_924a3d97_fk_BookItems_id` (`book_item_id`),
  KEY `OrdersItems_order_id_04639840_fk_Orders_id` (`order_id`),
  CONSTRAINT `OrdersItems_book_item_id_924a3d97_fk_BookItems_id` FOREIGN KEY (`book_item_id`) REFERENCES `bookitems` (`id`),
  CONSTRAINT `OrdersItems_order_id_04639840_fk_Orders_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;