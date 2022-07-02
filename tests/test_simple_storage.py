from brownie import SimpleStorage, accounts

# To test just one function: brownie test -k testname
# Use "brownie test -s" for more detailed results
# Brownie's testing is very similar to pytest, use its documentation for reference


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 49
    transaction = simple_storage.store(expected, {"from": account})
    transaction.wait(1)
    # Assert
    assert simple_storage.retrieve() == expected
