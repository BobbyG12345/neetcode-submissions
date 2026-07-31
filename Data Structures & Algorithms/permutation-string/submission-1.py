class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # 1️⃣ 构建 s1 计数字典
        s1_dict = {}
        for c in s1:
            s1_dict[c] = s1_dict.get(c, 0) + 1

        # 2️⃣ 枚举每个窗口起点
        for i in range(len(s2) - len(s1) + 1):
            # ⚠️ 每个窗口都要一份“新的拷贝”
            temp = s1_dict.copy()
            valid = True

            # 3️⃣ 检查长度为 len(s1) 的窗口
            for j in range(i, i + len(s1)):
                if s2[j] in temp and temp[s2[j]] > 0:
                    temp[s2[j]] -= 1
                else:
                    valid = False
                    break

            if valid:
                return True

        return False
