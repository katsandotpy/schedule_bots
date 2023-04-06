-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Апр 05 2023 г., 22:17
-- Версия сервера: 5.7.39
-- Версия PHP: 8.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `schedule_bot`
--

-- --------------------------------------------------------

--
-- Структура таблицы `userdata`
--

CREATE TABLE `userdata` (
  `telegramid` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `napr` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `forma` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `userdatafull`
--

CREATE TABLE `userdatafull` (
  `napr` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `forma` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `userdatafull`
--

INSERT INTO `userdatafull` (`napr`, `forma`) VALUES
('', ''),
('pi', 'ochn'),
('ur', 'ochn'),
('ek', 'ochn'),
('rso', 'ochn'),
('fin', 'ochn'),
('ped', 'zaochn'),
('rso', 'zaochn'),
('gmu', 'zaochn'),
('mj', 'zaochn'),
('ek', 'zaochn'),
('ur', 'ochzaochn'),
('gmu', 'ochzaochn'),
('ek', 'ochzaochn'),
('pi', 'ochzaochn');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
