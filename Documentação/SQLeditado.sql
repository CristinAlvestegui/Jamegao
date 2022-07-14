create database Jamegao;
use Jamegao;

create table Jamegoes(
cod int not null auto_increment primary key,
jameg varchar(15) not null
)Engine=InnoDB;

alter table Jamegoes add atalho varchar(20) not null;
describe Jamegoes;

create table Atalho(
cod int not null auto_increment primary key,
atal varchar(50) not null
) Engine = InnoDB;

drop table Atalho;
