class Solution:
    def countAndSay(self, n: int) -> str:
        num = []
        num.append("")
        num.append("1")

        if n==1:
            return num[1]

        for i in range(2,n+1):
            p = []
            s = ""

            for x in num[i-1]:
                if p==[] or x==p[0]:
                    p.append(x)
                else:
                    s += str(len(p))
                    s += p[0]
                    p = []
                    p.append(x)

            s += str(len(p))
            s += p[0]

            num.append(s)

        return num[n]
