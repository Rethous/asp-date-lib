import clingo
import sys

class MyModel:
    def __init__(self):
        self.answer = []
        self.cost = None

def run(instance):
    ctl = clingo.Control()
    m = MyModel()
    def on_model(model):
        m.answer = model.symbols(atoms=True)
        m.cost = model.cost
    ctl.configuration.solve.models="0"
    ctl.load("../date-lib.lp")
    ctl.load(instance)

    ctl.ground([("base",[])])
    ctl.solve(on_model=on_model)
    return m

def test_date_consider_month():
    answer = set(run("date_consider_month_2020.lp").answer)
    assert({clingo.parse_term("date_consider((31,1,2020))")} <= answer)
    assert({clingo.parse_term("date_consider((28,2,2020))")} <= answer)
    assert({clingo.parse_term("date_consider((29,2,2020))")} <= answer)
    assert({clingo.parse_term("date_consider((30,2,2020))")}.isdisjoint(answer))
    assert({clingo.parse_term("date_consider((30,4,2020))")} <= answer)
    assert({clingo.parse_term("date_consider((31,4,2020))")}.isdisjoint(answer))

    answer = set(run("date_consider_month_2021.lp").answer)
    assert({clingo.parse_term("date_consider((31,1,2021))")} <= answer)
    assert({clingo.parse_term("date_consider((28,2,2021))")} <= answer)
    assert({clingo.parse_term("date_consider((29,2,2021))")}.isdisjoint(answer))
    assert({clingo.parse_term("date_consider((30,2,2021))")}.isdisjoint(answer))
    assert({clingo.parse_term("date_consider((31,4,2021))")}.isdisjoint(answer))

    answer = set(run("date_consider_month_2004.lp").answer)
    assert({clingo.parse_term("date_consider((31,1,2004))")} <= answer)
    assert({clingo.parse_term("date_consider((28,2,2004))")} <= answer)
    assert({clingo.parse_term("date_consider((29,2,2004))")} <= answer)
    assert({clingo.parse_term("date_consider((30,2,2004))")}.isdisjoint(answer))
    assert({clingo.parse_term("date_consider((30,4,2004))")} <= answer)
    assert({clingo.parse_term("date_consider((31,4,2004))")}.isdisjoint(answer))

def test_is_leap_year():
    answer = set(run("date_consider_month_2020.lp").answer)
    assert({clingo.parse_term("is_leap_year(2020)")} <= answer)
    #assert({clingo.parse_term("is_leap_year(2020)")}.isdisjoint(answer))
    #assert({clingo.parse_term("is_leap_year(2020)")} not in answer)
    
    answer = set(run("date_consider_month_2021.lp").answer)
    assert({clingo.parse_term("is_leap_year(2021)")}.isdisjoint(answer))

    answer = set(run("date_consider_month_2004.lp").answer)
    assert({clingo.parse_term("is_leap_year(2004)")} <= answer)
