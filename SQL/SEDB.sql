show databases;
drop database sedb;
create database SEDB;
use SEDB;


create table customer(
	user_ID varchar(20) not null primary key,
    Password_ varchar(20) not null
);

create table product(
	user_ID varchar(20) not null,
    product_ID int not null auto_increment,
    product_name varchar(20) not null,
    price int not null,
    register_date date,
    keyword varchar(20),
    description_ varchar(50),
    soldout boolean,
    foreign key (user_ID) references customer(user_ID),
    primary key (product_ID)
);

create table follow(
	user_ID varchar(20) not null,
    followee varchar(20) not null,
    foreign key (user_ID) references customer(user_ID),
    foreign key (followee) references product(user_ID),
    primary key (user_ID, followee)
);

create table Product_image(
	product_id int not null,
    image varchar(80) not null,
    foreign key (product_id) references product(product_ID),
    primary key (product_id, image)
);
desc customer;
desc product;
desc follow;
desc product_image;