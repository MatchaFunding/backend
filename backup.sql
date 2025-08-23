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
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_beneficiario`
--

LOCK TABLES `backend_beneficiario` WRITE;
/*!40000 ALTER TABLE `backend_beneficiario` DISABLE KEYS */;
INSERT INTO `backend_beneficiario` VALUES (1,'MatchaFunding S.A.','2025-01-01','RM','Av. Vicuña Mackenna 3939','JU','SRL','EMP','12.345.678-9','12.345.678-9'),(2,'AGRICOLA JULIO GIDDINGS E I R L','2025-01-01','RM','N/A','NA','EIRL','EMP','520014225','520014225'),(3,'BEATRIZ EDITH ARAYA ARANCIBIA ASESORIAS EN TECNOLOGIAS DE INFORMACION','2025-01-01','RM','N/A','NA','EIRL','EMP','520015787','520015787'),(4,'SAENS POLIMEROS Y REVESTIMIENTOS LIMITADA','2025-01-01','RM','N/A','NA','EIRL','EMP','520035087','520035087'),(5,'LACTEOS CHAUQUEN SPA','2025-01-01','RM','N/A','NA','EIRL','EMP','520041435','520041435'),(6,'CALEB OTONIEL ARAYA CASTILLO','2025-01-01','RM','N/A','NA','EIRL','EMP','520043462','520043462'),(7,'IQUIQUE TELEVISION PRODUCCIONES TELEVISIVAS Y EVENTOS LIMITADA','2025-01-01','RM','N/A','NA','EIRL','EMP','520046666','520046666'),(8,'ALEJANDRO MARIO CAEROLS SILVA','2025-01-01','RM','N/A','NA','EIRL','EMP','520050310','520050310'),(9,'SOCIEDAD AGRICOLA Y VIVERO SAN RAFAEL LIMITADA','2025-01-01','RM','N/A','NA','EIRL','EMP','533065740','533065740'),(10,'FUNDACION DESAFIO','2025-01-01','RM','N/A','NA','EIRL','EMP','533090079','533090079'),(11,'FUNDACION BASURA','2025-01-01','RM','N/A','NA','EIRL','EMP','533232264-9','533232264-9'),(12,'FRIMA S A','2025-01-01','RM','N/A','NA','EIRL','EMP','590291404','590291404'),(13,'ANGLO AMERICAN TECHNICAL & SUSTAINABILITY SERVICES LTD','2025-01-01','RM','N/A','NA','EIRL','EMP','592803909','592803909'),(14,'LABORELEC LATIN AMERICA','2025-01-01','RM','N/A','NA','EIRL','EMP','592819600','592819600'),(15,'INSTITUTO ANTARTICO CHILENO','2025-01-01','RM','N/A','NA','EIRL','EMP','606050003','606050003'),(16,'INSTITUTO NACIONAL DE ESTADISTICAS','2025-01-01','RM','N/A','NA','EIRL','EMP','607030006','607030006'),(17,'CASA DE MONEDA DE CHILE S.A.','2025-01-01','RM','N/A','NA','EIRL','EMP','608060006','608060006'),(18,'SERVICIO NACIONAL DEL PATRIMONIO CULTURAL','2025-01-01','RM','N/A','NA','EIRL','EMP','609050004','609050004'),(19,'UNIVERSIDAD DE CHILE','2025-01-01','RM','N/A','NA','EIRL','EMP','609100001','609100001'),(20,'UNIVERSIDAD DE SANTIAGO DE CHILE','2025-01-01','RM','N/A','NA','EIRL','EMP','609110007','609110007'),(21,'UNIVERSIDAD DEL BIO BIO','2025-01-01','RM','N/A','NA','EIRL','EMP','609110066','609110066'),(22,'ACADEMIA POLITECNICA MILITAR','2025-01-01','RM','N/A','NA','EIRL','EMP','611010214','611010214'),(23,'INSTITUTO DE FOMENTO PESQUERO','2025-01-01','RM','N/A','NA','EIRL','EMP','613100008','613100008'),(24,'INSTITUTO DE INVESTIGACIONES AGROPECUARIAS','2025-01-01','RM','N/A','NA','EIRL','EMP','613120009','613120009'),(25,'AGUAS ANDINAS S A','2025-01-01','RM','N/A','NA','EIRL','EMP','618080005','618080005'),(26,'CENTRO DEL AGUA PARA ZONAS ARIDAS Y SEMIARIDAS DE AMERICA LATINA','2025-01-01','RM','N/A','NA','EIRL','EMP','619686004','619686004'),(27,'UNIVERSIDAD DE O\'HIGGINS','2025-01-01','RM','N/A','NA','EIRL','EMP','619805305','619805305'),(28,'FUNDACION PATRIMONIO NUESTRO','2025-01-01','RM','N/A','NA','EIRL','EMP','650028449','650028449'),(29,'ASOCIACION GREMIAL DE PRODUCTORES DE OVINOS DE LA NOVENA REGION','2025-01-01','RM','N/A','NA','EIRL','EMP','650030354','650030354'),(30,'FUNDACION SNP PATAGONIA SUR','2025-01-01','RM','N/A','NA','EIRL','EMP','650034244','650034244'),(31,'FUNDACION SENDERO DE CHILE','2025-01-01','RM','N/A','NA','EIRL','EMP','650164067','650164067'),(32,'PEQUENOS Y MEDIANOS INDUSTRIALES MADEREROS DEL BIO BIO A.G.','2025-01-01','RM','N/A','NA','EIRL','EMP','650175484','650175484'),(33,'ASOCIACION GREMIAL DE CANALES REGIONALES DE TELEVISION DE SENAL ABIERTA DE CHILE','2025-01-01','RM','N/A','NA','EIRL','EMP','650181492','650181492'),(34,'FEDERACION DE EMPRESAS DE TURISMO DE CHILE - FEDERACION GREMIAL','2025-01-01','RM','N/A','NA','EIRL','EMP','650195086','650195086'),(35,'FUNDACION URBANISMO SOCIAL','2025-01-01','RM','N/A','NA','EIRL','EMP','650222784','650222784'),(36,'ASOC CHILENA DE ORGANIZACIONES DE FERIAS LIBRES ASOF A G','2025-01-01','RM','N/A','NA','EIRL','EMP','650245601','650245601'),(37,'FUNDACION BANIGUALDAD','2025-01-01','RM','N/A','NA','EIRL','EMP','650251504','650251504'),(38,'ASOCIACION GREMIAL CHILENA DE DESARROLLADORES DE VIDEOJUEGOS','2025-01-01','RM','N/A','NA','EIRL','EMP','650276531','650276531'),(39,'VISION VALDIVIA,CAPITAL NAUTICA DEL PACIFICO SUR-ASOCIACION GREMIAL','2025-01-01','RM','N/A','NA','EIRL','EMP','650290771','650290771'),(40,'AGENCIA CHILENA DE EFICIENCIA ENERGETICA','2025-01-01','RM','N/A','NA','EIRL','EMP','650308484','650308484'),(41,'FUNDACION SERVICIO JESUITA A MIGRANTES','2025-01-01','RM','N/A','NA','EIRL','EMP','650308921','650308921'),(42,'FUND JUVENTUD EMPRENDEDORA','2025-01-01','RM','N/A','NA','EIRL','EMP','650324900','650324900'),(43,'FUNDACION FRAUNHOFER CHILE RESEARCH','2025-01-01','RM','N/A','NA','EIRL','EMP','650331923','650331923'),(44,'ORGANIZACION NO GUBERNAMENTAL DE DESARROLLO CORPORACION DE DESARROLLO PHOENIX BR','2025-01-01','RM','N/A','NA','EIRL','EMP','650345738','650345738'),(45,'SOCIEDAD GEOGRAFICA DE DOCUMENTACION ANDINA','2025-01-01','RM','N/A','NA','EIRL','EMP','650348397','650348397'),(46,'AGENCIA REGIONAL DE DESARROLLO PRODUCTIVO DE LA ARAUCANIA','2025-01-01','RM','N/A','NA','EIRL','EMP','650348915','650348915'),(47,'ASOCIACION DE ARQUITECTOS Y PROFESIONALES POR EL PATRIMONIO DE VALPARAISO PLAN','2025-01-01','RM','N/A','NA','EIRL','EMP','650410394','650410394'),(48,'FUNDACION GANAMOS TODOS','2025-01-01','RM','N/A','NA','EIRL','EMP','650421396','650421396'),(49,'CORPORACION REGIONAL DE DESARROLLO DE LA REGION DE TARAPACA','2025-01-01','RM','N/A','NA','EIRL','EMP','650429044','650429044'),(50,'ASOCIACION GREMIAL DE EMPRENDEDORES EN CHILE A.G','2025-01-01','RM','N/A','NA','EIRL','EMP','650462130','650462130'),(51,'ORGANIZ¬N NO GUBERNAMENTAL DE DESARROLLO LA RUTA SOLAR EN LIQUIDACIóN','2025-01-01','RM','N/A','NA','EIRL','EMP','650505573','650505573'),(52,'FUNDACION IMPULSORA DE UN NUEVO SECTOR EN LA ECONOMIA SISTEMA B','2025-01-01','RM','N/A','NA','EIRL','EMP','650521935','650521935'),(53,'ASOCIACION NACIONAL DE EMPRESAS ESCOS','2025-01-01','RM','N/A','NA','EIRL','EMP','650531965','650531965'),(54,'CENTRO DE INVESTIGACION DE POLIMEROS AVANZADOS','2025-01-01','RM','N/A','NA','EIRL','EMP','650534875','650534875'),(55,'CONSEJO DE INST. PROFESIONALES Y CENTROS DE FORMACION TECNICA ACRED. A.G','2025-01-01','RM','N/A','NA','EIRL','EMP','650544846','650544846'),(56,'PROPIETARIOS E INDUSTRIALES FORESTALES','2025-01-01','RM','N/A','NA','EIRL','EMP','650545095','650545095'),(57,'FUNDACION INRIA CHILE','2025-01-01','RM','N/A','NA','EIRL','EMP','650580443','650580443'),(58,'ASOCIACION DE MUNICIPALIDADES PARQUE CORDILLERA','2025-01-01','RM','N/A','NA','EIRL','EMP','650604849','650604849'),(59,'FUNDACION DE BENEFICENCIA RECYCLAPOLIS','2025-01-01','RM','N/A','NA','EIRL','EMP','650604865','650604865'),(60,'FUND CIENTIFICA Y CULTURAL BIOCIENCIA','2025-01-01','RM','N/A','NA','EIRL','EMP','650612108','650612108'),(61,'CORPORACION PARA EL DESARROLLO DE MALLECO','2025-01-01','RM','N/A','NA','EIRL','EMP','650623460','650623460'),(62,'CORPORACION CULTURAL ACONCAGUA SUMMIT','2025-01-01','RM','N/A','NA','EIRL','EMP','650646665','650646665'),(63,'CORPORACION MUNICIPAL DE LA CULTURA Y LAS ARTES DE SAN ANTONIO','2025-01-01','RM','N/A','NA','EIRL','EMP','650654935','650654935'),(64,'AGRUPACION ACERCA REDES MARIQUINA','2025-01-01','RM','N/A','NA','EIRL','EMP','650661257','650661257'),(65,'ASOCIACION GREMIAL DE RENOVADORES Y RECAUCHADORES DE NEUMATICOS DE CHILE','2025-01-01','RM','N/A','NA','EIRL','EMP','650665791','650665791'),(66,'ASOCIACION INDIGENA AYMARA SUMA JUIRA DE CARIQUIMA','2025-01-01','RM','N/A','NA','EIRL','EMP','650694422','650694422'),(67,'FUNDACION DEPORTE LIBRE','2025-01-01','RM','N/A','NA','EIRL','EMP','650707044','650707044'),(68,'FUNDACION PARA EL TRABAJO UNIVERSIDAD ARTURO PRAT','2025-01-01','RM','N/A','NA','EIRL','EMP','650718593','650718593'),(69,'CENTRO REGIONAL DE ESTUDIOS EN ALIMENTOS SALUDABLES','2025-01-01','RM','N/A','NA','EIRL','EMP','650725166','650725166'),(70,'FUNDACION PARA EL DESARROLLO SUSTENTABLE DE FRUTILLAR','2025-01-01','RM','N/A','NA','EIRL','EMP','650742575','650742575'),(71,'FUNDACION CSIRO-CHILE RESEARCH','2025-01-01','RM','N/A','NA','EIRL','EMP','650756444','650756444'),(72,'CORPORACION YO TAMBIEN','2025-01-01','RM','N/A','NA','EIRL','EMP','650766989','650766989'),(73,'CORPORACION MUNICIPAL DE TURISMO VICUNA','2025-01-01','RM','N/A','NA','EIRL','EMP','650802845','650802845'),(74,'FUNDACION LEITAT CHILE','2025-01-01','RM','N/A','NA','EIRL','EMP','650812832','650812832'),(75,'LO BARNECHEA EMPRENDE','2025-01-01','RM','N/A','NA','EIRL','EMP','650816412','650816412'),(76,'CORPORACION CONSTRUYENDO MIS SUENOS','2025-01-01','RM','N/A','NA','EIRL','EMP','650879465','650879465'),(77,'FUNDACION PARQUE CIENTIFICO TECNOLOGICO DE LA REGION DE ANTOFAGASTA','2025-01-01','RM','N/A','NA','EIRL','EMP','650881222','650881222'),(78,'COOPERATIVA PESQUERA Y COMERCIALIZADORA CALETA SAN PEDRO','2025-01-01','RM','N/A','NA','EIRL','EMP','650886666','650886666'),(79,'COOPERATIVA M-31 DE TONGOY','2025-01-01','RM','N/A','NA','EIRL','EMP','650899466','650899466'),(80,'COOPERATIVA DE TRABAJO PARA EL DESARROLLO LOCAL Y LA ECONOMÍA SOLIDARIA','2025-01-01','RM','N/A','NA','EIRL','EMP','650910567','650910567'),(81,'CORP. REG.. AYSEN DE INV. Y DES. COOPER. CENTRO DE INV.EN ECOSIST.DE LA PATAGONI','2025-01-01','RM','N/A','NA','EIRL','EMP','650911466','650911466'),(82,'FUNDACION CENTRO DE ESTUDIOS DE MONTANA','2025-01-01','RM','N/A','NA','EIRL','EMP','650922875','650922875'),(83,'FUNDACION LABORATORIO CAMBIO SOCIAL','2025-01-01','RM','N/A','NA','EIRL','EMP','650923537','650923537'),(84,'FUNDACION TANTI','2025-01-01','RM','N/A','NA','EIRL','EMP','650941675','650941675'),(85,'ASOCIACION CHILENA DE BIOMASA A.G','2025-01-01','RM','N/A','NA','EIRL','EMP','650945573','650945573'),(86,'COOPERATIVA DE TRASHUMANTES DE ILLAPEL','2025-01-01','RM','N/A','NA','EIRL','EMP','650946324','650946324'),(87,'FUNDACION INSTITUTO DE INVESTIGACION AUSTRAL','2025-01-01','RM','N/A','NA','EIRL','EMP','650983033','650983033'),(88,'FUNDACION LEGADO CHILE','2025-01-01','RM','N/A','NA','EIRL','EMP','650983084','650983084'),(89,'FUNDACION PARA LA INCLUSION TECNOLOGICA KODEA','2025-01-01','RM','N/A','NA','EIRL','EMP','651020190','651020190'),(90,'ASOC NACIONAL DE SOMMELIERS DE CHILE A G','2025-01-01','RM','N/A','NA','EIRL','EMP','651031702','651031702'),(91,'CORPORACION CONSORCIO LECHERO','2025-01-01','RM','N/A','NA','EIRL','EMP','651040825','651040825'),(92,'FUNDACION UC DAVIS CHILE LIFE SCIENCES INNOVATION CENTER','2025-01-01','RM','N/A','NA','EIRL','EMP','651080746','651080746'),(93,'FUNDACION HUELLA LOCAL','2025-01-01','RM','N/A','NA','EIRL','EMP','651134099','651134099'),(94,'CORPORACION CHILENA DE INVESTIGACION DEL AGUA','2025-01-01','RM','N/A','NA','EIRL','EMP','651137322','651137322'),(95,'FUNDACION COCINAMAR','2025-01-01','RM','N/A','NA','EIRL','EMP','651161851','651161851'),(96,'ORGANIZACION NO GUBERNAMENTAL DE DESARROLLO VIVIENDA LOCAL','2025-01-01','RM','N/A','NA','EIRL','EMP','651170745','651170745'),(97,'FUNDACION CHILWE CULTURA MEDIOAMBIENTAL Y COMUNIDAD','2025-01-01','RM','N/A','NA','EIRL','EMP','651214475','651214475'),(98,'ASOCIACION DE EXPORTADORES DE CARNE A.G','2025-01-01','RM','N/A','NA','EIRL','EMP','651215366','651215366'),(99,'FUNDACION EN LOS OJOS DE MI MADRE','2025-01-01','RM','N/A','NA','EIRL','EMP','651228115','651228115'),(100,'FUND LUXEMBURGO','2025-01-01','RM','N/A','NA','EIRL','EMP','651236908','651236908'),(101,'COOPERATIVA AGRICOLA AGROPECUARIOS CANELA LIMITADA','2025-01-01','RM','N/A','NA','EIRL','EMP','651252520','651252520'),(102,'ORGANIZACION NO GUBERNAMENTAL DE DESARROLLO MUSEO CAMPESINO EN MOVTO U ONG MUCAM','2025-01-01','RM','N/A','NA','EIRL','EMP','651254558-9','651254558-9'),(103,'COOPERATIVA DE RECICLAJE Y VALORIZACION DE RESIDUOS AGROINDUSTRIALES Y COMUNITAR','2025-01-01','RM','N/A','NA','EIRL','EMP','651344883','651344883'),(104,'ASOCIACION CLUB EXPERIENSATIVA','2025-01-01','RM','N/A','NA','EIRL','EMP','651424038','651424038'),(105,'COOPERATIVA AGRICOLA Y CAMPESINA LA COMPAñIA LIMITADA','2025-01-01','RM','N/A','NA','EIRL','EMP','651457122','651457122'),(106,'FUNDACION FOCUS','2025-01-01','RM','N/A','NA','EIRL','EMP','651515874','651515874'),(107,'FUNDACION MEJOR CIUDADANO','2025-01-01','RM','N/A','NA','EIRL','EMP','651529514','651529514'),(108,'ASOCIACION GREMIAL DE EMPRESAS DE TECNOLOGIA PARA LA INDUSTRIA MUSICAL (MUSTACH)','2025-01-01','RM','N/A','NA','EIRL','EMP','651605474','651605474');
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
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_proyecto`
--

LOCK TABLES `backend_proyecto` WRITE;
/*!40000 ALTER TABLE `backend_proyecto` DISABLE KEYS */;
INSERT INTO `backend_proyecto` VALUES (1,'Cultivo de Trigo','Cultivo de Trigo',6,12,'RM','Agricultura',2),(2,'Cultivos Forrajeros En Praderas Mejoradas o Sembradas, Cultivos Suplementarios Forrajeros','Cultivos Forrajeros En Praderas Mejoradas o Sembradas, Cultivos Suplementarios Forrajeros',6,12,'RM','Agricultura',2),(3,'Cultivo de Frutos Oleaginosos (incluye El Cultivo de Aceitunas)','Cultivo de Frutos Oleaginosos (incluye El Cultivo de Aceitunas)',6,12,'RM','Agricultura',2),(4,'ALQUILER DE Bienes Inmuebles Amoblados o con Equipos y Maquinarias','Alquiler de Bienes Inmuebles Amoblados o con Equipos y Maquinarias',6,12,'RM','Otras Actividades de Servicios de Apoyo A Las Empresas',3),(5,'COMPAÑA, VENTA Y ALQUILER (excepto Amoblados) de Inmuebles','Compra, Venta y Alquiler (excepto Amoblados) de Inmuebles',6,12,'RM','Otras Actividades de Servicios de Apoyo A Las Empresas',3),(6,'OTRAS ACTIVIDADES DE SERVICIOS PERSONALES N.C.P.','Otras Actividades de Servicios Personales N.C.P.',6,12,'RM','Otras Actividades de Servicios de Apoyo A Las Empresas',3),(7,'Construccion de Otras Obras de Ingenieria Civil','Construccion de Otras Obras de Ingenieria Civil',6,12,'RM','Ingenieria Civil',4),(8,'ELABORACION DE PRODUCTOS LACTEOS','Elaboracion de Productos Lacteos',6,12,'RM','Lacteos',5),(9,'Fabricacion de Otros Productos Elaborados de Metal','Fabricacion de otros productos elaborados de metal',6,12,'RM','259900',6),(10,'TPTV','Produccion y emision de programas televisivos',6,12,'RM','Medios de Comunicacion',7),(11,'Vino y Aguas Minerales','Elaboracion de Vinos, Produccion de Aguas Minerales y Otras Aguas Embotelladas',6,12,'RM','Agricultura',8),(12,'Cultivo de Plantas Vivas Incluida La Produccion En Viveros (excepto Viveros Forestales)','Actividad relacionada con la producción de plantas vivas en viveros',6,12,'RM','Agricultura',9),(13,'Desafio','Actividades culturales y recreativas',6,12,'RM','Cultura y Recreación',10),(14,'Asistencia Social','Actividades de asistencia social sin alojamiento',6,12,'RM','Asociaciones N.C.P.',11),(15,'Cria de Ganado Bovino','Cria de ganado bovino para la producción de carne o como ganado reproductor',6,12,'RM','Agricultura',12),(16,'Explotación de Mataderos','Explotación de mataderos de bovinos, ovinos, equinos, caprinos, porcinos y camelidos',6,12,'RM','Agricultura',12),(17,'Transporte de Carga','Transporte de carga por carretera',6,12,'RM','Logística',12),(18,'Procesamiento de Datos','Procesamiento de datos, hospedaje y actividades conexas',6,12,'RM','Tecnología',12),(19,'Otras Actividades de Servicio','Otras actividades de servicio a las empresas N.C.P.',6,12,'RM','Servicios',12),(20,'Sustainability Consulting','Provee servicios de consultor©a en sostenibilidad y reducción del impacto ambiental.',6,12,'RM','Empresas de Servicios de Ingenieria y Actividades Conexas de Consultoria Tecnica',13),(21,'LABRETECH','Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria',6,12,'RM','Ciencias Naturales y La Ingenieria',14),(22,'Admin. Pub.','Actividades de la Admin. Pub. en Gen.',6,12,'RM','Admin. Pub.',15),(23,'Admin. Pub.','Actividades de La Administracion Publica En General',6,12,'RM','Org. Admin. Pub.',16),(24,'IMPRESION','Actividades de impresion N.C.P.',6,12,'RM','Impresion y Fabricacion',17),(25,'ANALISIS Y CONSERVACION DE BIBLIOTECAS Y ARCHIVOS','Realizar un analisis y conservacion de las bibliotecas y archivos del Servicio Nacional del Patrimonio Cultural',6,12,'RM','Actividades de Bibliotecas y Archivos',18),(26,'Educación Superior','Actividades de enseñanza superior en universidades públicas',6,12,'RM','Educación',19),(27,'Educación Superior','Actividades de enseñanza superior en universidades públicas',6,12,'RM','Educación',20),(28,'ENSENANZA SUPERIOR EN UNIVERSIDADES PUBLICAS','Actividades de apoyo a la enseñanza en universidades públicas',6,12,'RM','Educación',21),(29,'Defensa','Actividades de Defensa',6,12,'RM','842200',22),(30,'Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Sociales y Las Humanidades','...',6,12,'RM','Ciencias Sociales y Humanidades',23),(31,'Cultivo de Especias','Actividades relacionadas con el cultivo de especias',6,12,'RM','Agricultura',24),(32,'Actividades de Apoyo A La Agricultura','Actividades que apoyan la agricultura',6,12,'RM','Agricultura',24),(33,'Investigaciones y Desarrollo Experimental En El Campo De Las Ciencias Sociales Y Las Humanidades','Investigaciones y desarrollo experimental en ciencias sociales y humanidades',6,12,'RM','Ciencias Sociales y Humanidades',24),(34,'CAPTACION Y DISTRIBUCION DE AGUA','Captacion, Tratamiento y Distribucion de Agua',6,12,'RM','Agua',25),(35,'Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria','Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria',6,12,'RM','Ciencia y Tecnología',26),(36,'Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Sociales y Las Humanidades','Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Sociales y Las Humanidades',6,12,'RM','Humanidades',26),(37,'Otras Actividades de Servicios Personales N.C.P.','Otras Actividades de Servicios Personales N.C.P.',6,12,'RM','Servicios',26),(38,'Educación Superior','Enseñanza Superior En Universidades Publicas',6,12,'RM','Org. Educacion Superior',27),(39,'949909 - Actividades de Otras Asociaciones N.C.P.','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Org. Sin Fines de Lucro 813 - Fundacion',28),(40,'Consultoria de Gestion','Actividades de Consultoria de Gestion',6,12,'RM','Agropecuario',29),(41,'Cultivo de Hortalizas y Melones','Cultivo de hortalizas y melones en Patagonia Sur',6,12,'RM','Agricultura',30),(42,'Venta Al Por Menor de Telas, Lanas, Hilos y Similares En Comercios Especializados','Venta al por menor de telas, lanas, hilos y similares en comercios especializados',6,12,'RM','Comercio',30),(43,'Venta Al Por Menor de Prendas y Accesorios de Vestir En Comercios Especializados','Venta al por menor de prendas y accesorios de vestir en comercios especializados',6,12,'RM','Comercio',30),(44,'Venta Al Por Menor de Recuerdos, Artesanias y Articulos Religiosos En Comercios Especializados','Venta al por menor de recuerdos, artesanías y artículos religiosos en comercios especializados',6,12,'RM','Comercio',30),(45,'Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria','Investigaciones y desarrollo experimental en el campo de las ciencias naturales y la ingeniería',6,12,'RM','Investigación',30),(46,'Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Sociales y Las Humanidades','Investigaciones y desarrollo experimental en el campo de las ciencias sociales y las humanidades',6,12,'RM','Investigación',30),(47,'Fundaciones y Corporaciones, Asociaciones Que Promueven Actividades Culturales o Recreativas','Fundaciones y corporaciones, asociaciones que promueven actividades culturales o recreativas',6,12,'RM','Cultura',30),(48,'Consultoria de Gestión','Actividades de Consultoria de Gestion',6,12,'RM','Gestión',31),(49,'Investigación','Actividades de Investigacion (incluye Actividades de Investigadores y Detectives Privados)',6,12,'RM','Investigación',31),(50,'A.G.','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Org.',32),(51,'ACTIVIDADES DE TELECOMUNICACIONES','Otras Actividades de Telecomunicaciones N.C.P.',6,12,'RM','Actividades de Sindicatos',33),(52,'Fundaciones y Corporaciones','Promoción de actividades culturales o recreativas',6,12,'RM','Actividades Culturales',34),(53,'Actividades de Otras Asociaciones N.C.P.','Actividades sin categorización específica',6,12,'RM','Otras Actividades',34),(54,'CSG','Actividades de Consultoria de Gestion',6,12,'RM','Asistencia Social',35),(55,'Proyecto ASOC CHILENA DE ORGA','Proyecto basado en actividades: 949909 - Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Desarrollo',36),(56,'BaniGualdad','Promoción de la igualdad y el desarrollo social',6,12,'RM','Desarrollo Social',37),(57,'Desarrollo de Videojuegos','Actividades de Asociaciones Empresariales y de Empleadores',6,12,'RM','Actividades de Asociaciones Empresariales y de Empleadores',38),(58,'949909 - Actividades de Otras Asociaciones N.C.P.','',6,12,'RM','',39),(59,'Consultoria de Gestion','Actividades de Consultoria de Gestion',6,12,'RM','Gestion',40),(60,'Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria','Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria',6,12,'RM','Ciencia',40),(61,'Otras Actividades Profesionales, Cientificas y Tecnicas N.C.P.','Otras Actividades Profesionales, Cientificas y Tecnicas N.C.P.',6,12,'RM','Profesional',40),(62,'Servicios Personales de Educacion','Servicios Personales de Educacion',6,12,'RM','Educacion',40),(63,'Servicio a migrantes','Promoción de actividades culturales y recreativas para migrantes',6,12,'RM','Actividades Culturales',41),(64,'JUVENTUD EMPRENDEDORA','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Otros Tipos de Enseñanza N.C.P.',42),(65,'Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria','Actividades culturales o recreativas',6,12,'RM','Ciencias Naturales y la Ingenieria',43),(66,'Fundaciones y Corporaciones, Asociaciones Que Promueven Actividades Culturales o Recreativas','',6,12,'RM','',43),(67,'Recuperacion y Reciclamiento de Desperdicios y Desechos Metalicos','Recuperacion y Reciclamiento de Desperdicios y Desechos Metalicos',6,12,'RM','Ambiente',44),(68,'Recuperacion y Reciclamiento de Papel','Recuperacion y Reciclamiento de Papel',6,12,'RM','Medio Ambiente',44),(69,'Recuperacion y Reciclamiento de Otros Desperdicios y Desechos N.C.P.','Recuperacion y Reciclamiento de Otros Desperdicios y Desechos N.C.P.',6,12,'RM','Ambiente',44),(70,'Actividades de Otras Asociaciones N.C.P.','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Economia',44),(71,'VTA','Venta Al Por Menor de Libros En Comercios Especializados',6,12,'RM','Educación',45),(72,'VTB','Venta Al Por Menor Por Correo, Por Internet y Via Telefonica',6,12,'RM','Comunicaciones',45),(73,'VTE','Edicion de Libros',6,12,'RM','Cultura',45),(74,'VTN','Otras Actividades de Servicios de Apoyo A Las Empresas N.C.P.',6,12,'RM','Servicios',45),(75,'Consultoria Gestion','Actividades de Consultoria de Gestion',6,12,'RM','Desarrollo Productivo',46),(76,'Actividades de Agencias de Viajes','Actividades de Agencias de Viajes',6,12,'RM','Agencias de Viajes',47),(77,'FGT','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Actividades Culturales o Recreativas',48),(78,'Cultura y Artes','Actividades culturales, eventos y espectaculos',6,12,'RM','Cultura y Artes',49),(79,'Servicios de Publicidad','Servicios de publicidad prestados por empresas',6,12,'RM','Publicidad',50),(80,'Actividades de Otras Asociaciones N.C.P.','Actividades de otras asociaciones n.c.p.',6,12,'RM','Asociaciones',50),(81,'Servicios de Publicidad','Prestación de servicios de publicidad a empresas',6,12,'RM','Publicidad y Marketing',51),(82,'Venta Al Por Menor de Libros En Comercios Especializados','Actividades de venta de libros en comercios especializados',6,12,'RM','Educación',52),(83,'Actividades de Otras Asociaciones N.C.P.','Actividades de otras asociaciones sin fines de lucro',6,12,'RM','Comunidad',52),(84,'Consultoria de Gestion','Actividades de Consultoria de Gestion',6,12,'RM','Gestion',53),(85,'CIPA','Recuperacion y Reciclamiento de Otros Desperdicios y Desechos N.C.P.',6,12,'RM','Ambiente',54),(86,'CIPA','Actividades de Consultoria de Gestion',6,12,'RM','Gestion',54),(87,'CIPA','Otros Servicios de Ensayos y Analisis Tecnicos (excepto Actividades de Plantas de Revision Tecnica)',6,12,'RM','Investigacion',54),(88,'CIPA','Fundaciones y Corporaciones, Asociaciones Que Promueven Actividades Culturales o Recreativas',6,12,'RM','Sociedad Civil',54),(89,'Asociaciones Empresariales y Empleadores','Actividades de Asociaciones Empresariales y de Empleadores',6,12,'RM','Asociaciones Empresariales y Empleadores',55),(90,'Proyecto PROPIETARIOS E INDUS','Proyecto basado en actividades: 702000 - Actividades de Consultoria de Gestion',6,12,'RM','Desarrollo',56),(91,'I+D en Ciencias Naturales e Ingenieria','Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria',6,12,'RM','Ciencias Naturales e Ingenieria',57),(92,'Forestación y Silvicultura','Servicios de forestación a cambio de una retribución o por contrata',6,12,'RM','Silvicultura',58),(93,'Servicios de Publicidad','Servicios de publicidad prestados por empresas',6,12,'RM','Cultura y Recreación',59),(94,'Fundaciones y Corporaciones','Promoción de actividades culturales y recreativas',6,12,'RM','Cultura y Recreación',59),(95,'Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria','Actividades de Investigacion (incluye Actividades de Investigadores y Detectives Privados) Otras Actividades de Servicios de Apoyo A Las Empresas N.C.P.',6,12,'RM','Ciencias Naturales y Ingenieria',60),(96,'949909','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Actividades de Otras Asociaciones N.C.P.',61),(97,'Otras Actividades Especializadas de Diseño N.C.P.','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Diseño y Creación',62),(98,'Fundaciones y Corporaciones','Promueven Actividades Culturales o Recreativas',6,12,'RM','Actividades Culturales',63),(99,'ASER','Asesoria y Gestion En La Compra o Venta de Pequeñas y Medianas Empresas',6,12,'RM','Empresariales',64),(100,'Consultoria de Gestón','Actividades de Consultoria de Gestion',6,12,'RM','Gestión y Consultoría',65),(101,'EAPC','Elaboracion de Otros Productos Alimenticios N.C.P.',6,12,'RM','Actividades Indigenas',66),(102,'DEPORTE LIBRE','Enseñanza Deportiva y Recreativa, Otros Tipos de Enseñanza N.C.P., Otras Actividades Deportivas N.C.P.',6,12,'RM','Actividades Culturales o Recreativas',67),(103,'Consultoria de Gestion','Actividades de Consultoria de Gestion',6,12,'RM','Gestion',68),(104,'Enseñanza Primaria, Secundaria Cientifico Humanista y Tecnico Profesional Privada','Enseñanza Primaria, Secundaria Cientifico Humanista y Tecnico Profesional Privada',6,12,'RM','Educacion',68),(105,'Enseñanza Superior En Centros de Formacion Tecnica','Enseñanza Superior En Centros de Formacion Tecnica',6,12,'RM','Educacion',68),(106,'CSEAS','Actividades de consultoria tecnica y otros servicios de ensayos y análisis técnicos',6,12,'RM','Ciencias Naturales y La Ingenieria',69),(107,'Desarrollo Sostenible','Actividades de consultoria de gestión y asociaciones profesionales',6,12,'RM','Desarrollo Social',70),(108,'Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria','Actividades de investigación en ciencias naturales e ingeniería',6,12,'RM','Ciencias Naturales e Ingeniería',71),(109,'990000','Actividades de Organizaciones y Organos Extraterritoriales',6,12,'RM','Org. Sin Fines de Lucro',72),(110,'Regulacion de Las Actividades de Organismos Que Prestan Servicios Sanitarios, Educativos, Culturales','Regulacion de las actividades de organismos que prestan servicios sanitarios, educativos, culturales',6,12,'RM','Sanidad',73),(111,'Otras Actividades de Esparcimiento y Recreativas N.C.P.','Otras actividades de esparcimiento y recreativas',6,12,'RM','Recreación',73),(112,'Fundaciones y Corporaciones, Asociaciones Que Promueven Actividades Culturales o Recreativas','Fundaciones y corporaciones, asociaciones que promueven actividades culturales o recreativas',6,12,'RM','Cultura',73),(113,'AOC N.C.P.','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Asociaciones',74),(114,'Consultoria Gestion','Actividades de Consultoria de Gestion',6,12,'RM','Gestion',75),(115,'Asociaciones N.C.P.','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Asociaciones',75),(116,'Construyendo Sueños','Actividades de Consultoria de Gestion y Investigacion',6,12,'RM','Desarrollo Sostenible',76),(117,'ACTIVIDAD 1','Alquiler de Bienes Inmuebles Amoblados o con Equipos y Maquinarias',6,12,'RM','Empresas de Asesoria y Consultoria En Inversion Financiera',77),(118,'EPECS','Elaboracion y Conservacion de Salmonidos',6,12,'RM','Pesca',78),(119,'VAPM','Venta Al Por Mayor de Productos Del Mar (pescados, Mariscos y Algas)',6,12,'RM','Comercio',78),(120,'VPMEC','Venta Al Por Menor En Comercios Especializados de Pescado, Mariscos y Productos Conexos',6,12,'RM','Comercio',78),(121,'ACUICULTURA MARINA','Servicios relacionados con la acuicultura marina',6,12,'RM','Acuicultura Marina',79),(122,'Desarrollo Local','Actividades de apoyo a la agricultura y otras actividades relacionadas',6,12,'RM','Economía Solidaria',80),(123,'Actividades de Otras Asociaciones N.C.P.','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Actividades de Otras Asociaciones N.C.P.',81),(124,'Consultoria de Gestion','Actividades de Consultoria de Gestion',6,12,'RM','Gestion',82),(125,'Enseñanza Deportiva y Recreativa','Enseñanza Deportiva y Recreativa',6,12,'RM','Deporte',82),(126,'Fundaciones y Corporaciones, Asociaciones Que Promueven Actividades Culturales o Recreativas','Fundaciones y Corporaciones, Asociaciones Que Promueven Actividades Culturales o Recreativas',6,12,'RM','Cultura',82),(127,'ASOCIACIONES N.C.P.','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','949909',83),(128,'FUNDACION TANTI','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Actividades Culturales o Recreativas',84),(129,'Asesoria y Gestion En La Compra o Venta de Pequeñas y Medianas Empresas','Actividades relacionadas con la asesor¡a y gestión en la compra o venta de pequeñas y medianas empresas',6,12,'RM','749001',85),(130,'Elaboracion de Productos Lacteos','Produccion de productos lacteos para la venta al por mayor',6,12,'RM','Agricultura',86),(131,'Venta Al Por Mayor de Animales Vivos','Comercio de animales vivos para la venta al por mayor',6,12,'RM','Comercio',86),(132,'Venta Al Por Menor de Alimento y Accesorios para Mascotas En Comercios Especializados','Comercio de alimentos y accesorios para mascotas en comercios especializados',6,12,'RM','Servicios',86),(133,'Transporte de Carga Por Carretera','Transporte de carga por carretera',6,12,'RM','Logistica',86),(134,'IIA','Actividades de Consultoria de Gestion, Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria',6,12,'RM','Ciencias Naturales y La Ingenieria',87),(135,'Otras Enseñanzas','Ensayos y Analisis Tecnicos (excepto Actividades de Plantas de Revision Tecnica)',6,12,'RM','Educación',88),(136,'Servicios de Publicidad','Servicios de publicidad prestados por empresas',6,12,'RM','Organización de Convenciones y Exposiciones Comerciales',89),(137,'Organizaciones de Convenciones','Organización de convenciones y exposiciones comerciales',6,12,'RM','Actividades de Otras Asociaciones N.C.P.',89),(138,'Enseñanza','Otros tipos de enseñanza N.C.P.',6,12,'RM','Actividades de Otras Asociaciones N.C.P.',89),(139,'ASOC NACIONAL DE SOMMELIERS DE CHILE A G','Otras Actividades de Servicio a Las Empresas N.C.P.',6,12,'RM','Organizaciones sin fines de lucro',90),(140,'I&D en Ciencias Naturales y Ingenieria','Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria',6,12,'RM','Ciencias Naturales',91),(141,'I+D en Ciencias Naturales e Ingenieria','Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria',6,12,'RM','Ciencias Naturales e Ingenieria',92),(142,'Enseñanza N.C.P.','Otros Tipos de Enseñanza N.C.P.',6,12,'RM','Educación',92),(143,'Fundaciones y Corporaciones','Fundaciones y Corporaciones, Asociaciones Que Promueven Actividades Culturales o Recreativas',6,12,'RM','Sociedad Civil',92),(144,'Huellas en el Paisaje','Construccion de Proyectos de Servicio Publico',6,12,'RM','Servicios Públicos',93),(145,'CIADEIA','Actividades de Consultoria de Gestion y Actividades de Investigacion (incluye Actividades de Investigadores y Detectives Privados)',6,12,'RM','Agua',94),(146,'OTROS TIPOS DE ENSEÑANZA N.C.P.','Actividades de enseñanza',6,12,'RM','Educación',95),(147,'SVI','Servicios de Arquitectura (diseño de Edificios, Dibujo de Planos de Construccion, Entre Otros)',6,12,'RM','Actividades',96),(148,'ACTIVIDADES DE OTRAS ASOCIACIONES N.C.P.','Actividades de Otras Asociaciones N.C.P.',6,12,'RM','Actividades de Otras Asociaciones N.C.P.',97),(149,'Exportadores de Carnes','Promoción y apoyo a la exportación de carnes',6,12,'RM','Actividades de Otras Asociaciones N.C.P.',98),(150,'ENSEÑANZA N.C.P.','Otros Tipos de Enseñanza',6,12,'RM','Actividades Culturales o Recreativas',99),(151,'Educativo','Actividades de Atencion En Instituciones para Personas de Edad y Personas con Discapacidad Fisica',6,12,'RM','Educación',100),(152,'Canales de Agropecuario','Explotación mixta de animales y cultivo de productos agrícolas',6,12,'RM','Agropecuario',101),(153,'MUCAM','Actividades de Consultoria de Gestion, Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Naturales y La Ingenieria, Investigaciones y Desarrollo Experimental En El Campo de Las Ciencias Sociales y Las Humanidades',6,12,'RM','Desarrollo de proyectos',102),(154,'Recogida y Valorización de Residuos Agroindustriales','Actividades de apoyo a la agricultura',6,12,'RM','Agricultura',103),(155,'Venta Al Por Menor de Flores, Plantas, Arboles, Semillas y Abonos En Comercios Especializados','Venta al por menor de productos relacionados con la salud humana',6,12,'RM','Atención a la Salud',104),(156,'Otros Servicios de Atencion de La Salud Humana Prestados Por Empresas','Servicios de atención médica en empresas',6,12,'RM','Atención a la Salud',104),(157,'Fundaciones y Corporaciones, Asociaciones Que Promueven Actividades Culturales o Recreativas','Promoción de actividades culturales y recreativas',6,12,'RM','Actividades Culturales',104),(158,'VTA','Venta Al Por Mayor de Materias Primas Agricolas',6,12,'RM','Agricultura',105),(159,'Consultoria Gestion','Actividades de Consultoria de Gestion',6,12,'RM','Org. Sin Fines de Lucro',106),(160,'Fundaciones y Corporaciones','Actividades de Fundaciones y Corporaciones',6,12,'RM','Actividades Culturales o Recreativas',107),(161,'PDTI','Procesamiento de Datos, Hospedaje y Actividades Conexas',6,12,'RM','631100',108);
/*!40000 ALTER TABLE `backend_proyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_ubicacion`
--

DROP TABLE IF EXISTS `backend_ubicacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backend_ubicacion` (
  `ID` bigint NOT NULL AUTO_INCREMENT,
  `Region` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Capital` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Calle` varchar(300) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Numero` int NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_ubicacion`
--

LOCK TABLES `backend_ubicacion` WRITE;
/*!40000 ALTER TABLE `backend_ubicacion` DISABLE KEYS */;
INSERT INTO `backend_ubicacion` VALUES (1,'RM','Santiago','Av. Libertador Bernardo O\'Higgins',123);
/*!40000 ALTER TABLE `backend_ubicacion` ENABLE KEYS */;
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

-- Dump completed on 2025-08-23  3:22:05
