/*
Navicat MySQL Data Transfer

Source Server         : 本地测试
Source Server Version : 50728
Source Host           : localhost:3306
Source Database       : colleagurcar

Target Server Type    : MYSQL
Target Server Version : 50728
File Encoding         : 65001

Date: 2020-01-10 18:30:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `authtoken_token`
-- ----------------------------
DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of authtoken_token
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('11', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('13', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('14', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('16', 'Can add Token', '6', 'add_token');
INSERT INTO `auth_permission` VALUES ('17', 'Can change Token', '6', 'change_token');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete Token', '6', 'delete_token');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 用户信息', '7', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 用户信息', '7', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 用户信息', '7', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 银行卡绑定', '8', 'add_bankcard');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 银行卡绑定', '8', 'change_bankcard');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 银行卡绑定', '8', 'delete_bankcard');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 轮播图', '9', 'add_banner');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 轮播图', '9', 'change_banner');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 轮播图', '9', 'delete_banner');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 系统信息推送顾客', '10', 'add_customermessage');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 系统信息推送顾客', '10', 'change_customermessage');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 系统信息推送顾客', '10', 'delete_customermessage');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 系统信息推送司机', '11', 'add_drivermessage');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 系统信息推送司机', '11', 'change_drivermessage');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 系统信息推送司机', '11', 'delete_drivermessage');
INSERT INTO `auth_permission` VALUES ('34', 'Can add 司机信息', '12', 'add_driverprofile');
INSERT INTO `auth_permission` VALUES ('35', 'Can change 司机信息', '12', 'change_driverprofile');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete 司机信息', '12', 'delete_driverprofile');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 审核记录', '13', 'add_examinelog');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 审核记录', '13', 'change_examinelog');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 审核记录', '13', 'delete_examinelog');
INSERT INTO `auth_permission` VALUES ('40', 'Can add 违规记录', '14', 'add_foullog');
INSERT INTO `auth_permission` VALUES ('41', 'Can change 违规记录', '14', 'change_foullog');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete 违规记录', '14', 'delete_foullog');
INSERT INTO `auth_permission` VALUES ('43', 'Can add 司机违规条目', '15', 'add_foulrule');
INSERT INTO `auth_permission` VALUES ('44', 'Can change 司机违规条目', '15', 'change_foulrule');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete 司机违规条目', '15', 'delete_foulrule');
INSERT INTO `auth_permission` VALUES ('46', 'Can add 总账目 - 虚拟', '16', 'add_drakbill');
INSERT INTO `auth_permission` VALUES ('47', 'Can change 总账目 - 虚拟', '16', 'change_drakbill');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete 总账目 - 虚拟', '16', 'delete_drakbill');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 行程订单', '17', 'add_cancellog');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 行程订单', '17', 'change_cancellog');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 行程订单', '17', 'delete_cancellog');
INSERT INTO `auth_permission` VALUES ('52', 'Can add 订单聊天记录', '18', 'add_chatmessage');
INSERT INTO `auth_permission` VALUES ('53', 'Can change 订单聊天记录', '18', 'change_chatmessage');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete 订单聊天记录', '18', 'delete_chatmessage');
INSERT INTO `auth_permission` VALUES ('55', 'Can add 行程评价', '19', 'add_coursecomments');
INSERT INTO `auth_permission` VALUES ('56', 'Can change 行程评价', '19', 'change_coursecomments');
INSERT INTO `auth_permission` VALUES ('57', 'Can delete 行程评价', '19', 'delete_coursecomments');
INSERT INTO `auth_permission` VALUES ('58', 'Can add 顾客行程广场', '20', 'add_customersquare');
INSERT INTO `auth_permission` VALUES ('59', 'Can change 顾客行程广场', '20', 'change_customersquare');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete 顾客行程广场', '20', 'delete_customersquare');
INSERT INTO `auth_permission` VALUES ('61', 'Can add 司机行程广场', '21', 'add_driversquare');
INSERT INTO `auth_permission` VALUES ('62', 'Can change 司机行程广场', '21', 'change_driversquare');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete 司机行程广场', '21', 'delete_driversquare');
INSERT INTO `auth_permission` VALUES ('64', 'Can add 行程订单', '22', 'add_order');
INSERT INTO `auth_permission` VALUES ('65', 'Can change 行程订单', '22', 'change_order');
INSERT INTO `auth_permission` VALUES ('66', 'Can delete 行程订单', '22', 'delete_order');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('6', 'authtoken', 'token');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('11', 'examine', 'drivermessage');
INSERT INTO `django_content_type` VALUES ('12', 'examine', 'driverprofile');
INSERT INTO `django_content_type` VALUES ('13', 'examine', 'examinelog');
INSERT INTO `django_content_type` VALUES ('14', 'examine', 'foullog');
INSERT INTO `django_content_type` VALUES ('15', 'examine', 'foulrule');
INSERT INTO `django_content_type` VALUES ('16', 'operation', 'drakbill');
INSERT INTO `django_content_type` VALUES ('17', 'order', 'cancellog');
INSERT INTO `django_content_type` VALUES ('18', 'order', 'chatmessage');
INSERT INTO `django_content_type` VALUES ('19', 'order', 'coursecomments');
INSERT INTO `django_content_type` VALUES ('20', 'order', 'customersquare');
INSERT INTO `django_content_type` VALUES ('21', 'order', 'driversquare');
INSERT INTO `django_content_type` VALUES ('22', 'order', 'order');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('8', 'users', 'bankcard');
INSERT INTO `django_content_type` VALUES ('9', 'users', 'banner');
INSERT INTO `django_content_type` VALUES ('10', 'users', 'customermessage');
INSERT INTO `django_content_type` VALUES ('7', 'users', 'userprofile');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-12-30 09:44:41.081209');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2019-12-30 09:44:41.157005');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2019-12-30 09:44:41.398360');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2019-12-30 09:44:41.443237');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2019-12-30 09:44:41.450225');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2019-12-30 09:44:41.461217');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2019-12-30 09:44:41.468171');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2019-12-30 09:44:41.471165');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2019-12-30 09:44:41.478161');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2019-12-30 09:44:41.485125');
INSERT INTO `django_migrations` VALUES ('11', 'users', '0001_initial', '2019-12-30 09:44:41.970824');
INSERT INTO `django_migrations` VALUES ('12', 'admin', '0001_initial', '2019-12-30 09:44:42.101978');
INSERT INTO `django_migrations` VALUES ('13', 'admin', '0002_logentry_remove_auto_add', '2019-12-30 09:44:42.111953');
INSERT INTO `django_migrations` VALUES ('14', 'authtoken', '0001_initial', '2019-12-30 09:44:42.185754');
INSERT INTO `django_migrations` VALUES ('15', 'authtoken', '0002_auto_20160226_1747', '2019-12-30 09:44:42.270555');
INSERT INTO `django_migrations` VALUES ('16', 'examine', '0001_initial', '2019-12-30 09:44:42.684874');
INSERT INTO `django_migrations` VALUES ('17', 'examine', '0002_auto_20191229_2128', '2019-12-30 09:44:43.116742');
INSERT INTO `django_migrations` VALUES ('18', 'order', '0001_initial', '2019-12-30 09:44:43.280310');
INSERT INTO `django_migrations` VALUES ('19', 'operation', '0001_initial', '2019-12-30 09:44:43.306208');
INSERT INTO `django_migrations` VALUES ('20', 'operation', '0002_drakbill_trade_no', '2019-12-30 09:44:43.389983');
INSERT INTO `django_migrations` VALUES ('21', 'order', '0002_auto_20191229_1926', '2019-12-30 09:44:44.061304');
INSERT INTO `django_migrations` VALUES ('22', 'sessions', '0001_initial', '2019-12-30 09:44:44.101165');
INSERT INTO `django_migrations` VALUES ('23', 'users', '0002_userprofile_is_driver', '2019-12-30 09:44:44.157016');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for `examine_drivermessage`
-- ----------------------------
DROP TABLE IF EXISTS `examine_drivermessage`;
CREATE TABLE `examine_drivermessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(500) NOT NULL,
  `has_read` varchar(30) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `examine_drivermessag_receiver_id_c4c8c0c3_fk_examine_d` (`receiver_id`),
  CONSTRAINT `examine_drivermessag_receiver_id_c4c8c0c3_fk_examine_d` FOREIGN KEY (`receiver_id`) REFERENCES `examine_driverprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of examine_drivermessage
-- ----------------------------

-- ----------------------------
-- Table structure for `examine_driverprofile`
-- ----------------------------
DROP TABLE IF EXISTS `examine_driverprofile`;
CREATE TABLE `examine_driverprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `driver_score` int(11) NOT NULL,
  `driver_status` varchar(11) DEFAULT NULL,
  `driver_money` varchar(100) NOT NULL,
  `add_time` date NOT NULL,
  `user_id_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `examine_driverprofil_user_id_id_deb2be9d_fk_users_use` (`user_id_id`),
  CONSTRAINT `examine_driverprofil_user_id_id_deb2be9d_fk_users_use` FOREIGN KEY (`user_id_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of examine_driverprofile
-- ----------------------------

-- ----------------------------
-- Table structure for `examine_examinelog`
-- ----------------------------
DROP TABLE IF EXISTS `examine_examinelog`;
CREATE TABLE `examine_examinelog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `license` varchar(100) NOT NULL,
  `f_id_card` varchar(100) NOT NULL,
  `b_id_card` varchar(100) NOT NULL,
  `f_car` varchar(100) NOT NULL,
  `l_car` varchar(100) NOT NULL,
  `r_car` varchar(100) NOT NULL,
  `status` varchar(30) DEFAULT NULL,
  `add_time` datetime(6) NOT NULL,
  `applicant_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `examine_examinelog_applicant_id_265b87fb_fk_examine_d` (`applicant_id`),
  CONSTRAINT `examine_examinelog_applicant_id_265b87fb_fk_examine_d` FOREIGN KEY (`applicant_id`) REFERENCES `examine_driverprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of examine_examinelog
-- ----------------------------

-- ----------------------------
-- Table structure for `examine_foullog`
-- ----------------------------
DROP TABLE IF EXISTS `examine_foullog`;
CREATE TABLE `examine_foullog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `applicant_id` int(11) NOT NULL,
  `foul_rule_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `examine_foullog_applicant_id_f570f233_fk_examine_d` (`applicant_id`),
  KEY `examine_foullog_foul_rule_id_ecef9b7e_fk_examine_foulrule_id` (`foul_rule_id`),
  CONSTRAINT `examine_foullog_applicant_id_f570f233_fk_examine_d` FOREIGN KEY (`applicant_id`) REFERENCES `examine_driverprofile` (`id`),
  CONSTRAINT `examine_foullog_foul_rule_id_ecef9b7e_fk_examine_foulrule_id` FOREIGN KEY (`foul_rule_id`) REFERENCES `examine_foulrule` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of examine_foullog
-- ----------------------------

-- ----------------------------
-- Table structure for `examine_foulrule`
-- ----------------------------
DROP TABLE IF EXISTS `examine_foulrule`;
CREATE TABLE `examine_foulrule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `s_name` varchar(6) NOT NULL,
  `msg` varchar(6) NOT NULL,
  `deduction` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of examine_foulrule
-- ----------------------------

-- ----------------------------
-- Table structure for `operation_drakbill`
-- ----------------------------
DROP TABLE IF EXISTS `operation_drakbill`;
CREATE TABLE `operation_drakbill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_money` int(11) NOT NULL,
  `add_time` date NOT NULL,
  `trade_no_id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_drakbill_trade_no_id_017888bd_fk_order_order_trade_no` (`trade_no_id`),
  CONSTRAINT `operation_drakbill_trade_no_id_017888bd_fk_order_order_trade_no` FOREIGN KEY (`trade_no_id`) REFERENCES `order_order` (`trade_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of operation_drakbill
-- ----------------------------

-- ----------------------------
-- Table structure for `order_cancellog`
-- ----------------------------
DROP TABLE IF EXISTS `order_cancellog`;
CREATE TABLE `order_cancellog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cancel` varchar(50) NOT NULL,
  `punish` varchar(50) NOT NULL,
  `overtime` varchar(50) NOT NULL,
  `deduction` varchar(50) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_cancellog_order_id_918695b1_fk_order_order_id` (`order_id`),
  CONSTRAINT `order_cancellog_order_id_918695b1_fk_order_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_cancellog
-- ----------------------------

-- ----------------------------
-- Table structure for `order_chatmessage`
-- ----------------------------
DROP TABLE IF EXISTS `order_chatmessage`;
CREATE TABLE `order_chatmessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(500) NOT NULL,
  `sender` varchar(30) NOT NULL,
  `has_read` varchar(30) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_chatmessage_order_id_c7f74bcf_fk_order_order_id` (`order_id`),
  CONSTRAINT `order_chatmessage_order_id_c7f74bcf_fk_order_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_chatmessage
-- ----------------------------

-- ----------------------------
-- Table structure for `order_coursecomments`
-- ----------------------------
DROP TABLE IF EXISTS `order_coursecomments`;
CREATE TABLE `order_coursecomments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `star` int(11) NOT NULL,
  `c_label` varchar(30) NOT NULL,
  `comments` varchar(200) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_coursecomments_order_id_a59a4878_fk_order_order_id` (`order_id`),
  CONSTRAINT `order_coursecomments_order_id_a59a4878_fk_order_order_id` FOREIGN KEY (`order_id`) REFERENCES `order_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_coursecomments
-- ----------------------------

-- ----------------------------
-- Table structure for `order_customersquare`
-- ----------------------------
DROP TABLE IF EXISTS `order_customersquare`;
CREATE TABLE `order_customersquare` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `origin` varchar(200) NOT NULL,
  `finish` varchar(200) NOT NULL,
  `remarks` varchar(200) NOT NULL,
  `mount` varchar(200) NOT NULL,
  `p_num` varchar(200) NOT NULL,
  `r_status` varchar(30) NOT NULL,
  `label_type` varchar(30) NOT NULL,
  `s_time` datetime(6) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `initiator_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_customersquare_initiator_id_8220aa3a_fk_users_use` (`initiator_id`),
  CONSTRAINT `order_customersquare_initiator_id_8220aa3a_fk_users_use` FOREIGN KEY (`initiator_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_customersquare
-- ----------------------------

-- ----------------------------
-- Table structure for `order_driversquare`
-- ----------------------------
DROP TABLE IF EXISTS `order_driversquare`;
CREATE TABLE `order_driversquare` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `origin` varchar(200) NOT NULL,
  `finish` varchar(200) NOT NULL,
  `remarks` varchar(200) NOT NULL,
  `mount` varchar(200) NOT NULL,
  `p_num` varchar(200) NOT NULL,
  `r_status` varchar(30) NOT NULL,
  `label_type` varchar(30) NOT NULL,
  `s_time` datetime(6) NOT NULL,
  `e_time` datetime(6) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `initiator_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_driversquare_initiator_id_b52fee18_fk_examine_d` (`initiator_id`),
  CONSTRAINT `order_driversquare_initiator_id_b52fee18_fk_examine_d` FOREIGN KEY (`initiator_id`) REFERENCES `examine_driverprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_driversquare
-- ----------------------------

-- ----------------------------
-- Table structure for `order_order`
-- ----------------------------
DROP TABLE IF EXISTS `order_order`;
CREATE TABLE `order_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(30) DEFAULT NULL,
  `trade_no` varchar(100) DEFAULT NULL,
  `pay_time` datetime(6) DEFAULT NULL,
  `mileage` varchar(200) NOT NULL,
  `origin` varchar(200) NOT NULL,
  `finish` varchar(200) NOT NULL,
  `take_time` varchar(200) NOT NULL,
  `amount` varchar(200) NOT NULL,
  `p_num` varchar(200) NOT NULL,
  `s_time` datetime(6) DEFAULT NULL,
  `e_time` datetime(6) DEFAULT NULL,
  `pay_status` varchar(30) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `driver_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_sn` (`order_sn`),
  UNIQUE KEY `trade_no` (`trade_no`),
  KEY `order_order_customer_id_5bbbd957_fk_users_userprofile_id` (`customer_id`),
  KEY `order_order_driver_id_f5d5d714_fk_examine_driverprofile_id` (`driver_id`),
  CONSTRAINT `order_order_customer_id_5bbbd957_fk_users_userprofile_id` FOREIGN KEY (`customer_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `order_order_driver_id_f5d5d714_fk_examine_driverprofile_id` FOREIGN KEY (`driver_id`) REFERENCES `examine_driverprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_order
-- ----------------------------

-- ----------------------------
-- Table structure for `users_bankcard`
-- ----------------------------
DROP TABLE IF EXISTS `users_bankcard`;
CREATE TABLE `users_bankcard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `card_num` varchar(200) NOT NULL,
  `bank` varchar(200) DEFAULT NULL,
  `add_time` date NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_bankcard_user_id_7510bdd6_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `users_bankcard_user_id_7510bdd6_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_bankcard
-- ----------------------------
INSERT INTO `users_bankcard` VALUES ('1', '4305784546579', '中行', '2019-12-31', '5');
INSERT INTO `users_bankcard` VALUES ('2', '46489711564564', '银行', '2019-12-31', '5');

-- ----------------------------
-- Table structure for `users_banner`
-- ----------------------------
DROP TABLE IF EXISTS `users_banner`;
CREATE TABLE `users_banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `image` varchar(200) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `index` int(11) NOT NULL,
  `add_time` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_banner
-- ----------------------------
INSERT INTO `users_banner` VALUES ('1', '1', '1', '1', '1', '2020-01-09');
INSERT INTO `users_banner` VALUES ('2', '2', '2', '2', '2', '2020-01-09');

-- ----------------------------
-- Table structure for `users_customermessage`
-- ----------------------------
DROP TABLE IF EXISTS `users_customermessage`;
CREATE TABLE `users_customermessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(500) NOT NULL,
  `has_read` varchar(30) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_customermessag_receiver_id_b1d03a2f_fk_users_use` (`receiver_id`),
  CONSTRAINT `users_customermessag_receiver_id_b1d03a2f_fk_users_use` FOREIGN KEY (`receiver_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_customermessage
-- ----------------------------

-- ----------------------------
-- Table structure for `users_userprofile`
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile`;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nick_name` varchar(50) NOT NULL,
  `birday` date DEFAULT NULL,
  `gender` varchar(6) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `home` varchar(100) NOT NULL,
  `company_address` varchar(100) NOT NULL,
  `company` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `credit_score` int(11) NOT NULL,
  `money` varchar(100) NOT NULL,
  `is_driver` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile
-- ----------------------------
INSERT INTO `users_userprofile` VALUES ('1', '123456', '2019-12-30 15:17:16.000000', '0', 'pqw', 'p', 'qw', 'aa', '1', '1', '2019-12-30 15:18:03.000000', 'pythonNB', '2019-12-30', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1');
INSERT INTO `users_userprofile` VALUES ('2', 'pbkdf2_sha256$36000$ipYaI0dliKtE$+x87i16xdYsanBEMRtxyohu22kVe/u1PGIxBctF5/08=', null, '0', '', '', '', '', '0', '1', '2019-12-30 15:58:19.052935', 'qwp', null, '男', '', '15681234566', 'users/images/default.png', '', '', '', '', '100', '0', '否');
INSERT INTO `users_userprofile` VALUES ('5', 'pbkdf2_sha256$36000$Oscs8NmwNdB9$4U9CsIVldRpOE/7Bn/0h/gNXCQBIok2iYEzk7fjUmbo=', null, '0', '123', '', '', '', '0', '1', '2019-12-30 16:01:30.009813', '132', null, '男', '', '15681234566', 'users/images/20191230/下载_vHOPCYs.jpg', '', '', '', '', '100', '0', '否');
INSERT INTO `users_userprofile` VALUES ('7', 'pbkdf2_sha256$36000$2bY3KQNGQbYq$o2h/X1Km6PlAb2VV2OepEUzi/ARp501rxlz6/fIkOVs=', null, '0', '12223', '', '', '', '0', '1', '2019-12-30 16:02:33.790233', 'qwp12', null, '男', '', '15681234566', 'users/images/default.png', '', '', '', '', '100', '0', '否');
INSERT INTO `users_userprofile` VALUES ('8', 'pbkdf2_sha256$36000$OIYZqFuJobMw$xC3XaMG5CBTtYdbkBHSqniLH3JPJsN67K6BjL+1wyug=', null, '0', '122232', '', '', '', '0', '1', '2019-12-30 16:03:08.274928', 'qwp12', null, '男', '', '15681234566', 'users/images/default.png', '', '', '', '', '100', '0', '否');

-- ----------------------------
-- Table structure for `users_userprofile_groups`
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_groups`;
CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_group_id_823cf2fc_uniq` (`userprofile_id`,`group_id`),
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_userprofile_gr_userprofile_id_a4496a80_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `users_userprofile_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `users_userprofile_user_permissions`;
CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_p_userprofile_id_permissio_d0215190_uniq` (`userprofile_id`,`permission_id`),
  KEY `users_userprofile_us_permission_id_393136b6_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_userprofile_us_permission_id_393136b6_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userprofile_us_userprofile_id_34544737_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_userprofile_user_permissions
-- ----------------------------
