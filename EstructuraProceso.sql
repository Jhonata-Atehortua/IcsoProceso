-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: icso
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actividadeseconomicas`
--

DROP TABLE IF EXISTS `actividadeseconomicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actividadeseconomicas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo_opa` int DEFAULT NULL,
  `descripcion_opa` varchar(50) DEFAULT NULL,
  `codigo_icso` int DEFAULT NULL,
  `descripcion_icso` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actividadeseconomicas`
--

LOCK TABLES `actividadeseconomicas` WRITE;
/*!40000 ALTER TABLE `actividadeseconomicas` DISABLE KEYS */;
/*!40000 ALTER TABLE `actividadeseconomicas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `activo`
--

DROP TABLE IF EXISTS `activo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nit` int DEFAULT NULL,
  `primerapellido` varchar(100) DEFAULT NULL,
  `segundoapellido` varchar(100) DEFAULT NULL,
  `nombres` varchar(100) DEFAULT NULL,
  `segundonombre` varchar(100) DEFAULT NULL,
  `nombreintegrado` varchar(100) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `telefono1` varchar(100) DEFAULT NULL,
  `fechaingreso` date DEFAULT NULL,
  `fechanacimiento` date DEFAULT NULL,
  `coddepartamento` int DEFAULT NULL,
  `codciudad` int DEFAULT NULL,
  `codcomuna` int DEFAULT NULL,
  `barrio` varchar(100) DEFAULT NULL,
  `estrato` int DEFAULT NULL,
  `celular` varchar(100) DEFAULT NULL,
  `actividadeconomicaid` int DEFAULT NULL,
  `negocioid` int DEFAULT NULL,
  `valorsolicitado` int DEFAULT NULL,
  `montoaprobado` int DEFAULT NULL,
  `plazo` int DEFAULT NULL,
  `periodicidaddias` int DEFAULT NULL,
  `tasaefectiva` float(10,2) DEFAULT NULL,
  `anualidad` int DEFAULT NULL,
  `cedulasociado` int DEFAULT NULL,
  `pagare` int DEFAULT NULL,
  `f_iniciofinanciacion` date DEFAULT NULL,
  `capital` int DEFAULT NULL,
  `saldocapital` int DEFAULT NULL,
  `miembroid` int DEFAULT NULL,
  `nombre_cs` varchar(100) DEFAULT NULL,
  `ced_prom` int DEFAULT NULL,
  `promotor` varchar(100) DEFAULT NULL,
  `cod` int DEFAULT NULL,
  `ZONA` varchar(100) DEFAULT NULL,
  `MUNICIPIO` varchar(100) DEFAULT NULL,
  `cuenta` varchar(100) DEFAULT NULL,
  `cooperativa` varchar(100) DEFAULT NULL,
  `POLIZA` varchar(100) DEFAULT NULL,
  `CORREO` text,
  `ced_ben_1` varchar(100) DEFAULT NULL,
  `nom_beneficiario_1` varchar(100) DEFAULT NULL,
  `parentesco_1` varchar(100) DEFAULT NULL,
  `ced_ben_2` varchar(100) DEFAULT NULL,
  `nom_beneficiario_2` varchar(100) DEFAULT NULL,
  `parentesco_2` varchar(100) DEFAULT NULL,
  `ciclo` int DEFAULT NULL,
  `sexo` varchar(50) DEFAULT NULL,
  `estado_civil` varchar(100) DEFAULT NULL,
  `barrio_id_icso` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=739464 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activo`
--

LOCK TABLES `activo` WRITE;
/*!40000 ALTER TABLE `activo` DISABLE KEYS */;
/*!40000 ALTER TABLE `activo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'icso'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-01 11:44:28
