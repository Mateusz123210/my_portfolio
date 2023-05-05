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