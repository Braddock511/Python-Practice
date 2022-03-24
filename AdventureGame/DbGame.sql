-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 22 Mar 2022, 20:29
-- Wersja serwera: 10.4.21-MariaDB
-- Wersja PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `dbgame`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `characters`
--

CREATE TABLE `characters` (
  `id` int(3) NOT NULL,
  `name` varchar(30) NOT NULL,
  `hp` int(5) NOT NULL,
  `damage` int(5) NOT NULL,
  `agility` int(5) NOT NULL,
  `intelligence` int(5) NOT NULL,
  `speed` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `characters`
--

INSERT INTO `characters` (`id`, `name`, `hp`, `damage`, `agility`, `intelligence`, `speed`) VALUES
(1, 'Warrior', 120, 100, 60, 20, 30),
(2, 'Wizard', 60, 140, 20, 100, 20),
(3, 'Archer', 80, 120, 80, 60, 50);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `main`
--

CREATE TABLE `main` (
  `id` int(3) NOT NULL,
  `id_user` int(3) NOT NULL,
  `id_character` int(3) NOT NULL,
  `Date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `monsters`
--

CREATE TABLE `monsters` (
  `id` int(3) NOT NULL,
  `name` varchar(100) NOT NULL,
  `hp` int(3) NOT NULL,
  `attack` int(3) NOT NULL,
  `dodge` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `monsters`
--

INSERT INTO `monsters` (`id`, `name`, `hp`, `attack`, `dodge`) VALUES
(1, 'Troll', 1000, 10, 0),
(2, 'Wolf', 200, 40, 30),
(3, 'Wraith', 100, 70, 70),
(4, 'Zombie', 1200, 5, 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `users`
--

CREATE TABLE `users` (
  `id` int(3) NOT NULL,
  `name` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `users`
--

INSERT INTO `users` (`id`, `name`, `password`) VALUES
(1, 'wruku2012', '40bd001563085fc35165329ea1ff5c5ecbdbbeef'),
(2, 'asd', 'f10e2821bbbea527ea02200352313bc059445190'),
(3, 'asd', 'aff024fe4ab0fece4091de044c58c9ae4233383a');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `weapons`
--

CREATE TABLE `weapons` (
  `id` int(3) NOT NULL,
  `id_character` int(3) NOT NULL,
  `name` varchar(50) NOT NULL,
  `attack` int(3) NOT NULL,
  `speed_attack` int(3) NOT NULL,
  `weight` decimal(3,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `weapons`
--

INSERT INTO `weapons` (`id`, `id_character`, `name`, `attack`, `speed_attack`, `weight`) VALUES
(1, 1, 'sword', 100, 50, '1.35'),
(2, 1, 'axe', 80, 60, '0.95'),
(3, 1, 'spear', 110, 40, '1.00'),
(4, 2, 'fire_wand', 200, 10, '0.20'),
(5, 2, 'wind_wand', 50, 100, '0.10'),
(6, 2, 'lighting_wand', 100, 50, '0.20'),
(7, 3, 'short_bow', 100, 50, '0.50'),
(8, 3, 'long_bow', 150, 20, '0.85'),
(9, 3, 'crossbow', 200, 10, '1.20');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `characters`
--
ALTER TABLE `characters`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `main`
--
ALTER TABLE `main`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_user` (`id_user`,`id_character`),
  ADD KEY `id_character` (`id_character`);

--
-- Indeksy dla tabeli `monsters`
--
ALTER TABLE `monsters`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `weapons`
--
ALTER TABLE `weapons`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_character` (`id_character`);

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `main`
--
ALTER TABLE `main`
  ADD CONSTRAINT `main_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `main_ibfk_2` FOREIGN KEY (`id_character`) REFERENCES `characters` (`id`);

--
-- Ograniczenia dla tabeli `weapons`
--
ALTER TABLE `weapons`
  ADD CONSTRAINT `weapons_ibfk_1` FOREIGN KEY (`id_character`) REFERENCES `characters` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
