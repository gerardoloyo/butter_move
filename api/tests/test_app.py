import json
import unittest
from flask_testing import TestCase
from api import create_app, db
from api.models.states_model import State

class TestApp(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app


    def setUp(self):
        db.create_all()
        state = State(
            abbreviation='CA',
            normal_commission=0.1,
            premium_commission=0.2,
            iva=0.05,
            base_discount={"value": 0.1, "min": 0, "max": 100, "min_bound": "exclusive", "max_bound": "exclusive"},
            total_discount={"value": 0.2, "min": 100, "max": 200, "min_bound": "inclusive", "max_bound": "exclusive"},
            premium_discount={"value": 0.1, "min": 0, "max": 200, "min_bound": "inclusive", "max_bound": "exclusive"}
        )
        db.session.add(state)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_estimate(self):
        response = self.client.post('/estimate', json={
            'state': 'CA',
            'estimation_type': 'NORMAL',
            'kilometers': 50.0,
            'base_amount': 100.0
        }, headers={'ip-client': '127.0.0.1'})

        self.assertEqual(response.status_code, 201)
        self.assertTrue('total_amount' in response.json)
        self.assertTrue('processed_date' in response.json)


    def test_add_state(self):
        response = self.client.post('/state', json={
            'abbreviation': 'NY',
            'normal_commission': 0.1,
            'premium_commission': 0.2,
            'iva': 0.05,
            'base_discount': {"value": 0.1, "min": 0, "max": 100, "min_bound": "inclusive", "max_bound": "exclusive"},
            'total_discount': {"value": 0.1, "min": 100, "max": 200, "min_bound": "inclusive", "max_bound": "exclusive"},
            'premium_discount': {"value": 0.1, "min": 0, "max": 200, "min_bound": "inclusive", "max_bound": "exclusive"}
        }, headers={'ip-client': '127.0.0.1'})

        self.assertEqual(response.status_code, 201)


    def test_estimate_invalid_state(self):
        response = self.client.post('/estimate', json={
            'state': 'INVALID',
            'estimation_type': 'NORMAL',
            'kilometers': 50,
            'base_amount': 100
        }, headers={'ip-client': '127.0.0.1'})

        self.assertEqual(response.status_code, 400)


    def test_estimate_invalid_estimation_type(self):
        response = self.client.post('/estimate', json={
            'state': 'CA',
            'estimation_type': 'INVALID',
            'kilometers': 50,
            'base_amount': 100
        }, headers={'ip-client': '127.0.0.1'})

        self.assertEqual(response.status_code, 400)


    def test_add_state_invalid_abbreviation(self):
        response = self.client.post('/state', json={
            'abbreviation': 'INVALID',
            'normal_commission': 0.1,
            'premium_commission': 0.2,
            'iva': 0.05,
            'base_discount': {"value": 0.1, "min": 0, "max": 100, "min_bound": "inclusive", "max_bound": "exclusive"},
            'total_discount': {"value": 0.1, "min": 100, "max": 200, "min_bound": "inclusive", "max_bound": "exclusive"},
            'premium_discount': {"value": 0.1, "min": 0, "max": 200, "min_bound": "inclusive", "max_bound": "exclusive"}
        }, headers={'ip-client': '127.0.0.1'})

        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
