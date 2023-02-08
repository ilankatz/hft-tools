from abis import (
    weth_abi,
    lending_pool_addresses_provider_abi,
    lending_pool_abi,
    erc20_abi,
    price_feed_abi,
    protocolDataProvider_abi,
    ui_abi
)
import time



AaveAddressProvider = "0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5"

def get_weth_goerli(privateKey, amount, web3):
    weth_address = web3.toChecksumAddress("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6")
    weth = web3.eth.contract(address=weth_address, abi=weth_abi)
    sw=web3.eth.account.from_key(privateKey)
    account = sw.address
    nonce = web3.eth.getTransactionCount(account)
    function_call = weth.functions.deposit()
    transaction = function_call.buildTransaction(
        {
            "chainId": 5,
            "from": account,
            "nonce": nonce,
            "value": amount,
        }
    )
    signed_txn = web3.eth.account.sign_transaction(
        transaction, private_key= privateKey
    )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    #web3.eth.wait_for_transaction_receipt(tx_hash)
    return web3.toHex(tx_hash)

def get_goerli_lending_pool(web3):
    lpapaddress = web3.toChecksumAddress("0x5E52dEc931FFb32f609681B8438A51c675cc232d")
    lpap = web3.eth.contract(address=lpapaddress, abi=lending_pool_addresses_provider_abi)
    lendPool = (lpap.functions.getLendingPool().call())
    return lendPool

def approveErc20_goerli(erc20_address, spender, amount, privateKey, web3, nonce = None):
    sw=web3.eth.account.from_key(privateKey)
    account = sw.address
    nonce = nonce if nonce else web3.eth.getTransactionCount(account)
    erc20 = web3.eth.contract(address=erc20_address, abi=erc20_abi)
    function_call = erc20.functions.approve(spender, amount)
    transaction = function_call.buildTransaction(
        {
            "chainId": 5,
            "from": account,
            "nonce": nonce,
        }
    )
    signed_txn = web3.eth.account.sign_transaction(
        transaction, private_key = privateKey
    )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    #web3.eth.wait_for_transaction_receipt(tx_hash)
    return web3.toHex(tx_hash)

def depositAave_goerli(privateKey, depositAssetAddress, amount, lending_pool, web3, nonce=None):
    account=web3.eth.account.from_key(privateKey).address
    lendCon = web3.eth.contract(address=lending_pool,abi=lending_pool_abi)
    nonce = nonce if nonce else web3.eth.getTransactionCount(account)
    tx = lendCon.functions.deposit(depositAssetAddress, amount, account, 0).buildTransaction(
        {
            "chainId": 5,
            "from": account,
            "nonce": nonce,
        }
    )
    signed_txn = web3.eth.account.sign_transaction(
        tx, private_key=privateKey
    )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)

def repayAave_goerli(privateKey, amount, lendPool, web3, erc20_address, nonce=None, stableRate = False):
    account=web3.eth.account.from_key(privateKey).address
    nonce = nonce if nonce else web3.eth.getTransactionCount(account)
    if stableRate == False:
        stableRate = 2
    else:
        stableRate = 1
    approveErc20_goerli(erc20_address,lendPool,amount,privateKey,web3,nonce)
    nonce += 1
    lendCon = web3.eth.contract(address=lendPool,abi=lending_pool_abi)
    tx = lendCon.functions.repay(erc20_address, amount, stableRate, account).buildTransaction(
        {
            "chainId": 5,
            "from": account,
            "nonce": nonce,
        }
    )
    signed_txn = web3.eth.account.sign_transaction(tx, private_key=privateKey)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)

def withdrawAave_goerli(privateKey, amount,lendPool, erc20,web3, nonce = None):
    account=web3.eth.account.from_key(privateKey).address
    nonce = nonce if nonce else web3.eth.getTransactionCount(account)
    lendCon = web3.eth.contract(address=lendPool,abi=lending_pool_abi)
    tx = lendCon.functions.withdraw(erc20, amount, account).buildTransaction(
        {
            "chainId": 5,
            "from": account,
            "nonce": nonce,
        }
    )
    signed_txn = web3.eth.account.sign_transaction(
        tx, private_key=privateKey
    )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)
    
def borrowAave_goerli(privateKey, erc20, amount, lendPool, web3, stableRate = False, nonce= None):
    account=web3.eth.account.from_key(privateKey).address
    nonce = nonce if nonce else web3.eth.getTransactionCount(account)
    if stableRate == False:
        stableRate = 2
    else:
        stableRate = 1
    lendCon = web3.eth.contract(address=lendPool,abi=lending_pool_abi)
    tx = lendCon.functions.borrow(erc20, amount, stableRate, 0, account).buildTransaction(
        {
            "chainId": 5,
            "from": account,
            "nonce": nonce,
        }
    )
    signed_txn = web3.eth.account.sign_transaction(
        tx, private_key=privateKey
    )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)

def userData_goerli(address, web3):
    uiCon = web3.eth.contract(address="0xcCb7a1B6B5D72c4AA633B114537cD20612fDccbB",abi=ui_abi)
    lpapaddress = web3.toChecksumAddress("0x5E52dEc931FFb32f609681B8438A51c675cc232d")
    return uiCon.functions.getUserReservesData(lpapaddress,address).call()

def getBorrowRates(asset, web3):
    rate = 0
    return rate
def getHealthFactor():
    return

def get_borrowable_data(lending_pool, account, web3):
   (
       total_collateral_eth,
       total_debt_eth,
       available_borrow_eth,
       current_liquidation_threshold,
       tlv,
       health_factor,
   ) = lending_pool.getUserAccountData(account.address)
   available_borrow_eth = web3.fromWei(available_borrow_eth, "ether")
   total_collateral_eth = web3.fromWei(total_collateral_eth, "ether")
   total_debt_eth = web3.fromWei(total_debt_eth, "ether")
   return (float(available_borrow_eth), float(total_debt_eth))


def repayAll_goerli(privateKey, web3, lendPool, nonce = None):
    account=web3.eth.account.from_key(privateKey).address
    nonce = nonce if nonce else web3.eth.getTransactionCount(account)
    assets = userData_goerli(account,web3)[0]
    borrowed = {}
    for asset in assets:
        con = web3.eth.contract(address=asset[0],abi=erc20_abi)
        if asset[4]/10**con.functions.decimals().call() > 1:
            borrowed[asset[0]] = asset[4]
    hashes = []
    for address in borrowed.keys():
        print(nonce)
        hash = repayAave_goerli(privateKey,borrowed[address],lendPool,web3,address, nonce=nonce)
        nonce += 2
        print(nonce)
        hashes.append(hash)
        print(hash)
    return hashes
