import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        convert = s.maketrans('', '', string.punctuation + " ")
        no_punc = s.translate(convert).lower()
        reversed_s = no_punc[::-1]
        return no_punc == reversed_s