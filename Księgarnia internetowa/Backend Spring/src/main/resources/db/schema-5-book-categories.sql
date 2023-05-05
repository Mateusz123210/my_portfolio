CREATE TABLE IF NOT EXISTS `bookcategories` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(22) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `BookCategories_name_5f91d8d9_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;