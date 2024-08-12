import re
import os
import psycopg
URL = os.getenv('DATABASE_URL')
conn = psycopg.connect(URL)
# try:
#     with conn.cursor() as cur:
#         cur.execute('CALL insert_test(%s, %s)', (name, age))
#         cur.fetchall()
#         for record in cur:
#             print(record)
#         conn.commit()
# except BaseException:
#     conn.rollback()
# else:
#     conn.commit()
# finally:
#     conn.close()
