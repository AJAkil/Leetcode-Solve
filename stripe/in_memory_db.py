def subscription_db(commands):
    sub = {}
    result = []
    
    
    for sub_commands in commands:
        sub_commands_list = sub_commands.split(",")
        time_stamp = int(sub_commands_list[0])
        operation = sub_commands_list[1]
        user = sub_commands_list[2]

        if operation == 'start':

            duration = int(sub_commands_list[3]) if len(sub_commands) > 3 else float('inf')
           
            if user not in sub:
                sub[user] = (time_stamp, time_stamp + duration)
            else:
                curr_start, curr_end = sub[user]

                if curr_end is not float('inf'):
                    new_end = max(curr_end, time_stamp) + duration 
                    sub[user] = (curr_start, new_end)
            
            
            result.append("")
            
        elif operation == 'end':
            if user in sub:
                start, _ = sub[user]
                sub[user] = (start, time_stamp) # store the start and end time 
            result.append("")
        elif operation == 'check':
            if user not in sub:
                result.append('inactive')
            else:
                start, end = sub[user]
                

                if start <= time_stamp <= end:
                    result.append('active')
                else:
                    result.append('inactive')
    print(sub)
    
    return result 


ops = ["1,start,Michael,10", "2,start,Michael,4", "5,check,Michael", "16,check,Michael"]
print(subscription_db(ops))
# Output: ["", "", "active", "inactive"]


