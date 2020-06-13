import json
class Auth:
    _user = {'username':'root', 'password':'secret'}
    def login(self, arg):
        obj = str(arg)
        dic = json.loads(obj)
        if (dic['username'] == self._user['username']) and (dic['password'] == self._user['password']):
            print('login success')  

    def validate(self, arg):
        user = {'username':'root', 'password':'secret'}
        obj = str(arg)
        dic = json.loads(obj)
        if (dic['username'] == self._user['username']) and (dic['password'] == self._user['password']):
            print('validate success')

    def user(self):
        print(self._user)

Auth = Auth()
Auth.login('{"username":"root", "password": "secret"}')
Auth.validate('{"username":"root", "password": "secret"}')
Auth.user()