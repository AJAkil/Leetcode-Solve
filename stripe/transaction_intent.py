merchant_db = {}
transaction_db  = {}

def start(mer_id, balance, refund_limit=None):
    merchant_db[mer_id] = {'balance': balance, 'mer_id': mer_id, 'refund_limit': refund_limit}

def new(txn_id, mer_id, amount):
    transaction_db[txn_id] = {
        'mer_id': mer_id,
        'amount': amount,
        'state': 'PENDING'
    }

def process(txn_id):
    if transaction_db[txn_id]['state'] == 'PENDING':
        transaction_db[txn_id]['state'] = 'IN_PROGRESS'

def complete(txn_id):
    txn = transaction_db[txn_id]
    if txn['state'] == 'IN_PROGRESS':
        txn['state'] = "DONE"
        merchant_db[txn['mer_id']]['balance']+= txn['amount']
        print(f"{txn['mer_id']} {merchant_db[txn['mer_id']]['balance']}")

def modify(txn_id, amount):
    txn = transaction_db['txn_id']

    if txn['state'] == 'PENDING':
        txn['amount'] = amount

def cancel(txn_id):
    txn = transaction_db[txn_id]

    if txn['state'] == 'IN_PROGRESS':
        txn['state'] = 'PENDING'

def return_(txn_id, timestamp=None):
    txn = transaction_db[txn_id]

    if txn['state'] == 'DONE':

        merchant = merchant_db[txn['mer_id']]
        refund_time_limit = merchant['refund_limit']

        if refund_time_limit == 0:
            pass 
        elif refund_time_limit == None or (timestamp <= refund_time_limit):
            merchant['balance'] -= txn['amount']
    
    print(f"{txn['mer_id']} {merchant_db[txn['mer_id']]['balance']}")

def run_commands(commands):
    for command in commands:
        parts = command.split(' ')
        
        if parts[0] == 'START':
            start(parts[1], float(parts[2]))
        elif parts[0] == 'NEW':
            new(parts[1], parts[2], float(parts[3]))
        elif parts[0] == 'PROCESS':
            process(parts[1])
        elif parts[0] == 'COMPLETE':
            complete(parts[1])
        elif parts[0] == 'MODIFY':
            modify(parts[1], float(parts[2]))
        elif parts[0] == 'CANCEL':
            cancel(parts[1])
        elif parts[0] == 'RETURN':
            return_(parts[1])
        else:
            # this means the commands have a time stamp at the start
            timestamp = int(parts[0])

            if parts[1] == 'START':
                start(parts[2], float(parts[3]), int(parts[4]))
            elif parts[1] == 'NEW':
                new(parts[2], parts[3], float(parts[4]))
            elif parts[1] == 'PROCESS':
                process(parts[2])
            elif parts[1] == 'COMPLETE':
                complete(parts[2])
            elif parts[1] == 'MODIFY':
                modify(parts[2], float(parts[3]))
            elif parts[1] == 'CANCEL':
                cancel(parts[2])
            elif parts[1] == 'RETURN':
                return_(parts[2], timestamp)

        
if __name__ == '__main__':
    commands = []
    command = input()

    while command != 'END':
        commands.append(command)
        command = input()
        #print(commands)
    
    run_commands(commands)

