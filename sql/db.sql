create database IF NOT EXISTS kfc;
 use kfc;

    Drop table If EXISTS Contem;
    Drop table If EXISTS Ingredientes;
    Drop table If EXISTS Menu_Comida;
    Drop table If EXISTS Menu;
    Drop table If EXISTS Comida;
    Drop table If EXISTS Categoria;

  Create Table Categoria(
    CategoriaId int(8) auto_increment,
    Nome varchar(32) unique,
    PRIMARY KEY(CategoriaId)
  );

 Create Table Comida(
  ComidaId int(8) auto_increment,
  Nome varchar(64) unique,
  CategoriaId int(8),
  EnerJ double(16,2),
  EnerCal double(8,2),
  Lip double(16,2),
  Sat double(16,2),
  Hidr double(16,2),
  Acucar double(16,2),
  Prot double(16,2),
  Sal double(16,2),
  PRIMARY KEY(ComidaId),
  FOREIGN KEY (CategoriaId) REFERENCES Categoria(CategoriaId)
 );

Create Table Menu(
  MenuId int(8) auto_increment,
  Nome varchar(64) unique,
  BebidasRestrit boolean,
  NBebidas int(8),
  PRIMARY KEY(MenuId)
 );


 Create table Menu_Comida(
  ComidaId int(8),
  MenuId int(8),
  Quantidade int(8),
  PRIMARY KEY(ComidaId,MenuId),
  FOREIGN KEY (ComidaId) REFERENCES Comida(ComidaId),
  FOREIGN key (MenuId) references Menu(MenuId) 
 );

 Create Table Ingredientes(
  IngreId int(8) auto_increment,
  Nome varchar(64) unique,
  PRIMARY KEY(IngreId)
 );

 Create table Contem(
  ComidaId int(8),
  IngreId int(8),
  PRIMARY KEY(ComidaId,IngreId),
  Foreign key (ComidaId) references Comida(ComidaID),
  Foreign key (IngreId) references Ingredientes(IngreId)
 );