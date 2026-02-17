# armazen
Script em Python para cálculo de tinta por metro quadrado e operações matemáticas

# 🎨 Calculadora de Tinta e Operações Matemáticas

## Sobre

Este projeto foi desenvolvido em Python com o objetivo de praticar lógica de programação e cálculos matemáticos em um fluxo interativo.

O programa simula uma conversa informal com o usuário e realiza dois tipos principais de cálculo:

1. Cálculo da quantidade de tinta necessária para pintar uma área.
2. Operações matemáticas com números informados pelo usuário.

---

## Funcionalidades

### 🎨 Cálculo de tinta

O programa:

- Pergunta se o usuário já sabe o tamanho da área em metros quadrados.
- Caso não saiba, calcula a área com base no comprimento e largura.
- Considera que:
  - 1 litro de tinta cobre 6m²
  - Cada lata possui 4 litros
  - O valor unitário da lata é R$ 80,00
- Calcula:
  - Quantidade necessária de latas (arredondando para cima)
  - Valor total da compra

---

### ➗ Operações matemáticas

Após o cálculo da tinta, o programa realiza:

- O dobro do primeiro número somado à metade do segundo
- O triplo do primeiro número somado ao terceiro
- O terceiro número elevado ao cubo

---

## Conceitos praticados

Neste projeto foram trabalhados:

- Entrada de dados (`input`)
- Conversão de tipos (`int`, `float`)
- Estruturas condicionais (`if`, `elif`)
- Operações matemáticas
- Arredondamento manual para cima
- Uso de f-strings
- Organização de fluxo lógico

---

## Como executar

Certifique-se de ter o Python instalado e execute:

```bash
python nome_do_arquivo.py
