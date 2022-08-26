from brownie import (
    Membership,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    config,
    network,
)
from scripts.helper import get_account, encode_function_data


def deploy_membership():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    membership = Membership.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # deploy the ProxyAdmin and use that as the admin contract
    proxy_admin = ProxyAdmin.deploy(
        {"from": account},
    )

    membership_encoded_initializer_function = encode_function_data(
        initializer=membership.initialize
    )

    # deploy the TransparentUpgradeableProxy and use that as the proxy contract
    proxy = TransparentUpgradeableProxy.deploy(
        membership.address,
        proxy_admin.address,
        membership_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )
    print(f"Proxy deployed to {proxy}!")
