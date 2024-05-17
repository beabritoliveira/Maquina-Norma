from multiplicacao import multABcomCD
from operacoesBasicas import add, zer, sub

def fatorial(A):
  B, C, D = 0,0,0
  if(zer(A)): 
    return
  while(not zer(A)):
    B = add(B)
    C = add(C)
    A = sub(A)
  C = sub(C)
  if(not zer(C)):
    D = multABcomCD(B,C) 
    D = D[0]
    while(not zer(C)):
     # print(C)
      C = sub(C) 
      if(not zer(C)):
        D = multABcomCD(D, C)
        D = D[0]
  else:
    D = add(D)
  return D

