function get_goerli_lending_pool(web3) {
    let lpapaddress = web3.toChecksumAddress("0x5E52dEc931FFb32f609681B8438A51c675cc232d")
    lpap = web3.eth.contract(address=lpapaddress, abi=lending_pool_addresses_provider_abi,)
    lendPool = (lpap.functions.getLendingPool().call())
    return lendPool
}

function approve_erc20_goerli(erc20_address, spender, amount, privateKey, web3, nonce = undefined) {
    sw = web3.eth.account.from_key(privateKey)
    account = sw.address
    nonce = (nonce === undefined) ? nonce : web3.eth.getTransactionCount(account)
    erc20 = web3.eth.contract(address=erc20_address, abi=erc20_abi)
    function_call = erc20.functions.approve(spender, amount)
    nonce = web3.eth.getTransactionCount(account)
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
    //web3.eth.wait_for_transaction_receipt(tx_hash)
    return web3.toHex(tx_hash)
}

function deposit_to_aave_goerli(privateKey, depositAssetAddress, amount, lending_pool, web3, nonce = undefined) {
    account=web3.eth.account.from_key(privateKey).address
    lendCon = web3.eth.contract(address=lending_pool,abi=lending_pool_abi)
    nonce = (nonce === undefined) ? nonce : web3.eth.getTransactionCount(account)
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
}
    
function withdrawAave_goerli(privateKey, amount,lendPool, erc20, web3, nonce = undefined) {
    account=web3.eth.account.from_key(privateKey).address
    nonce = (nonce === undefined) ? nonce : web3.eth.getTransactionCount(account) //check if nonce was provided as a function argument
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
}

function borrowAave_goerli(privateKey, erc20, amount, lendPool, web3, stableRate = false, nonce) {
    account=web3.eth.account.from_key(privateKey).address
    nonce = (nonce === undefined) ? nonce : web3.eth.getTransactionCount(account)
    if (stableRate === false) {
        stableRate = 2
    }
    else {
        stableRate = 1
    }
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
}

function repayAave_goerli(privateKey, amount, lendPool, web3, erc20_address = undefined, nonce = undefined, stableRate = false) {
    account=web3.eth.account.from_key(privateKey).address
    nonce = (nonce === undefined) ? nonce : web3.eth.getTransactionCount(account)
    if (stableRate === false) {
        stableRate = 2
    }
    else {
        stableRate = 1
    }
    approve_erc20_goerli(account,lendPool,amount,privateKey,web3,nonce)
    lendCon = web3.eth.contract(address=lendPool,abi=lending_pool_abi)
    tx = lendCon.functions.repay(erc20_address, amount, stableRate, account).buildTransaction(
        {
            "chainId": 5,
            "from": account,
            "nonce": nonce + 1,
        }
    )
    signed_txn = web3.eth.account.sign_transaction(
        tx, private_key=privateKey
    )
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return web3.toHex(tx_hash)
}