from mysqlconnection import connect_to_mysql

class User:
    DB = "users_db"
    
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connect_to_mysql(cls.DB).query_db(query)
        
        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results

    @classmethod
    def update (cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        results = connect_to_mysql(cls.DB).query_db(query, data)
        return results


