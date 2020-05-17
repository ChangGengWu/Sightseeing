-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 19, 2020 at 02:41 PM
-- Server version: 8.0.17
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test2`
--

-- --------------------------------------------------------

--
-- Table structure for table `site_attr`
--

CREATE TABLE `site_attr` (
  `id` int(8) NOT NULL,
  `type` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `tag` varchar(45) COLLATE utf8mb4_general_ci NOT NULL,
  `color` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `shape` varchar(10) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `site_attr`
--

INSERT INTO `site_attr` (`id`, `type`, `tag`, `color`, `shape`) VALUES
(1, '景點與地標', '景點和地標', 'red', 'square'),
(2, '景點與地標', '古蹟', 'red', 'square'),
(3, '景點與地標', '建築物', 'red', 'square'),
(4, '景點與地標', '宗教聖地', 'red', 'square'),
(5, '景點與地標', '景觀徒步區', 'red', 'square'),
(6, '景點與地標', '史跡徒步區', 'red', 'square'),
(7, '景點與地標', '農場', 'red', 'square'),
(8, '景點與地標', '教育景點', 'red', 'square'),
(9, '景點與地標', '瞭望台', 'red', 'square'),
(10, '景點與地標', '地區', 'red', 'square'),
(11, '景點與地標', '橋樑', 'red', 'square'),
(12, '景點與地標', '政府建築', 'red', 'square'),
(13, '景點與地標', '觀景台和觀景塔', 'red', 'square'),
(14, '景點與地標', '古代遺址', 'red', 'square'),
(15, '景點與地標', '燈塔', 'red', 'square'),
(16, '景點與地標', '碼頭和木板人行道', 'red', 'square'),
(17, '景點與地標', '紀念碑和雕像', 'red', 'square'),
(18, '景點與地標', '教堂和大教堂', 'red', 'square'),
(19, '景點與地標', '競技場和體育場館', 'red', 'square'),
(20, '景點與地標', '大學與學校', 'red', 'square'),
(21, '景點與地標', '農場', 'red', 'square'),
(22, '景點與地標', '神秘景點', 'red', 'square'),
(23, '景點與地標', '市政中心', 'red', 'square'),
(24, '景點與地標', '其他牧場和農場', 'red', 'square'),
(25, '景點與地標', '噴泉', 'red', 'square'),
(26, '景點與地標', '城堡', 'red', 'square'),
(27, '景點與地標', '礦區', 'red', 'square'),
(28, '景點與地標', '自駕觀景遊', 'red', 'square'),
(29, '景點與地標', '軍事基地和設施', 'red', 'square'),
(30, '自然與公園', '公園', 'red', 'square'),
(31, '自然與公園', '登山步道', 'red', 'square'),
(32, '自然與公園', '水域', 'red', 'square'),
(33, '自然與公園', '海灘', 'red', 'square'),
(34, '自然與公園', '溫泉和間歇泉', 'red', 'square'),
(35, '自然與公園', '山脈', 'red', 'square'),
(36, '自然與公園', '單車專用道', 'red', 'square'),
(37, '自然與公園', '花園', 'red', 'square'),
(38, '自然與公園', '島嶼', 'red', 'square'),
(39, '自然與公園', '地質構造', 'red', 'square'),
(40, '自然與公園', '森林', 'red', 'square'),
(41, '自然與公園', '瀑布', 'red', 'square'),
(42, '自然與公園', '國家公園', 'red', 'square'),
(43, '自然與公園', '自然和野生動物區', 'red', 'square'),
(44, '自然與公園', '大洞穴和洞窟', 'red', 'square'),
(45, '自然與公園', '山谷', 'red', 'square'),
(46, '自然與公園', '遊樂場', 'red', 'square'),
(47, '自然與公園', '動物園', 'red', 'square'),
(48, '自然與公園', '水壩', 'red', 'square'),
(49, '自然與公園', '其他自然景觀與公園', 'red', 'square'),
(50, '自然與公園', '珊瑚礁', 'red', 'square'),
(51, '自然與公園', '遊艇碼頭', 'red', 'square'),
(52, '自然與公園', '水族館', 'red', 'square'),
(53, '自然與公園', '州立公園', 'red', 'square'),
(54, '自然與公園', '摩托車專用道', 'red', 'square'),
(55, '自然與公園', '滑雪和滑雪板區', 'red', 'square'),
(56, '博物館', '特色博物館', 'red', 'square'),
(57, '博物館', '歷史博物館', 'red', 'square'),
(58, '博物館', '藝術博物館', 'red', 'square'),
(59, '博物館', '美術館', 'red', 'square'),
(60, '博物館', '軍事博物館', 'red', 'square'),
(61, '博物館', '科學博物館', 'red', 'square'),
(62, '博物館', '兒童博物館', 'red', 'square'),
(63, '博物館', '自然歷史博物館', 'red', 'square'),
(64, '動物園和水族館', '動物園', 'red', 'square'),
(65, '動物園和水族館', '水族館', 'red', 'square'),
(66, '水上樂園和遊樂場', '主題樂園', 'red', 'square'),
(67, '水上樂園和遊樂場', '水上樂園', 'red', 'square'),
(68, 'Spa', 'Spa', 'red', 'square'),
(69, 'Spa', '健康/健身俱樂部和健身中心', 'red', 'square'),
(70, 'Spa', '溫泉', 'red', 'square'),
(71, 'Spa', '浴池和土耳其浴', 'red', 'square'),
(72, 'Spa', '瑜伽與皮拉提斯', 'red', 'square'),
(73, '夜生活', '酒吧和夜店', 'red', 'square'),
(74, '夜生活', '咖啡館', 'red', 'square'),
(75, '夜生活', '舞蹈俱樂部和迪斯可舞廳', 'red', 'square'),
(76, '夜生活', '品酒酒吧', 'red', 'square'),
(77, '夜生活', '酒吧、夜店和酒館遊覽', 'red', 'square'),
(78, '休閒與娛樂', '遊戲和娛樂中心', 'red', 'square'),
(79, '休閒與娛樂', '遊樂場', 'red', 'square'),
(80, '休閒與娛樂', '電影院', 'red', 'square'),
(81, '休閒與娛樂', '繪畫和陶藝工作室', 'red', 'square'),
(82, '休閒與娛樂', '角色體驗', 'red', 'square'),
(83, '休閒與娛樂', '農夫市場', 'red', 'square'),
(84, '休閒與娛樂', '體育館', 'red', 'square'),
(85, '休閒與娛樂', '保齡球館', 'red', 'square'),
(86, '休閒與娛樂', '其他休閒與娛樂', 'red', 'square'),
(87, '休閒與娛樂', '騎乘和活動', 'red', 'square'),
(88, '', '自然與公園', 'red', 'square'),
(89, '', '休閒與娛樂', 'red', 'square'),
(90, '', '博物館', 'red', 'square'),
(91, '', '動物園和水族館', 'red', 'square'),
(92, '', '水上樂園和遊樂場', 'red', 'square'),
(93, '', '夜生活', 'red', 'square'),
(94, '', '飲食', 'red', 'square'),
(95, '', '購物', 'red', 'square'),
(96, '', '農貿市場', 'red', 'square'),
(97, '', '2019台灣燈會', 'red', 'square'),
(98, '', '文青必訪', 'red', 'square'),
(99, '', '水上活動', 'red', 'square'),
(100, '', '古蹟巡禮', 'red', 'square'),
(101, '', '打卡熱點', 'red', 'square'),
(102, '', '生態體驗', 'red', 'square'),
(103, '', '吃海鮮', 'red', 'square'),
(104, '', '地質奇觀', 'red', 'square'),
(105, '', '寺廟祈福', 'red', 'square'),
(106, '', '拍婚紗', 'red', 'square'),
(107, '', '泡溫泉', 'red', 'square'),
(108, '', '迎曙光', 'red', 'square'),
(109, '', '非吃不可', 'red', 'square'),
(110, '', '看展覽', 'red', 'square'),
(111, '', '看海景', 'red', 'square'),
(112, '', '夏天戲水', 'red', 'square'),
(113, '', '浪漫約會', 'red', 'square'),
(114, '', '海灣旅遊', 'red', 'square'),
(115, '', '特別企劃', 'red', 'square'),
(116, '', '送夕陽', 'red', 'square'),
(117, '', '國家公園', 'red', 'square'),
(118, '', '國家風景區', 'red', 'square'),
(119, '', '逛老街', 'red', 'square'),
(120, '', '逛夜市', 'red', 'square'),
(121, '', '部落旅遊', 'red', 'square'),
(122, '', '單車漫遊', 'red', 'square'),
(123, '', '森林步道', 'red', 'square'),
(124, '', '無障礙', 'red', 'square'),
(125, '', '登山步道', 'red', 'square'),
(126, '', '漫遊客庄', 'red', 'square'),
(127, '', '網美必拍', 'red', 'square'),
(128, '', '賞夜景', 'red', 'square'),
(129, '', '賞花', 'red', 'square'),
(130, '', '戰地文化', 'red', 'square'),
(131, '', '燈塔', 'red', 'square'),
(132, '', '親子共遊', 'red', 'square'),
(133, '', '藝術', 'red', 'square'),
(134, '', '鐵道旅遊', 'red', 'square'),
(135, '', '觀景平台', 'red', 'square');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `site_attr`
--
ALTER TABLE `site_attr`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
