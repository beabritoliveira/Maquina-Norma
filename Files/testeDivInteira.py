#Teste se o valor da divisão inteira é zero 
#Teste_mod(A, B) usando C, D, E, C’, D’, E’ 
from multiplicacao import multABcomCD
from operacoesBasicas import add, sub, zer
from testeMenor import testeMenor

def divisao(A,B):
  C,D,E,F,G,H = 0,0,0, 0, 0,0
  if(zer(B) or zer(A)):
    A = 0
  else:
    while(not zer(A)):
      A = sub(A)
      C = add(C)
      G = add(G)
    while(not zer(B)):
      B = sub(B)
      D = add(D)
      H = add(H)
      
    while(not zer(C)):
      while(not zer(D)):
        C = sub(C)
        D = sub(D)
        E = add(E)
        if(zer(C) and not zer(D)):
          if(not testeMenor(G, H)): 
            #resto = G - H
            while(not zer(H)):
              G = sub(G)
              H = sub(H)
          # else resto = G
          break
        elif(zer(D)):  # B > A ou B == A
          if(zer(C)):
            while(not zer(G)): # B == A => resto = 0
                G = sub(G)
          else: # B > A
            # resto = B - multiplicação(F, H)
            A = multABcomCD(F, H)[0]
            while(not zer(A)):
              G = sub(G)
              A = sub(A)
              #G = G - A
          F = add(F)
      while(not zer(E)):
        E = sub(E)
        D = add(D)
  return D, F, G
# D => divisor
# F => quoeficiente
# G => resto

def Teste_mod(A,B):
  div = divisao(A, B)
  resto = div[2]
  if(zer(resto)): # resto == 0
    return True
  return False
