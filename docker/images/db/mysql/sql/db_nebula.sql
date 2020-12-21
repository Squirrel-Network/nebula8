-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: May 12, 2020 at 11:12 PM
-- Server version: 8.0.20
-- PHP Version: 7.4.5

SET SQL_MODE = `NO_AUTO_VALUE_ON_ZERO`;
START TRANSACTION;
SET time_zone = `+00:00`;


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `%DATABASE%`
--
CREATE DATABASE IF NOT EXISTS `%DATABASE%` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `%DATABASE%`;

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE IF NOT EXISTS `answers` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `question_text` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `answer_text` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `id_group` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `bad_words`
--

CREATE TABLE IF NOT EXISTS `bad_words` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `word` varchar(255) NOT NULL,
  `id_group` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ban_table`
--

CREATE TABLE IF NOT EXISTS `ban_table` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) NOT NULL,
  `motivation_text` varchar(255) NOT NULL,
  `user_date` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `user_id_index` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `card_table`
--

CREATE TABLE IF NOT EXISTS `card_table` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `card_img` varchar(255) NOT NULL,
  `card_bio` varchar(255) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `id_group` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `user_index` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `config_bot`
--

CREATE TABLE IF NOT EXISTS `config_bot` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `plugin_option` tinyint NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `fixed_default`
--

CREATE TABLE IF NOT EXISTS `fixed_default` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `id_group` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

CREATE TABLE IF NOT EXISTS `groups` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `welcome_messages` text NOT NULL,
  `welcome_buttons_text` varchar(15) NOT NULL,
  `welcome_buttons_url` varchar(50) NOT NULL,
  `community_id` varchar(30) NOT NULL,
  `telegram_chat_id` varchar(30) NOT NULL,
  `rules` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `language` varchar(6) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `group_id_key` (`telegram_chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `help_table`
--

CREATE TABLE IF NOT EXISTS `help_table` (
  `ID` int NOT NULL,
  `help_text` text NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `jokes`
--

CREATE TABLE IF NOT EXISTS `jokes` (
  `ID` int NOT NULL,
  `joke_text` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `language`
--

CREATE TABLE IF NOT EXISTS `language` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `language_set` varchar(4) NOT NULL,
  `id_group` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `logchannel_table`
--

CREATE TABLE IF NOT EXISTS `logchannel_table` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `channel_id` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `channel_index` (`channel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `rules_table`
--

CREATE TABLE IF NOT EXISTS `rules_table` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `rules_text` text NOT NULL,
  `id_group` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `unique_id_group` (`id_group`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE IF NOT EXISTS `test` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `urls`
--

CREATE TABLE IF NOT EXISTS `urls` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text` text,
  `url` text,
  `id_group` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(50) NOT NULL,
  `user_nickname` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `useridkey` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `welcome_table`
--

CREATE TABLE IF NOT EXISTS `welcome_table` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `id_group` varchar(50) NOT NULL,
  `welcome_text` text NOT NULL,
  `b_options` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `index_group` (`id_group`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;