from web3 import Web3
from dotenv import load_dotenv
import os
from keySign import encrypt, sign, updateenv
load_dotenv()

def send(fromKeys, toAddress, amount, incGas = False):
    sw=web3.eth.account.from_key(fromKeys)
    fromAddress=sw.address
    nonce = web3.eth.getTransactionCount(fromAddress)
    estimate = web3.eth.estimateGas({'to': toAddress, 'from': fromAddress, 'value': amount})
    if incGas == True:
        amount -= (web3.eth.estimateGas({'to': toAddress, 'from': fromAddress, 'value': amount}))*web3.eth.gas_price
    tx = {
        'nonce': nonce,
        'to': toAddress,
        'value': amount,
        'gas': estimate,
        'gasPrice': web3.eth.gas_price
    }
    signed_tx = web3.eth.account.sign_transaction(tx, fromKeys)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return(web3.toHex(tx_hash))

def encSend(slices, toAddress, amount, envvars, incGas = False):
    key = sign(slices)
    sw=web3.eth.account.from_key(key)
    fromAddress=sw.address
    slices = encrypt(key)
    updateenv(slices,envvars)
    ret = send(key, toAddress, amount, incGas)
    return ret

def senderc20(fromKey, address, toAddress, amount, chainid):
    sw=web3.eth.account.from_key(fromKey)
    fromAddress=sw.address
    abi = [
        {
        "constant": False,
        "inputs": [
            {"name": "to", "type": "address"},
            {"name": "value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "success", "type": "bool"}],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function",
        }
    ]
    contract = web3.eth.contract(address=address,abi=abi)
    tx = contract.functions.transfer(
        toAddress,
        amount,
    ).buildTransaction({
        'chainId': chainid,
        'gas': 70000,
        'gasPrice': web3.toWei('1', 'gwei'),
        'nonce': web3.eth.getTransactionCount(fromAddress),
    })
    signed_tx = web3.eth.account.signTransaction(tx, private_key=fromKey)
    hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return(web3.toHex(hash))

def safeSendErc20(slices, tokenAddress, toAddress,amount,chainid, envvars):
    key = sign(slices)
    ss = encrypt(key)
    updateenv(ss,envvars)
    ret = senderc20(key,tokenAddress,toAddress,amount,chainid)
    return ret
