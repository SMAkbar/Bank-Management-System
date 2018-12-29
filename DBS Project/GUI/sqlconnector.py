import mysql.connector
class SQLconnection:
    def __init__(self):
        prop = {
            "user": "root",
            'password': 'zxcvbn',
            'host': '127.0.0.1',
            'database': 'bank',

        }
        self.cnx = mysql.connector.connect(**prop)
        self.cursor = self.cnx.cursor()
    def getBalance(self, id):
        query = f'select * from customer where customer_id = {id}'
        self.cnx._execute_query(query)

    def getCategory(self):
        query = 'select * from userData2'
        self.cnx._execute_query(query)

    def getResultSet(self):
        em = []
        for i in self.cursor:
            em.append(list(i))
        return em

if __name__ == '__main__':
    sql = SQLconnection()
    sql.getCategory()
    result = sql.getResultSet()

    print(result[0])
    #print(str(result[0][7])[:4])