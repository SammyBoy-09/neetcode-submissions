class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return ss == ss[::-1]