from brownie import (
    MemberMap,
    Membership,
    MembershipV2,
    TestMap,
)
from scripts.helper import get_account, get_accounts
import pytest


@pytest.fixture(autouse=True, scope="module")
def account():
    return get_account()


@pytest.fixture(autouse=True, scope="module")
def accounts():
    return get_accounts()


@pytest.fixture(autouse=True, scope="module")
def Map(account):
    MemberMap.deploy({"from": account})


@pytest.fixture(scope="module")
def TestMemberMap(account):
    return TestMap.deploy({"from": account})


@pytest.fixture(scope="module")
def MembershipMap(account):
    membership = Membership.deploy({"from": account})
    membership.initialize({"from": account})
    return membership


@pytest.fixture(scope="module")
def MembershipV2Map(account):
    return MembershipV2.deploy({"from": account})
