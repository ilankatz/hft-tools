var Tx = require('ethereumjs-tx');

const provider = "https://goerli.infura.io/v3/19422f0b6f114fcea2b8b0b8d480728e" //node provider

Web3 = require("web3")
web3 = new Web3(new Web3.providers.HttpProvider(provider)) //instatiate web3 object

address = "0xE4c3ff85A999178B923919954b7fFA7492FA50C7" //public key
private_key = "20581c4277871777beeabe069b2304fe0223d6018200dd50188cbb1a3e3e7f54" 

aaveGoerliDai_address = "0x75Ab5AB1Eef154C0352Fc31D2428Cef80C7F8B33" //goerli chain address for Dai tokens used by Aave

BN = web3.utils.BN //BigNumber library

require("./abis") //import abis from abis.js

mainFunc(web3, address)

async function mainFunc(web3, address) {
    //set up wallet and web3 variables
    web3.eth.handleRevert = true;
    web3.eth.accounts.wallet.add(private_key)
    //get balance as a test
    let balance = await getbalance(address)
    console.log(balance)
    //get the aave pool address which we'll deposit into
    poolAddress = await get_goerli_lending_pool(web3)
    console.log(poolAddress)

    //deposit, borrow, repay, and withdraw crypto using aave
    amt = new BN(10).pow(BN(19))
    transactionNumber = await web3.eth.getTransactionCount(address)
    console.log(deposit_to_aave_goerli(poolAddress, amt, private_key, aaveGoerliDai_address, web3, transactionNumber))
    console.log(borrow_to_aave_goerli(poolAddress, amt, private_key, aaveGoerliDai_address, web3, false, transactionNumber+2))
    console.log(repay_to_aave_goerli(poolAddress, amt, private_key, aaveGoerliDai_address, web3, false, transactionNumber+3))
    console.log(withdraw_to_aave_goerli(poolAddress, amt, private_key, aaveGoerliDai_address, web3, transactionNumber+5))
    return
}

async function getbalance(address) {
    const balance = await web3.eth.getBalance(address)
    return balance
}

async function get_goerli_lending_pool(web3) {
    let lpapaddress = web3.utils.toChecksumAddress("0x5E52dEc931FFb32f609681B8438A51c675cc232d")
    lpap = new web3.eth.Contract(lending_pool_addresses_provider_abi,lpapaddress)
    lendPool = (lpap.methods.getLendingPool().call())
    return lendPool
}

async function approve_erc20_goerli(spender, amount, privateKey, erc20_address, web3, nonce = undefined) {
    signerWallet = web3.eth.accounts.privateKeyToAccount(privateKey)
    account = signerWallet.address
    nonce = (nonce === undefined) ? await web3.eth.getTransactionCount(account) : nonce
    erc20 = new web3.eth.Contract(erc20_abi, erc20_address)
    console.log("approve nonce: " + nonce)
    const tx = {
        from: account,
        to: erc20_address,
        nonce: nonce,
        gas: 10000000,
        data: erc20.methods.approve(spender, amount).encodeABI()
    }
    const signature = await web3.eth.accounts.signTransaction(tx, privateKey)
    
    receipt = web3.eth.sendSignedTransaction(signature.rawTransaction)
    
}

async function deposit_to_aave_goerli(lending_pool, amount, privateKey, tokenAddress, web3, nonce = undefined) {
    signerWallet = web3.eth.accounts.privateKeyToAccount(privateKey)
    account = signerWallet.address
    lendCon = new web3.eth.Contract(lending_pool_abi,lending_pool)
    nonce = (nonce === undefined) ? await web3.eth.getTransactionCount(account) : nonce
    approve_erc20_goerli(lending_pool, amount, privateKey, tokenAddress, web3, nonce++)
    console.log("deposit nonce: " + nonce)
    const tx_obj = {
        from: account,
        to: lending_pool,
        nonce: nonce,
        gas: 10000000,
        data: lendCon.methods.deposit(tokenAddress, amount, account, 0).encodeABI()
    }
    tx = web3.eth.sendTransaction(tx_obj)
    return tx
}

async function withdraw_to_aave_goerli(lending_pool, amount, privateKey, tokenAddress, web3, nonce = undefined) {
    signerWallet = web3.eth.accounts.privateKeyToAccount(privateKey)
    account = signerWallet.address
    nonce = (nonce === undefined) ? await web3.eth.getTransactionCount(account) : nonce //check if nonce was provided as a function argument
    lendCon = new web3.eth.Contract(lending_pool_abi,lending_pool)
    console.log("withdraw nonce: " + nonce)
    const tx_obj = {
        from: account,
        to: lending_pool,
        nonce: nonce,
        gas: 10000000,
        data: lendCon.methods.withdraw(tokenAddress, amount, account).encodeABI()
    }
    tx = web3.eth.sendTransaction(tx_obj)
    return tx
}

async function borrow_to_aave_goerli(lending_pool, amount, privateKey, tokenAddress, web3, stableRate = false, nonce = undefined) {
    signerWallet = web3.eth.accounts.privateKeyToAccount(privateKey)
    account = signerWallet.address
    nonce = (nonce === undefined) ? await web3.eth.getTransactionCount(account) : nonce
    console.log("borrow nonce: " + nonce)
    if (stableRate === false) {
        stableRate = 2
    }
    else {
        stableRate = 1
    }
    lendCon = new web3.eth.Contract(lending_pool_abi,lending_pool)
    const tx_obj = {
        from: account,
        to: lending_pool,
        nonce: nonce,
        gas: 10000000,
        data: lendCon.methods.borrow(tokenAddress, amount, stableRate, 0, account).encodeABI()
    }
    tx = web3.eth.sendTransaction(tx_obj)
    return tx
}

async function repay_to_aave_goerli(lending_pool, amount, privateKey, tokenAddress, web3, stableRate = false, nonce = undefined) {
    signerWallet = web3.eth.accounts.privateKeyToAccount(privateKey)
    account = signerWallet.address
    lendCon = new web3.eth.Contract(lending_pool_abi,lending_pool)
    nonce = (nonce === undefined) ? await web3.eth.getTransactionCount(account) : nonce
    if (stableRate === false) {
        stableRate = 2
    }
    else {
        stableRate = 1
    }
    approve_erc20_goerli(lending_pool,amount,privateKey,tokenAddress,web3,nonce++)
    console.log("repay nonce: " + nonce)
    lendCon = new web3.eth.Contract(lending_pool_abi, lending_pool)
    const tx_obj = {
        from: account,
        to: lending_pool,
        nonce: nonce,
        gas: 10000000,
        data: lendCon.methods.repay(tokenAddress, amount, stableRate, account).encodeABI()
    }
    tx = web3.eth.sendTransaction(tx_obj)
    return tx
}