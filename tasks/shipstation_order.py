import json

from . import BaseTask

from . import shipstation

class Task(BaseTask):
    def _qualified(self, jreq):
        try:
            param = json.loads(jreq['context'])['responses']
            if param == "NEWORDER":
                return {"content":"Okay, hold on.",
                    "actions":[{'name':'switch_task', 'context':{'name':'shipstation_start'}}]}
        except:
            pass

        return {"content":"Thank you for your business.",
                "actions":[{'name':'end_task'}]}

    def _initial(self, jreq):
        print (jreq)
        data = shipstation.get_data_record(jreq['state']['orderid'], jreq['metadata'])

        if len(data['orders']) == 0:
            return {"content":"Sorry I could not find that order.",
                    "actions":[{'name':'switch_task', 'context':{'name':'shipstation_start'}}]}

        
        content = json.dumps(data['orders'][0]) + """
Do not just write out a script. You are having a spoken conversation with the user. This is an order record. You are having a phone conversation. %s. When they appear to be done, call the qualified function with no parameters. If they appear to want to lookup a new order, call qualified function with the parameter "NEWORDER".
""" % jreq['metadata']['shipstation_order_prompt']
        print (content)
        return ({'content':content})
    