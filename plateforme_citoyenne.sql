-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  mar. 18 mai 2021 à 15:12
-- Version du serveur :  8.0.18
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `plateforme_citoyenne`
--

-- --------------------------------------------------------

--
-- Structure de la table `activite_activites`
--

DROP TABLE IF EXISTS `activite_activites`;
CREATE TABLE IF NOT EXISTS `activite_activites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` int(10) UNSIGNED NOT NULL,
  `intitule` varchar(1000) NOT NULL,
  `resultat_attendu` varchar(1000) NOT NULL,
  `indicateur` varchar(255) NOT NULL,
  `cible` int(10) UNSIGNED NOT NULL,
  `cout` bigint(20) UNSIGNED NOT NULL,
  `resultat_atteints` longtext,
  `taux_execution` int(11) DEFAULT NULL,
  `cout_effective` bigint(20) UNSIGNED DEFAULT NULL,
  `observation` longtext,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  `devise_id` int(11) NOT NULL,
  `generic_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `activite_activites_devise_id_d8863d90_fk_activite_devise_id` (`devise_id`),
  KEY `activite_activites_generic_id_64f4b14b_fk_generique` (`generic_id`)
) ;

-- --------------------------------------------------------

--
-- Structure de la table `activite_activites_etiquette`
--

DROP TABLE IF EXISTS `activite_activites_etiquette`;
CREATE TABLE IF NOT EXISTS `activite_activites_etiquette` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `activites_id` int(11) NOT NULL,
  `etiquette_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `activite_activites_etiqu_activites_id_etiquette_i_a8df0873_uniq` (`activites_id`,`etiquette_id`),
  KEY `activite_activites_e_etiquette_id_b7063717_fk_activite_` (`etiquette_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `activite_activites_financement`
--

DROP TABLE IF EXISTS `activite_activites_financement`;
CREATE TABLE IF NOT EXISTS `activite_activites_financement` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `activites_id` int(11) NOT NULL,
  `sourcefinancement_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `activite_activites_finan_activites_id_sourcefinan_f50a2568_uniq` (`activites_id`,`sourcefinancement_id`),
  KEY `activite_activites_f_sourcefinancement_id_902d5254_fk_activite_` (`sourcefinancement_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `activite_activites_pogrammation`
--

DROP TABLE IF EXISTS `activite_activites_pogrammation`;
CREATE TABLE IF NOT EXISTS `activite_activites_pogrammation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `activites_id` int(11) NOT NULL,
  `programmephysique_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `activite_activites_pogra_activites_id_programmeph_20640524_uniq` (`activites_id`,`programmephysique_id`),
  KEY `activite_activites_p_programmephysique_id_62312bdd_fk_activite_` (`programmephysique_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `activite_activites_structure`
--

DROP TABLE IF EXISTS `activite_activites_structure`;
CREATE TABLE IF NOT EXISTS `activite_activites_structure` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `activites_id` int(11) NOT NULL,
  `structureresponsable_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `activite_activites_struc_activites_id_structurere_77840875_uniq` (`activites_id`,`structureresponsable_id`),
  KEY `activite_activites_s_structureresponsable_8dc970ad_fk_activite_` (`structureresponsable_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `activite_devise`
--

DROP TABLE IF EXISTS `activite_devise`;
CREATE TABLE IF NOT EXISTS `activite_devise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `devise` varchar(255) NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `devise` (`devise`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `activite_etiquette`
--

DROP TABLE IF EXISTS `activite_etiquette`;
CREATE TABLE IF NOT EXISTS `activite_etiquette` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `intitule` varchar(255) NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `intitule` (`intitule`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `activite_programmephysique`
--

DROP TABLE IF EXISTS `activite_programmephysique`;
CREATE TABLE IF NOT EXISTS `activite_programmephysique` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trimestre` varchar(255) NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `trimestre` (`trimestre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `activite_sourcefinancement`
--

DROP TABLE IF EXISTS `activite_sourcefinancement`;
CREATE TABLE IF NOT EXISTS `activite_sourcefinancement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source` varchar(255) NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `source` (`source`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `activite_structureresponsable`
--

DROP TABLE IF EXISTS `activite_structureresponsable`;
CREATE TABLE IF NOT EXISTS `activite_structureresponsable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nom` (`nom`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
CREATE TABLE IF NOT EXISTS `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `authtoken_token`
--

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`) VALUES
('df03c971b61fdae4ffe5358c47dd7d2a548de788', '2021-05-13 17:44:57.522236', 1);

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add devise', 7, 'add_devise'),
(26, 'Can change devise', 7, 'change_devise'),
(27, 'Can delete devise', 7, 'delete_devise'),
(28, 'Can view devise', 7, 'view_devise'),
(29, 'Can add etiquette', 8, 'add_etiquette'),
(30, 'Can change etiquette', 8, 'change_etiquette'),
(31, 'Can delete etiquette', 8, 'delete_etiquette'),
(32, 'Can view etiquette', 8, 'view_etiquette'),
(33, 'Can add source financement', 9, 'add_sourcefinancement'),
(34, 'Can change source financement', 9, 'change_sourcefinancement'),
(35, 'Can delete source financement', 9, 'delete_sourcefinancement'),
(36, 'Can view source financement', 9, 'view_sourcefinancement'),
(37, 'Can add structure responsable', 10, 'add_structureresponsable'),
(38, 'Can change structure responsable', 10, 'change_structureresponsable'),
(39, 'Can delete structure responsable', 10, 'delete_structureresponsable'),
(40, 'Can view structure responsable', 10, 'view_structureresponsable'),
(41, 'Can add Programmations Physique', 11, 'add_programmephysique'),
(42, 'Can change Programmations Physique', 11, 'change_programmephysique'),
(43, 'Can delete Programmations Physique', 11, 'delete_programmephysique'),
(44, 'Can view Programmations Physique', 11, 'view_programmephysique'),
(45, 'Can add Activité', 12, 'add_activites'),
(46, 'Can change Activité', 12, 'change_activites'),
(47, 'Can delete Activité', 12, 'delete_activites'),
(48, 'Can view Activité', 12, 'view_activites'),
(49, 'Can add Année', 13, 'add_annee'),
(50, 'Can change Année', 13, 'change_annee'),
(51, 'Can delete Année', 13, 'delete_annee'),
(52, 'Can view Année', 13, 'view_annee'),
(53, 'Can add structure', 14, 'add_structure'),
(54, 'Can change structure', 14, 'change_structure'),
(55, 'Can delete structure', 14, 'delete_structure'),
(56, 'Can view structure', 14, 'view_structure'),
(57, 'Can add niveau', 15, 'add_niveau'),
(58, 'Can change niveau', 15, 'change_niveau'),
(59, 'Can delete niveau', 15, 'delete_niveau'),
(60, 'Can view niveau', 15, 'view_niveau'),
(61, 'Can add generic table', 16, 'add_generictable'),
(62, 'Can change generic table', 16, 'change_generictable'),
(63, 'Can delete generic table', 16, 'delete_generictable'),
(64, 'Can view generic table', 16, 'view_generictable'),
(65, 'Can add Token', 17, 'add_token'),
(66, 'Can change Token', 17, 'change_token'),
(67, 'Can delete Token', 17, 'delete_token'),
(68, 'Can view Token', 17, 'view_token'),
(69, 'Can add token', 18, 'add_tokenproxy'),
(70, 'Can change token', 18, 'change_tokenproxy'),
(71, 'Can delete token', 18, 'delete_tokenproxy'),
(72, 'Can view token', 18, 'view_tokenproxy');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$XfzYEb5tdu4J9NkoKX5xWf$GHRwpoqI6h3FT2ZKlujtW4aTRgA7nnyrWRXas/OTwTw=', '2021-05-18 13:49:13.356730', 1, 'salsec', '', '', 'zsalsec@gmail.com', 1, 1, '2021-05-12 11:27:54.777680');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ;

--
-- Déchargement des données de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-05-12 11:36:55.503911', '1', 'PAM', 1, '[{\"added\": {}}]', 14, 1),
(2, '2021-05-13 15:36:14.316869', '1', 'salsec', 2, '[]', 4, 1),
(3, '2021-05-13 17:44:57.537235', '1', 'df03c971b61fdae4ffe5358c47dd7d2a548de788', 1, '[{\"added\": {}}]', 18, 1),
(4, '2021-05-18 13:50:07.598297', '2', 'ANPTIC', 1, '[{\"added\": {}}]', 14, 1);

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(12, 'activite', 'activites'),
(7, 'activite', 'devise'),
(8, 'activite', 'etiquette'),
(11, 'activite', 'programmephysique'),
(9, 'activite', 'sourcefinancement'),
(10, 'activite', 'structureresponsable'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(17, 'authtoken', 'token'),
(18, 'authtoken', 'tokenproxy'),
(5, 'contenttypes', 'contenttype'),
(13, 'generiquemodel', 'annee'),
(16, 'generiquemodel', 'generictable'),
(15, 'generiquemodel', 'niveau'),
(14, 'generiquemodel', 'structure'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-05-12 11:23:15.624028'),
(2, 'auth', '0001_initial', '2021-05-12 11:23:57.345841'),
(3, 'admin', '0001_initial', '2021-05-12 11:24:04.076661'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-05-12 11:24:04.137253'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-05-12 11:24:04.200827'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-05-12 11:24:10.826200'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-05-12 11:24:16.291904'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-05-12 11:24:18.729952'),
(9, 'auth', '0004_alter_user_username_opts', '2021-05-12 11:24:18.778625'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-05-12 11:24:20.571055'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-05-12 11:24:20.661179'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-05-12 11:24:20.881230'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-05-12 11:24:27.917934'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-05-12 11:24:30.894967'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-05-12 11:24:33.026300'),
(16, 'auth', '0011_update_proxy_permissions', '2021-05-12 11:24:33.114707'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-05-12 11:24:35.698459'),
(18, 'sessions', '0001_initial', '2021-05-12 11:24:36.964602'),
(19, 'generiquemodel', '0001_initial', '2021-05-12 11:25:45.218671'),
(20, 'activite', '0001_initial', '2021-05-12 11:26:50.326195'),
(21, 'authtoken', '0001_initial', '2021-05-13 17:29:25.810545'),
(22, 'authtoken', '0002_auto_20160226_1747', '2021-05-13 17:29:25.925544'),
(23, 'authtoken', '0003_tokenproxy', '2021-05-13 17:29:25.975544');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('adpn9djyk9f99ebikgd4jou4xiwkxtiv', '.eJxVjEEOgjAQRe_StWmmpdDWpXvO0Mx0BosaSCisjHcXEha6_e-9_1YJt7WkrcqSRlZXZdTldyPMT5kOwA-c7rPO87QuI-lD0Setup9ZXrfT_TsoWMteC7Ej8sIxBMhDFGaEgXzECF1A2zY0OPBNa9pAXYBI2WUgsyfirAX1-QIQsDhg:1lgn9q:VIta39EALKBJr7779TW02y07R45wcRCUZh7XCQzQI2I', '2021-05-26 11:36:06.079256'),
('hbu0uk52mazcdwrisv427ef9z81aq2rl', '.eJxVjEEOgjAQRe_StWmmpdDWpXvO0Mx0BosaSCisjHcXEha6_e-9_1YJt7WkrcqSRlZXZdTldyPMT5kOwA-c7rPO87QuI-lD0Setup9ZXrfT_TsoWMteC7Ej8sIxBMhDFGaEgXzECF1A2zY0OPBNa9pAXYBI2WUgsyfirAX1-QIQsDhg:1lhDMF:74PnGt_33i2f7BtBOsMxyqGZjkwfoXHnPsDi4qqvasY', '2021-05-27 15:34:39.323252'),
('j9hil3clm0e0wsra3conn2god1xspxl5', '.eJxVjEEOgjAQRe_StWmmpdDWpXvO0Mx0BosaSCisjHcXEha6_e-9_1YJt7WkrcqSRlZXZdTldyPMT5kOwA-c7rPO87QuI-lD0Setup9ZXrfT_TsoWMteC7Ej8sIxBMhDFGaEgXzECF1A2zY0OPBNa9pAXYBI2WUgsyfirAX1-QIQsDhg:1lj05x:JjGEEoSBd3HY_nmO9yvnk_lqa4Ujke6YfRo6UTkisCQ', '2021-06-01 13:49:13.803769');

-- --------------------------------------------------------

--
-- Structure de la table `generiquemodel_annee`
--

DROP TABLE IF EXISTS `generiquemodel_annee`;
CREATE TABLE IF NOT EXISTS `generiquemodel_annee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `annee` smallint(5) UNSIGNED NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `annee` (`annee`)
) ;

-- --------------------------------------------------------

--
-- Structure de la table `generiquemodel_generictable`
--

DROP TABLE IF EXISTS `generiquemodel_generictable`;
CREATE TABLE IF NOT EXISTS `generiquemodel_generictable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `intitule` varchar(255) NOT NULL,
  `code` int(10) UNSIGNED NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  `element_parent_id` int(11) DEFAULT NULL,
  `niveau_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `generiquemodel_gener_element_parent_id_cd8f2fa0_fk_generique` (`element_parent_id`),
  KEY `generiquemodel_gener_niveau_id_36792fbc_fk_generique` (`niveau_id`)
) ;

-- --------------------------------------------------------

--
-- Structure de la table `generiquemodel_generictable_annee`
--

DROP TABLE IF EXISTS `generiquemodel_generictable_annee`;
CREATE TABLE IF NOT EXISTS `generiquemodel_generictable_annee` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `generictable_id` int(11) NOT NULL,
  `annee_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `generiquemodel_genericta_generictable_id_annee_id_4b9d5e2a_uniq` (`generictable_id`,`annee_id`),
  KEY `generiquemodel_gener_annee_id_98379d93_fk_generique` (`annee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `generiquemodel_generictable_structure`
--

DROP TABLE IF EXISTS `generiquemodel_generictable_structure`;
CREATE TABLE IF NOT EXISTS `generiquemodel_generictable_structure` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `generictable_id` int(11) NOT NULL,
  `structure_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `generiquemodel_genericta_generictable_id_structur_bf5566f8_uniq` (`generictable_id`,`structure_id`),
  KEY `generiquemodel_gener_structure_id_56ce8afa_fk_generique` (`structure_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `generiquemodel_niveau`
--

DROP TABLE IF EXISTS `generiquemodel_niveau`;
CREATE TABLE IF NOT EXISTS `generiquemodel_niveau` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `niveau` varchar(255) NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `niveau` (`niveau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `generiquemodel_structure`
--

DROP TABLE IF EXISTS `generiquemodel_structure`;
CREATE TABLE IF NOT EXISTS `generiquemodel_structure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `budjet` bigint(20) UNSIGNED NOT NULL,
  `date_ajout` datetime(6) NOT NULL,
  `date_modification` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nom` (`nom`)
) ;

--
-- Déchargement des données de la table `generiquemodel_structure`
--

INSERT INTO `generiquemodel_structure` (`id`, `nom`, `budjet`, `date_ajout`, `date_modification`) VALUES
(1, 'PAM', 1852013, '2021-05-12 11:36:55.500934', '2021-05-12 11:36:55.500934'),
(2, 'ANPTIC', 12548698, '2021-05-18 13:50:07.572972', '2021-05-18 13:50:07.572972');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `activite_activites`
--
ALTER TABLE `activite_activites`
  ADD CONSTRAINT `activite_activites_devise_id_d8863d90_fk_activite_devise_id` FOREIGN KEY (`devise_id`) REFERENCES `activite_devise` (`id`),
  ADD CONSTRAINT `activite_activites_generic_id_64f4b14b_fk_generique` FOREIGN KEY (`generic_id`) REFERENCES `generiquemodel_generictable` (`id`);

--
-- Contraintes pour la table `activite_activites_etiquette`
--
ALTER TABLE `activite_activites_etiquette`
  ADD CONSTRAINT `activite_activites_e_activites_id_8aa393ee_fk_activite_` FOREIGN KEY (`activites_id`) REFERENCES `activite_activites` (`id`),
  ADD CONSTRAINT `activite_activites_e_etiquette_id_b7063717_fk_activite_` FOREIGN KEY (`etiquette_id`) REFERENCES `activite_etiquette` (`id`);

--
-- Contraintes pour la table `activite_activites_financement`
--
ALTER TABLE `activite_activites_financement`
  ADD CONSTRAINT `activite_activites_f_activites_id_63d8fba3_fk_activite_` FOREIGN KEY (`activites_id`) REFERENCES `activite_activites` (`id`),
  ADD CONSTRAINT `activite_activites_f_sourcefinancement_id_902d5254_fk_activite_` FOREIGN KEY (`sourcefinancement_id`) REFERENCES `activite_sourcefinancement` (`id`);

--
-- Contraintes pour la table `activite_activites_pogrammation`
--
ALTER TABLE `activite_activites_pogrammation`
  ADD CONSTRAINT `activite_activites_p_activites_id_db0009e3_fk_activite_` FOREIGN KEY (`activites_id`) REFERENCES `activite_activites` (`id`),
  ADD CONSTRAINT `activite_activites_p_programmephysique_id_62312bdd_fk_activite_` FOREIGN KEY (`programmephysique_id`) REFERENCES `activite_programmephysique` (`id`);

--
-- Contraintes pour la table `activite_activites_structure`
--
ALTER TABLE `activite_activites_structure`
  ADD CONSTRAINT `activite_activites_s_activites_id_43d09558_fk_activite_` FOREIGN KEY (`activites_id`) REFERENCES `activite_activites` (`id`),
  ADD CONSTRAINT `activite_activites_s_structureresponsable_8dc970ad_fk_activite_` FOREIGN KEY (`structureresponsable_id`) REFERENCES `activite_structureresponsable` (`id`);

--
-- Contraintes pour la table `authtoken_token`
--
ALTER TABLE `authtoken_token`
  ADD CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Contraintes pour la table `generiquemodel_generictable`
--
ALTER TABLE `generiquemodel_generictable`
  ADD CONSTRAINT `generiquemodel_gener_element_parent_id_cd8f2fa0_fk_generique` FOREIGN KEY (`element_parent_id`) REFERENCES `generiquemodel_generictable` (`id`),
  ADD CONSTRAINT `generiquemodel_gener_niveau_id_36792fbc_fk_generique` FOREIGN KEY (`niveau_id`) REFERENCES `generiquemodel_niveau` (`id`);

--
-- Contraintes pour la table `generiquemodel_generictable_annee`
--
ALTER TABLE `generiquemodel_generictable_annee`
  ADD CONSTRAINT `generiquemodel_gener_annee_id_98379d93_fk_generique` FOREIGN KEY (`annee_id`) REFERENCES `generiquemodel_annee` (`id`),
  ADD CONSTRAINT `generiquemodel_gener_generictable_id_22847c73_fk_generique` FOREIGN KEY (`generictable_id`) REFERENCES `generiquemodel_generictable` (`id`);

--
-- Contraintes pour la table `generiquemodel_generictable_structure`
--
ALTER TABLE `generiquemodel_generictable_structure`
  ADD CONSTRAINT `generiquemodel_gener_generictable_id_5241e60d_fk_generique` FOREIGN KEY (`generictable_id`) REFERENCES `generiquemodel_generictable` (`id`),
  ADD CONSTRAINT `generiquemodel_gener_structure_id_56ce8afa_fk_generique` FOREIGN KEY (`structure_id`) REFERENCES `generiquemodel_structure` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
