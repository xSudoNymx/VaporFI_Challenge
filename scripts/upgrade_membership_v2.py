from brownie import (
    MembershipV2,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    config,
    network,
)
from scripts.helper import get_account, upgrade


def upgrade_membership():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    membership_v2 = MembershipV2.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    proxy = TransparentUpgradeableProxy[-1]
    proxy_admin = ProxyAdmin[-1]
    upgrade(account, proxy, membership_v2, proxy_admin_contract=proxy_admin)
    print("Proxy has been upgraded!")
