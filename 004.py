import json
class Auth:
    _user = {'username':'root', 'password':'secret'}
    userAktif = {}
    def login(self, arg):
        obj = str(arg)
        dic = json.loads(obj)
        if (dic['username'] == self._user['username']) and (dic['password'] == self._user['password']):
            self.userAktif = dic
            print('login success')  

    def logout(self):
        self.userAktif = None
        print("success")

    def validate(self, arg):
        user = {'username':'root', 'password':'secret'}
        obj = str(arg)
        dic = json.loads(obj)
        if (dic['username'] == self._user['username']) and (dic['password'] == self._user['password']):
            print('validate success')

    def user(self):
        print("Information about current logged in user.", self.userAktif)

    def check(self):
        if self.userAktif is None:
            print("false")
        else:
            print("true")

    def guest(self):
        if self.userAktif is None:
            print("true")
        else:
            print("false")



Auth = Auth()
print("Status Login")
Auth.login('{"username":"root", "password": "secret"}')
Auth.validate('{"username":"root", "password": "secret"}')
Auth.user()
Auth.check()
Auth.guest() 
print("\n")
print("Status logout")
Auth.logout()
Auth.check()
Auth.guest()