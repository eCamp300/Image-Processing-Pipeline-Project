import mysql.connector
from datetime import datetime

def log_generation(image_url, status, error_message=None):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="pipline_metrics",
            user="root",
            password="your_password"
        )
        cursor = connection.cursor()

        #SQL insertion for logging successful generations and failed image URLs.
        sql = """INSERT INTO generation_logs
               (timestamp, requested_url, status, error_log)
               VALUES (%s, %s, %s, %s)"""
        values = (datetime.now(), image_url, status, error_message)
        cursor.execute(sql, values)
        connection.commit()


    except mysql.connector.Error as err:
        print(f"Database loggin failed: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
