import unittest
from api.services.estimations_service import EstimationsService
from api.models.states_model import State
from api import db

class TestEstimationsService(unittest.TestCase):

    def setUp(self):
        self.state = State(
            abbreviation='CA',
            normal_commission=0.1,
            premium_commission=0.2,
            iva=0.05,
            base_discount='{"value": 0.1, "min": 0, "max": 100, "min_bound": "exclusive", "max_bound": "exclusive"}',
            total_discount='{"value": 0.2, "min": 100, "max": 200, "min_bound": "inclusive", "max_bound": "exclusive"}',
            premium_discount='{"value": 0.1, "min": 0, "max": 200, "min_bound": "inclusive", "max_bound": "exclusive"}'
        )
        db.session.add(self.state)
        db.session.commit()

    def tearDown(self):
        db.session.delete(self.state)
        db.session.commit()

    def test_normal_estimation(self):
        estimation_service = EstimationsService(
            state='CA',
            estimation_type='NORMAL',
            kilometers=50,
            base_amount=100
        )
        response = estimation_service.calculate_estimation()
        self.assertEqual(response[1], 200)

    def test_premium_estimation(self):
        estimation_service = EstimationsService(
            state='CA',
            estimation_type='PREMIUM',
            kilometers=50,
            base_amount=100
        )
        response = estimation_service.calculate_estimation()
        self.assertEqual(response[1], 200)
