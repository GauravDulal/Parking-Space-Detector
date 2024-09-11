-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 11, 2024 at 07:57 AM
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
(65, 23, '08:12:34', '08:12:30', '08:12:34', 0.1, 'Exit', 'Unpaid'),
(66, 54, '08:12:35', '08:12:30', '08:12:35', 0.14, 'Exit', 'Unpaid'),
(67, 20, '08:12:41', '08:12:30', '08:12:41', 0.3, 'Exit', 'Unpaid'),
(68, 20, '08:12:52', '08:12:52', '08:12:52', 0, 'Entry', 'Unpaid'),
(69, 23, '08:12:52', '08:12:52', '08:12:52', 0, 'Entry', 'Unpaid'),
(70, 54, '08:12:52', '08:12:52', '08:12:52', 0, 'Entry', 'Unpaid'),
(71, 23, '08:12:55', '08:12:52', '08:12:55', 0.09, 'Exit', 'Unpaid'),
(72, 54, '08:12:57', '08:12:52', '08:12:57', 0.13, 'Exit', 'Unpaid'),
(73, 20, '08:13:02', '08:12:52', '08:13:02', 0.29, 'Exit', 'Unpaid'),
(74, 20, '08:13:13', '08:13:13', '08:13:13', 0, 'Entry', 'Unpaid'),
(75, 23, '08:13:13', '08:13:13', '08:13:13', 0, 'Entry', 'Unpaid'),
(76, 54, '08:13:13', '08:13:13', '08:13:13', 0, 'Entry', 'Unpaid'),
(77, 23, '08:14:24', '08:14:20', '08:14:24', 0.11, 'Exit', 'Unpaid'),
(78, 54, '08:14:25', '08:14:20', '08:14:25', 0.15, 'Exit', 'Unpaid'),
(79, 23, '08:30:18', '08:30:14', '08:30:18', 0.09, 'Exit', 'Unpaid'),
(80, 54, '08:30:19', '08:30:14', '08:30:19', 0.13, 'Exit', 'Unpaid'),
(81, 20, '08:30:25', '08:30:14', '08:30:25', 0.29, 'Exit', 'Unpaid'),
(82, 20, '08:30:36', '08:30:36', '08:30:36', 0, 'Entry', 'Unpaid'),
(83, 23, '08:30:36', '08:30:36', '08:30:36', 0, 'Entry', 'Unpaid'),
(84, 54, '08:30:36', '08:30:36', '08:30:36', 0, 'Entry', 'Unpaid'),
(85, 23, '08:32:00', '08:31:56', '08:32:00', 0.1, 'Exit', 'Unpaid'),
(86, 54, '08:32:01', '08:31:56', '08:32:01', 0.14, 'Exit', 'Unpaid'),
(87, 20, '08:32:07', '08:31:56', '08:32:07', 0.3, 'Exit', 'Unpaid'),
(88, 20, '08:32:17', '08:32:17', '08:32:17', 0, 'Entry', 'Unpaid'),
(89, 23, '08:32:17', '08:32:17', '08:32:17', 0, 'Entry', 'Unpaid'),
(90, 54, '08:32:17', '08:32:17', '08:32:17', 0, 'Entry', 'Unpaid'),
(91, 23, '08:32:45', '08:32:42', '08:32:45', 0.09, 'Exit', 'Unpaid'),
(92, 54, '08:32:47', '08:32:42', '08:32:47', 0.13, 'Exit', 'Unpaid'),
(93, 20, '08:32:52', '08:32:42', '08:32:52', 0.29, 'Exit', 'Unpaid'),
(94, 20, '08:33:03', '08:33:03', '08:33:03', 0, 'Entry', 'Unpaid'),
(95, 23, '08:33:03', '08:33:03', '08:33:03', 0, 'Entry', 'Unpaid'),
(96, 54, '08:33:03', '08:33:03', '08:33:03', 0, 'Entry', 'Unpaid'),
(97, 23, '08:35:05', '08:35:02', '08:35:05', 0.09, 'Exit', 'Unpaid'),
(98, 54, '08:35:07', '08:35:02', '08:35:07', 0.13, 'Exit', 'Unpaid'),
(99, 20, '08:35:12', '08:35:02', '08:35:12', 0.29, 'Exit', 'Unpaid'),
(100, 20, '08:35:23', '08:35:23', '08:35:23', 0, 'Entry', 'Unpaid'),
(101, 23, '08:35:23', '08:35:23', '08:35:23', 0, 'Entry', 'Unpaid'),
(102, 54, '08:35:23', '08:35:23', '08:35:23', 0, 'Entry', 'Unpaid'),
(103, 23, '08:35:27', '08:35:23', '08:35:27', 0.09, 'Exit', 'Unpaid'),
(104, 54, '08:35:28', '08:35:23', '08:35:28', 0.13, 'Exit', 'Unpaid'),
(105, 23, '08:37:26', '08:37:22', '08:37:26', 0.09, 'Exit', 'Unpaid'),
(106, 54, '08:37:27', '08:37:22', '08:37:27', 0.13, 'Exit', 'Unpaid'),
(107, 20, '08:37:33', '08:37:22', '08:37:33', 0.29, 'Exit', 'Unpaid'),
(108, 20, '08:37:43', '08:37:43', '08:37:43', 0, 'Entry', 'Unpaid'),
(109, 23, '08:37:43', '08:37:43', '08:37:43', 0, 'Entry', 'Unpaid'),
(110, 54, '08:37:43', '08:37:43', '08:37:43', 0, 'Entry', 'Unpaid'),
(111, 23, '08:37:47', '08:37:43', '08:37:47', 0.09, 'Exit', 'Unpaid'),
(112, 54, '08:37:48', '08:37:43', '08:37:48', 0.13, 'Exit', 'Unpaid'),
(113, 23, '09:06:03', '09:05:59', '09:06:03', 0.11, 'Exit', 'Unpaid'),
(114, 54, '09:06:04', '09:05:59', '09:06:04', 0.14, 'Exit', 'Unpaid'),
(115, 20, '09:06:10', '09:05:59', '09:06:10', 0.3, 'Exit', 'Unpaid'),
(116, 23, '09:07:08', '09:07:05', '09:07:08', 0.09, 'Exit', 'Unpaid'),
(117, 54, '09:07:10', '09:07:05', '09:07:10', 0.13, 'Exit', 'Unpaid'),
(118, 23, '09:07:36', '09:07:32', '09:07:36', 0.09, 'Exit', 'Unpaid'),
(119, 54, '09:07:37', '09:07:32', '09:07:37', 0.13, 'Exit', 'Unpaid'),
(120, 20, '09:07:43', '09:07:32', '09:07:43', 0.29, 'Exit', 'Unpaid'),
(121, 20, '09:07:53', '09:07:53', '09:07:53', 0, 'Entry', 'Unpaid'),
(122, 23, '09:07:53', '09:07:53', '09:07:53', 0, 'Entry', 'Unpaid'),
(123, 54, '09:07:53', '09:07:53', '09:07:53', 0, 'Entry', 'Unpaid'),
(124, 23, '09:16:25', '09:16:21', '09:16:25', 0.09, 'Exit', 'Unpaid'),
(125, 54, '09:16:26', '09:16:21', '09:16:26', 0.13, 'Exit', 'Unpaid'),
(126, 23, '09:17:35', '09:17:31', '09:17:35', 0.09, 'Exit', 'Unpaid'),
(127, 54, '09:17:36', '09:17:31', '09:17:36', 0.13, 'Exit', 'Unpaid'),
(128, 23, '09:17:57', '09:17:54', '09:17:57', 0.09, 'Exit', 'Unpaid'),
(129, 54, '09:17:59', '09:17:54', '09:17:59', 0.13, 'Exit', 'Unpaid'),
(130, 20, '09:18:04', '09:17:54', '09:18:04', 0.29, 'Exit', 'Unpaid'),
(131, 20, '09:18:15', '09:18:15', '09:18:15', 0, 'Entry', 'Unpaid'),
(132, 23, '09:18:15', '09:18:15', '09:18:15', 0, 'Entry', 'Unpaid'),
(133, 54, '09:18:15', '09:18:15', '09:18:15', 0, 'Entry', 'Unpaid');

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
  `payment_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_id`, `space_id`, `entry_time`, `exit_time`, `cost`, `payment_status`) VALUES
(1, 23, '09:07:32', '09:07:36', 0.09, 'Unpaid'),
(2, 54, '09:07:32', '09:07:37', 0.13, 'Unpaid'),
(3, 20, '09:07:32', '09:07:43', 0.29, 'Unpaid'),
(4, 23, '09:17:54', '09:17:57', 0.09, 'Unpaid'),
(6, 20, '09:17:54', '09:18:04', 0.29, 'Unpaid');

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
  ADD PRIMARY KEY (`payment_id`);

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
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=134;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
