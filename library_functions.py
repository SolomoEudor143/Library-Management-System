import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="solomoeudor.space",
  user="dps",
  password="nobitches",
  database="lms"
)

cursor = mydb.cursor()

current_user = None

def login(email,password):
  global current_user
  sql = "Select Customer_id from customers where email= %s and password = %s"
  val = (email,password)
  cursor.execute(sql,val)
  customer_id = cursor.fetchone()
  current_user = customer_id[0]

def register_user(name,email,password):
  try:
    email.lower()
    sql = "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)"
    val = (name, email, password)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")
  except:
    print("This user already exists")

def list_issues():
  cursor.execute("SELECT * FROM issue_log")
  users = cursor.fetchall()
  print(users)

def list_users():
  cursor.execute("SELECT * FROM customers")
  users = cursor.fetchall()
  print(users)

def list_books():
  cursor.execute("SELECT * FROM books")
  books = cursor.fetchall()
  return books

def search_book(book_name):
  sql = "SELECT * FROM books WHERE lower(title) = lower(%s)"
  val = (book_name,)
  cursor.execute(sql,val)
  result = cursor.fetchone()
  return result

def issue_book(book_list):
  global current_user
  for i in book_list:
    cursor.execute("Select issued from books where book_id = %s", (i,))
    check = cursor.fetchone()[0]
    if current_user and check == False:
      sql = "Insert into issue_log(book_id,customer_id,issued_on) values(%s,%s,%s)"
      val = (i, current_user, datetime.date.today().strftime('%Y-%m-%d'))
      cursor.execute(sql,val)
      cursor.execute("UPDATE books SET issued = 1 WHERE book_id = %s", (i,))
  mydb.commit()

def return_book(book_id):
  global current_user
  cursor.execute("SELECT issued_on FROM issue_log WHERE book_id = %s AND customer_id = %s AND returned_on IS NULL",(book_id, current_user))
  result = cursor.fetchone()
  if not result:
    return 0
  issued_on = result[0]
  returned_on = datetime.date.today()
  days_held = (returned_on - issued_on).days
  fine = 0
  if days_held > 14:
    fine = (days_held - 14) * 1
  cursor.execute("UPDATE issue_log SET returned_on = %s WHERE book_id = %s AND customer_id = %s AND returned_on IS NULL",(returned_on, book_id, current_user))
  cursor.execute("UPDATE books SET issued = 0 WHERE book_id = %s",(book_id,))
  mydb.commit()
  return fine

def issue_log():
  sql = "SELECT * FROM issue_log WHERE customer_id = %s AND returned_on IS NULL"
  cursor.execute(sql, (current_user,))
  result = cursor.fetchall()
  return result

def get_name(bid):
  sql = "SELECT title from books where book_id = %s"
  cursor.execute(sql, (bid,))
  result = cursor.fetchone()[0]
  return result

def issue_count():
  global current_user
  sql = "SELECT COUNT(issue_id) FROM issue_log WHERE customer_id = %s AND returned_on IS NULL"
  cursor.execute(sql, (current_user,))
  count = cursor.fetchone()[0]
  return count

def reset_issue():
  cursor.execute("UPDATE books SET issued = 0")
  cursor.execute("TRUNCATE TABLE issue_log")
  mydb.commit()

def reset_customers():
  cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
  cursor.execute("TRUNCATE TABLE customers")
  cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
  mydb.commit()