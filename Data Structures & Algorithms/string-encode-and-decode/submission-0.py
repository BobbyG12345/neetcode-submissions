class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f'{len(s)}#{s}'
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 找到 '#' 的位置
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])             # 取数字长度
            res.append(s[j+1:j+1+length])    # 取字符串
            i = j + 1 + length               # 移动到下一个字符串起点
        return res
