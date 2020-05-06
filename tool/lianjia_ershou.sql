CREATE TABLE `ershou` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `district` varchar(50) DEFAULT NULL,
  `area` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `desc` varchar(256) DEFAULT NULL,
  `pic` varchar(256) DEFAULT NULL,
  `lianjia_id` varchar(50) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;