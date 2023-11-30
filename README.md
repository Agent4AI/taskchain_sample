# taskchain_sample

Install ngrok

python -m venv venv

pip install -r requirements.txt

flask --app app run -p 8090 --debug

You'll have to modify shipstation.py to use your own credentials since taskchain won't have them. 

Use this JSON for your taskchain configuration:

            [
                {
                    "name": "shipstation_start",
                    "endpoint": "https://[YOURHOST]/integrations/demo/"
                },
                {
                    "name": "shipstation_order",
                    "endpoint": "https://[YOURHOST]/integrations/demo/"
                }
            ]



