from api import create_app, db
from api.models.states_model import State

app = create_app()

@app.before_first_request
def create_initial_states():
    db.create_all()

    if State.query.count() == 0:
        initial_states = [
            State(
                abbreviation='NY',
                normal_commission=0.25,
                premium_commission=0.35,
                iva=0.21,
                base_discount={'value': 0.0}, 
                total_discount={'value': 0.0}, 
                premium_discount={'value': 0.05, 'min': 25.0, 'min_bound': 'exclusive', 'max': 'inf', 'max_boundary': 'exclusive'}
            ),
            State(
                abbreviation='CA',
                normal_commission=0.23, 
                premium_commission=0.33,
                iva=0.0,
                base_discount={'value': 0.0}, 
                total_discount={'value': 0.05, 'min': 26.0, 'min_bound': 'exclusive', 'max': 'inf', 'max_boundary': 'exclusive'}, 
                premium_discount={'value': 0.05, 'min': 25.0, 'min_bound': 'exclusive', 'max': 'inf', 'max_boundary': 'exclusive'}
            ),
            State(
                abbreviation='AZ',
                normal_commission=0.20,
                premium_commission=0.30,
                iva=0.0,
                base_discount={'value': 0.0}, 
                total_discount={'value': 0.05, 'min': 26.0, 'min_bound': 'exclusive', 'max': 'inf', 'max_boundary': 'exclusive'}, 
                premium_discount={'value': 0.05, 'min': 25.0, 'min_bound': 'exclusive', 'max': 'inf', 'max_boundary': 'exclusive'}
            ),
            State(
                abbreviation='TX',
                normal_commission=0.18,
                premium_commission=0.28,
                iva=0.0,
                base_discount={'value': 0.03, 'min': 20.0, 'min_bound': 'inclusive', 'max': 30.0, 'max_boundary': 'inclusive'}, 
                total_discount={'value': 0.05, 'min': 30.0, 'min_bound': 'exclusive', 'max': 'inf', 'max_boundary': 'exclusive'}, 
                premium_discount={'value': 0.05, 'min': 25.0, 'min_bound': 'exclusive', 'max': 'inf', 'max_boundary': 'exclusive'}
            ),
            State(
                abbreviation='OH',
                normal_commission=0.15,
                premium_commission=0.25,
                iva=0.0,
                base_discount={'value': 0.03, 'min': 20.0, 'min_bound': 'inclusive', 'max': 30.0, 'max_boundary': 'inclusive'}, 
                total_discount={'value': 0.05, 'min': 30.0, 'min_bound': 'exclusive', 'max': 'inf', 'max_boundary': 'exclusive'}, 
                premium_discount={'value': 0.05, 'min': 25.0, 'min_bound': 'exclusive', 'max': 'inf', 'max_boundary': 'exclusive'}
            )
        ]

        for state in initial_states:
            db.session.add(state)

        db.session.commit()

if __name__ == '__main__':
    app.run()