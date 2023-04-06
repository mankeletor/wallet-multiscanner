from web3 import Web3
from multiprocessing import Pool
import os
import secrets

redes = [
    ('https://bsc-dataseed.binance.org/', 'BNB', '0.0001'),
    ('https://eth.llamarpc.com', 'ETH', '0.001'),
    ('https://polygon.llamarpc.com', 'MATIC', '0.044'),
    ('https://rpcapi.fantom.network', 'FMT', '0.86'),
    ('https://forno.celo.org', 'CELO','0.073'),
    ('https://evm.kava.io', 'KAVA','0.057'),
    ('https://rpc.api.moonriver.moonbeam.network', 'MOVR','0.89'),
    ('https://rpc.api.moonbeam.network', 'GLMR','0.13'),
    ('https://rpc.fuse.io', 'FUSE','0.66'),
    ('https://rpc.gnosischain.com', 'xDAI','0.05'),
    ('https://evm.cronos.org', 'CRO', '0.72')
]

def procesar_red(red):
    n = 1
    url, sym, min = red
    min = float(min)
    web3 = Web3(Web3.HTTPProvider(url))
    while True:
        sender_pk = secrets.token_hex(32)
        sender_addr = web3.eth.account.from_key(sender_pk).address
        balance = web3.eth.get_balance(sender_addr)
        balance = web3.fromWei(balance, 'ether')

        if balance > min:

            print((f"{balance} {sym} {sender_pk} WINNER!!!!"))
            file1 = open("wallets.txt", "a")
            file1.write(f"{balance} {sym} {sender_addr} {sender_pk}\n")
            file1.close()
        else: 
            print(balance,sym,end='\r')
        n += 1

if __name__ == '__main__':
    with Pool(processes=8) as pool:
        pool.map(procesar_red, redes)
