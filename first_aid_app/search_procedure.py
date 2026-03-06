import mysql.connector

def get_connection():
  return mysql.connector.connect(
    host='localhost',
    user='root',
    password='S40!xQ38!xL26!',
    database='first_aid_app'
  )

def search_procedure(keyword):
  conn = get_connection()
  cursor = conn.cursor(dictionary=True)#a cursor is an object used to execute SQL queries
  #query results will be returned as Python dictionaries 
  
  query = """
      SELECT title, category, symptoms, steps, warnings, call_emergency
        FROM procedures
        WHERE title LIKE %s
        OR symptoms LIKE %s 
    """
  #where title OR symptoms contains the keyword
  
  search_term =f"%{keyword}%" #The % symbols are SQL wildcards. Make the search more flexible.
  cursor.execute(query, (search_term, search_term))
  results = cursor.fetchall()

  cursor.close()
  conn.close()

  return results
