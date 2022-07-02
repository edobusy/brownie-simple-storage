# You can import smart contracts by their name via brownie
from brownie import accounts, config, network, SimpleStorage

# To deploy in a non-simulated network, use the command:
# brownie run scriptPath --network networkName
# REMEMBER: Put the infura project id in the .env before running the code: export WEB3_INFURA_PROJECT_ID=...


def deploy_simple_storage():
    # account = accounts[0]
    # account = accounts.add(config["wallets"]["from_key"])
    account = get_account()
    # Deploying only requires the address of the deployer
    # When deploying a contract, a contract object is returned, which can be used to call functions and actively interact with the deployed contract
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(49, {"from": account})
    # This is similar to the receipt function in web3, as we wait for the transaction to be completed, but we have to include how many blocks we are waiting for
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
