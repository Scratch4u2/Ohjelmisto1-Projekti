# Ohjelmisto 1-kurssin Projekti

Tämä on Metropolian Tieto- ja Viestintätekniikan Ohjelmisto 1-kurssin lentopeliprojektin repository, joka on toteutettu kurssin loppuprojektina. 
Projektin tarkoituksena oli kehittää yksinkertainen lentopeli, jossa käytetään python ohjelmointikieltä sekä hyödynnetään tietokantaa.

###    Projektin kehittäjinä:
- Eemil Nurmi
- Rene Kilpeläinen
- Onni Kivinen
- Patrik Skogberg
## Toiminta ohjeet pelin ajamiseen

1. Mariadb MSI-paketin lataaminen https://mariadb.org/download/
  - Aja asennusohjelma oletuksilla.
  - Käytä kohdissa 'Käyttäjä' ja 'Salasana' molemmissa tekstiä 'root'. Sekä aseta kohtaan 'Portti' luku: 3306.

Alustavasti tarvitaan flight_game tietokanta, jonka luontiskripti löytyy Metropolian Moodlesta. Luontiskripti on lisätty myös tämän repositoryn kansioon "Database", jossa (flight_game_luontiskripti.sql). Tarvitset sitä kohdassa (2.)

2. Lentopelin tietokannan luominen MariaDB:ssä
  - Step1: Luo tietokanta (create database flight_game)
  - Step2: Siirry MariaDB:ssä äsken luomaasi tietokantaan (use flight_game)
  - Step3: Aja (flight_game_luontiskripti.sql) MySQL Command Line Clientissä seuraavalla komennolla:
    - source full\path\tosql\flight_game_luontiskripti.sql   <- muokkaa reitti, siten minne sen olet ladannut.

4. Lataa libraryt; colorama ja art - (esim. IDE:n terminaalissa aja komennot: pip install colorama, pip install art , tai "käsin" lataa IDE:n osioista expansions/extensions)

5. Aja KYSYMYSTAULUNLUONTI.py tiedosto vain KERRAN, jotta saadaan tarvittava (questions) taulu valmiiseen flight_game tietokantaan.

6. Aja high_score_into_database.py tiedosto, jotta saadaan tarvittava (high_score) taulu valmiiseen flight_game tietokantaan.


---
### (Kuva) tietokannan relaatiomallista 
![alt text](flight_game_relation_model.png)

questions-, ja high_score taulut lisätty alkuperäiseen tietokantaan (ks. toimintaohjeet).

## Tietokannan sql-koodi
```sql
-- --------------------------------------------------------
-- Verkkotietokone:              127.0.0.1
-- Palvelinversio:               11.4.0-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Versio:              12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for taulu flight_game.airport
CREATE TABLE IF NOT EXISTS `airport` (
  `id` int(11) NOT NULL,
  `ident` varchar(40) NOT NULL,
  `type` varchar(40) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `latitude_deg` double DEFAULT NULL,
  `longitude_deg` double DEFAULT NULL,
  `elevation_ft` int(11) DEFAULT NULL,
  `continent` varchar(40) DEFAULT NULL,
  `iso_country` varchar(40) DEFAULT NULL,
  `iso_region` varchar(40) DEFAULT NULL,
  `municipality` varchar(40) DEFAULT NULL,
  `scheduled_service` varchar(40) DEFAULT NULL,
  `gps_code` varchar(40) DEFAULT NULL,
  `iata_code` varchar(40) DEFAULT NULL,
  `local_code` varchar(40) DEFAULT NULL,
  `home_link` varchar(40) DEFAULT NULL,
  `wikipedia_link` varchar(40) DEFAULT NULL,
  `keywords` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ident`),
  KEY `iso_country` (`iso_country`),
  CONSTRAINT `airport_ibfk_1` FOREIGN KEY (`iso_country`) REFERENCES `country` (`iso_country`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.country
CREATE TABLE IF NOT EXISTS `country` (
  `iso_country` varchar(40) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `continent` varchar(40) DEFAULT NULL,
  `wikipedia_link` varchar(40) DEFAULT NULL,
  `keywords` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`iso_country`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.game
CREATE TABLE IF NOT EXISTS `game` (
  `id` varchar(40) NOT NULL,
  `co2_consumed` int(8) DEFAULT NULL,
  `co2_budget` int(8) DEFAULT NULL,
  `location` varchar(10) DEFAULT NULL,
  `screen_name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `location` (`location`),
  CONSTRAINT `game_ibfk_1` FOREIGN KEY (`location`) REFERENCES `airport` (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.goal
CREATE TABLE IF NOT EXISTS `goal` (
  `id` int(11) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `icon` varchar(8) DEFAULT NULL,
  `target` varchar(40) DEFAULT NULL,
  `target_minvalue` decimal(8,2) DEFAULT NULL,
  `target_maxvalue` decimal(8,2) DEFAULT NULL,
  `target_text` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.goal_reached
CREATE TABLE IF NOT EXISTS `goal_reached` (
  `game_id` varchar(40) NOT NULL,
  `goal_id` int(11) NOT NULL,
  PRIMARY KEY (`game_id`,`goal_id`),
  KEY `goalid` (`goal_id`),
  CONSTRAINT `goal_reached_ibfk_1` FOREIGN KEY (`game_id`) REFERENCES `game` (`id`),
  CONSTRAINT `goal_reached_ibfk_2` FOREIGN KEY (`goal_id`) REFERENCES `goal` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Tietojen vientiä ei oltu valittu.

-- Dumping structure for taulu flight_game.questions
CREATE TABLE IF NOT EXISTS `questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` text DEFAULT NULL,
  `correct_answer` text DEFAULT NULL,
  `wrong_answer_1` text DEFAULT NULL,
  `wrong_answer_2` text DEFAULT NULL,
  `wrong_answer_3` text DEFAULT NULL,
  `wrong_answer_4` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Tietojen vientiä ei oltu valittu.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
```
README.md kirjoittanut Onni Kivinen
