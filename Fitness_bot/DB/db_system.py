from dataclasses import dataclass

import psycopg2

con = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password=1,
    host='localhost',
    port=5432
)

cur = con.cursor()


@dataclass
class DB:
    user_id: int = None
    is_bot: str = None
    first_name: str = None
    last_name: str = None
    username: str = None
    language_code: str = None
    phone_number: str = None

    query = """
        create table if not exists fitness_user(
            id serial primary key,
            user_id bigint,
            is_bot varchar(5),
            first_name varchar(30),
            last_name varchar(30),
            username varchar(30),
            language_code varchar(5),
            phone_number varchar(20)
            
        )
        """
    cur.execute(query)
    con.commit()

    def add_user(self, user_id, is_bot, first_name, last_name, username, language_code):
        query = """
            insert into fitness_user(user_id, is_bot, first_name, last_name, username,language_code)
            values (%s,%s,%s,%s,%s,%s)
        """
        params = (user_id, is_bot, first_name, last_name, username, language_code)

        cur.execute(query,params)
        con.commit()

    def if_exists(self, user_id):
        query = """
            select * from fitness_user where user_id = %s
        """
        param = (user_id,)
        cur.execute(query, param)
        if cur.fetchall():
            return True
        return False

    def update_number(self, user_id, phone_number):
        query = """
            update fitness_user set phone_number=%s where user_id = %s
        """
        param = (phone_number, user_id)
        cur.execute(query, param)
        con.commit()


