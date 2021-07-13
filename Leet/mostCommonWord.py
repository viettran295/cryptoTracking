'''
Input: paragraph = "Bob hit a ball, 
the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), 
so it is the most frequent non-banned word in the paragraph. 
Counter()
.most_common() return Tuple (immutable in nature)
isalpha()
'''
from typing import Counter, List


def Solve(paragraph: str, banned: List[str])->List[str]:
    ans = ""
    for i in paragraph.lower():
        if i.isalpha():
            ans+=i;
        else:
            ans+=" "
    ans = ans.split(' ')
    ans = Counter(ans)
    for i in ans.most_common():
        # i[0] != " " and i[0] not in banned
        if i[0] and i[0] not in banned:
            return i[0]
if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit", "ball"]
    