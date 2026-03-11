from database_conn import get_db_connection


def search_procedure(keyword):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT title, category, symptoms, steps, warnings, call_emergency
        FROM procedures
        WHERE title LIKE %s
        OR symptoms LIKE %s
    """
    search_term = f"%{keyword}%"

    try:
        cursor.execute(query, (search_term, search_term))
        results = cursor.fetchall()
        return results
    finally:
        cursor.close()
        conn.close()