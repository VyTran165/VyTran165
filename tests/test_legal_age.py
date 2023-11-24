import pytest
from t3_can_vote_and_retiring_age import User
from t3_pre_retire_and_retiring_percent import User1
from t3_can_vote_and_can_drink import User2

@pytest.mark.parametrize('age, can_vote, retirement_years', [
    (16, False, 49),
    (18, True, 47),
    (65, True, 0)
])
def test_can_vote_and_retirement_years(age, can_vote, retirement_years):
    user_instance = User(age)
    assert user_instance.can_vote() == can_vote
    assert user_instance.retirement_years() == retirement_years

@pytest.mark.parametrize('age, pre_retire, retire_percent',[
    (18,42,0),
    (60,0,60),
    (61,0,68),
])

def test_pre_retire_and_retire_percent(age, pre_retire, retire_percent):
    user_instance = User1(age)
    assert user_instance.pre_retire() == pre_retire
    assert user_instance.retirement_percent() == retire_percent

@pytest.mark.parametrize('age,can_vote,can_drink',[
    (18, True, False),
    (21, True, True),
    (16, False, False),
])

def test_can_drink_and_can_vote(age, can_vote, can_drink):
    user_instance = User2(age)
    assert user_instance.can_vote() == can_vote
    assert user_instance.can_drink() == can_drink