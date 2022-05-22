show databases;

DROP database if exists `SEDB`;

create database SEDB; -- --데이터베이스 생성 -- --

use SEDB;

create table customer (
   ID varchar(20) not null,
   primary key(ID),
   Password_ varchar(20)
   );
   
show tables;

select* from customer;
insert into Customer values ('Park', 'dong256');
insert into Customer values ('Ho', 'shin234');
insert into Customer values ('Jun', 'shin1');
insert into Customer values ('Lee', 'gun234');
insert into Customer values ('Yang', 'yang1720');

select * from customer; 