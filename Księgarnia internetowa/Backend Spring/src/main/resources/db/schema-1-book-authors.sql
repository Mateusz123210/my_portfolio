CREATE TABLE IF NOT EXISTS `bookauthors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  `surname` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;