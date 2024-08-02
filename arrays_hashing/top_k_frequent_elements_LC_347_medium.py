class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {} 

        for num in nums:
            counter_dict[num] = 1 + counter_dict.get(num, 0)
        
        freq_upper_bound = max(set(counter_dict.values()))

        frequency_to_list = [[] for _ in range(freq_upper_bound + 1)]

        for num, freq in counter_dict.items():
            frequency_to_list[freq].append(num)
        
        result = []
        for i in range(len(frequency_to_list) - 1 , 0, -1):
            if frequency_to_list[i] is not []:
                result.extend(frequency_to_list[i])

            if len(result) == k:
                break
        
        return result

        

        