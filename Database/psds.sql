-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 13, 2024 at 03:26 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
(1, 'sanks@mail.com', 'scrypt:32768:8:1$JSOwzEFGzovjzXeh$93aa0e2219401aca8701967ba24186527222feaaa6dba6edd27afaa966389a33d6467b0023bf8bd4ff8bbe0bbf15200c27cc49b0e45aab210bb5442d28d0647b'),
(2, 'sups@mail.com', 'scrypt:32768:8:1$aK8q9ryDQyk2SGFv$58091054cd53216731fb7bed14d110a0e90a65893a83690e9a47f89b192cdfea39f5582318d3867b85136ce7539b7dfad4d4b68214b39b0d7fe5bf4c97acd69a');

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
(1, 23, '16:42:30', '16:42:26', '16:42:30', 0.09, 'Exit', 'Unpaid'),
(2, 54, '16:42:31', '16:42:26', '16:42:31', 0.13, 'Exit', 'Unpaid'),
(3, 20, '16:42:37', '16:42:26', '16:42:37', 0.3, 'Exit', 'Unpaid'),
(4, 23, '16:45:31', '16:45:28', '16:45:31', 0.09, 'Exit', 'Paid'),
(5, 54, '16:45:32', '16:45:28', '16:45:32', 0.13, 'Exit', 'Unpaid'),
(6, 20, '16:45:38', '16:45:28', '16:45:38', 0.29, 'Exit', 'Unpaid'),
(7, 23, '16:49:27', '16:49:24', '16:49:27', 0.09, 'Exit', 'Unpaid'),
(8, 54, '16:49:29', '16:49:24', '16:49:29', 0.13, 'Exit', 'Unpaid'),
(9, 20, '16:49:34', '16:49:24', '16:49:34', 0.29, 'Exit', 'Unpaid');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL,
  `space_id` int(255) NOT NULL,
  `entry_time` time NOT NULL,
  `exit_time` time NOT NULL,
  `cost` float NOT NULL,
  `payment_status` varchar(255) NOT NULL,
  `log_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_id`, `space_id`, `entry_time`, `exit_time`, `cost`, `payment_status`, `log_id`) VALUES
(10, 23, '16:45:28', '16:45:31', 0.09, 'Paid', 4),
(11, 54, '16:45:28', '16:45:32', 0.13, 'Paid', 5),
(12, 20, '16:45:28', '16:45:38', 0.29, 'Paid', 6),
(13, 23, '16:49:24', '16:49:27', 0.09, 'Paid', 7),
(14, 54, '16:49:24', '16:49:29', 0.13, 'Paid', 8),
(15, 20, '16:49:24', '16:49:34', 0.29, 'Paid', 9);

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
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `fk_log_id` (`log_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_creds`
--
ALTER TABLE `admin_creds`
  MODIFY `Aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `log`
--
ALTER TABLE `log`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `fk_log_id` FOREIGN KEY (`log_id`) REFERENCES `log` (`log_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
