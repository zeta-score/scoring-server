from flask import Flask
import json 
import requests 
from collections import deque 

app = Flask(__name__)

with open('./api_key.json', mode='r') as key_file:
	api_key = json.loads(key_file.read())['key']

# Etherscan will reject bots with 403 error, must spoof user-agent
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

"""takes in an known malicious account address and updates scores from there"""
@app.route('/update/<mal_acct_address>')
def update(mal_acct_address: 'str', root_zeta: float=1.0):
	# gather all the required information
	## current Zeta score of sender node
	## current Zeta score of current node (if it's not in db, set it to initialized value of .5, which is neutral and at decision boundary)
	## how many hops from the malicious node
	## the value of the transaction recieved from the malicious node
	# BFS the graph
	## calculate zeta score and update to db as you go
	## stopping criterion: upper limit on hops or stop when you've gotten to edge of graph
	queue = deque()
	visited = set()
	queue.append(mal_acct_address)
	# TODO: push root_zeta score to Firebase
	while 0 < len(queue):
		node = queue.popleft() 
		if node not in visited:
			visited.add(node)
			# find all neighbors (incoming and outgoing transactions)
			tx_addrs = {'in':[], 'out':[]}
			for trans in data.get('result'):
				# check if it's an incoming transaction
			    if mal_acct_address is not trans.get('from'):
			        tx_addrs['in'].append(trans.get('from'))
			    else: # it must be an outgoing transaction
			        tx_addrs['out'].append(trans.get('to'))
	        	# TODO: query firebase for zeta score of non-current node 
	        	## if it's not in db, update the zeta score in db to be 0 (so sigmoid products .5) and use that
	        	
			queue.append(node)
		pass
	pass

def fetch_txs(acct_address):
	print(f'fetching from Etherscan for account={acct_address}')
	headers = {'User-Agent' : user_agent}
	norm_txs_url = f"http://api-ropsten.etherscan.io/api?module=account&action=txlist&address={acct_address}&sort=asc&apikey={api_key}"
	try:
		res = requests.get(norm_txs_url, headers=headers)
	except requests.exceptions.ConnectionError:
		raise ConnectionRefusedError
	if res.status_code == 200:
		data = res.json()
		if '1' == data.get('status'):
			return data
	raise Exception(f"Problem with connection, status code: {res.status_code}")

@app.route('/hello')
def hello():
	return 'Hello world!'
 
if __name__ == '__main__':
	app.run() 