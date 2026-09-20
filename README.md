# 🌹 Gilded Rose - Refatoração & Arquitetura Limpa

Projeto final prático de refatoração do sistema de inventário **Gilded Rose**, aplicando boas práticas de Engenharia de Software, princípios SOLID, Design Patterns, cobertura rigorosa de testes unitários e fluxo profissional em equipe com Git/GitHub.

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
* Criada a interface abstrata `ItemUpdater` (`item_updater.py`) com o contrato `atualizar(item: Item)`.
* Cada regra de negócio foi isolada em sua respectiva classe:
  * `AtualizadorNormal`: itens comuns (-1 qualidade/dia; -2 após o vencimento).
  * `AtualizadorAgedBrie`: ganha qualidade (+1/dia; +2 após o vencimento).
  * `AtualizadorSulfuras`: item lendário, imutável e com qualidade fixa (80).
  * `AtualizadorBackstage`: ingressos com aceleração progressiva e perda total após o concerto.
  * `AtualizadorConjurado`: degrada duas vezes mais rápido (-2/dia; -4 após o vencimento).

### 2. Princípios SOLID Aplicados
* **SRP (Single Responsibility Principle):** Cada atualizador é responsável estritamente pela evolução de um único tipo de item.
* **OCP (Open/Closed Principle):** A introdução de novos tipos de itens não exige alterações em lógicas existentes — basta criar um novo atualizador que herde de `ItemUpdater`. A feature do item **Conjurado** serviu como prova prática deste princípio.
* **LSP (Liskov Substitution Principle):** Qualquer atualizador pode ser executado uniformemente através da interface comum.

### 3. Eliminação de Strings e Números Mágicos
* Centralização de limites e constantes em `constants.py`:
  * `QUALIDADE_MAXIMA = 50`
  * `QUALIDADE_MINIMA = 0`
  * `QUALIDADE_SULFURAS = 80`

---

## 🧪 Testes Automatizados e Qualidade

O projeto conta com uma suíte abrangente de testes automatizados utilizando `pytest`, cobrindo regras nominais, casos de borda (limites 0 e 50), comportamento pós-vencimento, orquestração e representação de itens.

* **Suíte de Testes:** 28 testes unitários e de integração passando (100% verde).
* **Cobertura de Código:** **99% de cobertura total** medida via `pytest-cov`, atingindo 100% na orquestração da classe principal `GildedRose` e em todos os atualizadores de regras de negócio.
* **Integração Contínua (CI):** Workflow automatizado via GitHub Actions executando a suíte de testes e validações a cada *push* e *Pull Request* na branch `main`.

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3.10 ou superior instalado.

### 1. Clonar o repositório
```bash
git clone [https://github.com/arqlarissalara-prog/gilded-rose-refactoring.git](https://github.com/arqlarissalara-prog/gilded-rose-refactoring.git)
cd gilded-rose-refactoring