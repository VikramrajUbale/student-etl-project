import snowflake.connector
from config import SNOWFLAKE_CONFIG

def load_data(df):
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG["user"],
        password=SNOWFLAKE_CONFIG["password"],
        account=SNOWFLAKE_CONFIG["account"],
        warehouse=SNOWFLAKE_CONFIG["warehouse"],
        database=SNOWFLAKE_CONFIG["database"],
        schema=SNOWFLAKE_CONFIG["schema"]
    )

    cur = conn.cursor()
    cur.execute("DELETE FROM student")

    for index, row in df.iterrows():
        query = f"""
        INSERT INTO student (ID, NAME, MARKS,GRADE, INSERTED_DTTS)
        VALUES ({row['id']}, '{row['name']}', {row['marks']}, '{row['grade']}','{row['INSERTED_DTTS']}')
        """
        cur.execute(query)

    cur.execute("select id, name, marks, grade,TO_VARCHAR(INSERTED_DTTS, 'YYYY-MM-DD HH24:MI:SS') from student;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()