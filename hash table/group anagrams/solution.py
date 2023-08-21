from typing import List


class GroupAnagrams:
    def get_hash(self, word: str) -> str:
        # Use this function to create has for word size greater than 1000
        hsh = [0] * 26
        for ltr in word:
            hsh[ord(ltr) - 97] += 1
        hsh = [str(i) for i in hsh]
        return "|".join(hsh)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = [["".join(sorted(word)), word] for word in strs]
        ans = dict()
        for item in strs:
            hsh, word = item
            if hsh in ans:
                ans[hsh] = ans[hsh] + [word]
            else:
                ans[hsh] = [word]
        return list(ans.values())
