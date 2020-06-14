import json, time
class Auth:
    _user = {'username':'root', 'password':'secret'}
    userAktif = {}
    last_login = None
    idUser = 0
    def login(self, arg):
        obj = str(arg)
        dic = json.loads(obj)
        if (dic['username'] == self._user['username']) and (dic['password'] == self._user['password']):
            self.userAktif = dic
            obj = str(1).zfill(5)
            self.idUser = obj
            print('login success')  

    def logout(self):
        self.userAktif = None
        self.last_login =  time.asctime(time.localtime(time.time()))
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
            print("Check false")
        else:
            print("Check true")

    def guest(self):
        if self.userAktif is None:
            print("Guest true")
        else:
            print("Guest false")

    def lastLogin(self):
        print("Last Login : ", self.last_login)

    def id(self):
        print("Id user : ", self.idUser)

Auth = Auth()
print("Status Login")
Auth.login('{"username":"root", "password": "secret"}')
Auth.validate('{"username":"root", "password": "secret"}')
Auth.user()
Auth.id()
Auth.check()
Auth.guest() 
print("\n")
print("Status logout")
Auth.logout()
Auth.check()
Auth.guest()
Auth.lastLogin()