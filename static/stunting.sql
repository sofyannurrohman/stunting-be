-- phpMyAdmin SQL Dump
-- version 5.2.1deb3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 23, 2025 at 06:22 AM
-- Server version: 8.0.42-0ubuntu0.24.04.1
-- PHP Version: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stunting`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE IF NOT EXISTS `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `alembic_version`
--

-- INSERT INTO `alembic_version` (`version_num`) VALUES
-- ('e15901cbcfc5');

-- --------------------------------------------------------

--
-- Table structure for table `information`
--

CREATE TABLE IF NOT EXISTS `information` (
  `id` int NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `content` varchar(1000) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` datetime DEFAULT CURRENT_TIMESTAMP,
  `category` varchar(255) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `information`
--

INSERT INTO `information` (`id`, `title`, `content`, `image_url`, `createdAt`, `updatedAt`, `category`, `source`) VALUES
(5, 'Pentingnya Imunisasi untuk Anak', 'Imunisasi melindungi anak dari penyakit berbahaya seperti campak, polio, dan hepatitis. Pemerintah menyarankan imunisasi lengkap pada tahun pertama kehidupan anak.', '/static/uploads/6ef7a0d374a0417c951a7ce97fa0ac97.png', '2025-05-21 07:50:51', '2025-05-21 07:50:51', 'Kesehatan Anak', 'https://www.kemkes.go.id/article/view/202103170001/pentingnya-imunisasi-bagi-anak.html'),
(6, 'Manfaat ASI Eksklusif Selama 6 Bulan', 'ASI eksklusif mengandung nutrisi penting dan antibodi yang membantu meningkatkan daya tahan tubuh bayi. WHO menyarankan pemberian ASI eksklusif selama 6 bulan pertama.', '/static/uploads/27aa330c8b204b809cd3953c73d9f8ff.png', '2025-05-21 07:58:22', '2025-05-21 07:58:22', 'Gizi Bayi', 'https://www.alodokter.com/asi-eksklusif'),
(7, 'Cara Menjaga Kesehatan Ibu Hamil', 'Ibu hamil perlu menjaga pola makan sehat, rutin berolahraga ringan, dan memeriksakan kehamilan secara berkala ke bidan atau dokter kandungan.', '/static/uploads/5158da5904bc43dabe3c3a9f604d27fa.png', '2025-05-21 08:02:39', '2025-05-21 08:02:39', 'Kehamilan', 'https://hellosehat.com/kehamilan/kesehatan-ibu-hamil/menjaga-kesehatan-ibu-hamil'),
(8, 'Stunting pada Anak: Penyebab dan Pencegahan', 'Stunting adalah kondisi gagal tumbuh akibat kekurangan gizi kronis. Pencegahan dilakukan sejak 1000 hari pertama kehidupan anak dengan nutrisi yang cukup dan pola asuh yang baik.', '/static/uploads/1faff06b31c44adc88d046789905e4bd.png', '2025-05-21 08:05:17', '2025-05-21 08:05:17', 'Stunting', 'ttps://www.who.int/indonesia/news/detail/06-03-2020-pencegahan-stunting'),
(9, 'Tips Mencegah Diare pada Balita', 'Cuci tangan sebelum makan dan setelah buang air, serta pastikan air minum yang diberikan sudah matang. Diare bisa menyebabkan dehidrasi berat pada anak.', '/static/uploads/1f1b826f173a4e61b9194b64667a9148.png', '2025-05-21 08:07:11', '2025-05-21 08:07:11', 'Penyakit Anak', 'https://www.cdc.gov/handwashing/global-handwashing-day.html');

-- --------------------------------------------------------

--
-- Table structure for table `toddlers`
--

CREATE TABLE IF NOT EXISTS `toddlers` (
  `id` int NOT NULL,
  `age_months` int DEFAULT NULL,
  `weight_kg` int DEFAULT NULL,
  `height_cm` int DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` datetime DEFAULT CURRENT_TIMESTAMP,
  `predicted` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `toddlers`
--

INSERT INTO `toddlers` (`id`, `age_months`, `weight_kg`, `height_cm`, `gender`, `name`, `user_id`, `createdAt`, `updatedAt`, `predicted`) VALUES
(2, 40, 13, 96, 'Laki-laki', 'Mevan Fadhilah', 2, '2025-05-17 21:59:58', '2025-05-17 21:59:58', 'Normal_Risk of Overweight'),
(3, 21, 9, 81, 'Perempuan', 'Gibran', 6, '2025-05-17 22:09:05', '2025-05-17 22:09:05', 'Normal_Normal weight'),
(4, 3, 5, 60, 'Laki-laki', 'Putra Wijaya', 4, '2025-05-17 22:12:02', '2025-05-17 22:12:02', 'Severely Stunted_Normal weight'),
(5, 45, 13, 96, 'Laki-laki', 'Nanang Adi Kusuma', 13, '2025-05-17 22:17:35', '2025-05-17 22:17:35', 'Tall_Normal weight'),
(6, 42, 13, 94, 'Perempuan', 'Nurfadilah', 6, '2025-05-17 22:23:28', '2025-05-17 22:23:28', 'Tall_Normal weight'),
(7, 27, 12, 85, 'Perempuan', 'Dewi Fitriyana', 2, '2025-05-17 22:28:37', '2025-05-17 22:28:37', 'Normal_Normal weight'),
(8, 11, 9, 74, 'Laki-laki', 'Miko', 2, '2025-05-17 22:31:56', '2025-05-17 22:31:56', 'Severely Stunted_Underweight'),
(9, 20, 9, 81, 'Laki-laki', 'Gilang Wicaksana', 2, '2025-05-17 22:33:21', '2025-05-17 22:33:21', 'Normal_Riskof Overweight'),
(10, 48, 14, 97, 'Perempuan', 'Hadriana', 2, '2025-05-17 22:37:11', '2025-05-17 22:37:11', 'Normal_Normal weight'),
(11, 49, 14, 97, 'Perempuan', 'Pramudita', 2, '2025-05-17 22:40:22', '2025-05-17 22:40:22', 'Normal_Riskof Overweight'),
(12, 38, 25, 104, 'Perempuan', 'Rara', 2, '2025-05-17 22:48:42', '2025-05-17 22:48:42', 'Tall_Underweight'),
(13, 22, 16, 89, 'Perempuan', 'Rara', 2, '2025-06-02 09:27:04', '2025-06-02 09:27:04', NULL),
(14, 22, 16, 89, 'Perempuan', 'qwe', 2, '2025-06-02 09:31:56', '2025-06-02 09:31:56', NULL),
(15, 22, 16, 89, 'Perempuan', 'qwe', 2, '2025-06-02 09:35:31', '2025-06-02 09:35:31', NULL),
(16, 22, 16, 89, 'Perempuan', 'qwe', 2, '2025-06-02 09:48:58', '2025-06-02 09:48:58', NULL),
(17, 6, 7, 70, 'Laki-laki', 'Putra Wijaya', 4, '2025-06-03 22:24:40', '2025-06-03 22:24:40', NULL),
(18, 6, 7, 70, 'Perempuan', 'Sofia', 4, '2025-06-03 22:48:47', '2025-06-03 22:48:47', NULL),
(19, 10, 18, 55, 'Perempuan', 'Sofia', 2, '2025-06-04 10:03:25', '2025-06-04 10:03:25', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `createdAt` datetime DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` datetime DEFAULT CURRENT_TIMESTAMP,
  `hashed_password` varchar(255) DEFAULT NULL,
  `role` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `createdAt`, `updatedAt`, `hashed_password`, `role`) VALUES
(2, 'admin', 'admin@admin.com', '2025-05-06 09:52:10', '2025-05-06 09:52:10', '$2b$12$lmWUDu1CUyzy2Ttfejs9h.HblpgD/3h48EtNjeSFhiLu0nVZ.x4cS', 'admin'),
(4, 'sofyan', 'sofyan@gmail.com', '2025-05-15 19:02:03', '2025-05-15 19:02:03', '$2b$12$gHKDRmWfBAk2ExlbX5v2K.2f28JUApDSbJZGBmmOueDGl04lWfZtW', 'admin'),
(6, 'Siti Nurhaliza', 'siti.nurhaliza@gmail.com', '2025-05-20 22:33:17', '2025-05-20 22:33:17', '$2b$12$/UJ3kpgoZf6SB0k5RrmviuR57o7SMB6qN.NHgzlUmrcUHaHmag7xS', 'user'),
(7, 'Lisa Maharani', 'lisa.maharani@gmail.com', '2025-05-20 22:33:18', '2025-05-20 22:33:18', '$2b$12$RfWa17P63RKb9DDRIyWR1OdWhXAUHJRitvLTFZsIRupjp8JBP5s2m', 'user'),
(8, 'Ayu Lestari', 'ayu.lestari@gmail.com', '2025-05-20 22:33:19', '2025-05-20 22:33:19', '$2b$12$YD4ZUs5gqkK9sGTDUG/3F.ZfQSYVltLv50wzQTFxH4q25Y5vaqj8G', 'user'),
(9, 'Desi Kartika', 'desi.kartika@gmail.com', '2025-05-20 22:33:19', '2025-05-20 22:33:19', '$2b$12$jzZhXGtEDcSn9ilJsXmwiOa8rAVRL3YXEcC/CCghlxXZ7ilL.j./m', 'user'),
(10, 'Intan Permata', 'intan.permata@gmail.com', '2025-05-20 22:33:20', '2025-05-20 22:33:20', '$2b$12$0otkIzfuhzUhjDfc.RJ9WO.O/6IS.EoI9RRJrfBRF/3vkwWiog/oq', 'user'),
(11, 'Melati Rahayu', 'melati.rahayu@gmail.com', '2025-05-20 22:33:21', '2025-05-20 22:33:21', '$2b$12$F4JmZb9iQBSjbuELDAWf.O.qfigaIycUOTXcWqxBvebe.X.tERANK', 'user'),
(12, 'Nina Anggraini', 'nina.anggraini@gmail.com', '2025-05-20 22:33:21', '2025-05-20 22:33:21', '$2b$12$a8/U3.xbWM075nSqCXa.w.m6GOsat4/5AZx4wbj4cjHqbvbMQsRYG', 'user'),
(13, 'Ratna Wulandari', 'ratna.wulandari@gmail.com', '2025-05-20 22:33:22', '2025-05-20 22:33:22', '$2b$12$kB9da8aQO7fcK0w1mMiWqexcNkse3wRfS6l.eGQ99f1Rb97SDG4L.', 'user'),
(14, 'Tiara Safitri', 'tiara.safitri@gmail.com', '2025-05-20 22:33:22', '2025-05-20 22:33:22', '$2b$12$xrUuZbKheERcjHqszjo5FeKy2KO4BbxeC3FZkRd8sC8E4Obw/6GLe', 'user'),
(15, 'Yuni Febrianti', 'yuni.febrianti@gmail.com', '2025-05-20 22:33:23', '2025-05-20 22:33:23', '$2b$12$QP/hKPDOFWeiTfmQGQSWyeMaR/qfCDS3nTLc7RCpXqfZuWRSkEQQK', 'user'),
(16, 'Stella', 'stella@gmail.com', '2025-06-04 10:19:19', '2025-06-04 10:19:19', '$2b$12$JSduhl1J4Stz759oV1//AeWoeWP.xpQjyiMVZYGIK3eLerL.4gL8C', 'user');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `information`
--
ALTER TABLE `information`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_information_id` (`id`);

--
-- Indexes for table `toddlers`
--
ALTER TABLE `toddlers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_toddlers_id` (`id`),
  ADD KEY `ix_toddlers_name` (`name`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_users_email` (`email`),
  ADD KEY `ix_users_id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `information`
--
ALTER TABLE `information`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `toddlers`
--
ALTER TABLE `toddlers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `toddlers`
--
ALTER TABLE `toddlers`
  ADD CONSTRAINT `toddlers_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
