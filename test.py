from nowstagram import app
import unittest

class NowstagramTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        print 'setUp'

    def tearDown(self):
        print 'tearDown'
        pass


    def register(self,username,password):
        return self.app.post('/reg/',data={'username':username,'password':password},follow_redirects = True)


    def login(self,username,password):
        return self.app.post('/login/',data={'username':username,'password':password},follow_redirects = True)

    def logout(self):
        return self.app.get('/logout')


    def test_reg_logout_login(self):
        assert self.register("hello","world").status_code ==200
        assert '-hello' in self.app.open('/').data

        assert  self.logout()
        self.logout()





