#pip install psycopg2

import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters

        conn = psycopg2.connect("dbname=TaskBuses user=postgres password=XXX")

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')

        conn = psycopg2.connect(
            database="TaskBuses", user='postgres', password='XXX', host='127.0.0.1', port='5432'
        )

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database buses:')
        cur.execute('SELECT * FROM buses')

        # display the PostgreSQL database server buses
        #print("Result ", cur.fetchall())

        for item in cur.fetchall():
            print(item)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
