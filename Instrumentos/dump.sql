BEGIN TRANSACTION;
CREATE TABLE INSTRUMENTOS(
   ID INTEGER PRIMARY KEY     AUTOINCREMENT,
   Name           TEXT    NOT NULL,
   Caracteristicas            TEXT     NOT NULL,
   Precio         REAL
);
INSERT INTO "INSTRUMENTOS" VALUES(1,'VIOLÍN','Se inicia con el frotamiento de las cuerdas del laúd y el rebab.',14444.0);
INSERT INTO "INSTRUMENTOS" VALUES(2,'VIOLA','Posee una forma abombada y la cintura en forma de C',14444.0);
INSERT INTO "INSTRUMENTOS" VALUES(3,'GUITARRA','tiene una caja de resonancia chata, con forma de ocho y una boca',600.0);
INSERT INTO "INSTRUMENTOS" VALUES(4,'MANDOLINA','Instrumento musical de 4 órdenes dobles. Las cuerdas se pulsan con una púa',298.0);
INSERT INTO "INSTRUMENTOS" VALUES(5,'PIANO','Uno de los instrumentos más grandes y pesados',14000.0);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('INSTRUMENTOS',5);
COMMIT;
