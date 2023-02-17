from brownie import OurToken
from scripts.helpers import get_account

def deploy():
    print("Deploying OurToken...")
    account = get_account()
    OurToken.deploy(100, {"from": account})
    print("Deployed OurToken!")

def main():
    deploy()