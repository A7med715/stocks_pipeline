CREATE TABLE stock (
    id INT AUTO_INCREMENT PRIMARY KEY,

    symbol VARCHAR(10) NOT NULL,

    trade_date DATE NOT NULL,

    open_price DECIMAL(10,2),

    high_price DECIMAL(10,2),

    low_price DECIMAL(10,2),

    close_price DECIMAL(10,2),

    volume BIGINT,

    UNIQUE(symbol, trade_date)
);