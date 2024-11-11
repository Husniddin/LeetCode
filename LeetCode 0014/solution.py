class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if len(strs) == 1:
            if strs[0] == '':
                return ''
            else:
                return strs[0]

        str0 = strs[0]
        str1 = strs[1]
        if str0=='' or str1=='':
            return ''

        common_prefix = ''
        i, j = 0, 0
        while i < len(str0) and j < len(str1):
            if str0[i] != str1[j]:
                break

            common_prefix += str0[i]
            i += 1
            j += 1

        if len(strs) == 2 or common_prefix == '':
            return common_prefix



        for i in range(2, len(strs)):
            if strs[i] == '' or strs[i][0] != common_prefix[0]:
                return ''
            if len(strs[i]) == 1:
                if strs[i][0] == common_prefix[0]:
                    common_prefix = common_prefix[0]
                else:
                    return ''
            
            if len(strs[i]) >= len(common_prefix):
                if strs[i][:len(common_prefix)] == common_prefix:
                    continue

                for j in reversed(range(1, len(common_prefix))):
                    if strs[i][j] != common_prefix[j]:
                        common_prefix = common_prefix[:j]

                continue

            if len(strs[i]) < len(common_prefix):
                if common_prefix[:len(strs[i])] == strs[i]:
                    continue
                
                for j in reversed(range(1, len(strs[i]))):
                    if strs[i][j] != common_prefix[j]:
                        common_prefix = common_prefix[:j]

        return common_prefix
        
        

# Test Cases

s = Solution()
print(s.longestCommonPrefix(["flower","flow", "floura", "flight", "abcflowabc"]))
print(s.longestCommonPrefix(["car", "cir"]))