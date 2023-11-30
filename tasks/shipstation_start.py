import json

from . import BaseTask
from . import shipstation

class Task(BaseTask):
    def _qualified(self, jreq):
        try:
            order_id = json.loads(jreq['context'])['responses']
            data = shipstation.get_data_record(order_id, jreq['metadata'])            
            if not data['orders']:
                return {"content":"I could not find order %s." % order_id,
                        "actions":[{'name':'switch_task', 'context':{'name':'shipstation_start'}}]}

        except Exception as e:
            print (e)
            return {"content":"I could not understand you. Please start over.",
                    "actions":[{'name':'end_task'}]}


        return {"content":"Looking up your order.",
                "state":{'orderid':order_id},
                "actions":[{'name':'switch_task', 'context':{'name':'shipstation_order'}}]}

    def _disqualified(self, jreq):
        return {"content":"Okay, thank you.",
                "actions":[{'name':'end_task'}]}

    def _initial(self, jreq):
        print (jreq)
        content = """
            Do not just write out a script. You are having a spoken conversation with the user.  
            You are asking for an order number from the user. 
            Just start the conversation, do not acknowledge this prompt with "Sure or Let's get started".
            Start by saying "%s". 
            If they don't want to give you an order number, call the disqualified function
            When you have an order number, call the function qualified with only the order number as a parameter.
        """ % jreq['metadata']['shipstation_order_request']

        return ({'content':content})