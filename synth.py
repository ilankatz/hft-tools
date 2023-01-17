from abis import (
    snx_exchange_rates_abi,
    transferMarginETH_abi,
    futuresMarketEth_abi,
    price_feed_abi
)
import time
from web3 import Web3

def synthPricePairs(source, destination, amount, web3):
    #snx_exchange_rates_contract = "0x061B75475035c20ef2e35E1002Beb90C3c1f24cC"
    snx_exchange_rates_contract = "0x913bd76F7E1572CC8278CeF2D6b06e2140ca9Ce2"
    snx_exchange_rates_contract_i = web3.eth.contract(address=snx_exchange_rates_contract, abi=snx_exchange_rates_abi)
    hexSource = source.encode("utf-8").hex()
    hexDest = destination.encode("utf-8").hex()
    return snx_exchange_rates_contract_i.functions.effectiveValueAndRates(hexSource,amount,hexDest).call()
    

def getSynthPrices(assets, web3):
    prices = {}
    #snx_exchange_rates_contract = "0x061B75475035c20ef2e35E1002Beb90C3c1f24cC"
    snx_exchange_rates_contract = "0x913bd76F7E1572CC8278CeF2D6b06e2140ca9Ce2"
    snx_exchange_rates_contract_i = web3.eth.contract(address=snx_exchange_rates_contract, abi=snx_exchange_rates_abi)
    for asset in assets:
        hexAsset = asset.encode("utf-8").hex()
        prices[asset] = snx_exchange_rates_contract_i.functions.ratesForCurrencies([(hexAsset)]).call()
    return prices

def changeMarginAccount(privateKey, asset, amount, web3, nonce = None):
    amount *= 10**18
    amount = int(amount)
    account=web3.eth.account.from_key(privateKey).address
    nonce = nonce if nonce else web3.eth.getTransactionCount(account)
    transferMarginAddress = web3.toChecksumAddress("0x0d10c032ad006c98c33a95e59ab3ba2b0849bd59")
    transferMarginEthCon = web3.eth.contract(address=transferMarginAddress, abi=transferMarginETH_abi)
    tx = transferMarginEthCon.functions.transferMargin(amount).buildTransaction(
        {
            "chainId": 420,
            "from": account,
            "nonce": nonce,
            #'gas': 350000,
            'gasPrice': web3.eth.gas_price
        }
    )
    signed_txn = web3.eth.account.sign_transaction(
        tx, private_key=privateKey
    )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)

def buyPerp(privateKey, amount, code, web3, nonce=None):
    amount *= 10**18
    amount = int(amount)
    account=web3.eth.account.from_key(privateKey).address
    nonce = nonce if nonce else web3.eth.getTransactionCount(account)
    address = web3.toChecksumAddress("0x0d10c032ad006c98c33a95e59ab3ba2b0849bd59")
    futuresMarketEthCon = web3.eth.contract(address=address,abi=futuresMarketEth_abi)
    tx = futuresMarketEthCon.functions.modifyPositionWithTracking(amount, code).buildTransaction(
        {
            "chainId": 420,
            "from": account,
            "nonce": nonce,
            #'gas': 1600000,
            'gasPrice': web3.eth.gas_price
        }
    )
    signed_txn = web3.eth.account.sign_transaction(
        tx, private_key=privateKey
    )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash), code

def closePosition(privateKey, asset, code, web3, nonce=None):
    account=web3.eth.account.from_key(privateKey).address
    nonce = nonce if nonce else web3.eth.getTransactionCount(account)
    address = web3.toChecksumAddress("0x0d10c032ad006c98c33a95e59ab3ba2b0849bd59")
    futuresMarketEthCon = web3.eth.contract(address=address,abi=futuresMarketEth_abi)
    tx = futuresMarketEthCon.functions.closePositionWithTracking(code).buildTransaction(
        {
            "chainId": 420,
            "from": account,
            "nonce": nonce,
            #'gas': 1600000,
            'gasPrice': web3.eth.gas_price
        }
    )
    signed_txn = web3.eth.account.sign_transaction(
        tx, private_key=privateKey
    )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash), code
def get_asset_price(feedAddress, web3):
    feedAddress = web3.toChecksumAddress(feedAddress)
    feed = web3.eth.contract(
        address=feedAddress, abi=price_feed_abi)
    latest_price = feed.functions.latestRoundData().call()[1],
    return (latest_price)[0]
