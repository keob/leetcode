class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        div1, div2, re = abs(dividend), abs(divisor), 0

        while div1 >= div2:
            i = k = 0
            while k <= div1:
                m = k
                k = k+k or div2
                if k <= div1:
                    i = i+i or 1
            re += i
            div1 -= m    
        re = -re if dividend>0 and divisor<0 or dividend<0 and divisor>0 else re
        if re<-2**31:
            return -2**31
        if re > 2**31-1:
            return 2**31-1
        return re
