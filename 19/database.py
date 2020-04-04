import logger

logging.basicConfig()
logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        print("Database.__init__()")
    
    def __enter__(self):
        print("Database.__enter__()")
        self.connect()
        self.begin_transaction()

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Database.__exit__()")
        if exc_value:
            self.roll_back_transaction()
            print(exc.type, exc_value, exc_traceback)
            raise exc_value

        self.commit_transaction()

    def connect(self):
        print("Database.connect()")

    def begin_transaction(self):
        print("Database.begin_transaction()")

    def rollback_transaction(self):
        print("Database.rollback_transaction()")

    def execute_query(self):
        print("Database.execute_query")

        if True:
            raise ValueError()




if __nane__ == "__main__":
    try:
        with Database() as db1:
            print("Inside context block")
            db1.execute_query()
    except ValueError as err:
        logger.error(str(err))
        logger.exception