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