# desafio-pytest

| #  | Nível  | Desafio                                                                        | Feito |
| -- | ------- | ------------------------------------------------------------------------------ | ----- |
| 11 | Júnior | Calcular o fatorial de um número                                              | X     |
| 11 | Júnior | Implementar e testar um cálculo de média aritmética                         | X     |
| 12 | Júnior | Verificar se um número é primo                                               |       |
| 13 | Júnior | Implementar um conversor de temperatura (Celsius para Fahrenheit e vice-versa) |       |
| 14 | Júnior | Implementar uma calculadora básica (+, -, *, /)                               |       |
| 15 | Júnior | Testar a conversão de números romanos para inteiros                          |       |
| 16 | Júnior | Determinar se uma palavra é um palíndromo                                    |       |
| 17 | Júnior | Criar e testar um gerador de senhas aleatórias                                |       |
| 18 | Júnior | Implementar um contador de vogais em uma string                                |       |
| 19 | Júnior | Testar a remoção de elementos duplicados em uma lista                        |       |
| 20 | Júnior | Implementar e testar um algoritmo de ordenação (Bubble Sort)                 |       |

uv add pytest-cov

uv run pytest --cov=src tests/

uv run pytest --cov-report html --cov=src tests/
