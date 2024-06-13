from mysqlconnection import connect_to_mysql

class User:
    DB = 'users_db'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connect_to_mysql(cls.DB).query_db(query)

        users = []

        for user in results:
            users.append(user)
        return users

    @classmethod
    def get_one(cls, id):

        data = {'id': id}

        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connect_to_mysql(cls.DB).query_db(query, data)

        if results :
            return cls(results[0])
        else:
            return None

    # CREATE
    @classmethod
    def create(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
        results = connect_to_mysql(cls.DB).query_db(query, data)

        return results

    # UPDATE
    @classmethod
    def update(cls, data):

        query = 'UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s'
        results = connect_to_mysql(cls.DB).query_db(query, data)
    
        return results

    # DELETE
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {'id': id}
        return connect_to_mysql(cls.DB).query_db(query, data)
