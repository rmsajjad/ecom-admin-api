CREATE TABLE categories (
    id INT AUTO_INCREMENT,
    category VARCHAR(50) NOT NULL,
    PRIMARY KEY (category),
    INDEX (id)
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    category VARCHAR(50),
    INDEX (id),
    FOREIGN KEY (category) REFERENCES categories(category)
);

CREATE TABLE inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    stock_level INT DEFAULT 0,
    last_updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT NOT NULL,
    total_price FLOAT NOT NULL,
    order_date DATETIME,
    INDEX (order_date),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
