from flask import Flask, render_template
import pymysql

sample = Flask(__name__)

MYSQL_PASSWORD = "super_secret_123"
API_KEY = "sk-1234567890abcdef"

@sample.route("/")
def main():
    try:
        conn = pymysql.connect(
            host="db",
            user="root",
            password="sena123",
            database="082_db",
            port=3306
        )
        conn.close()
        db_status = "Conexión exitosa a la base de datos"
    except Exception as e:
        db_status = f"Error al conectar a la base de datos: {e}"

    return render_template("index.html", db_status=db_status), 500

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=True)