from turtle import update
from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    prosumer_1 = accounts.add(config["wallets"]["from_key_1"])
    prosumer_2 = accounts.add(config["wallets"]["from_key_2"])
    consumer = accounts.add(config["wallets"]["from_key_3"])
    print(prosumer_1)
    print(prosumer_2)
    print(consumer)
    simple_storage = SimpleStorage.deploy({"from": prosumer_1})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": prosumer_1})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    pass


# def get_account():
# if network.show_active() == "development"


def main():
    deploy_simple_storage()
