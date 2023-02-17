from brownie import network, accounts, config

LOCAL_NETWORKS = ["development", "ganache-local"]

def get_account(index=None, id=None):
    if index is not None:
        return accounts[index]
    
    if id is not None:
        return accounts.load(id)

    if get_network() in LOCAL_NETWORKS:
        return accounts[0]
    
    return accounts.add(config["wallet"]["from_key"])

def get_network():
    return network.show_active()