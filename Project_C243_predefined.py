from web3 import Web3
from web3.middleware import geth_poa_middleware
url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

Latest_Block = web3.eth.get_block('latest')
print("Latest Block of ethereum blockchain:", Latest_Block)

block_transaction_count=web3.eth.get_block_transaction_count(17885055)
print('Number of transactions happened in the block:', block_transaction_count)

Block_count=134
Newest_block='latest'
Reward_percentiles=None
Transaction_fee=web3.eth.fee_history(Block_count,Newest_block,Reward_percentiles)
print('Number of transactions happened in the block:', Transaction_fee)