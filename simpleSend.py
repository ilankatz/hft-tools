from web3 import Web3

provider = ''
web3 = Web3(Web3.HTTPProvider(provider))
account_1 = ''
private_key1 = ''
account_2 = ''
private_key2 = ''

#balance here is formatted in ether, 
balance = web3.eth.getBalance(account_1)
print(balance)

#get the nonce.  Prevents one from sending the transaction twice
nonce = web3.eth.getTransactionCount(account_1)
gas = 2000000
gasprice = web3.toWei('10', 'gwei')

#build a transaction in a dictionary
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': balance - gas*gasprice,
    'gas': gas,
    'gasPrice': gasprice
}

#sign the transaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key1)

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction hash
print(web3.toHex(tx_hash))
