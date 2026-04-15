import pymysql
import sys

DB_HOST = "192.168.100.20"
DB_USER = "cjulib"
DB_PASS = "security"
DB_PORT = 3306
DB_NAME = "cju"

def get_connection():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT,
            database=DB_NAME,
            charset='utf8'
        )
        return conn
    except Exception as e:
        print("DB 연결 실패:", e)
        sys.exit()

def get_cursor():
    conn = get_connection()
    return conn, conn.cursor()