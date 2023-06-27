# Sequence_Of_Squares
Considerando uma sequência de números a0, a1, ...aN, em que um elemento é igual à soma dos dígitos quadrados do elemento anterior. A sequência termina quando um elemento que já estava na sequência aparece novamente.  Dado o primeiro elemento, encontre o comprimento da sequência.a0

**Exemplo**:
 
Para a0 = 16, a saída deve ser 9

Veja como os elementos da sequência são construídos:

a0 = 16

a1 = 1^2 + 6^2 = 37

a2 = 3^2 + 7^2 = 58

a3 = 5^2 + 8^2 = 89

a4 = 8^2 + 9^2 = 145

a5 = 1^2 + 4^2 + 5^2 = 42

a6 = 4^2 + 2^2 = 20

a7 = 2^2 + 0^2 = 4

a8 = 4^2 = 16, o que já ocorreu antes (a0)

Assim, são 9 elementos na sequência.

Para a0 = 103, a saída deve ser 4

A sequência é a seguinte: 103 -> 10 -> 1 -> 1, 4 elementos ao todo.

**Entrada/Saída**:

[input] inteiro a0

Primeiro elemento de uma sequência, inteiro positivo.

Restrições: 1 ≤ a0 ≤ 650.

[output] um inteiro
