select * from agenda.funcionario;

alter table usuario modify column senha text not null;

select * from login.usuario;

create table login.usuario (id int primary key auto_increment, usuario varchar(15) not null unique , 
nome varchar(30) not null, senha text not null, telefone varchar(14), 
cargo varchar(20), datacad date, cpf varchar(14));

insert into login.usuario (nome , senha, usuario) values ("Ana Beatriz" ,"ana2022", "anab");

delete from login.usuario;

drop table login.usuario