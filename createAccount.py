from eth_account import Account
import secrets

priv = secrets.token_hex(32)
print ("SAVE BUT DO NOT SHARE THIS:", priv)
acct = Account.from_key("0x" + priv)
print("Address:", acct.address)
