import mysql.connector
import pandas as pd
from csv import reader

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user='root',
        password='***********',
        host='************',
        port='******',
        database='event_ticket_system')
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    return connection
def load_third_party(connection, file_path):
    cursor = connection.cursor()
    # [Iterate through the CSV file and execute insert statement]

    cursor.execute("""DROP TABLE IF EXISTS ticket_sales""")

    cursor.execute("""
        CREATE TABLE ticket_sales(
                ticket_id INT,
                trans_date DATE,
                event_id INT,
                event_name VARCHAR(50),
                event_date DATE,
                event_type VARCHAR(10),
                event_city VARCHAR(20),
                customer_id INT,
                price DECIMAL(10,2),
                num_tickets INT
                );
           """
           )


    #sql = 'INSERT INTO event_ticket_system.ticket_sales (ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    f = open(file_path,"r")
    dt = reader(f)
    sql = """INSERT INTO event_ticket_system.ticket_sales VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    for row in dt:
        cursor.execute(sql, tuple(row))
    connection.commit()
    cursor.close()
def query_popular_tickets(connection):
# Get the most popular ticket in the past month
    sql_statement = """
                WITH top_selling_tickets
                AS (SELECT 
                    event_name,
                    ROW_NUMBER() OVER (
                        ORDER BY num_tickets DESC) row_num
                    FROM 
                    ticket_sales
                )
                SELECT 
                   event_name
                FROM 
                top_selling_tickets
                WHERE row_num <= 3;"""
                
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records



connection = get_db_connection()
load_third_party(connection, 'third_party_sales_1.csv')
records = query_popular_tickets(connection)
print("Here are the most popular tickets in the past month: ")
for rec in records:
    print("- ",rec[0])
    
