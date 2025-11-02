def reverseBits(n):
        result =0
        for i in range(32):
            result<<=1
            a=n&1
            result= result| a
            n>>=1
        return result
print(reverseBits(456))