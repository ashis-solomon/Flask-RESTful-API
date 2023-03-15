class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, user_dict):
        return cls(
            id=user_dict['id'],
            name=user_dict['name'],
            email=user_dict['email'],
            password=user_dict['password']
        )