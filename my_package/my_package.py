import sqlite3


def add(a, b):
    return a + b


def test():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS customers (
            customer_id INT PRIMARY KEY,
            customer_name VARCHAR(255),
            country VARCHAR(50)
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS orders (
            order_id INT PRIMARY KEY,
            order_date DATE,
            customer_id INT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INT PRIMARY KEY,
            order_id INT,
            product_id INT,
            quantity INT,
            unit_price DECIMAL(10, 2),
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS products (
            product_id INT PRIMARY KEY,
            product_name VARCHAR(255),
            category_id INT,
            price DECIMAL(10, 2),
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        );
        """
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS categories (
            category_id INT PRIMARY KEY,
            category_name VARCHAR(255)
        );
        """
    )

    # Insert data
    cursor.execute(
        """INSERT INTO customers (customer_id, customer_name, country)
            VALUES
                (1, 'Customer A', 'USA'),
                (2, 'Customer B', 'Canada'),
                (3, 'Customer C', 'UK'),
                (4, 'Customer D', 'Australia');
        """
    )

    cursor.execute(
        """INSERT INTO orders (order_id, order_date, customer_id)
            VALUES
                (101, '2023-10-01', 1),
                (102, '2023-10-02', 2),
                (103, '2023-10-03', 3),
                (104, '2023-10-04', 4);
        """
    )

    cursor.execute(
        """INSERT INTO order_items (order_item_id, order_id, product_id, quantity, unit_price)
            VALUES
                (1001, 101, 1, 2, 10.99),
                (1002, 101, 2, 3, 15.99),
                (1003, 102, 1, 1, 10.99),
                (1004, 103, 3, 5, 8.99),
                (1005, 103, 2, 2, 15.99),
                (1006, 104, 4, 4, 12.49);
        """
    )

    cursor.execute(
        """INSERT INTO products (product_id, product_name, category_id, price)
            VALUES
                (1, 'Product 1', 1, 10.99),
                (2, 'Product 2', 1, 15.99),
                (3, 'Product 3', 2, 8.99),
                (4, 'Product 4', 2, 12.49);"""
    )

    cursor.execute(
        """INSERT INTO categories (category_id, category_name)
            VALUES
                (1, 'Category A'),
                (2, 'Category B');"""
    )

    # Commit the changes
    conn.commit()

    # Query data
    cursor.execute(
        """SELECT 
                    p.product_name,
                    SUM(oi.quantity * oi.unit_price) AS total_sales
                FROM products p
                JOIN order_items oi ON p.product_id = oi.product_id
                GROUP BY p.product_name
                ORDER BY total_sales DESC;"""
    )
    rows = cursor.fetchall()
    print("-------print all records-------")
    for row in rows:
        print(row)


if __name__ == "__main__":
    test()
