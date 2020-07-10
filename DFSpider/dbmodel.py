import mysql.connector as mc


class db_model:

    def __init__(self, conf, fnm=0):
        self.connect = mc.connect(
            host=conf['host'],
            user=conf['user'],
            password=conf['password'],
            database=conf['database'],
            charset=conf['charset']
        )
        self.cursor = self.connect.cursor()
        self.fnm = fnm

    def creat_table(self, table, content=""):
        self.fnm = len(content.split(","))
        self.cursor.execute("CREATE TABLE " + table + " (" + content + ")")

    def insert_one(self, table, row):
        value = self.get_value()
        sql = "INSERT INTO " + table + " (name, address) VALUES (" + value + ")"
        self.cursor.execute(sql, row)
        self.connect.commit()
        print(self.cursor.rowcount + " row inserted")

    def insert_many(self, table, rows):
        value = self.get_value()
        sql = "INSERT INTO " + table + " (name, address) VALUES (" + value + ")"
        self.cursor.execute(sql, rows)
        self.connect.commit()
        print(self.cursor.rowcount + " rows inserted")

    def get_value(self):
        value = "%s"
        for i in range(self.fnm - 1):
            value += ",%s"
        return value
