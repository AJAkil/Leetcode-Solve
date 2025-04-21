if __name__ == '__main__':
    N = int(input())
    input_data = []
    parsed_data = []
    
    for i in range(N):
        input_data.append(input())
    
    for input_ in input_data:
        timestamp, u_id, amount, card_number, merchant = input_.split(',')

        parsed_data.append(
            {
                'timestamp': int(timestamp),
                'u_id': u_id,
                'amount': float(amount),
                'card_number': card_number,
                'merchant': merchant
            }
        )
    
    # sort the parsed data
    parsed_data.sort(key = lambda x: x['timestamp'])

    for data in parsed_data:
        timestamp = data['timestamp']
        u_id = data['u_id']
        amount = data['amount']
        outcome = 'APPROVE'

        print(f"{timestamp} {u_id} {amount} {outcome}")


