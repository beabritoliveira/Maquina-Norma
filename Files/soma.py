#Caso 2) A := A + B usando C, onde o registrador C armazena a soma, A e B ficam zerados.
from operacoesBasicas import add, sub, zer


def somaABcomC(A,B):
  C = 0;
  while(not zer(A)):
    C = add(C);
    A = sub(A);
  while(not zer(B)):
    C = add(C);
    B = sub(B);
  return C;

print(somaABcomC(3,2))
