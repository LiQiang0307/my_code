/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50016
Source Host           : localhost:3306
Source Database       : chuzhandong

Target Server Type    : MYSQL
Target Server Version : 50016
File Encoding         : 65001

Date: 2021-04-24 23:19:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for 2020103173
-- ----------------------------
DROP TABLE IF EXISTS `2020103173`;
CREATE TABLE `2020103173` (
  `id` int(11) NOT NULL,
  `str_name` varchar(255) NOT NULL,
  `str_string` varchar(255) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of 2020103173
-- ----------------------------
INSERT INTO `2020103173` VALUES ('1', '初占东', '2020103173');
INSERT INTO `2020103173` VALUES ('2', '小明', '2020111111');
