class PaymentProcessing:

    def __init__(self):
        self.merchant_tracker = {}
        self.payment_intent_tracker = {}
        self.payment_states = ['REQUIRES_ACTION', 'PROCESSING', 'COMPLETED']
    

    def init_payment(self, merchant_id, starting_balance):
        if not merchant_id in self.merchant_tracker:
            self.merchant_tracker[merchant_id] = starting_balance
    
    def create_payment_intent(self, payment_intent_id, merchant_id, amount):
        if (not payment_intent_id in self.payment_intent_tracker) and (merchant_id in self.merchant_tracker) and (amount > 0):
            self.payment_intent_tracker[payment_intent_id] = [merchant_id, amount, self.payment_states[0], False]
        
    def attempt_payment(self, payment_intent_id):
        if (payment_intent_id in self.payment_intent_tracker) and (self.payment_intent_tracker[payment_intent_id][2] == self.payment_states[0]):
            self.payment_intent_tracker[payment_intent_id][-1] = self.payment_states[1]
    
    def change_to_succeed_state(self, payment_intent_id):
        if (payment_intent_id in self.payment_intent_tracker) and (self.payment_intent_tracker[payment_intent_id][2] == self.payment_states[1]):
            self.payment_intent_tracker[payment_intent_id][2] = self.payment_states[2]
            self.merchant_tracker[self.payment_intent_tracker[payment_intent_id][0]] += 50
    
    def update_temp_payment_intent(self, payment_intent_id, new_amount):
        if (payment_intent_id in self.payment_intent_tracker) and (self.payment_intent_tracker[payment_intent_id][2] == self.payment_status[0]) and (new_amount > 0):
            self.payment_intent_tracker[payment_intent_id][1] = new_amount
    
    def failed_payment(self, pay_int_id):
        if(pay_int_id in self.payment_intent_tracker) and (self.payment_intent_tracker[pay_int_id][2] == self.payment_status[1]):
            self.payment_intent_tracker[pay_int_id][2] = self.payment_status[1]
    
    def refund(self, pay_int_id):
        if(pay_int_id in self.payment_intent_tracker) and (self.payment_intent_tracker[pay_int_id][2] == self.payment_status[-1]) and (self.payment_intent_tracker[pay_int_id][-1] == False):
            self.payment_intent_tracker[pay_int_id][-1] = True # refunded
            self.merchant_tracker[self.payment_intent_tracker[pay_int_id][0]] -= self.payment_intent_tracker[pay_int_id][1]
    



if __name__ == "__main__":
    payment_input = ''
    command = ''
    paymentProcessor = PaymentProcessing()

    while(payment_input != 'END'):
        
        payment_input = str(input())

        if payment_input.startswith("INIT"):
            command = payment_input.split(" ")

            merchant_id = command[1]
            init_balance = float(command[2])

            paymentProcessor.init_payment(merchant_id, init_balance)
        elif payment_input.startswith("CREATE"):
            command = payment_input.split(" ")

            payment_id = command[1]
            merchant_id = command[2]
            balance = float(command[3])

            paymentProcessor.create_payment_intent(payment_id, merchant_id, balance)
        elif payment_input.startswith("ATTEMPT"):
            command = payment_input.split(" ")

            paymentProcessor.attempt_payment(command[1])
        elif payment_input.startswith("SUCCEED"):
            command = payment_input.split(" ")

            paymentProcessor.change_to_succeed_state(command[1])
    
    print(paymentProcessor.merchant_tracker['m1'])
    print(paymentProcessor.merchant_tracker['m2'])
                
    