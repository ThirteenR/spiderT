import mysql.connector as mc


class db_mode:

    def __init__(self, **conf):
        self.connect = mc.connect(**conf)
        self.cursor = self.connect.cursor()
        self.fnm = 0
        self.table = None

    def close(self):
        if self.connect is not None:
            self.connect.close()

    def creat_table(self, **table):
        self.fnm = len(table['field'].split(","))
        self.table = table['name']
        print("tablename is " + self.table)
        try:
            print(table['field'])
            print("creating table " + self.table)
            self.cursor.execute("CREATE TABLE " + table['name'] + " (" + table['field'] + ")")
        except Exception as e:
            print(e)

    def insert(self, filednames: list, rows: list):
        fl = ",".join(filednames)
        value = self.get_value()
        sql = "INSERT INTO " + self.table + " (" + fl + ")  VALUES (" + value + ")"
        print(sql)
        self.connect.cursor().executemany(sql, rows)
        self.connect.commit()
        print(str(self.cursor.rowcount) + " rows inserted")

    def get_value(self):
        ll = []
        for i in range(self.fnm):
            ll.append('%s')
        return ','.join(ll)
