-- Adminer 4.8.1 MySQL 10.4.28-MariaDB dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `inventario_v1.0` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `inventario_v1.0`;

DROP TABLE IF EXISTS `actualizado`;
CREATE TABLE `actualizado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(10) NOT NULL,
  `responsable` varchar(20) NOT NULL,
  `fecha_baja` varchar(20) NOT NULL,
  `fecha_alta` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `actualizado` (`id`, `status`, `responsable`, `fecha_baja`, `fecha_alta`) VALUES
(1,	'activo',	'aa1',	'24/02/2024',	'24/05/2008');

DROP TABLE IF EXISTS `materiales`;
CREATE TABLE `materiales` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(40) NOT NULL,
  `descripcion` text NOT NULL,
  `fecha_alta` varchar(20) NOT NULL,
  `status` varchar(10) NOT NULL,
  `responsable` varchar(20) NOT NULL,
  `fecha_baja` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

INSERT INTO `materiales` (`id`, `codigo`, `descripcion`, `fecha_alta`, `status`, `responsable`, `fecha_baja`) VALUES
(1,	'aa1',	'computadora completa',	'24/05/2008',	'activo',	'aa1',	''),
(2,	'a',	'monitores',	'25/08/2008',	'activo',	'aa1',	''),
(3,	'a',	'a',	'a',	'Habilitado',	'a',	'a'),
(4,	'a',	'a',	'a',	'Habilitado',	'a',	'a'),
(5,	'b',	'b',	'b',	'Habilitado',	'b',	'b'),
(6,	'f',	'f',	'f',	'Deshabilit',	'f',	'f');

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clave_empleado` varchar(15) NOT NULL,
  `apellido_paterno` varchar(50) NOT NULL,
  `apellido_materno` varchar(50) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

INSERT INTO `usuarios` (`id`, `clave_empleado`, `apellido_paterno`, `apellido_materno`, `nombre`) VALUES
(1,	'aa1',	'Martinez',	'Medina',	'Jose G'),
(2,	'aa2',	'JOSE GUADALUPE',	'GOCHI',	'VERGARA'),
(3,	'aa3',	'MANUEL',	'MEJIA',	'DIAZ'),
(4,	'aa4',	'MARIO',	'VERGARA',	'RIOS'),
(5,	'aa5',	'MANUEL',	'JIMENEZ',	'MORENO'),
(6,	'dsadas',	'dsadas',	'dsadsa',	'dassda'),
(7,	'dsadas',	'dasdas',	'dsadas',	'dsads'),
(8,	'dsadsa',	'dasdsa',	'dasdas',	'dasdsa'),
(9,	'q',	'q',	'q',	'q'),
(10,	'a',	'a',	'a',	'a'),
(11,	'q',	'q',	'q',	'q');

-- 2024-08-02 00:32:55
