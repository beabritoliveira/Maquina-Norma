#Caso 1) A := A * B usando C , D, onde o registrador A armazena o produto, B tem seu valor restaurado, C e D ficam zerados.
from operacoesBasicas import add, sub, zer


def multABcomCD(A,B):
  C = 0;
  D = 0;
  if(zer(B) or zer(A)):
    A = 0
  else:
    while(not zer(A)):
      A = sub(A);
      C = add(C)
    while(not zer(B)):
      B = sub(B);
      D = add(D);
    while(not zer(C)):
      while(not zer(D)):
        D = sub(D);
        A = add(A);
        B = add(B);
      C = sub(C);
      while(not zer(B) and not zer(C)):
        B = sub(B);
        D = add(D);
  return A, B, C, D
