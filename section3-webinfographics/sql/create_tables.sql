CREATE TABLE `Entities` (
    id int(5) UNSIGNED NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    isHighlight bool,
    primaryImage varchar(255),
    link varchar(255) ,
    countryId int(5) UNSIGNED NOT NULL,
    departmentId int(5) UNSIGNED NOT NULL,
    accessionYear int(5),
    primary key(id)
);

CREATE TABLE `Countries` (
    id int(5) UNSIGNED NOT NULL AUTO_INCREMENT,
    name varchar(255),
    primary key(id)
);
CREATE TABLE `Departments` (
    id int(5) UNSIGNED NOT NULL AUTO_INCREMENT,
    name varchar(255),
    primary key(id)
);
CREATE TABLE `Dates` (
    id int(5) UNSIGNED NOT NULL AUTO_INCREMENT,
    idEntity int(5) UNSIGNED NOT NULL,
    restorationStart datetime,
    restorationEnd datetime,
    primary key(id)
);
CREATE TABLE `Metrics` (
    id int(5) UNSIGNED NOT NULL AUTO_INCREMENT,
    idEntity int(5) UNSIGNED NOT NULL,
    impressionTotal float,
    descriptionInformative float,
    visualFeedback float,
    primary key(id)
);