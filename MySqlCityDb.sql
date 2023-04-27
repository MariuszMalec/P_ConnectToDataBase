create database MySqlCityDb;
use MySqlCityDb;

drop table City;

CREATE TABLE City (
	Id		   int   	not null,
	Name	   nvarchar(25)	not null,
	constraint PK_City primary key (Id),
	constraint UQ_City_Name unique (Name)
);

insert into City (Id, Name) values (1, 'Gdańsk');
insert into City (Id, Name) values (2, 'Elbląg');

select * from City;