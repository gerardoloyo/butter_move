# Butter Move API

This is a Flask application that provides APIs for estimating prices based on different states and their commission rates, discounts, and taxes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you'll need:

- Python 3.6 or newer
- Git

### Installing

1. Clone the Git repository:

```bash
git clone <YOUR_GIT_REPO>
cd butter_move

2. Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
pip install -r requirements.txt

3. Run the app

```bash
python app.py

Now the application should be running at http://127.0.0.1:5000
Application is loaded with all the states asked on requirements NY, CA, AZ, TX, OH

API Documentation
-Estimate
    URL: /estimate
    Method: POST
    Headers: 'ip-client': <IP_ADDRESS>
    
    Data Params:
    {
        "state": <state_abbreviation>,
        "estimation_type": <"NORMAL"|"PREMIUM">,
        "kilometers": <float>,
        "base_amount": <float>
    }

    Success Response:
    {
        "total_amount": <float>,
        "processed_date": <date_time>
    }


Add State
    URL: /state
    Method: POST
    Headers: 'ip-client': <IP_ADDRESS>
    Data Params:
    {
        "abbreviation": <state_abbreviation>,
        "normal_commission": <float>,
        "premium_commission": <float>,
        "iva": <float>,
        "base_discount": <json_dict>,
        "total_discount": <json_dict>,
        "premium_discount": <json_dict>
    }

    Example of base_discount, total_discount, and premium_discount:
    // This json is used to genrate the discounts rules
    {
        "min": 0.0,
        "max": 100.0, 
        "min_bound": "inclusive", // include min bound in range
        "max_bound": "exclusive", // exclude max bound in range
        "value": 0.1 // Discount percentage
    }
    With first 4 parameters the range [0.0,100.0) is generated. So this rule only applies when 0 <= kilometers < 100. And applies the 10% discount


    Success Response:
    {
        "message": "State added sucessfully",
        "result": "OK"
    }


Update State
    URL: /state
    Method: PATCH
    Headers: 'ip-client': <IP_ADDRESS>
    Data Params:
    {
        "abbreviation": <state_abbreviation>,
        "normal_commission": <float>,
        "premium_commission": <float>,
        "iva": <float>,
        "base_discount": <json_dict>,
        "total_discount": <json_dict>,
        "premium_discount": <json_dict>
    }

    Example of base_discount, total_discount, and premium_discount:
    {
        "min": 0,
        "max": 100,
        "min_bound": "inclusive",
        "max_bound": "exclusive",
        "value": 0.1
    }

    Success Response:
    {
        "message": "State updated successfully",
        "result": "OK"
    }
