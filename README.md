# 🌹 Gilded Rose - Refatoração & Arquitetura Limpa

Projeto final prático de refatoração do sistema de inventário **Gilded Rose**, aplicando boas práticas de Engenharia de Software, princípios SOLID, Design Patterns, cobertura rigorosa de testes unitários e esteira de CI/CD automatizada com GitHub Actions.

---

## 📌 Sobre o Projeto

A **Gilded Rose** é uma loja que comercializa itens mágicos e convencionais. A cada passagem de dia, o sistema atualiza duas propriedades fundamentais de cada item:
* `sell_in`: dias restantes para venda do item.
* `quality`: valor de qualidade do item.

### Problemas do Código Legado
O sistema original apresentava severos *code smells*:
* Função monolítica (`att`) com altíssima complexidade ciclomática.
* Aninhamentos profundos (*Arrow Anti-Pattern* / ifs aninhados).
* Nomes indecifráveis de variáveis e métodos.
* Números mágicos (`50`, `0`, `80`, `11`, `6`) e strings repetidas espalhadas pelo código.
* Violação dos princípios da Responsabilidade Única (SRP) e Aberto/Fechado (OCP).

---

## 🏗️ Arquitetura e Decisões Técnicas

A refatoração transformou o código legado adotando padrões modernos de design e Clean Code:

### 1. Padrão Strategy & Polimorfismo
* Criada a interface abstrata `AtualizadorDeItem` (`item_updater.py`) com o contrato `atualizar(item: Item)`.
* Cada regra de negócio foi isolada em sua respectiva classe de estratégia:
  * `AtualizadorNormal`: itens comuns (-1 qualidade/dia; -2 após o vencimento).
  * `AtualizadorAgedBrie`: ganha qualidade (+1/dia; +2 após o vencimento).
  * `AtualizadorSulfuras`: item lendário, imutável e com qualidade fixa (80).
  * `AtualizadorBackstage`: ingressos com aceleração progressiva e perda total após o concerto.
  * `AtualizadorConjurado`: degrada duas vezes mais rápido (-2/dia; -4 após o vencimento).

### 2. Princípios SOLID Aplicados
* **SRP (Single Responsibility Principle):** Cada atualizador é responsável estritamente pela evolução de um único tipo de item. A classe `GildedRose` apenas orquestra as chamadas.
* **OCP (Open/Closed Principle):** A introdução de novos tipos de itens não exige alterações em lógicas existentes — basta criar um novo atualizador que herde de `AtualizadorDeItem`. A nova funcionalidade do item **Conjurado** serviu como prova prática deste princípio.
* **LSP (Liskov Substitution Principle):** Qualquer atualizador pode ser executado uniformemente através da interface comum.

### 3. Eliminação de Strings e Números Mágicos
* Centralização de limites e constantes em `constants.py`:
  * `QUALIDADE_MAXIMA = 50`
  * `QUALIDADE_MINIMA = 0`
  * `QUALIDADE_SULFURAS = 80`

---

## 🧪 Testes Automatizados e Qualidade

O projeto conta com uma suíte de testes robusta utilizando `pytest`, cobrindo casos nominais, regras especiais e valores de borda (limites 0 e 50, dia exato do vencimento e comportamento pós-vencimento).

* **Testes unitários:** 28 testes passando (100% verde).
* **Cobertura de código:** **99% de cobertura total** medida com `pytest-cov`, atingindo 100% de cobertura em todos os atualizadores de regras de negócio e na classe principal `GildedRose`.

---

## ⚙️ Integração Contínua (CI/CD)

O repositório possui uma esteira automatizada configurada via **GitHub Actions** (`.github/workflows/testes.yml`):
* Executa automaticamente em todo `push` ou `pull_request` na branch `main`.
* Configura o ambiente Linux (`ubuntu-latest`) com Python 3.11.
* Instala as dependências via `requirements.txt`.
* Roda a suíte completa de testes (`pytest -v`) para garantir que nenhuma alteração quebre o sistema.

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3.10 ou superior instalado.

### 1. Clonar o repositório
```bash
git clone https://github.com/arqlarissalara-prog/gilded-rose-refactoring.git
cd gilded-rose-refactoring
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Executar a suíte de testes
```bash
pytest -v
```

### 4. Verificar a cobertura de código
```bash
pytest --cov=gilded_rose --cov-report=term-missing
```