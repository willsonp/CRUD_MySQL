CREATE DATABASE  IF NOT EXISTS `products` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `products`;
-- MySQL dump 10.13  Distrib 5.7.38, for Win64 (x86_64)
--
-- Host: localhost    Database: products
-- ------------------------------------------------------
-- Server version	5.7.38-log

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
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `persona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `salario` double NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,'WILLSON PEREZ','LA VEGA REP. DOM.','M',NULL,15000,'2023-10-07 19:19:42','2023-10-07 19:19:18'),(3,'Test','Testing','M','test@test.com',200,'2023-10-10 22:13:05','2023-10-10 22:13:05'),(4,'Test3','Testing 4','F','test@233.com',2500,'2023-10-10 22:19:32','2023-10-10 22:19:32'),(5,'prueba','prueba 3','F','prueba@mail.com',1450,'2023-10-10 22:25:10','2023-10-10 22:25:10'),(6,'Nuevo Emplado','nuevo la vega','M','nuevo@test.com',1233,'2023-10-10 22:26:01','2023-10-10 22:26:01');
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `costo` float DEFAULT NULL,
  `status` varchar(1) DEFAULT 'A',
  `created` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Salsa BBQ',10,6,'A','2021-05-17 19:02:18','2023-10-11 22:30:42'),(2,'Azucar refinada',10,8,'A','2023-10-11 08:19:51','2023-10-11 22:30:42'),(3,'Cafe Molido el Campo',12.4,4.32,'A','2023-10-11 08:21:03','2023-10-11 22:30:42'),(4,'Yuca Valenciana',10,15,'A','2023-10-11 09:23:55','2023-10-11 22:30:42'),(5,'Platanos maduros',20,25,'A','2023-10-11 09:27:35','2023-10-11 22:30:42'),(6,'Arroz la Garza',2000,2100,'A','2023-10-11 09:30:46','2023-10-11 22:26:08'),(7,'Aceite de maiz',235,100,'A','2023-10-11 10:56:59','2023-10-11 17:24:45'),(8,'Berengena Criolla',15,12,'A','2023-10-11 11:16:22','2023-10-11 20:44:43'),(9,'Nuevo Producto para probar orden',150,100,'A','2023-10-11 20:47:21','2023-10-11 22:30:42');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'products'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-12 15:35:16
