from api import create_app, db
from api.models.states_model import State

app = create_app()

@app.before_first_request
def create_initial_states():
    db.create_all()

    if State.query.count() == 0:
        initial_states = [
            State(abbreviation='NY', normal_commission=0.25, premium_commission=0.35),
            State(abbreviation='CA', normal_commission=0.23, premium_commission=0.33),
            State(abbreviation='AZ', normal_commission=0.20, premium_commission=0.30),
            State(abbreviation='TX', normal_commission=0.18, premium_commission=0.28),
            State(abbreviation='OH', normal_commission=0.15, premium_commission=0.25)
        ]

        for state in initial_states:
            db.session.add(state)

        db.session.commit()

if __name__ == '__main__':
    app.run()