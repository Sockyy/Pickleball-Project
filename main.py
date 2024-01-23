#
# Homework #2: Pickleball Madness
#
# 1.	You know that you've got to go back to school, so you want to 
# create a solution that your Aunt Mary can use long after you are gone. 
# You have decided that you are going to write a Python program that she 
# can use to get the answers that she needs about how her store is doing.
#
# 2.	Using Python and SQLite, you will create a Python program that 
# will create a database with the appropriate four tables that Aunt Mary 
# will need to store information about her store.
#
# 3.	You will then load these tables with the information that is 
# provided.
#
# 4.	You will then use your Python program to answer the following 
# questions:
# a.	What customers (first name, last name, address, city, state, zip 
# code) purchased Pickleball products?
#
# b.	Of the customers in Aunt Mary’s database, which ones have made a 
# purchase?
#
# c.	Of the products in Aunt Mary’s inventory, what products have been 
# sold?
#
# d.	How much money did Aunt Mary make selling Pickleball products?
#
# e.	How much money did Aunt Mary make selling Tennis products?
#
# f.	How much money did Aunt Mary make on her first sale?
# g.	How much money did Aunt Mary make on her last sale?
# h.	Create a result that shows each customer’s (first name, last name, 
# state) who has made a purchase.
#
# Student Name: Parker Kimbleton

import sqlite3

# Use command only if tables haven't been created yet
# cursor -> cursor that is connected to desired database
def createTables(cursor):

  print("Creating Tables:\n")

  # CUSTOMER Table creation
  cursor.execute('''CREATE TABLE CUSTOMER (
  customerID INTEGER PRIMARY KEY,
  firstName CHAR (30) NOT NULL,
  lastName CHAR (30) NOT NULL,
  street CHAR (30),
  city CHAR (30),
  state CHAR (20),
  zipCode INTEGER,
  phone INTEGER
);''')
  print('Customer Table Created Successfully!  (1/4)')

  # PRODUCT Table creation
  cursor.execute('''CREATE TABLE PRODUCT(
  productID INTEGER PRIMARY KEY,
  name CHAR (30) NOT NULL,
  description CHAR (100),
  category CHAR (20) NOT NULL,
  vendorID INTEGER NOT NULL,
  vendorName CHAR (30)
);''')
  print('Product Table Created Successfully!  (2/4)')

  # PURCHASE Table creation
  cursor.execute('''CREATE TABLE PURCHASE(
  invoiceID INTEGER PRIMARY KEY,
  customerID INTEGER NOT NULL,
  invoiceDate DATE NOT NULL,
  totalSale NUMERIC (5,2) NOT NULL,
  totalPaid NUMERIC (5,2) NOT NULL,
  paymentType CHAR (10) NOT NULL,
  CONSTRAINT fk_customerID
  	FOREIGN KEY(customerID)
  		REFERENCES CUSTOMER(customerID)
);''')
  print('Purchase Table Created Successfully!  (3/4)')

  # SOLD_ITEM creation
  cursor.execute('''CREATE TABLE SOLD_ITEM(
  lineID INTEGER NOT NULL,
  invoiceID INTEGER NOT NULL,
  productID INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  salesPrice NUMERIC (5,2) NOT NULL,
  PRIMARY KEY (lineID, invoiceID, productID),
  CONSTRAINT fk_productID
  	FOREIGN key(productID)
  		REFERENCES PRODUCT(productID),
  CONSTRAINT fk_invoiceID
  	FOREIGN KEY(invoiceID)
  		REFERENCES PURCHASE(invoiceID)
);''')
  print('Sold Item Table Created Successfully!  (4/4)')

# use if tables are empty
# cursor -> cursor that's using desired database that has correct tables
def insertData(cursor):

  print('Inserting Data:\n')

  # CUSTOMER Data to be inserted
  cursor.execute('''INSERT INTO CUSTOMER (customerID, firstname, lastname, street, city, state, zipcode, phone) VALUES
	(1, 'Bob', 'Johnson', '1234 Main St', 'Tampa', 'FL', 33660, '813-555-1234'),
    (2, 'Ann', 'Majors', '675 Oak Ln', 'Oakland', 'CA', 12345, '425-555-2468'),
    (3, 'Barb', 'Sweeny', '34 Pine Ridge', 'Orlando', 'FL', 98765, '764-555-9476'),
    (4, 'Art', 'Puett', '123 Apple Way', 'Dallas', 'TX', 24680, '123-555-8765'),
    (5, 'Bobbi', 'Marschall', '98 Jenkins Dr.', 'St. Louis', 'MO', 13579, '614-555-9123'),
    (6, 'Les', 'Peterson', '450 Pikes St.', 'Tampa', 'FL', 98765, '845-555-7284'),
    (7, 'Amanda', 'Maples', '389 Lewis Rd.', 'Miami', 'FL', 54321, '175-555-9274'),
    (8, 'Jenny', 'McPherson', '48 Alta Vista Dr.', 'Los Angles', 'CA', 86420, '882-555-4423'),
    (9, 'Mike', 'Diesen', '12 Pointer Ln', 'New York', 'NY', 97531, '782-555-4444'),
    (10, 'Robert', 'Makely', '925 State St.', 'Lakeland', 'FL', 16028, '345-555-6667');''')
  print("Customer data has been inserted.  (1/4)")

  #PRODUCT Data to be inserted
  cursor.execute('''INSERT INTO PRODUCT (productID, name, description, category, vendorid, vendorname) VALUES
	(1, 'Pickleball Paddle', 'Paddle for Pickleball', 'Pickleball', 100, 'Pickle Products'),
    (2, 'Tennis Ball', 'Ball to use in Tennis', 'Tennis', 200, 'Tennis World'),
    (3, 'Ping Pong Paddle', 'Paddle for Ping Pong', 'Ping Pong', 300, 'Ping Pong Products'),
    (4, 'Squash Racket', 'Racket for Squash', 'Squash', 400, 'Squash Masters'),
    (5, 'Racquetball Ball', 'Ball to use in Racquetball', 'Racquetball', 500, 'Racketball Outlet'),
    (6, 'Badmiton Racket', 'Racket for Badmition', 'Badmition', 600, 'Badmition Universe'),
    (7, 'Pickleball Net', 'Net for Pickleball', 'Pickleball', 100, 'Pickle Products'),
    (8, 'Pickleball Ball', 'Ball to use in Pickleball', 'Pickleball', 100, 'Pickle Products'),
    (9, 'Tennis Racket', 'Racket for Tennis', 'Tennis', 200, 'Tennis World'),
    (10, 'Badmition Net', 'Net for Badmition', 'Badmition', 600, 'Badmition Universe');''')
  print('Product data has been inserted.  (2/4)')

  #PURCHASE Data to be inserted
  cursor.execute('''INSERT INTO PURCHASE (invoiceid, customerid, invoicedate, totalsale, totalpaid, paymenttype) VALUES
	(1, 2, '2023-05-01', 125.86, 125.86, 'Cash'),
    (2, 2, '2023-05-02', 75.25, 75.25, 'Check'),
    (3, 2, '2023-05-03', 209.15, 209.15, 'Credit'),
    (4, 1, '2023-05-04', 55.54, 55.54, 'Credit'),
    (5, 10, '2023-05-05', 32.13, 32.13, 'Credit'),
    (6, 7, '2023-05-06', 25.75, 25.75, 'Cash'),
    (7, 6, '2023-05-07', 111.14, 111.14, 'Bitcoin'),
    (8, 5, '2023-05-08', 89.72, 89.72, 'Credit'),
    (9, 3, '2023-05-09', 12.24, 12.24, 'Cash'),
    (10, 8, '2023-05-10', 62.34, 62.34, 'Cash');''')
  print('Purchase data has been inserted.  (3/4)')

  #SOLD_ITEM data to be inserted
  cursor.execute('''INSERT INTO SOLD_ITEM (lineid, invoiceid, productid, quantity, salesprice) VALUES
	(1, 1, 1, 10, 11.70),
    (2, 2, 10, 2, 34.99),
    (3, 3, 4, 1, 194.51),
    (4, 4, 2, 7, 7.38),
    (5, 5, 8, 5, 5.98),
    (6, 6, 6, 4, 5.99),
    (7, 7, 1, 2, 51.68),
    (8, 8, 9, 8, 10.43),
    (9, 9, 3, 3, 3.79),
    (10, 10, 1, 5, 11.60);''')
  print('Sold Item data has been inserted.  (4/4)')

# prints data from the fetchall in a nicer format
# data -> the cursor.fetchall() statement after executing your desired select statement
def printSelect(data):
  for i in data:
    for x in i:
      print(f'{x}',end=' ')
    print('\n') 

if __name__ == '__main__':

  # change parameter if wanting to use different database
  connection = sqlite3.connect("pickleball.db")
  crsr = connection.cursor()

  #if we dont get past this we're gonna have rough day
  print("Connected\n\n")

  # createTables(crsr)
  
  # insertData(crsr)

  # question a
  crsr.execute('''SELECT DISTINCT CUSTOMER.firstName, CUSTOMER.lastName, CUSTOMER.street, CUSTOMER.city, CUSTOMER.state, CUSTOMER.zipCode FROM SOLD_ITEM JOIN PURCHASE ON SOLD_ITEM.invoiceID = PURCHASE.invoiceID JOIN CUSTOMER ON PURCHASE.customerID = CUSTOMER.customerID JOIN PRODUCT ON SOLD_ITEM.productID = PRODUCT.productID WHERE category = 'Pickleball';''')
  selectedData = crsr.fetchall()

  print("Question a - What customers purchased Pickleball products?\n")
  printSelect(selectedData)

  
  #question b
  crsr.execute('''SELECT DISTINCT CUSTOMER.firstName, CUSTOMER.lastName, CUSTOMER.street, CUSTOMER.city, CUSTOMER.state, CUSTOMER.zipCode FROM SOLD_ITEM JOIN PURCHASE ON SOLD_ITEM.invoiceID = PURCHASE.invoiceID JOIN CUSTOMER ON PURCHASE.customerID = CUSTOMER.customerID;''')
  selectedData = crsr.fetchall()

  print('\n\nQuestion b - Of the customers in Aunt Mary\'s database, which ones have made a purchase?\n')
  printSelect(selectedData)

  
  #question c
  crsr.execute('''SELECT DISTINCT PRODUCT.name FROM SOLD_ITEM JOIN PRODUCT ON SOLD_ITEM.productID = PRODUCT.productID''')
  selectedData = crsr.fetchall()

  print('\n\nQuestion c - Of the products in Aunt Mary\'s inventory, which products have been sold?\n')
  printSelect(selectedData)


  #question d
  crsr.execute('''SELECT SUM(PURCHASE.totalPaid) FROM PURCHASE JOIN SOLD_ITEM ON PURCHASE.invoiceID = SOLD_ITEM.invoiceID JOIN PRODUCT ON SOLD_ITEM.productID = PRODUCT.productID WHERE category = 'Pickleball';''')
  selectedData = crsr.fetchall()

  print('\n\nQuestion d - How much money did Aunt Mary make selling Pickleball products?\n')
  printSelect(selectedData)


  #question e
  crsr.execute('''SELECT SUM(PURCHASE.totalPaid) FROM PURCHASE JOIN SOLD_ITEM ON PURCHASE.invoiceID = SOLD_ITEM.invoiceID JOIN PRODUCT ON SOLD_ITEM.productID = PRODUCT.productID WHERE category = 'Tennis';''')
  selectedData = crsr.fetchall()

  print('\n\nQuestion e - How much money did Aunt Mary make selling Tennis products?\n')
  printSelect(selectedData)


  #question f
  crsr.execute('''SELECT PURCHASE.invoiceID, ' | ',totalPaid FROM SOLD_ITEM JOIN PURCHASE ON SOLD_ITEM.invoiceID = PURCHASE.invoiceID WHERE PURCHASE.invoiceID = 1;''')
  selectedData = crsr.fetchall()

  print('\n\nQuestion f - How much money did Aunt Mary make on her first sale?\n')
  printSelect(selectedData)


  #question g
  crsr.execute('''SELECT MAX(PURCHASE.invoiceID), ' | ', totalPaid FROM SOLD_ITEM JOIN PURCHASE ON SOLD_ITEM.invoiceID = PURCHASE.invoiceID;''')
  selectedData = crsr.fetchall()

  print('\n\nQuestion g - How much money did Aunt Mary make on her last sale?\n')
  printSelect(selectedData)


  #question h
  crsr.execute('''SELECT DISTINCT firstName, lastName, state FROM CUSTOMER JOIN PURCHASE ON CUSTOMER.customerID = PURCHASE.customerID''')
  selectedData = crsr.fetchall()

  print('\n\nQuestion h - Create a result that shows customer data for those who\'ve made a purchase.\n')
  printSelect(selectedData)


  #Saves changes (mainly here on off chance tables need to be recreated/data needs to be re-entered)
  connection.commit()
  connection.close()