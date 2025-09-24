CREATE DATABASE IF NOT EXISTS miniproject;
USE miniproject;

-- Menu Table
CREATE TABLE menu (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Users Table
CREATE TABLE user_details (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(15) UNIQUE NOT NULL
);

-- Cart Table
CREATE TABLE cart (
    cart_id INT PRIMARY KEY,
    user_id INT,
    item_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_details(user_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES menu(item_id) ON DELETE CASCADE
);

-- Orders Table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_details(user_id) ON DELETE CASCADE
);

-- Order Items Table
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    item_id INT,
    qty INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES menu(item_id) ON DELETE CASCADE
);
DROP TABLE menu;
DROP TABLE user_details;
DROP TABLE cart;
DROP TABLE orders;
DROP TABLE order_items;

