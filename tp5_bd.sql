-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-10-2024 a las 22:16:33
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tp5_bd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `stores`
--

CREATE TABLE `stores` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `stores`
--

INSERT INTO `stores` (`id`, `name`, `address`) VALUES
(1, 'Store Brian', '3 4174'),
(2, 'Deportes Dani', '25 2525'),
(3, 'Kiosco 24hs', '13 145'),
(4, 'Store 9', '9 9'),
(5, 'Store 10', '10 10'),
(6, 'Store 11', '11 11'),
(7, 'Store 12', '12 12'),
(8, 'Store 13', '13 13'),
(9, 'Store 14', '14 14'),
(10, 'Store 15', '15 15'),
(12, 'Store16', '16 16');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `rol` varchar(255) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `store_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `password`, `rol`, `telephone`, `address`, `status`, `store_id`) VALUES
(5, 'Brian Frank', 'brianfrank@gmail.com', 'pruebapass', 'Administrador', '2215246622', '4 4171', 'Activo', 1),
(6, 'Juancito', 'juancito@ve.com', '12345', 'Administrador', '12323', '1 e1', 'Activo', 1),
(8, 'Santiago', 's', 'q', 'Administrador', '77777', '666 elm st', 'Activo', 1),
(9, 'Pepe', 'pepe@gmail.com', 'pepe1234', 'Empleado', '121231', 'avenidasiempreviva', 'Activo', 1),
(10, 'Daniel', 'dani@mail.com', 'dani55', 'Empleado', '5551212', '77 777', 'Activo', 1),
(12, 'luis', 'luis@mail.com', 'HRELwD60', 'Empleado', '5451111', '1 123', 'Activo', 2),
(13, 'ana', 'ana@mail.com', 'kM7Wwfvl', 'Empleado', '7789999', '88 888', 'Activo', 3),
(14, 'emilia', 'emi@mail.com', 'OW4cJdIN', 'Empleado', '5253333', '55 455', 'Activo', 4),
(15, 'fernando', 'fer@mail.com', 'iY2joxMw', 'Empleado', '6655656', '68 777', 'Activo', 1),
(16, 'soledad', 'sole@mail.com', 'kN2cxKjE', 'Empleado', '5554455', '46 555', 'Activo', 2),
(20, 'Rolo', 'rolo@mail.com', 'Y4ltBC67', 'Empleado', '5561111', '12 23', 'Bloqueado', 10),
(21, 'lali', 'lali@mail.com', 'IQaOS4E3', 'Empleado', '7778888', '79 79', 'Activo', 8);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `stores`
--
ALTER TABLE `stores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `stores`
--
ALTER TABLE `stores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
