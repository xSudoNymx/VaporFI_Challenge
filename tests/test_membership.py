import brownie
import pytest


@pytest.fixture(autouse=True)
def shared_setup(fn_isolation):
    pass


def test_create_membership(accounts, MembershipMap):
    MembershipMap.createMembership(accounts[1], "Sudo1", {"from": accounts[0]})
    MembershipMap.createMembership(accounts[2], "Sudo2", {"from": accounts[0]})
    MembershipMap.createMembership(accounts[3], "Sudo3", {"from": accounts[0]})
    assert MembershipMap.getMembership(1)[1] == "Sudo1"
    assert MembershipMap.getMembership(2)[1] == "Sudo2"
    assert MembershipMap.getMembership(3)[1] == "Sudo3"


def test_create_membership_revert(accounts, MembershipMap):
    MembershipMap.createMembership(accounts[1], "Sudo1", {"from": accounts[0]})
    with brownie.reverts():
        MembershipMap.createMembership(accounts[1], "Sudo1", {"from": accounts[0]})
    MembershipMap.createMembership(accounts[2], "Sudo2", {"from": accounts[0]})
    with brownie.reverts():
        MembershipMap.createMembership(accounts[2], "Sudo2", {"from": accounts[0]})
    MembershipMap.createMembership(accounts[3], "Sudo3", {"from": accounts[0]})
    with brownie.reverts():
        MembershipMap.createMembership(accounts[3], "Sudo3", {"from": accounts[0]})
    assert MembershipMap.getMembership(1)[1] == "Sudo1"
    assert MembershipMap.getMembership(2)[1] == "Sudo2"
    assert MembershipMap.getMembership(3)[1] == "Sudo3"


def test_create_membership_multi(accounts, MembershipMap):
    MembershipMap.createMemberships(
        (accounts[1], accounts[2], accounts[3]),
        ("Sudo1", "Sudo2", "Sudo3"),
        {"from": accounts[0]},
    )
    assert MembershipMap.getMembership(1)[1] == "Sudo1"
    assert MembershipMap.getMembership(2)[1] == "Sudo2"
    assert MembershipMap.getMembership(3)[1] == "Sudo3"


def test_create_membership_multi_revert(accounts, MembershipMap):
    MembershipMap.createMemberships(
        (accounts[1], accounts[2], accounts[3]),
        ("Sudo1", "Sudo2", "Sudo3"),
        {"from": accounts[0]},
    )
    with brownie.reverts():
        MembershipMap.createMemberships(
            (accounts[1], accounts[2], accounts[3]),
            ("sudo", "sudo", "sudo"),
            {"from": accounts[0]},
        )
    assert MembershipMap.getMembership(1)[1] == "Sudo1"
    assert MembershipMap.getMembership(2)[1] == "Sudo2"
    assert MembershipMap.getMembership(3)[1] == "Sudo3"


def test_update_membership(accounts, MembershipMap):
    MembershipMap.createMembership(accounts[1], "Sudo1", {"from": accounts[0]})
    MembershipMap.createMembership(accounts[2], "Sudo2", {"from": accounts[0]})
    MembershipMap.createMembership(accounts[3], "Sudo3", {"from": accounts[0]})
    assert MembershipMap.getMembership(1)[1] == "Sudo1"
    assert MembershipMap.getMembership(2)[1] == "Sudo2"
    assert MembershipMap.getMembership(3)[1] == "Sudo3"
    MembershipMap.updateMembership(1, "Sudo1_new", {"from": accounts[1]})
    assert MembershipMap.getMembership(1)[1] == "Sudo1_new"
    MembershipMap.updateMembership(2, "Sudo2_new", {"from": accounts[2]})
    assert MembershipMap.getMembership(2)[1] == "Sudo2_new"
    MembershipMap.updateMembership(3, "Sudo3_new", {"from": accounts[3]})
    assert MembershipMap.getMembership(3)[1] == "Sudo3_new"


def test_update_membership_reverts(accounts, MembershipMap):
    MembershipMap.createMembership(accounts[1], "Sudo1", {"from": accounts[0]})
    assert MembershipMap.getMembership(1)[1] == "Sudo1"
    with brownie.reverts():
        MembershipMap.updateMembership(1, "Sudo1_new", {"from": accounts[0]})


def test_delete_membership(accounts, MembershipMap):
    MembershipMap.createMembership(accounts[1], "Sudo1", {"from": accounts[0]})
    MembershipMap.createMembership(accounts[2], "Sudo2", {"from": accounts[0]})
    MembershipMap.createMembership(accounts[3], "Sudo3", {"from": accounts[0]})
    assert MembershipMap.getMembership(1)[1] == "Sudo1"
    assert MembershipMap.getMembership(2)[1] == "Sudo2"
    assert MembershipMap.getMembership(3)[1] == "Sudo3"
    MembershipMap.deleteMembership(1, {"from": accounts[0]})
    with brownie.reverts():
        MembershipMap.getMembership(1)
    MembershipMap.deleteMembership(2, {"from": accounts[0]})
    with brownie.reverts():
        MembershipMap.getMembership(2)
    MembershipMap.deleteMembership(3, {"from": accounts[0]})
    with brownie.reverts():
        MembershipMap.getMembership(3)
