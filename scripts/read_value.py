from brownie import SimpleStorage, accounts, config


def read_contract():
    # SimpleStorage is an object containing all its deployments
    # Get latest deployment
    simple_storage = SimpleStorage[-1]
    # We would need the Address and ABI, but brownie abstracts the process by looking for that information automatically
    print(simple_storage.retrieve())


def main():
    read_contract()
