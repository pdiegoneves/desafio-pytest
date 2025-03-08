| # | Nível      | Desafio                                                | Arquivos                                      | Feito |
| - | ----------- | ------------------------------------------------------ | --------------------------------------------- | ----- |
| 1 | Estagiário | Verificar se uma string está vazia                    | ola.py / test_ola.py                         | X     |
| 2 | Estagiário | Testar se um número é par ou ímpar                  | par_impar.py / test_par_impar.py             | X     |
| 3 | Estagiário | Verificar se um número é positivo, negativo ou zero  | verificar_num.py / test_verificar_num.py     | X     |
| 4 | Estagiário | Verificar se uma lista contém um determinado elemento | test_verificar_lista.py / verifcar_lista.py  | X     |
| 5 | Estagiário | Contar a ocorrência de uma letra em uma string        | contar_letras.py / test_contar_letras.py     | X     |
| 6 | Estagiário | Verificar se dois números são múltiplos entre si    | multiplo.py / test_multiplo.py               | X     |
| 7 | Estagiário | Inverter uma string                                    | inverter_string.py / test_inverter_string.py | X     |
| 8 | Estagiário | Testar se um ano é bissexto                           | ano_bissexto.py / test_ano_bissexto.py       | X     |

uv add pytest-cov

uv run pytest --cov=src tests/

uv run pytest --cov-report html --cov=src tests/
