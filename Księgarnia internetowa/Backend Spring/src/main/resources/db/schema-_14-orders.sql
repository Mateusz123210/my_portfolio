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