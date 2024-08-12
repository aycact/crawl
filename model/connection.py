import re
import os
import psycopg
conn = psycopg.connect(os.environ['DATABASE_URL'])
with conn.cursor() as cur:
    cur.execute('SHOW TABLES FROM tuvi')
    rows = cur.fetchall()
    print(rows)