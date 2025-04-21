def BIN_gap_filler(BIN, intervals):
    START = 0
    END = 9999999999
    res = []
    
    for i, interval in enumerate(intervals):
        s, e,  brand = interval.split(",")
        s = int(s)
        e = int(e)
        
        mod_s = s
        mod_e = e

        if i == 0:
            # the start
            if s  > START:
                mod_s = START
        
        if i + 1 < len(intervals):
            # check with the next one
            next_s, _, _  = intervals[i+1].split(',')
            next_s = int(next_s)

            if e + 1 < next_s:
                mod_e = next_s - 1

        elif i+1 == len(intervals):
            # at the end 

            if e < END:
                mod_e = END
        
        res.append([mod_s, mod_e, brand])

    # sort the results based on first value
    

    return res

def BIN_gap_filler_1(BIN, intervals):
    
    START = 0
    END = 9999999999
    parsed = []

    for i, interval in enumerate(intervals):
        data = interval.split(',')
        s = data[0]
        e = data[1]
        brand = data[2]

        s = int(s)
        e = int(e)

        parsed.append((s,e,brand))

    parsed.sort(key=lambda x: x[0])

    parsed[0] = (0, parsed[0][1], parsed[0][2])
    parsed[-1] = (parsed[-1][0], 9999999999, parsed[-1][2])

    for s,e, brand in parsed:
        full_s = BIN + str(s).zfill(10)
        full_e = BIN + str(e).zfill(10)
        print(f"{full_s},{full_e},{brand}")

def BIN_gap_filler_2(BIN, intervals):
    START = 0
    END = 9999999999
    res = []
    
    intervals.sort(key=lambda x: int(x.split(',')[0]))

    for i, interval in enumerate(intervals):
        s,e,brand = interval.split(',')
        s = int(s)
        e = int(e)

        mod_s = s 
        mod_e = e 

        if i == 0 and s > START:
            mod_s = START 
        
        if i + 1 < len(intervals):
            next_s = int(intervals[i+1].split(',')[0])
            if e + 1 < next_s:
                mod_e = next_s - 1 
        elif i + 1 == len(intervals):
            if e < END:
                mod_e = END 
        
        res.append([mod_s, mod_e, brand])
    
    return res

def BIN_gap_filler_3(BIN, intervals):
    START = 0
    END = 9999999999
    res = []

    intervals.sort(key=lambda x: int(x.split(',')[0]))

    # now to find the covering intervals
    first_cover = intervals[0].split(',')
    covers = [f"{first_cover[0]},{first_cover[1]},{first_cover[2]}"]
    print(covers)
    for i, interval in enumerate(intervals[1:]):
        s,e,brand = interval.split(',')
        s = int(s)
        e = int(e)
        
        prev_s, prev_e, _ = covers[-1].split(',')
        prev_s = int(prev_s)
        prev_e = int(prev_e)
        
        # now check
        if s > prev_s and e > prev_e:
            # found a new cover
            
            covers.append(f"{s},{e},{brand}")
            print(covers)
    
    print(covers)
    # covers contain the covering interavl. now we do the same logic again
    res = BIN_gap_filler_2(BIN,covers)

    for s,e,brand in res:
        fill_s = BIN + str(s).zfill(10)
        fill_e = BIN + str(e).zfill(10)
        print(f"{fill_s},{fill_e},{brand}")


def BIN_gap_filler_4(BIN, intervals):
    intervals_extended = BIN_gap_filler_2(BIN, intervals)
    print('intervals extended: ')
    print(intervals_extended)
    res = [intervals_extended[0]]

    for i, (s, e, brand) in enumerate(intervals_extended[1:]):
        

        s = int(s)
        e = int(e)

        last_s, last_e, last_brand = res[-1]

        last_s = int(last_s)
        last_e = int(last_e)

        if last_e + 1 == s and last_brand == brand:
            res[-1] = ([last_s, e, last_brand])
        else:
            res.append([s,e,brand])
    
    # print the results
    for s,e,brand in res:
        full_s = BIN + str(s).zfill(10)
        full_e = BIN + str(e).zfill(10)

        print(f"{full_s},{full_e},{brand}")


if __name__ == "__main__": 
    BIN = input()
    N = int(input())
    intervals = []

    for i in range(N):
        s,e,brand = input().split(',')
        intervals.append(f"{s},{e},{brand}")
    
    # res = BIN_gap_filler(BIN, intervals)
    # final_res = []

    # for s,e,brand in res:
    #     full_s = str(BIN) + str(s).zfill(10)
    #     full_e = str(BIN) + str(e).zfill(10)
    #     final_res.append([full_s, full_e,brand])

    # final_res.sort(key=lambda x: int(x[0]))

    # for s,e,brand in final_res:
    #     print(f"{s},{e},{brand}")
    print(intervals)
    BIN_gap_filler_4(BIN, intervals)

    

