digit_to_letter = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def dfs(start_index, path, res, digits):

    # end condition
    if start_index == len(digits):
        res.append("".join(path))
        return 


    # get leaf condition
    number = digits[start_index]

    for letter in digit_to_letter[number]:
        path.append(letter)
        dfs(start_index+1, path, res, digits)
        path.pop()

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []

        if digits:
            dfs(0, path, res, digits)
        return res
        