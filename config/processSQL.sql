create database etl_python;
create database metadata;
create database retail;
create database source_data;
CREATE DATABASE if not exists test CHARACTER SET utf8;
Drop database metadata;
Drop database retail;

use etl_python;
create table if not exists etl_demo (
    id int auto_increment primary key,
    name varchar(20),
    dage_id varchar(32)
);

use source_data;
create table sys_barcode
(
    code         varchar(50)                            not null comment 'productBarcode'
        primary key,
    name         varchar(200) default ''                null comment 'productName',
    spec         varchar(200) default ''                null comment 'productSize',
    trademark    varchar(100) default ''                null comment 'productTrademark',
    addr         varchar(200) default ''                null comment 'productAddr',
    units        varchar(50)  default ''                null comment 'productUnits',
    factory_name varchar(200) default ''                null comment 'productFactoryName',
    trade_price  varchar(20)  default '0.0000'          null comment 'productTradePrice',
    retail_price varchar(20)  default '0.0000'          null comment 'productRetailPrice',
    updateAt     timestamp    default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP comment 'productUpdateAt',
    wholeunit    varchar(50)                            null comment 'wholeunit',
    wholenum     int                                    null comment 'wholenum',
    img          varchar(500)                           null comment 'productImg',
    src          varchar(20)                            null comment 'productSrc'
);

INSERT INTO `sys_barcode` VALUES('014893249557', 'Japan Cooking', '', '', '', 's', '', '', '', '2017-07-01 19:07:09', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('123456789012', 'Spices Mix', '', '', '', 'm', '', '', '', '2018-12-05 12:34:56', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('987654321098', 'Organic Pasta', '', '', '', 'l', '', '', '', '2019-03-21 08:45:32', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('555512349876', 'Tomato Sauce', '', '', '', 'xl', '', '', '', '2020-10-15 17:29:18', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('789012345678', 'Whole Wheat Bread', '', '', '', 'm', '', '', '', '2021-06-30 10:15:42', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('333333333333', 'Green Tea', '', '', '', 's', '', '', '', '2016-04-22 09:08:23', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('444455556666', 'Mixed Nuts', '', '', '', 'm', '', '', '', '2017-11-11 11:11:11', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('777788889999', 'Organic Honey', '', '', '', 's', '', '', '', '2018-08-08 08:08:08', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('987654321000', 'Vanilla Extract', '', '', '', 'l', '', '', '', '2020-05-05 15:45:55', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('123123123123', 'Coconut Milk', '', '', '', 'xl', '', '', '', '2021-02-02 22:22:22', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('999000888777', 'Gluten-Free Cookies', '', '', '', 's', '', '', '', '2019-09-09 14:14:14', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('111222333444', 'Quinoa Salad', '', '', '', 'm', '', '', '', '2018-07-07 07:07:07', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('555444333222', 'Pineapple Slices', '', '', '', 'l', '', '', '', '2017-06-06 06:06:06', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('987654321111', 'Chia Seeds', '', '', '', 'xl', '', '', '', '2020-04-04 04:04:04', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('777666555444', 'Canned Beans', '', '', '', 's', '', '', '', '2019-03-03 03:03:03', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('444333222111', 'Frozen Berries', '', '', '', 'm', '', '', '', '2018-02-02 02:02:02', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('888777666555', 'Almond Butter', '', '', '', 'l', '', '', '', '2017-01-01 01:01:01', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('222333444555', 'Soy Milk', '', '', '', 'xl', '', '', '', '2016-12-12 12:12:12', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('666777888999', 'Canned Tuna', '', '', '', 's', '', '', '', '2015-11-11 11:11:11', null, null, null, null);
INSERT INTO `sys_barcode` VALUES('999888777666', 'Rice Crackers', '', '', '', 'm', '', '', '', '2014-10-10 10:10:10', null, null, null, null);
