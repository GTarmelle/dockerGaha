def euler_E2():
  limit = 4000000
  result = ""
  sumeven = 2
  swap = 0
  fprev =1
  factu = 2
  while (factu <= limit):
    swap = factu
    factu = fprev + factu
    fprev = swap
    if(factu%2 == 0):
      sumeven += factu
  result += str(sumeven) + "\n" 
  return result
  
print(euler_E2())