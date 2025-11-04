CREATE TABLE IF NOT EXISTS bebidas(
    idsabores            INTEGER PRIMARY KEY AUTOINCREMENT,
    Sabor               VARCHAR(50),
    Com_gelo            BOOLEAN,
    Limao               BOOLEAN,
);                      

CREATE TABLE IF NOT EXISTS cliente(
    idCliente           INTEGER PRIMARY KEY AUTOINCREMENT,
    nome                VARCHAR(500),
    Cpf                 VARCHAR(11),
    Cartao_aprovar      BOOLEAN,
);                      

CREATE TABLE IF NOT EXISTS sabores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(200),               l
);