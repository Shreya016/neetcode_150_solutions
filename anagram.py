class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted=''.join(sorted(s))
        t_sorted=''.join(sorted(t))
        if s_sorted.lower() == t_sorted.lower():
            return True
        else:
            return False