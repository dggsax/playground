-- phpMyAdmin SQL Dump
-- version 4.0.10.20
-- https://www.phpmyadmin.net
--
-- Host: sql.mit.edu
-- Generation Time: Aug 01, 2017 at 11:05 PM
-- Server version: 5.1.72-2-log
-- PHP Version: 5.5.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dangonzo+edu`
--

-- --------------------------------------------------------

--
-- Table structure for table `mostec_flights_2017`
--

CREATE TABLE IF NOT EXISTS `mostec_flights_2017` (
  `firstName` text NOT NULL,
  `lastName` text NOT NULL,
  `cellNumber` int(11) NOT NULL,
  `parentCell1` int(10) NOT NULL,
  `parentCell2` int(10) NOT NULL,
  `travelMethod` text NOT NULL,
  `arrivalDate` date NOT NULL,
  `arrivalTime` time NOT NULL,
  `airportPickupTime` time DEFAULT NULL,
  `method` text NOT NULL,
  `shuttleNeeded` text NOT NULL,
  `city` text NOT NULL,
  `airportCode` int(11) NOT NULL,
  `airline` text NOT NULL,
  `terminal` text NOT NULL,
  `flightNumber` int(11) NOT NULL,
  `taEscort` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mostec_flights_2017`
--

INSERT INTO `mostec_flights_2017` (`firstName`, `lastName`, `cellNumber`, `parentCell1`, `parentCell2`, `travelMethod`, `arrivalDate`, `arrivalTime`, `airportPickupTime`, `method`, `shuttleNeeded`, `city`, `airportCode`, `airline`, `terminal`, `flightNumber`, `taEscort`) VALUES
('Kidist', 'Adamu', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:00:00', '12:00:00', 'Shuttle', 'Yes', 'Atlanta', 0, 'Southwest', 'A', 187, 'Shift 2'),
('Esther', 'Adegoke', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Maxine', 'Aguilar', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '07:35:00', '09:00:00', 'Shuttle', 'Yes', 'Chicago', 0, 'Southwest', 'A', 1707, 'Shift '),
('Munira', 'Alimire', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '11:26:00', '01:00:00', 'Shuttle', 'Yes', 'St.Paul ', 0, 'United ', 'B', 1191, 'Shift 2'),
('Orlando', 'Anaya', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '05:56:00', '07:00:00', 'Shuttle', 'Yes', 'Phoenix', 0, 'American ', 'B', 2399, 'Shift 1'),
('Aemu', 'Anteneh', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '09:59:00', '11:00:00', 'Shuttle', 'Yes', 'Washington D.C.', 0, 'JetBlue', 'C', 56, 'Shift 2'),
('Ana', 'Ardila', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:00:00', '12:00:00', 'Shuttle', 'Yes', 'Orlando', 0, 'Southwest ', 'A', 200, 'Shift 2'),
('Saul', 'Arias', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Omoruyi', 'Atekha', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '00:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Carlos', 'Ayala Bellido', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '12:30:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Emmanuel', 'Aybar Estrella', 2147483647, 2147483647, 0, 'MBTA', '2017-08-01', '11:00:00', '00:00:00', 'MBTA', 'No', '', 0, '', '', 0, ''),
('Benjamin', 'Barrera', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:15:00', '02:00:00', 'Shuttle', 'Yes', 'Houston', 0, 'Southwest ', 'A', 1745, 'Shift 2'),
('Claudia', 'Cabral', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '10:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Nicolas', 'Caminero', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '11:33:00', '01:00:00', 'Shuttle', 'Yes', 'Fort Lauderdale', 0, 'Spirit', 'B', 610, ''),
('Donovan', 'Carr', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '11:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Carlos', 'Castillo', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '09:59:00', '11:00:00', 'Shuttle', 'Yes', 'Atlanta', 0, 'Delta ', 'A', 2594, 'Shift 2'),
('Alejandro', 'Castro Macias', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '12:28:00', '02:00:00', 'Shuttle', 'Yes', 'Houston', 0, 'United', 'B', 0, 'Shift 2'),
('Diana', 'Contreras', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Lord', 'Crawford', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '10:30:00', '12:00:00', 'Shuttle', 'Yes', 'New York City', 0, 'JetBlue', 'C', 632, 'Shift 2'),
('Solomina', 'Darko', 2037689824, 2037689824, 2035250433, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Even', 'Davila', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:55:00', '03:00:00', 'Shuttle', 'Yes', 'Brownsville', 0, 'American', 'B', 0, 'Shift 2'),
('Suuba', 'Demby', 2147483647, 2147483647, 2147483647, 'Parent', '0000-00-00', '00:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Kayla', 'DeSoto', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '05:31:00', '07:00:00', 'Shuttle', 'Yes', 'Las Vegas', 0, 'JetBlue ', 'C', 878, 'Shift 1'),
('Kristie', 'Diep', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '07:07:00', '08:00:00', 'Shuttle', 'Yes', 'Los Angeles', 0, 'United', 'C', 1225, 'Shift 1'),
('Manuel', 'Dominguez', 2142267486, 2142267486, 2145002992, 'Air', '2017-08-01', '11:58:00', '01:00:00', 'Shuttle', 'Yes', 'Dallas/Ft. Worth', 0, 'Spirit', 'B', 254, 'Shift 2'),
('Justin', 'Du', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '09:30:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Sergio', 'Echeverria', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:33:00', '01:00:00', 'Shuttle', 'Yes', 'Fort Lauderdale', 0, 'Spirit', 'B', 0, 'Shift 2'),
('Chukwuka', 'Emuwa', 2023753534, 2023753534, 2024928134, 'Air', '2017-08-01', '12:14:00', '01:00:00', 'Shuttle', 'Yes', 'Washington D.C.', 0, 'American ', 'B', 2139, 'Shift 2'),
('Jean-Rafael', 'Ereyi', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '10:08:00', '11:00:00', 'Shuttle', 'Yes', 'Charlotte', 0, 'American ', 'B', 1980, ''),
('Rafael', 'Esteves', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '02:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Riley', 'Flores', 2017256645, 2017256645, 2017258565, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Luis', 'Franco', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '00:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Albert', 'Garcia', 2147483647, 2147483647, 0, 'Parent', '2017-08-01', '00:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Adrian', 'Garza', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:55:00', '03:00:00', 'Shuttle', 'Yes', 'Dallas/Ft. Worth', 0, 'American ', 'B', 1094, 'Shift 2'),
('Ricardo Jr', ' Gayle', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '09:44:00', '11:00:00', 'Shuttle', 'Yes', 'Philadelphia', 0, 'Jetblue', 'C', 0, ''),
('Danielle', 'Geathers', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '10:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Miles', 'George', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '00:00:00', '00:00:00', 'Car', '', '', 0, '', '', 0, ''),
('Elissa', 'Gibson', 2147483647, 2147483647, 0, 'Parent', '2017-07-31', '11:00:00', '12:00:00', 'Shuttle', 'No', 'Atlanta', 0, 'Southwest', 'A', 187, ''),
('Angel', 'Gomez', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '11:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Paolina', 'Gonzales', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '01:15:00', '02:00:00', 'Shuttle', 'Yes', 'Houston', 0, 'Southwest ', 'A', 1745, 'Shift 2'),
('Ronald', 'Gonzalez', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '11:00:00', '12:00:00', 'Shuttle', 'Yes', 'Orlando', 0, 'Southwest', 'A', 200, 'Shift 2'),
('Gabriel', 'Grajeda', 2147483647, 2147483647, 2147483647, 'MBTA', '2017-08-01', '02:00:00', '00:00:00', '', 'No', '', 0, '', '', 0, ''),
('Daniela', 'Gross', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Fernando', 'Hernandez', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '05:34:00', '07:00:00', 'Shuttle', 'Yes', 'San Diego', 0, 'JetBlue', 'C', 20, 'Shift 1'),
('Minh', 'Hoang', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:00:00', '01:15:00', 'Uber', 'Yes', 'San Jose', 0, 'Southwest ', 'A', 3815, 'Shift 1'),
('Ashley', 'Holton', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '10:46:00', '12:00:00', 'Shuttle', 'Yes', 'St.Paul ', 0, 'Delta ', 'A', 0, 'Shift 2'),
('Sophia', 'Horowicz', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '08:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Sophie', 'Howell', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '10:30:00', '00:00:00', '', 'No', '', 0, 'Delta', '', 2792, ''),
('Jordan', 'Huyghue', 2147483647, 2147483647, 0, 'Parent', '2017-08-01', '09:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Valeria', 'Jimenez', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '11:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Devin', 'Johnson', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '08:44:00', '10:00:00', 'Shuttle', 'Yes', 'New York City', 0, 'Delta', 'A', 0, ''),
('Faduma', 'Khalif', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '09:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Iris', 'Kim', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '12:28:00', '02:00:00', 'Shuttle', 'Yes', 'Austin', 0, 'United', 'B', 0, 'Shift 2'),
('Aaron', 'Leiss', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '09:33:00', '11:00:00', 'Shuttle', 'Yes', 'Detroit', 0, 'Delta', 'A', 2437, 'Shift 2'),
('Jacob', 'Lerma', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:15:00', '02:00:00', 'Shuttle', 'Yes', 'Corpus Christi', 0, 'Southwest ', 'A', 667, 'Shift 2'),
('Mario', 'Leyva', 2064077084, 2064077084, 2147483647, 'Air', '2017-08-01', '07:07:00', '08:00:00', 'Shuttle', 'Yes', 'Los Angeles ', 0, 'United ', 'C', 1225, 'Shift 1'),
('Isabelle', 'Lilienthal', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:00:00', '12:00:00', 'Shuttle', 'Yes', 'Orlando', 0, 'Southwest ', 'A', 200, 'Shift 2'),
('Kerlina', 'Liu', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '09:16:00', '10:00:00', 'Shuttle', 'Yes', 'Chicago', 0, 'JetBlue', 'C', 412, 'Shift 2'),
('Andrea', 'Llamas', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '10:16:00', '11:00:00', 'Shuttle', 'Yes', 'Miami', 0, 'American ', 'B', 1509, 'Shift 2'),
('Bryan', 'Lopez', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '12:28:00', '02:00:00', 'Shuttle', 'Yes', 'Harlingen', 0, 'United', 'B', 3427, 'Shift 2'),
('David', 'Lopez', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '06:30:00', '08:00:00', 'Shuttle', 'Yes', 'Los Angeles ', 0, 'Delta', 'A', 0, 'Shift 1'),
('Alexis', 'Mack', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '01:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Renata', 'Martinez', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:55:00', '03:00:00', 'Shuttle', 'Yes', 'Brownsville ', 0, 'American', 'B', 5940, 'Shift 2'),
('*Kevin', 'Marx', 2147483647, 2147483647, 0, 'MBTA', '2017-08-01', '11:00:00', '00:00:00', 'MBTA', 'No', 'Boston', 0, '', '', 0, ''),
('Nicholas', 'Mijares', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:33:00', '01:00:00', 'Shuttle', 'Yes', 'Fort Lauderdale', 0, 'Spirit', 'B', 0, 'Shift 2'),
('Izabella', 'Moran', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '09:16:00', '10:00:00', 'Shuttle', 'Yes', 'Chicago', 0, 'JetBlue ', 'C', 412, 'Shift 2'),
('Joalda', 'Morancy', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '11:00:00', '12:00:00', 'Shuttle', 'Yes', 'Orlando', 0, 'Southwest', 'A', 200, 'Shift 2'),
('Lisa', 'Moshiro', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '09:49:00', '11:00:00', 'Shuttle', 'Yes', 'Washington D.C', 0, '', '', 0, 'Shift 2'),
('Ashley', 'Muller', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '08:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Jepchirchir', 'Mutwol', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:58:00', '01:00:00', 'Shuttle', 'Yes', 'Dallas/Forth Worth International Airport', 0, 'Spirit ', 'B', 254, 'Shift 2'),
('Richard', 'Nabahe', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '05:42:00', '07:00:00', 'Shuttle', 'Yes', 'San Francisco', 0, 'Delta ', 'A', 2818, 'Shift 1'),
('Duy', 'Nguyen', 2147483647, 2147483647, 0, 'Parent', '2017-08-01', '07:07:00', '00:00:00', 'Car', 'No', 'Los Angeles', 0, '', '', 0, ''),
('Serena', 'Nguyen', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:12:00', '12:00:00', 'Shuttle', 'Yes', 'Nashville', 0, 'Delta ', 'A', 2485, 'Shift 2'),
('Mikael', 'Nida', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', '', '', 0, '', '', 0, ''),
('Claire', 'Olivas', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:27:00', '03:00:00', 'Shuttle', 'Yes', 'Houston', 0, 'United', 'B', 362, 'Shift 2'),
('Rafael', 'Olivera-Cintron', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '09:13:00', '10:00:00', 'Shuttle', 'Yes', 'Orlando', 0, 'Jetblue  ', 'C', 52, 'Shift 2'),
('Ozioma', 'Ozor-Ilo', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:12:00', '12:00:00', 'Shuttle', 'Yes', 'Atlanta', 0, 'Delta', 'A', 2796, 'Shift 2'),
('Luis', 'Pabon', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '12:28:00', '02:00:00', 'Shuttle', 'Yes', 'Houston', 0, 'United ', 'B', 1253, 'Shift 2'),
('Monica', 'Patino', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '09:16:00', '10:00:00', 'Shuttle', 'Yes', 'Chicago', 0, 'Jetblue ', 'C', 0, 'Shift 2'),
('Pedro', 'Pavao-Neto', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '10:20:00', '12:00:00', 'Shuttle', 'Yes', 'Miami', 0, 'American ', 'B', 1509, 'Shift 2'),
('Kelvin', 'Pierre', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '02:00:00', '00:00:00', 'Car', 'No', 'Atlanta', 0, '', '', 0, ''),
('Lucy', 'Qu', 2147483647, 2147483647, 2147483647, 'Bus (South Station)', '2017-08-01', '12:20:00', '01:00:00', 'Shuttle', 'Yes', 'New York City', 0, 'Greyhound', '', 0, 'Shift 2'),
('Andrea', 'Quinones', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '12:28:00', '02:00:00', 'Shuttle', 'Yes', 'Houston', 0, 'United ', 'B', 1253, 'Shift 2'),
('Sara', 'Recarey', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Diana', 'Renteria', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '10:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Daniela', 'Rodriguez', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:00:00', '00:00:00', '', 'No', '', 0, '', '', 0, ''),
('Sadey', 'Rodriguez', 2147483647, 2147483647, 2147483647, 'Air', '2017-07-31', '05:00:00', '07:00:00', 'Shuttle', 'Yes', 'Laredo', 0, 'American ', 'B', 2811, 'Shift 1'),
('Sebastian', 'Rodriguez', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Andrew', 'Sepulveda', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '07:45:00', '09:00:00', 'Shuttle', 'Yes', 'Los Angeles', 0, 'Virgin', 'C', 370, 'Shift 1'),
('Megha', 'Sharma', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '10:10:00', '11:00:00', 'Shuttle', 'Yes', 'Baltimore', 0, 'Southwest', 'A', 2083, 'Shift 2'),
('Nailah', 'Smith', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '11:12:00', '12:00:00', 'Shuttle', 'Yes', 'Atlanta', 0, 'Delta', 'A', 2796, 'Shift 2'),
('Briana', 'Soriano', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '07:07:00', '08:00:00', 'Shuttle', 'Yes', 'Los Angeles', 0, 'United', 'C', 1225, 'Shift 1'),
('Jonathan', 'Sultan', 2147483647, 2147483647, 0, 'Train (South Station), Parent', '2017-07-31', '10:00:00', '00:00:00', '', 'No', 'Ft. Lauderdale ', 0, 'United', 'B', 0, ''),
('Sovanny', 'Taylor', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '00:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Isabella', 'Torres', 2067997549, 2067997549, 2066796589, 'Air', '2017-08-01', '07:21:00', '08:00:00', 'Shuttle', 'Yes', 'Seattle ', 0, 'Alaska ', 'A', 24, 'Shift 1'),
('Yahaira', 'Torres', 2147483647, 2147483647, 2147483647, 'Parent', '0000-00-00', '01:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Randy', 'Truong', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:51:00', '03:00:00', 'Shuttle', 'Yes', 'Orlando', 0, 'Delta ', 'A', 124, 'Shift 2'),
('Sebastian', 'Tsai', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '07:07:00', '08:00:00', 'Shuttle', 'Yes', 'Los Angeles', 0, 'United', 'C', 1225, 'Shift 1'),
('Brooke', 'Turpeau', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '12:18:00', '01:00:00', 'Shuttle', 'Yes', 'Atlanta', 0, 'JetBlue', 'C', 396, 'Shift 2'),
('Ayanna', 'Vasquez', 2147483647, 2147483647, 0, 'Parent', '2017-08-01', '11:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Maythe', 'Vega', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:55:00', '03:00:00', 'Shuttle', 'Yes', 'Brownsville ', 0, 'American', 'B', 5940, 'Shift 2'),
('Bryant', 'Villamil', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '07:07:00', '08:00:00', 'Shuttle', 'Yes', 'Los Angeles ', 0, 'United', 'C', 1225, 'Shift 1'),
('Rhiannan', 'Wackes', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '01:30:00', '03:00:00', 'Shuttle', 'Yes', 'Baltimore', 0, 'Southwest', 'A', 1965, 'Shift 2'),
('Paul', 'Wehling', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '10:48:00', '12:00:00', 'Shuttle', 'Yes', 'St. Paul ', 0, 'Delta', 'A', 0, 'Shift 2'),
('Remington', 'Wichterman', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '05:56:00', '07:00:00', 'Shuttle', 'Yes', 'Phoenix', 0, 'American', 'B', 2399, 'Shift 1'),
('Cathy', 'Wiesinger', 2147483647, 2147483647, 2147483647, 'Parent', '2017-08-01', '12:00:00', '00:00:00', 'Car', 'No', '', 0, '', '', 0, ''),
('Arthur', 'Willis', 2147483647, 2147483647, 2147483647, 'Air', '2017-08-01', '10:45:00', '12:00:00', 'Shuttle', 'Yes', 'Chicago  ', 0, 'Southwest', 'A', 107, 'Shift 2'),
('Djana', 'Wright', 2147483647, 2147483647, 0, 'Air', '2017-08-01', '01:16:00', '02:00:00', 'Shuttle', 'Yes', 'Chicago  ', 0, 'American', 'B', 1257, 'Shift 2');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
