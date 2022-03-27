class Usuario:
    def __init__(self,id_usuario=None,username=None,password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password
        pass
    @property
    def id_usuario(self):
        return self._id_usuario
    @property
    def username(self):
        return self._username
    @property
    def password(self):
        return self._password

    @id_usuario.setter
    def id_usuario(self,id_usuario):
        self._id_usuario =id_usuario
        pass
    @username.setter
    def username(self,username):
        self._username = username
        pass
    @password.setter
    def password(self,password):
        self._password = password
        pass
    def __str__(self):
        return f'''Usuario: {self._id_usuario}  {self._username} {self._password}
        '''
    pass