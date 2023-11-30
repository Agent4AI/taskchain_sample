import sys
import importlib


def get_task_class(jreq):
    importlib.import_module("tasks."+ jreq['name'])
    print ("Calling ", jreq['name'])
    return getattr(sys.modules["tasks." + jreq['name']], 'Task')

class BaseTask():
    def __init__(self):
        pass

    def _disqualified(self, jreq):
        return {"content":"Sorry, that is incorrect",
                "actions":[{'name':'end_call'}]}

    def _qualified(self, jreq):
        return {"content":"Okay, thank you.",
                "actions":[{'name':'end_task'}]}

    def call(self, jreq):
        print ("Calling", jreq['action'])
        if jreq['action'] == 'initial':
            return self._initial(jreq)
        if jreq['action'] == 'qualified':
            return self._qualified(jreq)
        if jreq['action'] == 'disqualified':
            return self._disqualified(jreq)
        