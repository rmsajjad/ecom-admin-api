
START TRANSACTION;

#Refrence Data for Products
INSERT INTO products (id, name, description, price, category) VALUES
(1, 'iPhone 16', 'Electronics, A Apple Product', 1200.00, 'Electronics'),
(2, 'iPhone 16 Pro', 'Electronics, A Apple Product', 1000.00, 'Electronics'),
(3, 'iPhone 16 Pro Max', 'Electronics, A Apple Product', 1000.00, 'Electronics'),
(4, 'Galaxy S25 128 GB, Black', 'A Product by Samsung', 1500.00, 'Electronics'),
(5, 'Galaxy S25 256 GB', 'A Product by Samsung', 1700.00, 'Electronics'),
(6, 'Galaxy S25 512 GB', 'A Product by Samsung', 1900.00, 'Electronics'),
(7, 'LEGO Star Wars', 'Great fun to play', 59.99, 'Toys'),
(8, 'PlayStation 5 Digital Edition', 'Great fun to play', 499.99, 'Toys'),
(9, 'PlayStation 5 Standard', 'A new upgraded, Fast and elegant', 459.99, 'Electronics'),
(10, 'AirPods Pro', 'Love to listen music with it', 249.99, 'Electronics'),
(11, 'Kindle Paperwhite', 'A best book reader', 139.99, 'Book'),
(12, 'Office Chair', 'A good option for remote work', 199.99, 'Furniture'),
(13, 'HP Laptop 15"', 'A good laptop for students', 749.00, 'Computers'),
(14, 'Dell Laptop 14"', 'A good laptop for students', 749.00, 'Computers');
(15, 'Amazon Fire Stick 4K', 'Stream all your favorites in 4K Ultra HD', 49.99, 'Electronics'),
(16, 'Samsung 55" QLED TV', 'Stunning color and clarity for your home entertainment', 699.99, 'Electronics'),
(17, 'Logitech Wireless Mouse', 'Comfortable and long battery life', 29.99, 'Electronics'),
(18, 'Anker Power Bank 20000mAh', 'Charge multiple devices on the go', 39.99, 'Electronics'),
(19, 'Instant Pot Duo 7-in-1', 'Pressure cooker, slow cooker & more', 89.99, 'Home & Kitchen'),
(20, 'Dyson V11 Vacuum Cleaner', 'Cordless powerful vacuum for home', 599.99, 'Home & Kitchen');


#Inventory Refrence Scripts
INSERT INTO inventory (id, product_id, stock_level, last_updated_at) VALUES
(1, 1, 50, '2025-05-01 10:00:00'),
(2, 2, 40, '2025-05-02 11:30:00'),
(3, 3, 30, '2025-05-03 09:45:00'),
(4, 4, 60, '2025-04-28 14:00:00'),
(5, 5, 20, '2025-05-01 13:20:00'),
(6, 6, 15, '2025-05-05 08:10:00'),
(7, 7, 100, '2025-04-25 12:15:00'),
(8, 8, 75, '2025-04-30 16:45:00'),
(9, 9, 35, '2025-04-29 10:30:00'),
(10, 10, 55, '2025-05-01 15:00:00'),
(11, 11, 85, '2025-04-22 11:00:00'),
(12, 12, 12, '2025-05-03 12:30:00'),
(13, 13, 25, '2025-04-26 17:15:00'),
(14, 14, 33, '2025-04-27 14:10:00'),
(15, 15, 40, '2025-05-02 10:00:00'),
(16, 16, 10, '2025-04-30 12:00:00'),
(17, 17, 90, '2025-04-28 15:30:00'),
(18, 18, 100, '2025-05-01 09:20:00'),
(19, 19, 27, '2025-04-24 11:45:00'),
(20, 20, 8, '2025-04-26 08:30:00');


#Refrence data for sale states
INSERT INTO sales (product_id, quantity, total_price, order_date) VALUES
(1, 10, 499.90, '2025-03-05 09:20:00'),
(2,  2, 1399.98, '2025-03-06 11:45:00'),
(3, 15,  449.85, '2025-03-07 15:10:00'),
(4,  8,  319.92, '2025-03-08 13:25:00'),
(5,  4,  359.96, '2025-03-09 12:30:00'),
(6,  1,  599.99, '2025-03-10 14:50:00'),
(7, 40,  799.60, '2025-02-11 10:15:00'),
(8,  5,  649.95, '2025-02-12 11:30:00'),
(9,  6,  539.94, '2025-02-13 09:10:00'),
(10,  7,  489.93, '2025-02-14 16:45:00'),
(11, 12,  359.88, '2025-02-15 14:05:00'),
(12, 30,  479.70, '2025-02-16 12:10:00'),
(13, 50,  449.50, '2025-02-17 17:20:00'),
(14, 60,  299.40, '2025-02-18 18:30:00'),
(16, 18,  197.82, '2025-02-19 13:40:00'),
(17, 20,  339.80, '2025-02-20 14:50:00'),
(18,  8,  479.92, '2025-03-11 17:05:00'),
(19,  3,  539.97, '2025-03-12 11:55:00'),
(20,  9,  449.91, '2025-03-13 12:35:00');

COMMIT;