import math

def factor(n):
  if ( n == 0):
    return None
  elif(n==1):
      return 1
  else:
      theFactors = []
      for i in range(2,n+1):
          while n % i == 0:
              n = n/i
              theFactors.append(i)
      return theFactors


if __name__ == '__main__':
    print(factor(144))