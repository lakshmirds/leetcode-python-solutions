class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for i in strs:
            while i[:len(prefix)] != prefix:
                prefix = prefix[:-1]

                if prefix == "":
                    return ""
        return prefix

        