-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: book.mysql.database.azure.com    Database: bookshopdb
-- ------------------------------------------------------
-- Server version	5.7.39-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookauthors`
--

DROP TABLE IF EXISTS `bookauthors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookauthors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  `surname` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookauthors`
--

LOCK TABLES `bookauthors` WRITE;
/*!40000 ALTER TABLE `bookauthors` DISABLE KEYS */;
INSERT INTO `bookauthors` VALUES (1,'Jon','Duckett'),(2,'Silvia Botros','Botros'),(3,'Jeremy','Tinley');
/*!40000 ALTER TABLE `bookauthors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookauthorships`
--

DROP TABLE IF EXISTS `bookauthorships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookauthorships` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `book_author_id` bigint(20) NOT NULL,
  `book_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `database_bookauthorships_book_id_0142b746_fk_database_books_id` (`book_id`),
  KEY `database_bookauthors_book_author_id_1f689a2c_fk_database_` (`book_author_id`),
  CONSTRAINT `database_bookauthors_book_author_id_1f689a2c_fk_database_` FOREIGN KEY (`book_author_id`) REFERENCES `bookauthors` (`id`),
  CONSTRAINT `database_bookauthorships_book_id_0142b746_fk_database_books_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookauthorships`
--

LOCK TABLES `bookauthorships` WRITE;
/*!40000 ALTER TABLE `bookauthorships` DISABLE KEYS */;
INSERT INTO `bookauthorships` VALUES (3,1,1),(4,2,2),(5,3,2);
/*!40000 ALTER TABLE `bookauthorships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookcategories`
--

DROP TABLE IF EXISTS `bookcategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookcategories` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(22) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `BookCategories_name_5f91d8d9_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookcategories`
--

LOCK TABLES `bookcategories` WRITE;
/*!40000 ALTER TABLE `bookcategories` DISABLE KEYS */;
INSERT INTO `bookcategories` VALUES (3,'Fantastyka'),(5,'Historyczne'),(1,'Kryminalne'),(4,'Nauka'),(2,'Przygodowe');
/*!40000 ALTER TABLE `bookcategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookcovers`
--

DROP TABLE IF EXISTS `bookcovers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookcovers` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `BookCovers_name_a7dfcaa3_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookcovers`
--

LOCK TABLES `bookcovers` WRITE;
/*!40000 ALTER TABLE `bookcovers` DISABLE KEYS */;
INSERT INTO `bookcovers` VALUES (1,'miÄ™kka'),(2,'twarda');
/*!40000 ALTER TABLE `bookcovers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookitems`
--

DROP TABLE IF EXISTS `bookitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookitems` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `code` int(11) NOT NULL,
  `book_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BookItems_book_id_11c410c6_fk_Books_id` (`book_id`),
  CONSTRAINT `BookItems_book_id_11c410c6_fk_Books_id` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookitems`
--

LOCK TABLES `bookitems` WRITE;
/*!40000 ALTER TABLE `bookitems` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'JavaScript i jQuery. Interaktywne strony WWW dla kaÅ¼dego. PodrÄ™cznik Front-End Developera','JeÅ¼eli chcesz poznaÄ‡ potencjaÅ‚ tego duetu i zaczÄ…Ä‡ tworzyÄ‡ atrakcyjne aplikacje internetowe, nie moÅ¼esz obejÅ›Ä‡ siÄ™ bez tej ksiÄ…Å¼ki. PomoÅ¼e Ci ona szybko stworzyÄ‡ pierwszy skrypt. W trakcie lektury poznasz niuanse skÅ‚adni JavaScriptu, sposoby obsÅ‚ugi zdarzeÅ„ oraz obiektowy model strony. DziÄ™ki dalszym rozdziaÅ‚om zdobÄ™dziesz wiedzÄ™ na temat jQuery oraz moÅ¼liwoÅ›ci tej biblioteki. Z pomocÄ… duetu JavaScript i jQuery bÅ‚yskawicznie rozwiÄ…Å¼esz kaÅ¼dy problem â€” asynchroniczne pobieranie danych z serwera, atrakcyjny interfejs uÅ¼ytkownika, zaawansowana obsÅ‚uga formularzy to tylko niektÃ³re z poruszanych tu tematÃ³w. KsiÄ…Å¼ka ta jest doskonaÅ‚ym ÅºrÃ³dÅ‚em informacji dla czytelnikÃ³w chcÄ…cych opanowaÄ‡ JavaScript oraz zwiÄ…zane z nim narzÄ™dzia!','978-83-283-4478-5',1,'2018-03-27','231x32x175',62.34,1,2,'648',_binary 'ÿ\Øÿ\à\0JFIF\0\0\0\0\0\0ÿ\Û\0C\0	\Z!\Z\"$\"$ÿ\Û\0CÿÀ\0\0\Ì\0€\"\0ÿ\Ä\0\0\0\0\0\0\0\0\0\0\0\0\0\0ÿ\Ä\0B\0\0\0\0\0\0!1AQ‘ð\"aq2#BRb’¡3Sr±Á$%C\Ñ4c‚“²\áñÿ\Ä\0\0\0\0\0\0\0\0\0\0\0\0\0\0ÿ\Ä\01\0\0\0\0\0\0\0\0!1AQa\"Á2‘±#q¡\Ñ\áðñ¢ÿ\Ú\0\0\0?\0ó\á*\Ú>%k\Æ)\â\â¯\Í\r\êõ†^Qa”x¸«óC\Å\Å_šyC/(\â\â¯\Í~he\å¼ ‹\ï+óFLŒ”\ä\ê\Ê%R\\P X+2N–Œl¼£¸\ìjn^›‰Nb¡\'(%–•L¥E	!AMl69oŠ7„I\èö±]](\å\Î0÷sIµÁñ9J.¥NB=.\ëÁtm\Ümó\Ôe¬a]\\Uù£¿\í†f^£2š“U‰:‚\ÞZR¤1¶;°”Y>›d/kG—”R‡•“&·g\r¥Â¢,\ã	\í\çÇ‚.*ü\ÐñqW\æ†^P\Ë\Ê.\"‹Š¿4<\\Uù¡—”2ò€.*ü\ÑT•\\x•¯¦^PN£M`õz\Ã.„7«\Ö\æ\0eÐ†]{˜{˜—Bt!\îa\î`]e¾\Ç\Ú\æ\æ<°\èEn:÷0÷0\r\äeÐ†]{˜{˜—Bt!\îa\î`]\'Q\ësN£\Ö\0¦õz\Ã.Œ7«MaoH—FtaoH[\Ò\0eÑ†][\Òô€taaÑ…½\"ý>Nb~q¹IV»Çœ6H™<\0\ã\ÕR¥6÷\"\ê(ªJ•4¬¶X°\è\Ã.ŒfÖ©sT™\å\ÊM \\f…\áq?xyHÂ·¤(®š\éURò™Yb®*\Ý¬42\è\Ã.Œ-\ézEÅƒ.Œ2\è\ÂÞ·¤\0Ë£M®=x\Å-\é\ê4\Ö\0oVºÃŸ(oW¬9À|¡Ï”9Ãœ\0\ç\ÊùCœ}6…¸\â[m\nZ\ÖBR”‹•l\0\Íâ€¿K‘œ©\ÔX§\Ó\åÜ™š˜XCM f¥µ\Ð˜©\ØgJ6‰\ÐÛ³3I\nqö\Í\Ó\áƒø]};.Æ»8oJšH‡ks-l8i•AÌ¶“½F\Ãi^Vk\Ô\ã\ê••…\'g+ª´šQ`”‘\Þ-e(üWÓ†d\åxó­g´U^\\«KUšs›\Û\é\Ó\îv\Z4\éõy©—ð¿r!«a\ä\âI5\É–\ÜH\Úm\â?t®>‡B7\ÄGZ¦NQ\êOS\ç\Ú-¾\Ñ\ÏxP:)\'x;ŒO³M­Qò\0¡\Ä™†–n¶\×m\çx\àF_¬ZÇ¸N[\ÓÅ”Ÿ—Iøw‰\Ë?²®)?¡Ïú­*\Z¬\ãð¤Á\'®XÅªQ\æmþ,}W\ïþ>P\ç\Ê.\ÍË¿\'6ô¤\ÓjiöVP\â©P\ÔE®q8y\ëN—†9ò‡>P\çp(9òŠFº\Å9\ÅS¨\×X›\Õ\ë¼¡½^°\ëH—”2‡ZC\Ü@£Ð½„ön\Ý.QœM^”ÿ\04w\Ç(Ë©·Â£r\Èþ\"†yü£\Îñª\ì³gRó·K¤\'d9N–pg}\Ï(nü ñ\Ú\át\Ü\Ãr¯MÍ¾†e\Ç]qVJ3*&<\ïµ¡u·ejú6¾\Ë\ß\èt:^œ’ñ\åù/r\Åf§!F¥\ÌTªs)–“—NÓŽ+;\0jI\Ð™1\å.Ó±¬ö4¯§®Ì„¹)’–¿\î\Ó÷«+Ÿaký Lc:¯\Ã\Ê¢J®ò\Íb\ê´\ïV8\Ã\ì2c„\ëH–\ì\Ïg•…<\ëñü¯ß™«©jz»”|+õ6˜Z½=‡ªÈ¨H¯²\ëJ6K¨Þ“ýŽ\ãœOøv±\'\\¤µR‘]\Ûpx’O‰µ\ïIó®»\ãÍi\ì‰¦ð\ÕTL4Vä£„	©prq<EôP\Ü}´1\ÔK}l\ÞgÑµwg_rOþIO´\Ì\Ý~AS\Ò-%5V\á\Ù\0|BG\Ø>|	ô\Ð\å8…´\ê\Úu\nCˆQJ’ AI\Z‚†=3Lž•©H3=\"ò^–y;M¬oò<Ð\Ñ\Ãö§‚•VJ«T–\Ç\Ç6“ß²‘œ\ÂF„~1ú0/†{¾š‰oHWù˜7ñKR\Ë\Êy@u”:\Ò7$e\å\ÛhzÃ­\"©\ÔzÀÞ¯X@\ê¯X[«À\ç·aÝ›\nú\ÚÄµ´‘Je\Û\ËK‘ÿ\0¤œÊ¸6ÿ\0¨‚4¼jû\ìùX¶ªgªlºšª¾°\æ\Ê\ÇúI<7¨Z˜ôä¬»2\Ò\íKK2†™i\r´\ÚvR„Œ‚@\Z(\â{Q\Ú/,¥»õ½\ï—O\Ï\ìMizwŠüY§\î\\$\0T¥\0\É$\Ø\Ç\ÈGšûo\íX–qt*;ªM]Ï¬q&\ß\à?7ò ß¯\ÞvÕ¦«³o\à¼(˜e)pÏ¼Á¹|!%Km6û		%G}ˆ\Ðg\É\Ñ+rô÷å©³NµR˜2\ÒKJ<3¦\×Bò6“—œc\ì¯g<$¯.W©ü)ð\êúò.\Õ5þb\ì\â`B3d)IÔ¶©:|\Ã\áÉ´I#aÚ˜X%-\Æ@\Ò3$p¦%ž«\Î\Ò%(s¯OÈ¨¢m„¢\ÊaA[6]\È\0\ídó9\Çw†AšhFæ™…15JVjfB…=0Ì¢\Ô\Û\êKv\ØZ+E‰JH”¦\ä\rD}»„1CT6\ënP\'\Å1\Ö\ÛuA\0 ¡\Âj67	UÅ‰°7À3{:ÅŽaªŠ›˜r›2¡ß fPt$q\Æñ\æNÒ¯³3,\ÔÌ»©u—P\Ú\ÒrRN`ˆó\ï\ìf,ú:n 0õ@\ÊÉ¸ós.Á\î\Ô\Éú\Ð@7ð}«h\íð\"ñ^¦´\æ\"£MKá¹•$·6ê“²ÁY\ÉB\Ê$ ’.7^ùg}i\á\ï,­\çM¡k>PLý/wO\àø\íc%)˜\Ät¤K“¬=\\Hÿ\0\È{ñG¨’AMÁ\n\\\Üý\ÄCÝªà¿£]j’Á©†2—UõC\äD[\Ùô\Ôg\×tn\în`[8¯r>ŠG¬R\Ý^	X\Ú9!½^±‘#*©•ðl¿°Œsª½coH}µ°¶\Ê\Ð.œk]I\\q·B#õ;‰m\í\Ýq-¿n§¨{1\Ä4Z\Ö——¤²Ü’¤šCN\É$[¸þ^)9\Øó\Î8N\ÝûJø?…0üÅ§\n\'\æPse\'V’~ùûGp\ËS—ƒ\rNJeu		\ç¤U\Ý-”º\ØD(X\Úùe¯¨\ÃÖ©\Ó4Êƒ’óJ+Qñ¥\Ü\Ïx	ù³\ß\Ç\Î9m7²T\Ór\ï%\ÛNôŸ>o§#kL\ír¾ƒ\Ê7‰þ«§¹¹À3”ZKÓ•yúƒ\Í1\'4Ì´’%¿‰.\Ë8\Òl\à;(²–/´49GQ;ŒpyÀ‡\n\È\ÊU\Z›¥\È\Ê9Jª)òZ3\Ìµ-,l‚\×x\\t\Ù+F6\êÑ¶§\á*\É\ï-1)\á\n°UËšö·´vy\Â6c¾ðH“øóE)9+O2’³“ÿ\0\n\Ñ\îz©;“…+±\Ø\r%D%dXf#ö»\ÎW&\'e*\r\Ó$*4\é6jtÚ½9UFfÂ¶~±i\ÙQYB´¸Ò”	3÷€°üµ#KO\ãYy6¨uºµ-R\ëu\ä-´žýNm¤ ]\Íc®Ÿ®Éµ†k¤=Iø¶qD³}\Ël¡2²Š\ïÁ\î\ÆÊ¥Uf\Ô\Ù\Î\ÖV™\Å\È\Äp’«ƒq›&\ÅRj€\ÅsÈ“–vQsa‡_S­)%&\Éw0…m‘h\ÚÑ’ö7\Ãawe%¥\å\éõo¡i’K©%…­sm´ñªº¬t¤¥ÄŒ\Â6O\Íx\éû8Ã•¬\';I¢\Õd\Õ+^}ú\Ää¬»—rc»	iµ§l–Á.%[y_H\Ù\É\Õ*\ÔgñøŽ»UÃ³¯NQ\ØL\ä\í:Fja¯¿47f\Ãw\å76ƒ‡ˆ;F¢· \ë´jl¼\Ý_éŠ¼ÔµBd8•Hµ4°¤\"\á\nRUó_d\Ú8Z¤\ä‹\ØK\r\Óe\Óg\éÉœ\îÁ=\ãÁH±\ßtŒ\âA¨V¥\Øo>õ\r‰*Žžuº#IR\ne6ò\ÛRagCf\î6F@¯\î\ØDL„„¤$\\\0,7\ÅÁr$ž\Éñ§\Â8Š\rbcü2¬™7–rdý\Â~\é\ÜN‡-REö%\åVfBT…ž\ì‹\í\Üf-¼q;aŠCWe¨´¶ƒ³S* m!)\êRŽä™ÿ\0s‚®\à™\Ú&‘Z*T\Ó%,–¦V\à\0‹}´¹ ¶d\0/|\í©4)ú‘\Ö\è\ÚÓ¦Ÿ/7\Éû2\Æ4R\æW7*\ØøW\á\ç¹\'D.\ÛXç“¨\ÓX“±NZŸIq—\ÛK\îM$¡\r+E\r\ê>C/{Db‹\ås¾2\ÂÛ§iª\Û\Ç\íF÷ð\ä7«]b¨R°¤’•pxE7«\ÖŠi5†Ix^®\ÅRD%	KO²\0q¡r‡‘ý#\"µJ–ª\Ê&\0\n¶\æö\Ï\å\ÄDgO›~Fq¹©e\ì8ƒqÀ\àù’\èuYz´—\Ä26œœh›”+ûŽ%-\å¦Z{y\æz\æ‘.—:»¶mSŸ£\åù„i=(üŒÛ’³((u³b8\Äq6”¦p»’$\Ôf\ê,\Íwwú´#kkA‘\Ýo\×ß±Ä´tU\äJ\Âf[Í§ú¤ùý\Äo2Ã²\ÓK\Ì6[u³e$\î9¡q¾‡e¡\ë4jQgukz÷]\r\ër8E\Û5\n™˜x€¿ð\ß)*µ…‡ˆ\Û;o&×‹+\ÃÍ¥IQ¬2ðA–H\Ù^Ê¬ƒa¥Æ¾G-\ãS)71#6\ÜÌ«¥©†•t(Z\àû\Æû\é¹\âòŸý¦p,$\í0.«/h\\[<Ê•xÁ’v˜\Ý[Ÿ£°À–o¼]].ð	o\n\ÖHHºw\Þ\Þ\×\Þ/Š†0\ËN¼ºHed´²	(&\Ù\á\Î\Ù\Ü\Æ{X–®\Ó\é\Ú\ÄbÍ­6I`›®-§”hªs\Ó3ó®LNM—~^ô€6€&\ÙXta\èt\ï6)Â©i\á-ôš\ÜÝ’ ;\Ì\Æ\Éü9$\ßñ»=m:Jn£>Ä„„»“3s\r²\ÒÔµ\0\ë(ø•aé©†¥¥Y[ï¼°†\Ûm%JZ‰°\0\rI1\êÄ»;F¥ú«,®»4>°ä¯…Gð’xý\â5\ÓA™²\Óg\ÙV\0§\àªE’õY„\'\ã&¸{´p@<È¹\Ýmhxº™ƒð\ë\Õò‡RT™YB«*eÏº<³ñ\0ó\"2ñ~\"¥\ájÕŠ³\Û7\áJm·Vod Tm\è\0¹\ÈG’ñ\î*Ÿ\Åø‘ú\Äù\ØJ¼\ì],4HÔ\æ\æ(3SUž˜©T_ž™\Ù\ïQV\Ê|’‘¹#@#|\Ã]b™A:X\"µT\êycz½aÖÞ­u‡8i”zŒ\Å.y3R\Ç1’\ÐtZx²Œ>p\ç¦§K\Ê1\Ë\Ð\è­e2X¥\ÏKÔ¤‘5,«¡ZƒªNð|\ãYŠ(I©¶™™r:\Ðð_G\07	?\Ø\Ç‡\ê\ï\Ò\';\æÁ[+°y¯¾<¼\Æ\ã\\¤\Ë’­\Ì\Ë8eÁtŸ\ìx”ŽJg£óF\Â\ãA»SÀý<³þ\í#/¥\'›\niA  JUv€W|\"§4–)„”l~\ï;Z\Þ\Ù\å~1 &m¥\Ï\É6~)9¸„ÞŽ?\Ì?X\á9\Ät\Ñ8\ê\Ã=J\Öi\Ô`RPðø®Oû¸\ÎY A—\Êö»W9ùœ\ã\éU‰²…]\× \Ü÷Yõ”kýI‰×°\Í\Zq‰|]ˆeÔ¥\Óe\\\rX\ßsòƒ\Ãk<£\'\ãW\Ì\Þö#Ù³”GŠ«\è@¬>©ypœ¤Ò±™?ó6ü ‘©6“kU9\Z-n«Qx1\'*\Ùq\ç-{Ào$\Ø¼›E\éÙ©y9G§&\æb]”u\ÅY(HÌ’c\Êý±vƒ1Œ«^I\ÇZ¡\Ê,‰f³ñÓ¾X\âwò2b¦=ûMi\Øæ£«_ø,HK•	)Qþ’N¥D|\Ë6>\Ã!—ZCœ9À´ŠG¬Sœ¨\×X½^°\ëXoVš\Ã\Ø@µ‡Z\Ã\ØC\Ø@µ\Î­¹H™(sirŽŸ¬@Ì¤ý\á\ç\å¾4\Þ\Â¢\ê+t<£^\æ\Ö+¨œR¬¦K\í8‡šC­,8\ÚÀRT“‘DrXÒ€§ºœ‹`›]öÓ©ü`Q\ï\Æ5\ØB¿ôk¿	6«\É,ü\Çý\Çùxx\ì\ê3É—F\Ãd)Å¦\àƒp”N‰\ã\Úy¥V÷zòq\í¥ý\Z\ë\Õ}‚öl\å^qœQ^”E4v\ä\Øu7øµ\îY\ÃI\Ï?˜ùŠR’„)kRR”¥)FÀ©<G=‘c¯¥’\Î©\ì‰\æ\Û•p	„¤|¤nXv q×†\í\ï´\Ã8\ì\Ö <ŸƒI,\ÔfR/\ß(\ÚAû ‹>c–ƒ8º¨t¼3\Òm.£ºI\Øiûr\í(b—þ‚¢­I¢Ë¹w\n·Æ¬•o¸7©Ï…¢Þµ‡({´\Úkµ‡°‡°€kN£×ŒS\ØA:5€\Õ\ë´†õzÃœ\0\ëHu¤9Ãœ\0\ëHu¤9Ãœ\0\ëH\ÜPªA»JL,\ì›Qû>G\ËúFŸœ9\Åñ\Ö\èyF­\å¤wq8\äÿ\0‚µTS\nøyG”‡‡\Î\â	@s\ã/þCœ9\ÂIo,¶\Æ\Ê;8Tt|\ß1Ö\ëHs‡8°\Üi´‡8s€i\ê=a\Î*G¬M\êõ„7«\Ö\ã”\0„=\Ç({ŽP÷¡\î9@\0	½’M³\È\ìl’@\Ôìœ£eL­\ÍS™KR­0\0_xTv‰Rô¹\Î\Ú[Mö¾qwöŽ f^˜PaN¼AY\ÙP\"\rÀ6$‚nMó79Á\Â5!* …M±±<!°±«Nÿ\0\ÛWûF\á8’}*BÜºvP\Ë#`*\àXª\Â\Öù…‰\Z“¾\ÅF¹?;0û\Î9±ß—J’…(\'\ë\0\n\Êÿ\0„EvF·/(@i¨\åq\Ê(!\î9C\Ür€T\ê=bž\ã”¨õ\á\07«\Ö\â\ït’I¹\Ö\Òx˜\×8s‹½\Òx˜wI\â`\\\á\Î.÷I\âa\Ý\'‰€-s‡8»\Ý\'‰‡tž&\0µ\Î\â\ïtž&\Òx˜\×8s‹½\Òx˜wI\â`\\\á\Î.÷I\âa\Ý\'‰€-s‚u\Z\ë{¤ñ1P\ØSÿ\Ù',4,1,1,1),(2,'Wysoko wydajne MySQL. Sprawdzone strategie dziaÅ‚ania na duÅ¼Ä… skalÄ™. Wydanie 4','MySQL od lat jest najbardziej znanÄ… i lubianÄ… bazÄ… danych typu open source. WciÄ…Å¼ speÅ‚nia oczekiwania uÅ¼ytkownikÃ³w, staje siÄ™ bowiem coraz bardziej zaawansowanym rozwiÄ…zaniem bazodanowym. RÃ³wnoczeÅ›nie roÅ›nie zÅ‚oÅ¼onoÅ›Ä‡ tego oprogramowania, pojawiajÄ… siÄ™ nowe funkcje i narzÄ™dzia. Ewoluuje teÅ¼ rola administratora bazy danych, podobnie jak zmienia siÄ™ podejÅ›cie do pracy zespoÅ‚owej. Efektem tych zmian powinno byÄ‡ dostarczenie aplikacji o wysokiej wartoÅ›ci biznesowej, takiej, ktÃ³ra bÄ™dzie siÄ™ skalowaÅ‚a wraz z organizacjÄ…. Warunkiem osiÄ…gniÄ™cia tego celu jest jednak gruntowna znajomoÅ›Ä‡ MySQL.\n\nTen starannie zaktualizowany przewodnik pozwoli Ci poznaÄ‡ zaawansowane techniki pracy z serwerem MySQL: poczÄ…wszy od tworzenia obiektÃ³w, poprzez projektowanie schematÃ³w, indeksÃ³w i zapytaÅ„, skoÅ„czywszy na optymalizacji serwera, sprzÄ™tu i systemu operacyjnego. Opisano tu bezpieczne i praktyczne sposoby skalowania aplikacji za pomocÄ… replikacji. Pokazano, jak moÅ¼na zapewniÄ‡ rÃ³wnowaÅ¼enie obciÄ…Å¼enia i sprawiÄ‡, Å¼e aplikacja bÄ™dzie dziaÅ‚aÅ‚a nawet w razie awarii. OmÃ³wiono najnowsze trendy pracy z serwerami MySQL (w tym bazy pracujÄ…ce w chmurze), a takÅ¼e nowe funkcje i narzÄ™dzia. Nie zabrakÅ‚o najlepszych praktyk w zakresie zapewniania bezpieczeÅ„stwa bazy, jej wydajnoÅ›ci i stabilnoÅ›ci. DziÄ™ki temu przewodnikowi zdobÄ™dziesz peÅ‚nÄ… wiedzÄ™ o tym, jak nowoczesne firmy uÅ¼ywajÄ… MySQL na duÅ¼Ä… skalÄ™.','\n978-83-283-9294-6',4,'2022-11-15','230x20x170',60.00,1,2,'368',_binary 'ÿ\Øÿ\à\0JFIF\0\0\0\0\0\0ÿ\Û\0C\0	\Z!\Z\"$\"$ÿ\Û\0CÿÀ\0\0\Ì\0€\"\0ÿ\Ä\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0ÿ\Ä\0>\0\0\0\0\0\0!1\"AQq2a#3BR‘¡±\Ñ%bÁ$7u’¢´\áÿ\Ä\0\0\0\0\0\0\0\0\0\0\0\0\0\0ÿ\Ä\0+\0\0\0\0\0\0\0\0\0!1AQ\"#a\Ñ$2‘±ðÿ\Ú\0\0\0?\0\ìˆ\Õ;±u^ƒ\Ëµ=ú\Â/\åaŠ\Ú|÷X\ÔI˜%–ž™¶\Ëe\åD24¡#Œ;p\à£w›…À·<\n\ÊToƒO,\×M*öY[S\Ñ¬Sö\ë\äz\×[¤Õ±OCH^\Þ\"m\ÞÛ’\r\Ç\Üp-l=Í­s*\É<žK\ÌE;S\Ç.]0YUü’H\Ø\Ä5¼öÛ¡¸¢\Ëu\Ï\áY\á\ê¿\ï\Ïû,€ˆz(þ°l_\Ú?¬c£I£€$ów\Ònû\ßøÍO4ó±hþ°l_\Ú?¬zÁ€<\ì_\Ú?¬ö\ë°`;ö\ë\Z•0´rüD*\r¾dòa\ÜVÀ hfŒ: ý9f\Õ\Z›\'Ó“\åñfl\Èk¦1\ÆV2Á@³[¢‹¨÷aõ!\ÆTjIZx…Ñ¿1GŸ\Ô}q§ªrZMM§ä ˜¦\É\n¼r4aû·Sup§‚A\ä_€|°›\"I\Z\É\Âmu#¡\íJ<mt€\ä[¦ :/S\æYV m¬\'‰j”\Ëj6*-\î[¡$n\ÈA\ç¬úd¸2!·>„`‘þXö]¿\\$–=†\"óö‡¤`\ÓËŸTf\Ë^s/ºûÇ‰ÔŠ®ø\Âc+kƒ¼{Z\Âý9À›}N\0>§\rtz‹(«\Ôù†›¦ª\ïs<º§«‰Q­\nË»»»Z\×;Iµ\ïnp\ë|\0lK\á»L\ç¹f£\È\éóœž \ÔP\Ôn\î¤\ØWv\Ö*x ªF\0rÁ€à¿¾\00`¿¾s\ì÷,\Èã¤“3¨0-ed4P…·\Í+mE\àqs\ç\Ð`,ó$‹l\í}ª	6ð1¡§3šÿ\0#¥\Îr\Ó;RU&øŒ°<Ok‘\Ê8½:0\0‹i6\ê)‹(&7qû~£\×\Â2†R\à\à-i¦\é5>Mð’L\Ôó£	)ª£h\\ta\ë\íüõ\0\ãOG\æy¬•™†K™\ÓT—„H\ê\Þ3ø\Ãh\å\ß\åg\"\Ìvð.A\é\Ë\äe¨¥*\äü;\ì?\íÆ±F#\Ó\0þXö\åým¢3=SÚž¤\ìú\Ýr\Êik5LRžž¦‘b…G©Z+\ã¨#ü±\ì1\Ñý¦\éýG\Ú&¥\Ñ$\ÔÙ¶C GYŠÚ¥m\âx\ìnB’¿¨ÀÖ—ª\ÎBf]¾OTOž¦iUF…•¤Ë ‡\á&–ö$òA~…Fõ\rmVW[£s\íE™\æ\Õ9¶lŸ{Ã“GWYNýõMfð)eŒ\Ý\Ö3f@P«pFã‹›Y\ê½«;L¦\ìo0Ž¶ºrŸX”ó\à1¼A6\Ò†1NA\âþ˜´\Ö8\Õ*\0«Â€:{z`e\Óù‹·j4;smJý§¶¢x³|ºF—\à“,¶\ë!È„A±‘,^\Þd\â9¤jóª]RµYµ-|yq92Q\îò£X\ßxK\nþª\Å]÷]SaN§¶®ûAdyª\Ìr\Ú\r-¨sÌ»&—¹\Îóz\nm\Ôô ŸÕ·›ô\èz\âM­;^\Ñ:kIeZ€\ÕÉ™Œ\æ0ù5%FJŠ\â@ \"uEÉµ¯n¼`\Ï\ÙÊ®’|\ïRA£³,\ç3\Ð%?\Ý\Õ™•\íTw÷\é\Ëø¶»£+\rA˜v‰§3<É²\És)è´¥MFÒ»\Z¡˜4¯O9$øŒE\éýG8·û8\í³/\Ô\Z–-/¨´¶w¢³š M6mÅ«\0\\ˆ\ÞÀnÿ\0§\Ï\Ë)¬h5®\Õ:rž’x§Ó•AQ$–\Û+Kx\nÛž\à\n‡?\È3\Í3«²¾\Ï(³Ò§,\Ö\"ƒuKU9jV¡\nkv±;—½‰ð~bÞ¸†5e%V©È…nc©d\í\ë\nc¨($35*µ\'¹º‘Ý¤@w}\Û!»o~m\Ó\ÃKeGYÿ\0‹&Z‰ó$¥øX³³GO ¿wð¡k.\æ\æ\Ã[÷°¹ú`NÒ™ŽVÚ»IlÏµ\\šölón®¤šZOˆçººŸ\ÃEa\Î\nõ¿–¶\Ê*µV©Ì³<\ïQüFO i³\Z&ƒ2™«Y+J\Ê\Ö?ˆÃ»Qc~:ƒÅº·=\Ê\âÍ²zÌ¶JŠªU«…¢y©e1L€‹]\\r¦\Ý–1i\\ƒ+\Ó:rƒO\äô\Ý\Æ_AÁe‹£ÔžIó$ùœ\Êy¶y¬+{NŠl\Ï8z\rM<\Ù{i¾òZ\ÑS¼q\î\à†6†Tf2	{\Ãu\ç }\î\ìo¶\ësn—\Â\ì[ƒn>˜\\\æTY«ƒ(\Ü\Ò‡\Þ#\Äm\éô8\ß\Æ:ˆ–H™X-€=\'\ålrw§óxµ\çh½¦\éHÌ™þÕŸ`PI¬¤jdC\Ç=.m\æ7y\Û\åôh\í—\éœ÷Sf\Ôu5RÍ¨k\ÅuJ\ÊWln%’ÀXy\ß\0sV™\ì\ï0 \í;I\Ò\ç5sÃª5nA\Ö\æÕ‚VY\"že]€0±\Ø`8ó9v°\ÔúƒMv\ÙD¹d:¡5™~¡š9\ØMðô\r½\Ûp!¬\êSŸ>}q\Ð\î\Ë\êõ\îS®æž³\ãrZ\Zšh`iŽE”\×¹o#¿ašv|ÿ\0µmQ\Ûv™¬\Ó\Ñf°\ÅK–RW Z’ªª%\×ô( @}y™ôö¯\Ñ\ÙÆ¬\Õý–\çZVijúúŠ¼\çOT¸f±\ï•%‡<q`AÆ¯fš·Ojÿ\0´&Ÿ\Õ5´‰Ag££\Zr\n\0†eÖ¢8ˆ\ãp€µ®½:\Û}Oöl\Òù¦ Ì³,³Q\ê\\‚›6•¥Ì²üº¬%=Acvð‘À$ž9›q\Æ$º«±-\rŸ\è<ŸH\ÉKUGO’&Ü®ª–r•\Í\æÁü\É<›ŽO<Xý¢µþM©i\ßG\ÒPf\Z\×&\Õz\åp\ÔÁ²Y‰”~<x\Ê\î\ç\Ò\×\ê18\ì[ÿ\0;{cÿ\0\Õ(?úƒ\r¹\Ù\Ç+\Êõ6Yª$\Öú¯1\ÎòúÈ§Š®²¡%=\Ú^ðÙð°$Í¹·\\nk/³\æK¨õ–o©Æ±\Õ\ÙENk*\ÉQ]Z°\Çu@ƒ€·</™=N\0¹°cCNe‹“dBT\ÔU-4t\âz‡\Ý,\r\Î|\Ø\Ú\äú\ã\00`À0„‘½°¸Gù\Û\0\"~Xöc§\Õ9k#µK=)Y²–6€N\Û\í$ƒe<\áñ?,{Dc‹MMœ³šŠ‡y\ÛiIZD»n$õ°\é~<<c,’j¨\×c+\êOú\ÛSdŠÒ£\æ	\Ä\ÅdWVR¤H A|b¦\Õ9K\ï/3\Æ›£s\Þ(·ˆqõ\é\é\ÏL1\Çþøjºƒ@ÖŽFr®®L€¨mÀ\"\Ï\È}y\Úî´¬Ò²üH!\Ò†IC—\ÚY<\ßm\Åý.2Y\'\í¼X×‰Pj,žz¨é£®S,µ«\r\Ç\Ê\×ƒ\äzcMM“¼\Ý\Ò\Õ;B!rx¯·Žm±°Ì•úV–z\nÔ¢”\Æl7Ycñ\â\ÃÌŒ9\Ñdy}0­‚,u\nÍ¼\Èþ-\×õ\ë\É´g9p\ÑGw’i#\Õy\0~4Ä„¼l7\Ûöñ\Íü½q\î‡R\åe\Õ+2£Ic\Ë^­ÓŽ9·\\kf\ZG-ž†Jzuzg+µqp¢\à‘´žA·O©\Æ\ÆY¦òú*r…\Zi\æi\âƒÁ$tÿ\0a‰]\ÛÞˆkN\×fµ^ZP4†X¿1˜4lD,7ô\ç\å\é\Ôyô8\ÉOªr‰!\ï^«`%¶xY·¨b»…‡#‹ý0­¥rgGG§•\Õ\ì[t\îny\ç“×“ýœz‡Kä°h\è­d\Ø?¸\Þ½ö·¯&\ÎS›\ÒfWX$üP‹#\'¢›ØƒÐŽ<°\ã†Ü£$Ë²©$’†Ÿºi\0\r\ã\'\ï‡,kªù¹1ŸMü¼1b¡„‘½°¸Gù\Û\0$–=†\Z\ÓN\åiZ•b\ïPX~! õ\ê<þcý\á\Ò?{z\Ä8§\Éh\ÉÇ†0„r ©Z\Ç\â^÷_/,{]3C\Ü\ÖA#LðUÊ²È†C\ÉA=H&\ç\Ü\áó)Ú‡¢\Ý\ìž\È\ëhÌˆ™iYÅ®%o	µþ\\XzË©%4\Í+Lc@¦F\ê\äu\'\ßŽ\ë]i\é:N÷5¬E´4\ÊA–[z!ÿ\0Q°¸˜\Â1\Ý\"%’sU\'d‹\ZY\Æo–dôoWš\×\ÓQS¢–i\'” °\ë×®9§Zv\é×½E=\ë•w$·\Ã\ÂvJlH\ndnO>\0:\ÛEn¡ûÂ¤U\×ÿ\0Ìªg”0’p\\†\Û\ãB\Ì|$zô=:ó‹Y\n,\ëa\Ûgf1Š=K¯{4¤7±\ÛcŒSvÙ¡Ä¡)\æ\Ìj\Å\ìZ\Z6°>ž+c–ª2ªzŠ4\Ôý\Ü\èO„!…\î¤\Ò\â\æÇ‘¶\Ü\á•\Ã,½\Ü1\Ë\ß#­•\è:ù\á~IP¾\ÙÓ¥iòu¦§\ÌþvM\é\\f\ã\è[\ÂO\Ð\â^¤pn1ÀT\Ó\æ40ø»¶\ßt¨Á6l8\ãþü\â\Üì›µ\Ü\Ë*’–’µ\ÍVV\Ì\é\Í\Ë\Â	\å¢=l.\ÎA‹°¤ŸPh\ê\ÇIQ\rU,U4ò,°Ê\ãu7¤\\ô¶2b\Åÿ\0#{apò7¶\0HþA\ì1\ëcù°Ç¬\0`ÁŠ3·\î\Ù\ßNTUim/±óh\ãÿ\0\ÆVqIqpti,G\'…¿™\ã\0•½²öµC¦)ªrlŠ¢\Z¬ÿ\0iVµ)>®:±\á?“\Ç–uNsœgY…VdùL\Õs!WrC™7X…n,:tòµ…†\ê³Zzj˜©\ê§?ˆ{\Ä\Ú¬\ÌÇ›\í\ç\Å\êy8@”ý\íB¤Yžö¿È¶\Ý`I[9\â\r£Ä±\ÅvUIe3»H\ÛL\\Å‡7½ù\ãƒkc¯Rbf’®s \ï¡‚…B\0×Ÿ÷q¥<ôð\ÓFóI\r3›¨³ÆŸ¨)^›\\\Øß›\ã~ŠŸ\âX³(\ÝYöª“¸(R|6Û¸~¶?HrQV\Í#\'H’hL¥³9`“3hÞšž-­\n\î„Tª=Ž\î~¶\è.Oòd¹$Yt´³\Ñ\ÃJª\Ò@ˆ<@ª‚§÷Y”“~Ÿ\ÉÃ–Ÿ\ÈÞŽžVA-L©”G´\Ùn9H”\\þ«ëœÿ\0(¨žŸ\ïD¤\ï# Œ$»€†HÀ³Ž/u#}Ç®\â<±\ææ”²\âl\í\Ã\ãÊ‘‰•¨v<hw»G—ƒaûm\Ïõ\éˆ>¢\Ì$Ô«	\Í=B$€%\íµø6\è	\ätq‹“B\èZýW•>uEsQ¼Œ\äBY€Tn›‹E®:Ÿ(‡h:Mª«¾î®§¯I\'–4jUe‰šh•ö\'À\Ë\ãÜ¢\â\ÄŒe¥Å“Ô­Ÿ‚\Ú\ÍL&º(·þ\Î:\ÊJ„:Z½\É*†Z&ú]¼¹\Ü=\Èòºñ\ËýiZìŸ´|”M˜G[$$Œ¼‘b\Ú\ÉÁ €Í·\ÈøM\Æ:€cØ‹³\É|†þFö\Â\á\äolIGòaXó\È=†#]¤\ë­? ´ô™¾}X±¬)\éÔƒ5K}‘¯V?\ä:›ûBv‡ÿ\0t,•”\Þõ\ÜP#‹Ù¿S\Û\Ïhò\ér£-šŠ¼Â¾L\Ó3¨\Ý_S?}<Ò¹2;¹½\Í\Ï[aß´NÒ³M}©\ês@‘¬. Q\ÒIŽ–>½Ý­\É<]­r~–´xL¬—§X\âT=Ù½¯\Ï\'\Ëÿ\0¾3l\Ö*‘·M:S\æDIQ\Â\r\Ù\Ô\í(×¸c}Þ\rÏ°û<ðòM$ˆ±øIo;| qo\èuó\Äa]vÕ·¨&\çÛ‹mAkùœo\ä9Fo˜L>êŠ ;{\Ô%\æH\à\é\Ó\Öø)Q#¬T=@Š:rò2¨ \Ü)‹þb\Â÷òÅ¥\ÙþšG5u=œ„nyò½Š\\tM« ä›˜¾]+¡eÊ¨~75\ËZÐ‰6¬@G7\é\Ó\åa\ÏB\0\èo‡×¬4\ì\Ñ\Ó[#ð\Ñ+_yk²Ü}„XpTó69rM\ä•-‘\×±\Æùc„\ÆË ¦†ªjh©œÈ²lbp\âì¿¸|²ó{«ºŽ˜k\Ë(³IœR\å9T\nñ\ÌþTH9=\ã\ÉTºÜ‹o\Û\Î%\ZS³\ÍYž“9¾WJUv¼\Ê\Üm¨-k\\\ÛpEŽ.m-§2½9—ü&YN0\ìÌ’,? \è<­¡¾Ni\äKŽLús)¤\ÈòJL¦…\n\Ó\Ò\Ä#K›“n¤ýI¹?S][¦ò\ÍE–KI]\Ëh\ê$\'É”ý6<1‡¬\è9\Ês\ìÛ¦õ--&cž\ê\Ä\"yj¿z”y!o;)\åw\Ùl!Tz\â\ãÁƒ\0Gù\Û„‘½°·\Õ^Ž\ÒÚ8‘’ŽŠ\ìw;žŠŠ<Ù€÷\Çv»­sNÑµs\ê<\Þ3L±¡†’™%%)¡7ðß‹’\r\ØùŸ¥†;{µÍ¨{Dû®Ÿ<Í³²š3\Z\ZR¨\'›€®\ÎA6Q¸\0-ó|qWmy\rüAª£\Èrxò7G+\ÒQ•$½Gvv¼ÄµÙ·¸`ñe\ã¦)$\ËÀƒ\Ò(©\r?‚ûŠp€·<_üð\å’d9¦mT‰H°D\ÎûN\îv2E¼¹\ãFšž\núJ<¾-°ˆ\ÂŸ¬\Û\ËÓŸ_s‹KHd”y5=\r³SÇ™\æµB¿Œ\Ûj‘\çb9\às\æl1D]º0ö}ÙžK÷%-vq$\Õ]\à3÷lƒovÇ€\0ó6\'Ÿ3oKÙ™-^d“\î\è\"jj`\í\Ö}¦À–\Þ%\à‹Xž}dC55QC*,{Q6£Xˆ\Õ[¼mbG6wB\r\Ö\Ø÷W4\ì\ÔNH\Õ5R,kG\â¹ð†bm\Éqô9P±\Ã(\Ësmkª[´´9SZj\ÉO\å\Î\Þ#¶\Æ\ä¨ €y¹7¸¹7V—\ÓYfCJRŽ\ïÜ–šr£|ŒI\'Ÿ!rl£|liœž“#\Éiò\ÚDP‘/‰‚\Ø\È\ç\æsõ\'œ9bñ‚Ž\å%6ö\0-ƒ\\ `Áƒ\00`ÀþFö\Â\á\äol\í´L¿A\é\äb\ÑÏœVƒ]H[™¦öôE¸$ÿ\0x\â¼ÿ\00\Ísª¼\Ê|Ö¢L\Ï6¨Ÿñ¦µ\ÚF&\ÛP@\0€ú\ïk}I˜j|ò]Aœ\Õ,•ó\ÈÁp”ð\Äj	ðŽ\ï{›\âûû3vF”©¹\ÔJ\Í<¬*2ºF!\\y±\ê:(±\ëkgü™²¨\"›\Ëtž¨›4¡›/­(bˆM»‘\'õ1\è|…Àç“Œô\Ù%mmcW\×üUTSg•6\áY•A^>eò>^X\î	\é\à6Or¨\èCó\Ä¶ü½%Ò´’Ç¶?†¬V\nÜŽ¶ÿ\01Œ5‘údû‰•¶KG¸N”\Ð\Ì\Õ\ÔBL\Ê`lW\×;•ÂžC†\â\Æ\Ò/³ø9ö{œ\ê|\Âø˜\n\ÒBeK0 ¸v\0’A;@\ç›_ö\\\ZTžb½Us±@¹\"þXöc\Êõ¦«\Ê{c2›ŽCžð}zH¬Zrqœ‡ø!S‹,l0c¤\È0`Á€0`\0\Â?\È\Þ\Ø\\#ü\í€9S\ì»\Ù`\Ï]5n¤Ë‰Ê¡”I—E0ð\ÕH/ø„±©\é~’zu\êÁÀÆ¶úL¿.\Þ\í%%<@’HH\ãEÀP\0ö®5Wj´oK¥#ŠªI•+\ê.´\êGšŽ²¯õ8F>‰n÷,öeU,X\0\É=)\Î\Õ;K\ÒušdÁ\rixZ	j6\Zª¾\ÓbO$ž\0õ$qˆ¸\Ìó÷$–ƒ3Ï³*\ç•\0‘~(EÄÒŠ¨¹\éc\åÏž+\ê=!<“™uc¦-\æ\â”\0Šl_\Ä8g$_p¹>ƒ\êpO,;i\Ò{7ø-ŽQ‹\ê~“#ížº‹*øI!\ÊeŽ‰v%A›½E-öð	\0s\ï\áÁ’v“Dý¢KžV@”+40÷\è“w‚£`\Ö\0€¥IA\Î()´Yx*§–ië»†z…€\Û\à¨+`	\n[|\Þ\\c\ÕUð¢âŽœ%¼WRt¸õ\0‚§\écô\äÉ¥\Ôt\'\×n;ñ\è\Ö2…\ÕUmžö½¦rÚˆ\Ñ\'3F\Ûo!\Ôr@ý¼u½\Ïÿ\0¸œ\äÙ•&m–A™P\Ê&¦wF\ë\È\"öòö\Ç%d\ÙN¤Ê©e›&Ô’Æ¡¹’£|V#‚QŽÐ¤Ž\0Ã&a«r:œµ\ä‰ÈŽ¡a¨ši:9°fE²£+Á—†ñ:ã–¡Jæ“‹õà«Œ\Zùyû]qƒµ6³\Íh\ê-÷³O´Š\×*À}MÁ·½üñ.\Ó=¥eY„j•‘\Ë\ßoz¨Z6ú‹r>¼[\ëŽ\çbNñ\å\å\ržDSkòm\Æ\Ý]£V‚1\\kÜ‹üQY~QŸeTtòSˆjey7´Ñ†,x-\â;\äµˆ¨,\Ë{\\qYXnRõ«Î–\Ô3\Ö,RkjZˆ\Å=LUjd;Ü¼rÆ—\0ü«º2AóKù\á“Niªº|²l®=[F£/‘U‘*ga‘\n\Ý:($0g¸%ö‘ar\Ùq„‘½±^\é<—5]CIšÅ©\â¬\Ë7\à\n¹%\ï•ÕŠ¹V>±Œ[ O%¬\'ù\Û\0s‡mý¥\Ðf¹õF‹+WP†¤°ª™@ –<•¸õ,Å‡0\ê\ÍaMKNñPµD²wB!\Ý$}\Û\0T\\±\å¹o\æ\ß\Î1ý 2G\\\ç`¡ª\ïb¿\ëI\\\Û\év?\Ñ\Ä:y¤vmŠ›#\0\àm#\ÂT}@øÆ‘u°$)¬\èj¥š?€¯\áRWc!I{ðO<\Û®Ëªv½-<ô\ÊÎ‘Hó\Æ\Ï0‹\ìQ~H\ä\ÛÏ „ü;C™\ÔG¡‘£>\\Y…\Çú\áE,©N³J‡c¥ö\í*›®D\Ñ6›7Ê¥\Ë38&\Ìþ²¯b–Åºñ³€/\â’¦YP2\Øë…ªâš’(ê¬¥•\0ƒuô$žx±?\Åa—ªTe\Îò+\Ó\"©¿\Ûù¶²¼\ã2\ÊrÀ)³:\ÊT…\\G`ñ•!\n°>V\"\ÖóÄª švq–g¹veKœw}\×x´ô\Î\Ö$\ÓÆ·“`\â.O<œ9ÿ\0ˆ\é2œò¦Š\\\Òr÷E¨B²£\Û{le$\Ü1[[¨a\èqÈ«*sE†LÞ¡g‹¹‘ã¦€T–&(‡T n±¿‰¼ø\Æî¤‚\Êah#Jp•À‚\æ.\Ö\'ý÷\Åb£HžY‘s\n\Ê\Ü\Ø\å™\É\"–y\r}\×\ë6e,E\Öû…­a\á<\ãaŸUeõS\Ò<òO	\r4{Š£ma¼u\à\ín,-\ÇL–&\Þc– †ž÷U\í\ÏE+\ïlÖ‘ûÊ¿™\'”,_€,°pr	Q\Ù>g-nUS@•®XD`»k•b¦\à\Z\ßSŒ4ý\ä±AT™WHó¡\ãmº±tv=:N‚\Ü1˜„ýžêš–£-¯¿´\Ô\Î\ÞÀ\ÛÏ›˜\Ç\\\\ú\Ó=Méš¼\êh\Zx\é¶E6$3ªýzn½¼\íŠKm\Ùlp–I(E[{\"\";\'\É \Ìi*\é&•{ªˆžE`\äEQ¶\àwl\0\î\'‚\Þxu\ÔÝŸeYü\æjÊºµ;§pi\ne@„‹ƒ\Ð®#\ÒöÍý\Û$\ÔðI%dl{\Êw,Š‰½\ÕYœ¯…\r¶\×¾‡1v³¦¦Š8iš¢j\é,‹\Âý\ßxJª\ÞKX!v	¼‹\\\ã%š\É\Û/„\ëc\Î6z\Ò=™eºsQÃš\ÒUM/tŽ	”øÜ7[\ÂBö6¿‹\çù\Û‡e\Ú\ïP\êü\î\Ò\å\ÑQe‘\Å\'{$‘\ÒT+mh¢!¬Ê—ñ?™\àyœY\Íò7¶/	©«F\Z½&M&N\ÞN\É\ÍkHÖ‡Re5\Â=‚®•\ä\âÇº{\Ø\ß\é\'õŠv‚rj¬\à\É\ãko±+\å\çÇ®,ß¶a;\ëLš’@OOAÞ¬l\r‹bo\Ï<¢ÿ\0X¦\ègš¢§–Wgu\ä\Þ\ÝlM½9\'NM6\ÎVnÖ¾\Ü\ÖI]L‚xn\0ðò\0?\í…øµ›NOK).\Ö1ß’Ì²\ÞÀùp\Ç\Z’%¢‘.kžMúF‡ýqƒ,¥†X¤,\ÚC€™	\ã\Äq¬\"\ëƒ\ÎK ¤µduõ\äù{c\Ýs…‘¡X­·»ÓŽ×­±\àÀ\Ãt¿\â.Ö¿ úh‡w¦§,\äÞ˜_øföÅ¬®Ï+P\ÕT÷¯-T4›Z3ú|`–Õ¿œLs&§\Íòø\Ò\0\æ$%ú0;–\ß\Õ\Æ+[<*•e.c³¦\ÌÏœLó\Z¹¨ò5\ÄGøŠF\æ\ÚHúÛŒKi\"8²¾†2b–m’F€˜…\Ø\î³ƒ\èHþ0\Û4ô\ÕÕ‘I›«‡Ud\ÚO-À¿—#‘\íˆ\Þ`\ïKU\ÜA#yŒW>\"\0×©\å‰&÷¹\Æo„Š8¤™‰\Ú@¦RÄ·$ó\ïÀ\è=1\Ëú‰_T·.nÌ¥¢\Ëg¥ª„Ip÷rÃªAn<ˆ\n¼t¤\ÑAWO\Ý\ËS\Âö6e§›ƒ\é\èqÉ½—TO4•4³J\Ò \Ý\Ûæµ€\ë\ëltÞ‘¨‘´®T\\†oƒŠ\ìG\'\Âñ\Ô÷D¦m>C“;3>U@\Ì\à†&™	`I6<s\É\'ù8X²,š\'g‹* ™·1Zd›ƒs\Ç[ªÿ\0\í˜\Ù\ï\ß\Ñpw\ïè¸­\"ý\Ùûf\Z,£,¢˜\ÍIAK¤[|pª›zq\Öù\Û;÷ô\\#L\ÅO\ÓU¶Ý¶ÿ\Ù',4,1,1,1);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `personal_data_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Clients_personal_data_id_9da9bd5e_fk_PersonalData_id` (`personal_data_id`),
  KEY `Clients_user_id_4c87af95_fk_Users_id` (`user_id`),
  CONSTRAINT `Clients_personal_data_id_9da9bd5e_fk_PersonalData_id` FOREIGN KEY (`personal_data_id`) REFERENCES `personaldata` (`id`),
  CONSTRAINT `Clients_user_id_4c87af95_fk_Users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `languages`
--

DROP TABLE IF EXISTS `languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `languages` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Languages_name_afabad0b_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `languages`
--

LOCK TABLES `languages` WRITE;
/*!40000 ALTER TABLE `languages` DISABLE KEYS */;
INSERT INTO `languages` VALUES (2,'angielski'),(3,'niemiecki'),(1,'polski');
/*!40000 ALTER TABLE `languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `creation_date` datetime(6) NOT NULL,
  `total_price` decimal(6,2) NOT NULL,
  `client_id` bigint(20) NOT NULL,
  `order_status_id` bigint(20) NOT NULL,
  `receivers_data_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Orders_order_status_id_7f631565_fk_OrdersStatuses_id` (`order_status_id`),
  KEY `Orders_receivers_data_id_c7eeb7e1_fk_ReceiversData_id` (`receivers_data_id`),
  KEY `Orders_client_id_71fdbbc0_fk_Clients_id` (`client_id`),
  CONSTRAINT `Orders_client_id_71fdbbc0_fk_Clients_id` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`),
  CONSTRAINT `Orders_order_status_id_7f631565_fk_OrdersStatuses_id` FOREIGN KEY (`order_status_id`) REFERENCES `ordersstatuses` (`id`),
  CONSTRAINT `Orders_receivers_data_id_c7eeb7e1_fk_ReceiversData_id` FOREIGN KEY (`receivers_data_id`) REFERENCES `receiversdata` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordersitems`
--

DROP TABLE IF EXISTS `ordersitems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordersitems` (
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordersitems`
--

LOCK TABLES `ordersitems` WRITE;
/*!40000 ALTER TABLE `ordersitems` DISABLE KEYS */;
/*!40000 ALTER TABLE `ordersitems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordersstatuses`
--

DROP TABLE IF EXISTS `ordersstatuses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordersstatuses` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordersstatuses`
--

LOCK TABLES `ordersstatuses` WRITE;
/*!40000 ALTER TABLE `ordersstatuses` DISABLE KEYS */;
/*!40000 ALTER TABLE `ordersstatuses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personaldata`
--

DROP TABLE IF EXISTS `personaldata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personaldata` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  `surname` varchar(32) COLLATE utf8_polish_ci NOT NULL,
  `email` varchar(164) COLLATE utf8_polish_ci NOT NULL,
  `tel` varchar(25) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personaldata`
--

LOCK TABLES `personaldata` WRITE;
/*!40000 ALTER TABLE `personaldata` DISABLE KEYS */;
/*!40000 ALTER TABLE `personaldata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publishers`
--

DROP TABLE IF EXISTS `publishers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `publishers` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Publishers_name_3e3c67b3_uniq` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publishers`
--

LOCK TABLES `publishers` WRITE;
/*!40000 ALTER TABLE `publishers` DISABLE KEYS */;
INSERT INTO `publishers` VALUES (1,'Helion');
/*!40000 ALTER TABLE `publishers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receiversdata`
--

DROP TABLE IF EXISTS `receiversdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receiversdata` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8_polish_ci NOT NULL,
  `personal_data_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ReceiversData_personal_data_id_ee868a30_fk_PersonalData_id` (`personal_data_id`),
  CONSTRAINT `ReceiversData_personal_data_id_ee868a30_fk_PersonalData_id` FOREIGN KEY (`personal_data_id`) REFERENCES `personaldata` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receiversdata`
--

LOCK TABLES `receiversdata` WRITE;
/*!40000 ALTER TABLE `receiversdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `receiversdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) COLLATE utf8_polish_ci NOT NULL,
  `password` char(1) COLLATE utf8_polish_ci NOT NULL,
  `is_employee` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-23 22:53:49
