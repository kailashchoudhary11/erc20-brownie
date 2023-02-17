from brownie import OurToken, web3
from scripts.helpers import get_account

INITIAL_SUPPLY = web3.toWei(1000, "ether")

def deploy():
    print("Deploying OurToken...")
    account = get_account()
    OurToken.deploy(INITIAL_SUPPLY, {"from": account})
    print("Deployed OurToken!")

def main():
    deploy()