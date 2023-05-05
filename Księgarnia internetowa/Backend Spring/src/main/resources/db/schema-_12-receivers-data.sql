CREATE TABLE IF NOT EXISTS `receiversdata` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `personal_data_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ReceiversData_personal_data_id_ee868a30_fk_PersonalData_id` (`personal_data_id`),
  CONSTRAINT `ReceiversData_personal_data_id_ee868a30_fk_PersonalData_id` FOREIGN KEY (`personal_data_id`) REFERENCES `personaldata` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;