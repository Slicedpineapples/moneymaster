-- phpMyAdmin SQL Dump
-- version 5.2.1-2.fc39
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 24, 2024 at 10:56 AM
-- Server version: 8.0.35
-- PHP Version: 8.2.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `moneymaster`
--

-- --------------------------------------------------------

--
-- Table structure for table `assets`
--

CREATE TABLE `assets` (
  `id` bigint UNSIGNED NOT NULL,
  `assetCategoryId` bigint NOT NULL,
  `value` bigint NOT NULL,
  `date` date NOT NULL,
  `userId` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `assets`
--

INSERT INTO `assets` (`id`, `assetCategoryId`, `value`, `date`, `userId`) VALUES
(1, 1, 15000, '2024-05-19', 1),
(2, 2, 990000, '2024-05-19', 2),
(3, 3, 20000, '2024-05-19', 2),
(4, 4, 15000, '2024-05-19', 2);

-- --------------------------------------------------------

--
-- Table structure for table `assetsCategory`
--

CREATE TABLE `assetsCategory` (
  `id` bigint UNSIGNED NOT NULL,
  `AssetName` varchar(255) NOT NULL,
  `numberOfItems` bigint NOT NULL,
  `location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `assetsCategory`
--

INSERT INTO `assetsCategory` (`id`, `AssetName`, `numberOfItems`, `location`) VALUES
(1, 'DTB', 300, 'Nairobi Securities'),
(2, 'kaploti', 3, 'Kamulu'),
(3, 'Cow', 1, 'Kisii'),
(4, 'Goats', 3, 'Kamulu');

-- --------------------------------------------------------

--
-- Table structure for table `currency`
--

CREATE TABLE `currency` (
  `id` bigint UNSIGNED NOT NULL,
  `currencyName` bigint NOT NULL,
  `rate` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `expenses`
--

CREATE TABLE `expenses` (
  `id` bigint UNSIGNED NOT NULL,
  `expensesPriceId` bigint NOT NULL,
  `currId` bigint NOT NULL,
  `expenseCategoryId` bigint NOT NULL,
  `userId` bigint NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `expenses`
--

INSERT INTO `expenses` (`id`, `expensesPriceId`, `currId`, `expenseCategoryId`, `userId`, `date`) VALUES
(30, 1, 1, 1, 1, '2024-05-19'),
(31, 2, 1, 2, 2, '2024-05-19'),
(32, 3, 1, 3, 2, '2024-05-19'),
(33, 4, 1, 4, 1, '2024-05-20'),
(34, 5, 1, 5, 1, '2024-05-21'),
(35, 6, 1, 6, 1, '2024-05-21'),
(36, 7, 1, 7, 1, '2024-05-21');

-- --------------------------------------------------------

--
-- Table structure for table `expensesCategory`
--

CREATE TABLE `expensesCategory` (
  `id` bigint UNSIGNED NOT NULL,
  `expenseName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `expensesCategory`
--

INSERT INTO `expensesCategory` (`id`, `expenseName`) VALUES
(1, 'Clothing'),
(2, 'bhang'),
(3, 'Food'),
(4, 'Transport'),
(5, 'Food'),
(6, 'Food'),
(7, 'Food');

-- --------------------------------------------------------

--
-- Table structure for table `expensesPrice`
--

CREATE TABLE `expensesPrice` (
  `id` bigint UNSIGNED NOT NULL,
  `itemName` varchar(55) NOT NULL,
  `Price` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `expensesPrice`
--

INSERT INTO `expensesPrice` (`id`, `itemName`, `Price`) VALUES
(1, 'Baseball Cap', 3000),
(2, 'big bang', 5000),
(3, 'pizza', 5600),
(4, 'Train Ticket', 1045),
(5, 'Banana', 549),
(6, 'Apple Juice', 329),
(7, 'Cookies', 549);

-- --------------------------------------------------------

--
-- Table structure for table `income`
--

CREATE TABLE `income` (
  `id` bigint UNSIGNED NOT NULL,
  `sourceAmountId` bigint NOT NULL,
  `IncomeCategoryId` bigint NOT NULL,
  `currId` bigint NOT NULL,
  `date` date NOT NULL,
  `userId` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `income`
--

INSERT INTO `income` (`id`, `sourceAmountId`, `IncomeCategoryId`, `currId`, `date`, `userId`) VALUES
(1, 1, 1, 1, '2024-05-19', 1),
(2, 2, 2, 1, '2024-05-19', 2),
(3, 3, 3, 1, '2024-05-19', 2),
(4, 4, 4, 1, '2024-05-19', 2),
(5, 5, 5, 1, '2024-05-19', 2),
(6, 6, 6, 1, '2024-05-19', 2),
(7, 7, 7, 1, '2024-05-19', 2),
(8, 8, 8, 1, '2024-05-19', 2),
(9, 9, 9, 1, '2024-05-19', 2),
(10, 10, 10, 1, '2024-05-20', 1),
(11, 11, 11, 1, '2024-05-21', 5);

-- --------------------------------------------------------

--
-- Table structure for table `incomeCategory`
--

CREATE TABLE `incomeCategory` (
  `id` bigint UNSIGNED NOT NULL,
  `incomeName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `incomeCategory`
--

INSERT INTO `incomeCategory` (`id`, `incomeName`) VALUES
(1, 'Work'),
(2, 'Labelling work'),
(3, 'Movie Shoot'),
(4, 'Gardening Job'),
(5, 'Stipend'),
(6, 'Dog food'),
(7, 'Laptop Sale'),
(8, 'Gift'),
(9, 'Sleeping assets'),
(10, 'Stipend'),
(11, 'Main');

-- --------------------------------------------------------

--
-- Table structure for table `incomeSource`
--

CREATE TABLE `incomeSource` (
  `id` bigint UNSIGNED NOT NULL,
  `sourceName` varchar(255) NOT NULL,
  `amount` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `incomeSource`
--

INSERT INTO `incomeSource` (`id`, `sourceName`, `amount`) VALUES
(1, 'KFC', 78000),
(2, 'DM', 24000),
(3, 'Movie Acting', 75000),
(4, 'Mello Diak', 78000),
(5, 'Stiped', 83700),
(6, 'Kolmax', 12000),
(7, 'Laptop sale', 80000),
(8, 'Hanon', 5000),
(9, 'House rent', 125000),
(10, 'Stipendium Hungaricum', 83700),
(11, 'Wolt', 12500);

-- --------------------------------------------------------

--
-- Table structure for table `liabilities`
--

CREATE TABLE `liabilities` (
  `id` bigint UNSIGNED NOT NULL,
  `dateDue` date NOT NULL,
  `liabilityCategoryId` bigint NOT NULL,
  `userId` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `liabilities`
--

INSERT INTO `liabilities` (`id`, `dateDue`, `liabilityCategoryId`, `userId`) VALUES
(1, '2024-05-19', 1, 1),
(2, '2024-05-19', 2, 2),
(3, '2024-05-20', 3, 2),
(4, '2024-05-20', 4, 2),
(5, '2024-05-21', 5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `liabilitiesCategory`
--

CREATE TABLE `liabilitiesCategory` (
  `id` bigint UNSIGNED NOT NULL,
  `liabilityName` varchar(255) NOT NULL,
  `grossAmount` bigint NOT NULL,
  `remainingAmount` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `liabilitiesCategory`
--

INSERT INTO `liabilitiesCategory` (`id`, `liabilityName`, `grossAmount`, `remainingAmount`) VALUES
(1, 'Rent', 300000, 300000),
(2, 'Automotive', 1000000, 800000),
(3, 'Rent', 300000, 300000),
(4, 'University', 100000, 80000),
(5, 'Girlfriend', 10000, 10000);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` bigint UNSIGNED NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` bigint NOT NULL,
  `region` varchar(255) NOT NULL,
  `userName` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `email`, `phone`, `region`, `userName`, `password`) VALUES
(1, 'felix@mail.com', 1234567891, 'Pest County', 'felix', '54a85d2ae7b0a4d8005ab5cf466d4e582c6ea9aa5060b261241ec65a0ea58506'),
(2, 'joy@mail.com', 1212121212, 'Pest County', 'joy', '54a85d2ae7b0a4d8005ab5cf466d4e582c6ea9aa5060b261241ec65a0ea58506'),
(3, '11@11.cpm', 1112121212, 'Pest County', 'helix', '54a85d2ae7b0a4d8005ab5cf466d4e582c6ea9aa5060b261241ec65a0ea58506'),
(4, 'nyabutofelix@outlook.com', 792274430, 'Budapest', 'nyabutofelix@outlook.com', '6ec424c4f335268e8aad1b925d67e28455b44587ebb5f61a34fd3836b5f8bd8e'),
(5, 'mafurufrancis@gmail.com', 0, 'Budapest', 'Francis', 'f8a871598d0328378536146730e8ad936b9c6a71533697a265b030636be1660e');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assets`
--
ALTER TABLE `assets`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `assetsCategory`
--
ALTER TABLE `assetsCategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `currency`
--
ALTER TABLE `currency`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `expenses`
--
ALTER TABLE `expenses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `expensesCategory`
--
ALTER TABLE `expensesCategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `expensesPrice`
--
ALTER TABLE `expensesPrice`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `income`
--
ALTER TABLE `income`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `incomeCategory`
--
ALTER TABLE `incomeCategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `incomeSource`
--
ALTER TABLE `incomeSource`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `liabilities`
--
ALTER TABLE `liabilities`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `liabilitiesCategory`
--
ALTER TABLE `liabilitiesCategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assets`
--
ALTER TABLE `assets`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `assetsCategory`
--
ALTER TABLE `assetsCategory`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `currency`
--
ALTER TABLE `currency`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `expenses`
--
ALTER TABLE `expenses`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `expensesCategory`
--
ALTER TABLE `expensesCategory`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `expensesPrice`
--
ALTER TABLE `expensesPrice`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `income`
--
ALTER TABLE `income`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `incomeCategory`
--
ALTER TABLE `incomeCategory`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `incomeSource`
--
ALTER TABLE `incomeSource`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `liabilities`
--
ALTER TABLE `liabilities`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `liabilitiesCategory`
--
ALTER TABLE `liabilitiesCategory`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` bigint UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
