-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 24, 2024 at 04:45 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `psds`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_creds`
--

CREATE TABLE `admin_creds` (
  `Aid` int(11) NOT NULL,
  `Amail` varchar(255) NOT NULL,
  `Apass` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_creds`
--

INSERT INTO `admin_creds` (`Aid`, `Amail`, `Apass`) VALUES
(1, 'sanks@mail.com', 'scrypt:32768:8:1$JSOwzEFGzovjzXeh$93aa0e2219401aca8701967ba24186527222feaaa6dba6edd27afaa966389a33d6467b0023bf8bd4ff8bbe0bbf15200c27cc49b0e45aab210bb5442d28d0647b');

-- --------------------------------------------------------

--
-- Table structure for table `log`
--

CREATE TABLE `log` (
  `log_id` int(11) NOT NULL,
  `space_id` int(255) NOT NULL,
  `log_time` time NOT NULL,
  `entry_time` time NOT NULL,
  `exit_time` time NOT NULL,
  `cost` float NOT NULL,
  `status` varchar(255) NOT NULL,
  `payment_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `log`
--

INSERT INTO `log` (`log_id`, `space_id`, `log_time`, `entry_time`, `exit_time`, `cost`, `status`, `payment_status`) VALUES
(1, 23, '20:29:28', '20:29:24', '20:29:28', 0.09, 'Exit', 'Unpaid'),
(2, 54, '20:29:29', '20:29:24', '20:29:29', 0.13, 'Exit', 'Unpaid'),
(3, 20, '20:29:35', '20:29:24', '20:29:35', 0.29, 'Exit', 'Unpaid'),
(4, 20, '20:29:46', '20:29:46', '20:29:46', 0, 'Entry', 'Unpaid'),
(5, 23, '20:29:46', '20:29:46', '20:29:46', 0, 'Entry', 'Unpaid'),
(6, 54, '20:29:46', '20:29:46', '20:29:46', 0, 'Entry', 'Unpaid'),
(7, 23, '20:29:49', '20:29:46', '20:29:49', 0.09, 'Exit', 'Unpaid'),
(8, 54, '20:29:50', '20:29:46', '20:29:50', 0.13, 'Exit', 'Unpaid');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_creds`
--
ALTER TABLE `admin_creds`
  ADD PRIMARY KEY (`Aid`);

--
-- Indexes for table `log`
--
ALTER TABLE `log`
  ADD PRIMARY KEY (`log_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_creds`
--
ALTER TABLE `admin_creds`
  MODIFY `Aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
