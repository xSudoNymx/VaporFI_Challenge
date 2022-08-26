import brownie
import pytest


@pytest.fixture(autouse=True)
def shared_setup(fn_isolation):
    pass


def test_add_Membership(accounts, TestMemberMap):
    TestMemberMap.add(accounts[0], "Sudo", 1, {"from": accounts[0]})
    assert TestMemberMap.exist(1) == True
    assert TestMemberMap.size() == 1
    TestMemberMap.add(accounts[1], "Sudo", 2, {"from": accounts[1]})
    TestMemberMap.add(accounts[2], "Sudo", 3, {"from": accounts[2]})
    assert TestMemberMap.exist(1) == True
    assert TestMemberMap.exist(2) == True
    assert TestMemberMap.exist(0) == False
    assert TestMemberMap.size() == 3


def test_get_Membership(accounts, TestMemberMap):
    TestMemberMap.add(accounts[0], "Sudo", 1, {"from": accounts[0]})
    membership = TestMemberMap.get(1)
    assert membership[0] == accounts[0]
    assert membership[1] == "Sudo"
    assert membership[3] - membership[2] == 30 * 24 * 60 * 60


def test_update_Membership(accounts, TestMemberMap):
    TestMemberMap.add(accounts[0], "Sudo1", 1, {"from": accounts[0]})
    TestMemberMap.add(accounts[1], "Sudo2", 2, {"from": accounts[1]})
    TestMemberMap.add(accounts[2], "Sudo3", 3, {"from": accounts[2]})
    TestMemberMap.update(1, "pseudo1", {"from": accounts[0]})
    TestMemberMap.update(2, "pseudo2", {"from": accounts[1]})
    TestMemberMap.update(3, "pseudo3", {"from": accounts[2]})
    assert TestMemberMap.size() == 3
    assert TestMemberMap.getUsername(1) == "pseudo1"
    assert TestMemberMap.getUsername(2) == "pseudo2"
    assert TestMemberMap.getUsername(3) == "pseudo3"


def test_remove_Membership(accounts, TestMemberMap):
    TestMemberMap.add(accounts[0], "Sudo1", 1, {"from": accounts[0]})
    TestMemberMap.add(accounts[1], "Sudo2", 2, {"from": accounts[1]})
    TestMemberMap.add(accounts[2], "Sudo3", 3, {"from": accounts[2]})
    assert TestMemberMap.size() == 3
    TestMemberMap.remove(1, {"from": accounts[0]})
    assert TestMemberMap.size() == 2
    TestMemberMap.remove(2, {"from": accounts[1]})
    assert TestMemberMap.size() == 1
    TestMemberMap.remove(3, {"from": accounts[2]})
    assert TestMemberMap.size() == 0
    assert TestMemberMap.exist(1) == False
    assert TestMemberMap.exist(2) == False
    assert TestMemberMap.exist(3) == False
