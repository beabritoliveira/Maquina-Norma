#Teste se o valor de um registrador é menor que outro registrador 
#A < B usando C, D, E 

from operacoesBasicas import add, sub, zer


def testeMenor(A, B):
  C, D, E = 0, 0, 0
  if(zer(B)):
    #Entra se A = B ou A > B   
    return False
  while(not zer(A)):
    A = sub(A)
    C = add(C)
  while(not zer(B)):
    B = sub(B)
    D = add(D)
  while(not zer(C)):
    C = sub(C)
    D = sub(D)
    if(zer(D)):
      return False
  return True
