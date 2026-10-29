# jogo-do-numero-secreto

# Adivinhe o Número

Jogo de terminal em Python: o programa sorteia um número e você tenta descobrir com o menor número de tentativas. O recorde de cada nível fica salvo em um arquivo.

## Requisitos

Python 3.6 ou superior. Não precisa instalar nenhuma biblioteca.

## Como rodar

```
python adivinhe_o_numero.py
```

## Níveis

- **Fácil:** número de 1 a 10, 5 tentativas
- **Médio:** número de 1 a 100, 7 tentativas
- **Difícil:** número de 1 a 1000, 10 tentativas

## Como jogar

- Escolha um nível e digite um número
- A cada erro, o jogo diz se o número é maior ou menor que o seu chute
- Entradas inválidas (letras ou números fora do intervalo) não gastam tentativas
- Ao vencer, o jogo compara seu resultado com o recorde do nível

## Exemplo de partida

```
Escolha um nível de 1 a 3: 1
Bem vindo ao jogo: Adivinhe o número!

======================================

Você escolheu o nível Fácil
Você tem 5 tentativas para adivinhar um número de 1 a 10
Qual o número secreto? 5
O número é MENOR que 5
Mais uma vez...

======================================

Qual o número secreto? 3
O número é MAIOR que 3
Mais uma vez...

======================================

Qual o número secreto? 4
Parabéns! O número era 4
Você venceu em 3 tentativas!
Novo recorde!
```

## Recordes

O melhor resultado de cada nível (menor número de tentativas) fica em `recordes.json`, criado automaticamente na primeira vitória. Se o arquivo não existir ou estiver vazio, o jogo começa sem recordes.
