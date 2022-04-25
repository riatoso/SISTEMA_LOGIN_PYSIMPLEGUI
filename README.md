# SISTEMA_LOGIN_PYSIMPLEGUI
 Sistema de login em banco MySQL com PYSimpleGUI.

 => BANCO DE DADOS - SCHEMA login

 => create table login.usuario (id int primary key auto_increment, usuario varchar(15) not null unique , 
    nome varchar(30) not null, senha text not null, telefone varchar(14), 
    cargo varchar(20), datacad date, cpf varchar(14));

 => Criptografia de senha gerado no cryptocode

 => Modulo de validação CPF , Telefone.

