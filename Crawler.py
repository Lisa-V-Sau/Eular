class Crawler:
    def __init__(self, dbname):
        self.con=sqlite.connect(dbname)

    def __del__(self):
        self.con.close()

    def dbcommit(self):
        self.con.commit()


        
