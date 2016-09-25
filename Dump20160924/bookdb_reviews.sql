-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bookdb
-- ------------------------------------------------------
-- Server version	5.7.10

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `content` text,
  `rating` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_reviews_users_idx` (`user_id`),
  KEY `fk_reviews_books1_idx` (`book_id`),
  CONSTRAINT `fk_reviews_books1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_reviews_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (31,58,3,'6789',1,'2016-09-22 15:33:42','2016-09-22 15:33:42'),(36,60,5,'assadasd',1,'2016-09-23 13:20:35','2016-09-23 13:20:35'),(37,61,5,'dsgsd',1,'2016-09-23 17:20:08','2016-09-23 17:20:08'),(38,62,5,'BBBBBBBBBBB',1,'2016-09-23 17:21:03','2016-09-23 17:21:03'),(39,59,5,'dddddddddddddddddddddddddddddd',4,'2016-09-23 23:46:14','2016-09-23 23:46:14'),(40,61,5,'EEEEEEEEEEEEEEEEEEEEEEEEE',5,'2016-09-23 23:46:39','2016-09-23 23:46:39'),(41,59,1,'00000000000000000000000000000',1,'2016-09-23 23:57:09','2016-09-23 23:57:09'),(42,59,3,'11111111111111111111111111111111',1,'2016-09-23 23:58:40','2016-09-23 23:58:40'),(43,63,3,'colorful',1,'2016-09-24 00:24:26','2016-09-24 00:24:26'),(49,56,3,'nnkkklhkl',1,'2016-09-24 02:24:45','2016-09-24 02:24:45'),(54,64,3,'ssdfsdfsdg',1,'2016-09-24 03:46:32','2016-09-24 03:46:32'),(55,56,5,'fskjfklasjfklafs',1,'2016-09-24 18:34:46','2016-09-24 18:34:46'),(56,56,5,'sdgsdgadsgsdg',1,'2016-09-24 18:34:56','2016-09-24 18:34:56'),(57,56,5,'fsasfasfasf',1,'2016-09-24 18:35:21','2016-09-24 18:35:21'),(59,57,5,'sdasdsd',1,'2016-09-24 21:06:38','2016-09-24 21:06:38'),(60,56,5,'asdasdasdasdasdasd',1,'2016-09-24 21:06:48','2016-09-24 21:06:48'),(61,56,5,'zcasdasda',1,'2016-09-24 21:06:57','2016-09-24 21:06:57'),(62,56,5,'xzczcxzxvzCV',1,'2016-09-24 21:07:04','2016-09-24 21:07:04'),(63,56,5,'zxzcxzxvZVX',1,'2016-09-24 21:07:14','2016-09-24 21:07:14');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-24 21:11:34
