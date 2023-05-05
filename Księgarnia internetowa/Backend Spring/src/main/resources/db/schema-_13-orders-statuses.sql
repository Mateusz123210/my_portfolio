CREATE TABLE IF NOT EXISTS `ordersstatuses` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(12) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;