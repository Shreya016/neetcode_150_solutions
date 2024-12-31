class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for words in strs:
            sorted_words=''.join(sorted(words))
            if sorted_words not in result:
                result[sorted_words]=[]
            result[sorted_words].append(words)
        return list(result.values())

        
        