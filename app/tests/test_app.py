import unittest
'''
Basic app unit tests
'''

from app import covid_app, create_app
create_app('testing')


class BasicTestCase(unittest.TestCase):
    def test_home(self):
        '''test home page'''
        tester = covid_app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_not_found(self):
        '''
        test not found url
        :return:
        '''
        tester = covid_app.test_client(self)
        response = tester.get('a', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_get_covid_data(self):
        '''
        test get state covid data
        :return:
        '''
        from app.routes.routes_util import get_data
        st, data=get_data('ca')
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data[0], dict)







if __name__ == '__main__':
    unittest.main()