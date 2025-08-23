-- MySQL dump 10.13  Distrib 9.2.0, for Win64 (x86_64)
--
-- Host: localhost    Database: MatchaFundingDB
-- ------------------------------------------------------
-- Server version	9.2.0

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add beneficiario',7,'add_beneficiario'),(26,'Can change beneficiario',7,'change_beneficiario'),(27,'Can delete beneficiario',7,'delete_beneficiario'),(28,'Can view beneficiario',7,'view_beneficiario'),(29,'Can add financiador',8,'add_financiador'),(30,'Can change financiador',8,'change_financiador'),(31,'Can delete financiador',8,'delete_financiador'),(32,'Can view financiador',8,'view_financiador'),(33,'Can add persona',9,'add_persona'),(34,'Can change persona',9,'change_persona'),(35,'Can delete persona',9,'delete_persona'),(36,'Can view persona',9,'view_persona'),(37,'Can add consorcio',10,'add_consorcio'),(38,'Can change consorcio',10,'change_consorcio'),(39,'Can delete consorcio',10,'delete_consorcio'),(40,'Can view consorcio',10,'view_consorcio'),(41,'Can add instrumento',11,'add_instrumento'),(42,'Can change instrumento',11,'change_instrumento'),(43,'Can delete instrumento',11,'delete_instrumento'),(44,'Can view instrumento',11,'view_instrumento'),(45,'Can add miembro',12,'add_miembro'),(46,'Can change miembro',12,'change_miembro'),(47,'Can delete miembro',12,'delete_miembro'),(48,'Can view miembro',12,'view_miembro'),(49,'Can add proyecto',13,'add_proyecto'),(50,'Can change proyecto',13,'change_proyecto'),(51,'Can delete proyecto',13,'delete_proyecto'),(52,'Can view proyecto',13,'view_proyecto'),(53,'Can add postulacion',14,'add_postulacion'),(54,'Can change postulacion',14,'change_postulacion'),(55,'Can delete postulacion',14,'delete_postulacion'),(56,'Can view postulacion',14,'view_postulacion'),(57,'Can add colaborador',15,'add_colaborador'),(58,'Can change colaborador',15,'change_colaborador'),(59,'Can delete colaborador',15,'delete_colaborador'),(60,'Can view colaborador',15,'view_colaborador'),(61,'Can add usuario',16,'add_usuario'),(62,'Can change usuario',16,'change_usuario'),(63,'Can delete usuario',16,'delete_usuario'),(64,'Can view usuario',16,'view_usuario');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_beneficiario`
--

DROP TABLE IF EXISTS `backend_beneficiario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_beneficiario` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `FechaDeCreacion` date NOT NULL,
  `RegionDeCreacion` varchar(30) NOT NULL,
  `Direccion` varchar(300) NOT NULL,
  `TipoDePersona` varchar(30) NOT NULL,
  `TipoDeEmpresa` varchar(30) NOT NULL,
  `Perfil` varchar(30) NOT NULL,
  `RUTdeEmpresa` varchar(12) NOT NULL,
  `RUTdeRepresentante` varchar(12) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_beneficiario`
--

LOCK TABLES `backend_beneficiario` WRITE;
/*!40000 ALTER TABLE `backend_beneficiario` DISABLE KEYS */;
INSERT INTO `backend_beneficiario` VALUES (1,'MatchaFunding S.A.','2025-01-01','RM','Av. Vicuña Mackenna 3939','JU','SRL','EMP','12.345.678-9','12.345.678-9');
/*!40000 ALTER TABLE `backend_beneficiario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_colaborador`
--

DROP TABLE IF EXISTS `backend_colaborador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_colaborador` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Persona_id` bigint NOT NULL,
  `Proyecto_id` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `backend_colaborador_Persona_id_c406811b_fk_backend_persona_ID` (`Persona_id`),
  KEY `backend_colaborador_Proyecto_id_4917ea19_fk_backend_proyecto_ID` (`Proyecto_id`),
  CONSTRAINT `backend_colaborador_Persona_id_c406811b_fk_backend_persona_ID` FOREIGN KEY (`Persona_id`) REFERENCES `backend_persona` (`ID`),
  CONSTRAINT `backend_colaborador_Proyecto_id_4917ea19_fk_backend_proyecto_ID` FOREIGN KEY (`Proyecto_id`) REFERENCES `backend_proyecto` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_colaborador`
--

LOCK TABLES `backend_colaborador` WRITE;
/*!40000 ALTER TABLE `backend_colaborador` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_colaborador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_consorcio`
--

DROP TABLE IF EXISTS `backend_consorcio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_consorcio` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `PrimerBeneficiario_id` bigint NOT NULL,
  `SegundoBeneficiario_id` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `backend_consorcio_PrimerBeneficiario_i_b6ef7ee0_fk_backend_b` (`PrimerBeneficiario_id`),
  KEY `backend_consorcio_SegundoBeneficiario__bdc99fa0_fk_backend_b` (`SegundoBeneficiario_id`),
  CONSTRAINT `backend_consorcio_PrimerBeneficiario_i_b6ef7ee0_fk_backend_b` FOREIGN KEY (`PrimerBeneficiario_id`) REFERENCES `backend_beneficiario` (`ID`),
  CONSTRAINT `backend_consorcio_SegundoBeneficiario__bdc99fa0_fk_backend_b` FOREIGN KEY (`SegundoBeneficiario_id`) REFERENCES `backend_beneficiario` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_consorcio`
--

LOCK TABLES `backend_consorcio` WRITE;
/*!40000 ALTER TABLE `backend_consorcio` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_consorcio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_financiador`
--

DROP TABLE IF EXISTS `backend_financiador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_financiador` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) NOT NULL,
  `FechaDeCreacion` date NOT NULL,
  `RegionDeCreacion` varchar(30) NOT NULL,
  `Direccion` varchar(300) NOT NULL,
  `TipoDePersona` varchar(30) NOT NULL,
  `TipoDeEmpresa` varchar(30) NOT NULL,
  `Perfil` varchar(30) NOT NULL,
  `RUTdeEmpresa` varchar(12) NOT NULL,
  `RUTdeRepresentante` varchar(12) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_financiador`
--

LOCK TABLES `backend_financiador` WRITE;
/*!40000 ALTER TABLE `backend_financiador` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_financiador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_instrumento`
--

DROP TABLE IF EXISTS `backend_instrumento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_instrumento` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Titulo` varchar(200) NOT NULL,
  `Alcance` varchar(30) NOT NULL,
  `Descripcion` varchar(1000) NOT NULL,
  `FechaDeApertura` date NOT NULL,
  `FechaDeCierre` date NOT NULL,
  `DuracionEnMeses` int NOT NULL,
  `Beneficios` varchar(1000) NOT NULL,
  `Requisitos` varchar(1000) NOT NULL,
  `MontoMinimo` int NOT NULL,
  `MontoMaximo` int NOT NULL,
  `Estado` varchar(30) NOT NULL,
  `TipoDeBeneficio` varchar(30) NOT NULL,
  `TipoDePerfil` varchar(30) NOT NULL,
  `EnlaceDelDetalle` varchar(300) NOT NULL,
  `EnlaceDeLaFoto` varchar(300) NOT NULL,
  `Financiador_id` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `backend_instrumento_Financiador_id_0b587c15_fk_backend_f` (`Financiador_id`),
  CONSTRAINT `backend_instrumento_Financiador_id_0b587c15_fk_backend_f` FOREIGN KEY (`Financiador_id`) REFERENCES `backend_financiador` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_instrumento`
--

LOCK TABLES `backend_instrumento` WRITE;
/*!40000 ALTER TABLE `backend_instrumento` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_instrumento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_miembro`
--

DROP TABLE IF EXISTS `backend_miembro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_miembro` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Beneficiario_id` bigint NOT NULL,
  `Persona_id` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `backend_miembro_Beneficiario_id_efa3b813_fk_backend_b` (`Beneficiario_id`),
  KEY `backend_miembro_Persona_id_1e107dcd_fk_backend_persona_ID` (`Persona_id`),
  CONSTRAINT `backend_miembro_Beneficiario_id_efa3b813_fk_backend_b` FOREIGN KEY (`Beneficiario_id`) REFERENCES `backend_beneficiario` (`ID`),
  CONSTRAINT `backend_miembro_Persona_id_1e107dcd_fk_backend_persona_ID` FOREIGN KEY (`Persona_id`) REFERENCES `backend_persona` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_miembro`
--

LOCK TABLES `backend_miembro` WRITE;
/*!40000 ALTER TABLE `backend_miembro` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_miembro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_persona`
--

DROP TABLE IF EXISTS `backend_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_persona` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(200) NOT NULL,
  `Sexo` varchar(30) NOT NULL,
  `RUT` varchar(12) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_persona`
--

LOCK TABLES `backend_persona` WRITE;
/*!40000 ALTER TABLE `backend_persona` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_postulacion`
--

DROP TABLE IF EXISTS `backend_postulacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_postulacion` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Resultado` varchar(30) NOT NULL,
  `MontoObtenido` int NOT NULL,
  `FechaDePostulacion` date NOT NULL,
  `FechaDeResultado` date NOT NULL,
  `Detalle` varchar(1000) NOT NULL,
  `Beneficiario_id` bigint NOT NULL,
  `Instrumento_id` bigint NOT NULL,
  `Proyecto_id` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `backend_postulacion_Beneficiario_id_33a8b4c0_fk_backend_b` (`Beneficiario_id`),
  KEY `backend_postulacion_Instrumento_id_6de725d9_fk_backend_i` (`Instrumento_id`),
  KEY `backend_postulacion_Proyecto_id_4e2b289e_fk_backend_proyecto_ID` (`Proyecto_id`),
  CONSTRAINT `backend_postulacion_Beneficiario_id_33a8b4c0_fk_backend_b` FOREIGN KEY (`Beneficiario_id`) REFERENCES `backend_beneficiario` (`ID`),
  CONSTRAINT `backend_postulacion_Instrumento_id_6de725d9_fk_backend_i` FOREIGN KEY (`Instrumento_id`) REFERENCES `backend_instrumento` (`ID`),
  CONSTRAINT `backend_postulacion_Proyecto_id_4e2b289e_fk_backend_proyecto_ID` FOREIGN KEY (`Proyecto_id`) REFERENCES `backend_proyecto` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_postulacion`
--

LOCK TABLES `backend_postulacion` WRITE;
/*!40000 ALTER TABLE `backend_postulacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_postulacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_proyecto`
--

DROP TABLE IF EXISTS `backend_proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_proyecto` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Titulo` varchar(300) NOT NULL,
  `Descripcion` varchar(500) NOT NULL,
  `DuracionEnMesesMinimo` int NOT NULL,
  `DuracionEnMesesMaximo` int NOT NULL,
  `Alcance` varchar(30) NOT NULL,
  `Area` varchar(100) NOT NULL,
  `Beneficiario_id` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `backend_proyecto_Beneficiario_id_83f3b5bc_fk_backend_b` (`Beneficiario_id`),
  CONSTRAINT `backend_proyecto_Beneficiario_id_83f3b5bc_fk_backend_b` FOREIGN KEY (`Beneficiario_id`) REFERENCES `backend_beneficiario` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_proyecto`
--

LOCK TABLES `backend_proyecto` WRITE;
/*!40000 ALTER TABLE `backend_proyecto` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_proyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_usuario`
--

DROP TABLE IF EXISTS `backend_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_usuario` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `NombreDeUsuario` varchar(200) NOT NULL,
  `Contrasena` varchar(200) NOT NULL,
  `Correo` varchar(200) NOT NULL,
  `Persona_id` bigint NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `backend_usuario_Persona_id_0d597647_fk_backend_persona_ID` (`Persona_id`),
  CONSTRAINT `backend_usuario_Persona_id_0d597647_fk_backend_persona_ID` FOREIGN KEY (`Persona_id`) REFERENCES `backend_persona` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_usuario`
--

LOCK TABLES `backend_usuario` WRITE;
/*!40000 ALTER TABLE `backend_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'backend','beneficiario'),(15,'backend','colaborador'),(10,'backend','consorcio'),(8,'backend','financiador'),(11,'backend','instrumento'),(12,'backend','miembro'),(9,'backend','persona'),(14,'backend','postulacion'),(13,'backend','proyecto'),(16,'backend','usuario'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'backend','0001_initial','2025-08-23 00:10:05.613999'),(2,'contenttypes','0001_initial','2025-08-23 01:10:56.111745'),(3,'auth','0001_initial','2025-08-23 01:10:56.508519'),(4,'admin','0001_initial','2025-08-23 01:10:56.617344'),(5,'admin','0002_logentry_remove_auto_add','2025-08-23 01:10:56.623358'),(6,'admin','0003_logentry_add_action_flag_choices','2025-08-23 01:10:56.629310'),(7,'contenttypes','0002_remove_content_type_name','2025-08-23 01:10:56.734354'),(8,'auth','0002_alter_permission_name_max_length','2025-08-23 01:10:56.779595'),(9,'auth','0003_alter_user_email_max_length','2025-08-23 01:10:56.799179'),(10,'auth','0004_alter_user_username_opts','2025-08-23 01:10:56.804933'),(11,'auth','0005_alter_user_last_login_null','2025-08-23 01:10:56.852615'),(12,'auth','0006_require_contenttypes_0002','2025-08-23 01:10:56.854277'),(13,'auth','0007_alter_validators_add_error_messages','2025-08-23 01:10:56.860104'),(14,'auth','0008_alter_user_username_max_length','2025-08-23 01:10:56.908789'),(15,'auth','0009_alter_user_last_name_max_length','2025-08-23 01:10:56.955490'),(16,'auth','0010_alter_group_name_max_length','2025-08-23 01:10:56.972781'),(17,'auth','0011_update_proxy_permissions','2025-08-23 01:10:56.987733'),(18,'auth','0012_alter_user_first_name_max_length','2025-08-23 01:10:57.036199'),(19,'backend','0002_alter_beneficiario_regiondecreacion_and_more','2025-08-23 01:10:57.049873'),(20,'sessions','0001_initial','2025-08-23 01:10:57.071526');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-23  2:12:41
