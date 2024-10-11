class Solution:
    """
    This class provides a solution to the LeetCode problem #347: Top K Frequent Elements.
    The `topKFrequent` method finds the `k` most frequent elements in a list of integers.
    Method:
        topKFrequent(nums: List[int], k: int) -> List[int]:
            Args:
                nums (List[int]): A list of integers.
                k (int): The number of top frequent elements to return.
            Returns:
                List[int]: A list of the `k` most frequent elements.
            Logic:
                1. Initialize an empty dictionary `counter_dict` to count the frequency of each element in `nums`.
                2. Iterate through `nums` and populate `counter_dict` with the frequency of each element.
                3. Determine the maximum frequency (`freq_upper_bound`) from the values in `counter_dict`.
                4. Create a list of lists `frequency_to_list` where the index represents the frequency and the value is a list of elements with that frequency.
                5. Populate `frequency_to_list` by iterating through `counter_dict` and appending elements to the corresponding frequency index.
                6. Initialize an empty list `result` to store the top `k` frequent elements.
                7. Iterate through `frequency_to_list` in reverse order (from highest frequency to lowest) and extend `result` with elements from `frequency_to_list` until `result` contains `k` elements.
                8. Return the `result` list containing the `k` most frequent elements.
    """
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

        

        