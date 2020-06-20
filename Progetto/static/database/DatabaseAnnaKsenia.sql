-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Giu 19, 2020 alle 15:09
-- Versione del server: 5.7.28-0ubuntu0.18.04.4
-- Versione PHP: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `DatabaseAnnaKsenia`
--
CREATE DATABASE IF NOT EXISTS `DatabaseAnnaKsenia` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `DatabaseAnnaKsenia`;

-- --------------------------------------------------------

--
-- Struttura della tabella `books`
--

DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
  `idbook` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `releasedate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `coduser` int(11) NOT NULL,
  `publisher` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `genere`
--

DROP TABLE IF EXISTS `genere`;
CREATE TABLE `genere` (
  `idgenere` int(11) NOT NULL,
  `genere` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `generibooks`
--

DROP TABLE IF EXISTS `generibooks`;
CREATE TABLE `generibooks` (
  `idgenerebook` int(11) NOT NULL,
  `codbook` int(11) NOT NULL,
  `codgenere` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `posts`
--

DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `idpost` int(11) NOT NULL,
  `title` text NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `coduser` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `reviews`
--

DROP TABLE IF EXISTS `reviews`;
CREATE TABLE `reviews` (
  `idreview` int(11) NOT NULL,
  `type` varchar(30) NOT NULL,
  `content` text NOT NULL,
  `reviewdate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `coduser` int(11) NOT NULL,
  `codbook` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struttura della tabella `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `usertype` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`idbook`),
  ADD KEY `coduser` (`coduser`);

--
-- Indici per le tabelle `genere`
--
ALTER TABLE `genere`
  ADD PRIMARY KEY (`idgenere`);

--
-- Indici per le tabelle `generibooks`
--
ALTER TABLE `generibooks`
  ADD PRIMARY KEY (`idgenerebook`),
  ADD KEY `codbook` (`codbook`),
  ADD KEY `codgenere` (`codgenere`);

--
-- Indici per le tabelle `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`idpost`),
  ADD KEY `coduser` (`coduser`);

--
-- Indici per le tabelle `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`idreview`),
  ADD KEY `coduser` (`coduser`),
  ADD KEY `codbook` (`codbook`);

--
-- Indici per le tabelle `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `books`
--
ALTER TABLE `books`
  MODIFY `idbook` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `genere`
--
ALTER TABLE `genere`
  MODIFY `idgenere` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `generibooks`
--
ALTER TABLE `generibooks`
  MODIFY `idgenerebook` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `posts`
--
ALTER TABLE `posts`
  MODIFY `idpost` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `reviews`
--
ALTER TABLE `reviews`
  MODIFY `idreview` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT per la tabella `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`coduser`) REFERENCES `users` (`id`);

--
-- Limiti per la tabella `generibooks`
--
ALTER TABLE `generibooks`
  ADD CONSTRAINT `generibooks_ibfk_1` FOREIGN KEY (`codgenere`) REFERENCES `genere` (`idgenere`),
  ADD CONSTRAINT `generibooks_ibfk_2` FOREIGN KEY (`codbook`) REFERENCES `books` (`idbook`);

--
-- Limiti per la tabella `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`coduser`) REFERENCES `users` (`id`);

--
-- Limiti per la tabella `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`coduser`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`codbook`) REFERENCES `books` (`idbook`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

GRANT USAGE ON *.* TO 'dbannaksenia'@'localhost' IDENTIFIED BY PASSWORD '*A77A4E29D1F19A007C71AB53F98FDF7EFB3CC597';

GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER ON `DatabaseAnnaKsenia`.* TO 'dbannaksenia'@'localhost' WITH GRANT OPTION;
