import logging

from src.db.db_connector.PostgresConnectionService import PostgresConnectionService


class BasePostgresRepo():
    @staticmethod
    def execute_statement(script):
        connection = PostgresConnectionService.get_db_connection()
        cursor = connection.cursor()
        cursor.execute(script)
        connection.commit()
        cursor.close()

    @staticmethod
    def execute_query(script):
        logging.info('start execute query ' + script)
        connection = PostgresConnectionService.get_db_connection()
        cursor = connection.cursor()
        cursor.execute(script)
        query_result = cursor.fetchall()
        cursor.close()
        logging.info('query result ' + str(query_result))
        return query_result
