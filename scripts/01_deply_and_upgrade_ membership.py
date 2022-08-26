from scripts.deploy_membership_v1 import deploy_membership
from scripts.upgrade_membership_v2 import upgrade_membership
from scripts.helper import get_account

from brownie import (
    Membership,
    MembershipV2,
    MemberMap,
    Contract,
    TransparentUpgradeableProxy,
)


def main():
    account = get_account()
    MemberMap.deploy({"from": account})

    deploy_membership()

    proxy = Contract.from_abi(
        "Membership", TransparentUpgradeableProxy[-1].address, Membership.abi
    )
    print(proxy.owner({"from": account}))
    proxy.createMembership(account, "John Doe", {"from": account})
    proxy.updateMembership(1, "Sudonym", {"from": account})

    upgrade_membership()

    proxy = Contract.from_abi(
        "MembershipV2", TransparentUpgradeableProxy[-1].address, MembershipV2.abi
    )
    print(f"Here is the initial Size of Memberships: {proxy.getMembershipCount()}")
    print(f"Membership Name: {proxy.getMembership(1)[1]}")
