#User function Template for python3
def GCD(a,b):
    if a==0:
        return b
    return GCD(b%a,a)
def LCM(a,b):
    return (a*b)//GCD(a,b)
def getSmallestDivNum(n):
    #RETURN ans
    if n==1:
        return 1
    a=2
    for i in range(3,n+1):
        if a<i:
            val=LCM(a,i)
        else:
            val=LCM(i,a)
        a=val
    return a

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        print(getSmallestDivNum(n))
# } Driver Code Ends