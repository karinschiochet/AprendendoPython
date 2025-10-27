# 🐍 Roteiro Completo de Estudos - Python do Zero ao Profissional

---

## 📚 FASE 1: FUNDAMENTOS (4-6 semanas)

### Semanas 1-2: Sintaxe Básica
**O que estudar:**
- ✅ Variáveis e tipos de dados (int, float, string, bool)
- ✅ Operadores (aritméticos, lógicos, comparação)
- ✅ Estruturas condicionais (if/elif/else)
- ✅ Loops (for, while)
- ✅ Funções básicas (def, parâmetros, return)
- ✅ Listas, tuplas e dicionários
- ✅ Input/Output (print, input)

**Recursos:**
- 📖 [Python.org Tutorial Oficial](https://docs.python.org/pt-br/3/tutorial/)
- 🎥 Curso Python para Iniciantes - Gustavo Guanabara (YouTube - GRATUITO)
- 📱 App: SoloLearn Python

**Exercícios:**
- [HackerRank - Python Basics](https://www.hackerrank.com/domains/python)
- [Exercism - Python Track](https://exercism.org/tracks/python) (com mentoria!)
- [CodingBat - Python](https://codingbat.com/python)

### Semanas 3-4: Estruturas de Dados Intermediárias
**O que estudar:**
- ✅ List comprehensions
- ✅ Manipulação de strings (métodos, formatação, f-strings)
- ✅ Sets e frozensets
- ✅ Métodos de listas e dicionários
- ✅ Funções built-in (map, filter, zip, enumerate)
- ✅ Tratamento de exceções (try/except/finally)

**Exercícios:**
- [LeetCode Easy Problems](https://leetcode.com/problemset/?difficulty=EASY&page=1&topicSlugs=array%2Cstring)
- [Python Principles - 25 Exercises](https://pythonprinciples.com/challenges/)
- Criar mini-projetos: calculadora, jogo da forca, to-do list CLI

### Semanas 5-6: Programação Orientada a Objetos (POO)
**O que estudar:**
- ✅ Classes e objetos
- ✅ Atributos e métodos
- ✅ Construtores (__init__)
- ✅ Herança e polimorfismo
- ✅ Encapsulamento (public, private, protected)
- ✅ Métodos especiais (__str__, __repr__, __len__)
- ✅ Decoradores (@property, @staticmethod, @classmethod)

**Recursos:**
- 📖 [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- 🎥 Corey Schafer - OOP Tutorial (YouTube)

**Exercícios:**
- Criar sistema de biblioteca (classes: Livro, Usuario, Biblioteca)
- Sistema bancário simples (Conta, ContaCorrente, ContaPoupanca)
- Jogo RPG com personagens (Heroi, Monstro, Inventario)

---

## 🚀 FASE 2: INTERMEDIÁRIO (6-8 semanas)

### Semanas 7-8: Trabalhando com Arquivos e Dados
**O que estudar:**
- ✅ Leitura/escrita de arquivos (txt, csv, json)
- ✅ Biblioteca `os` e `pathlib`
- ✅ Manipulação de CSV (módulo csv e pandas)
- ✅ JSON (json.dumps, json.loads)
- ✅ Expressões regulares (regex - módulo `re`)
- ✅ Datetime e timezone

**Bibliotecas:**
```python
import csv
import json
import os
import pathlib
from datetime import datetime
import re
```

**Exercícios:**
- Analisador de logs (extrair IPs, timestamps, erros)
- Conversor CSV → JSON
- Gerador de relatórios a partir de arquivos

### Semanas 9-10: Bibliotecas Essenciais
**O que estudar:**
- ✅ **Requests** - requisições HTTP/APIs REST
- ✅ **Beautiful Soup** - web scraping
- ✅ **Pandas** - manipulação de dados tabulares
- ✅ **NumPy** - computação numérica (básico)
- ✅ Ambientes virtuais (venv, virtualenv)
- ✅ Gerenciamento de dependências (pip, requirements.txt)

**Mini-projetos:**
- 🌐 Consultar APIs públicas (ViaCEP, GitHub API, OpenWeather)
- 📊 Análise de dataset CSV com pandas
- 🕷️ Web scraper de notícias/preços

### Semanas 11-12: Banco de Dados
**O que estudar:**
- ✅ SQL básico (SELECT, INSERT, UPDATE, DELETE, JOINs)
- ✅ SQLite com Python (módulo `sqlite3`)
- ✅ PostgreSQL/MySQL com `psycopg2` ou `pymysql`
- ✅ ORMs: SQLAlchemy (básico)
- ✅ Boas práticas: SQL injection, prepared statements

**Projeto:**
- 💾 Sistema CRUD completo (Create, Read, Update, Delete)
- Exemplo: Sistema de cadastro de clientes com histórico de pedidos

### Semanas 13-14: Testes e Qualidade de Código
**O que estudar:**
- ✅ Unittest (biblioteca padrão)
- ✅ Pytest (framework moderno)
- ✅ Mocks e fixtures
- ✅ TDD (Test-Driven Development) - conceitos
- ✅ Linters: pylint, flake8
- ✅ Formatadores: black, autopep8
- ✅ Type hints e mypy

**Exemplo de teste:**
```python
import pytest

def somar(a, b):
    return a + b

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0
```

---

## 💼 FASE 3: PROFISSIONAL (8-12 semanas)

### Escolha SUAS trilhas de especialização:

#### 🌐 Trilha 1: Desenvolvimento Web
**O que estudar:**
- ✅ **Flask** (micro-framework) ou **FastAPI** (moderno, async)
- ✅ **Django** (framework full-stack)
- ✅ REST APIs (GET, POST, PUT, DELETE)
- ✅ Autenticação (JWT, OAuth2)
- ✅ Frontend básico (HTML, CSS, JavaScript - necessário)
- ✅ Deploy (Heroku, AWS, Docker)

**Recursos:**
- 📖 [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- 📖 [FastAPI Documentation](https://fastapi.tiangolo.com/pt/)
- 🎥 Corey Schafer - Django/Flask Tutorials

**Projeto final:**
- 🚀 API REST completa (ex: sistema de e-commerce, blog, task manager)

---

#### 📊 Trilha 2: Data Science / Análise de Dados
**O que estudar:**
- ✅ **Pandas** (avançado) - manipulação de dados
- ✅ **NumPy** - arrays e computação numérica
- ✅ **Matplotlib / Seaborn** - visualização de dados
- ✅ **Jupyter Notebooks** - análise interativa
- ✅ Estatística básica
- ✅ Machine Learning (Scikit-learn) - introdução
- ✅ SQL avançado (window functions, CTEs)

**Recursos:**
- 📖 [Python for Data Analysis (Wes McKinney)](https://wesmckinney.com/book/)
- 🎥 [Kaggle Learn - Python](https://www.kaggle.com/learn/python)
- 📊 Datasets: [Kaggle](https://www.kaggle.com/datasets), [UCI ML Repository](https://archive.ics.uci.edu/)

**Projeto final:**
- 📈 Análise exploratória de dataset real (ex: dados do banco, COVID-19, vendas)
- 🤖 Modelo preditivo simples (regressão, classificação)

---

#### 🤖 Trilha 3: Automação e DevOps
**O que estudar:**
- ✅ **Selenium** - automação web
- ✅ **Paramiko / Fabric** - automação SSH
- ✅ **Ansible** - automação de infraestrutura
- ✅ **Docker** - containers
- ✅ **CI/CD** - GitHub Actions, GitLab CI
- ✅ Scripts de monitoramento e alertas
- ✅ APIs de cloud (boto3 para AWS)

**Recursos:**
- 📖 [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- 🎥 Tech With Tim - Automation Tutorials

**Projeto final:**
- 🔧 Suite de automação para tarefas do banco (ex: relatórios automáticos, validações de compliance, backup automatizado)

---

#### 🔒 Trilha 4: Segurança da Informação (PERFEITA PRA VOCÊ!)
**O que estudar:**
- ✅ **Scapy** - manipulação de pacotes de rede
- ✅ **Requests + BeautifulSoup** - análise de vulnerabilidades web
- ✅ **Cryptography** - criptografia
- ✅ **Nmap + Python** - scanning de rede
- ✅ Análise de logs (regex, pandas)
- ✅ Detecção de anomalias
- ✅ Scripts de pentest (com responsabilidade!)

**Recursos:**
- 📖 [Black Hat Python](https://nostarch.com/black-hat-python2E)
- 📖 Violent Python (Justin Seitz)
- 🔐 [OWASP Top 10](https://owasp.org/www-project-top-ten/)

**Projeto final:**
- 🛡️ Scanner de vulnerabilidades customizado
- 📊 Dashboard de análise de logs de segurança
- 🚨 Sistema de detecção de fraudes (correlaciona com seu trabalho!)

---

## 🎯 DICAS DE OURO PARA SE TORNAR PROFISSIONAL

### 1. **Código TODOS OS DIAS** (consistência > intensidade)
- ⏰ Reserve 1-2h por dia (de preferência mesmo horário)
- 🔥 Mantenha um streak no GitHub (contribuições diárias)
- 📝 Projetos pequenos são melhores que projetos gigantes inacabados

### 2. **Leia código de outras pessoas**
- 👀 Explore repositórios populares no GitHub
- 📚 Leia código de bibliotecas que você usa
- 🤝 Participe de code reviews (mesmo que de projetos open source)

### 3. **Construa um portfólio**
- 🌟 GitHub com README bem escrito
- 📂 3-5 projetos completos e documentados
- 🎨 Evite tutoriais copiados - faça projetos originais!

**Exemplos de projetos para portfólio:**
- Sistema de análise de fraudes bancárias (correlaciona com seu trabalho!)
- API REST com autenticação e testes
- Dashboard de monitoramento (ex: servidores Linux)
- Bot de Telegram/Discord útil
- Ferramenta CLI profissional

### 4. **Aprenda a debuggar**
- 🐛 Use `pdb` (Python debugger)
- 🔍 Print debugging é OK no começo, mas evolua
- 📊 Aprenda a ler stack traces
- 🧪 Escreva testes antes de debugar

### 5. **Domine o terminal e Git**
```bash
# Git essencial
git init
git add .
git commit -m "mensagem clara"
git push origin main
git branch feature/nova-funcionalidade
git merge
```

### 6. **Siga boas práticas desde o início**
- ✅ PEP 8 (style guide do Python)
- ✅ Nomes descritivos de variáveis
- ✅ Funções pequenas e focadas (uma responsabilidade)
- ✅ Docstrings para funções/classes
- ✅ Type hints quando possível

**Exemplo de código limpo:**
```python
def calcular_desconto(preco: float, percentual: int) -> float:
    """
    Calcula o preço com desconto aplicado.
    
    Args:
        preco: Preço original do produto
        percentual: Percentual de desconto (0-100)
    
    Returns:
        Preço final com desconto aplicado
    
    Raises:
        ValueError: Se percentual for inválido
    """
    if not 0 <= percentual <= 100:
        raise ValueError("Percentual deve estar entre 0 e 100")
    
    desconto = preco * (percentual / 100)
    return preco - desconto
```

### 7. **Entre na comunidade Python**
- 💬 [Python Brasil (Telegram)](https://t.me/pythonbrasil)
- 🐦 Siga: @realpython, @kennethreitz, @gvanrossum
- 📺 YouTube: Corey Schafer, Tech With Tim, ArjanCodes
- 📰 Newsletter: Real Python, Python Weekly

### 8. **Participe de desafios**
- 🏆 Advent of Code (dezembro - mas arquivos disponíveis o ano todo)
- 💻 LeetCode contests semanais
- 🎮 Project Euler (matemática + programação)
- 🌐 Hacktoberfest (outubro - contribuições open source)

### 9. **Estude algoritmos e estruturas de dados**
- 📚 Livro: "Grokking Algorithms" (visual e didático)
- 🎓 [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)
- 🧮 Foco em: arrays, hash tables, árvores, grafos, busca, ordenação

### 10. **Aprenda inglês técnico**
- 📖 Documentação oficial é em inglês
- 🌍 Maioria dos recursos de qualidade estão em inglês
- 💼 Mercado de trabalho valoriza MUITO
- 🎧 Pratique lendo docs, vendo vídeos, participando de fóruns

---

## 📋 CHECKLIST DO PROFISSIONAL PYTHON

Você pode se considerar profissional quando:

- [ ] Consegue resolver problemas reais sem tutoriais
- [ ] Sabe quando usar cada estrutura de dados
- [ ] Entende POO e aplica quando necessário
- [ ] Escreve testes automatizados
- [ ] Sabe debuggar código complexo
- [ ] Usa Git com confiança
- [ ] Lê e entende código de terceiros
- [ ] Conhece pelo menos 1 framework/biblioteca a fundo
- [ ] Tem 3+ projetos completos no GitHub
- [ ] Contribuiu para algum projeto open source (mesmo que documentação!)
- [ ] Sabe otimizar código (Big O notation básico)
- [ ] Escreve código limpo e legível

---

## 📅 CRONOGRAMA REALISTA

**Total: 18-26 semanas (4-6 meses)**

| Fase | Duração | Dedicação/dia |
|------|---------|---------------|
| Fundamentos | 6 semanas | 1-2h |
| Intermediário | 8 semanas | 1.5-2h |
| Especialização | 8-12 semanas | 2-3h |

**⚡ Acelerado (dedicação full-time):** 3 meses  
**🐢 Confortável (pós-trabalho):** 6 meses  
**🎯 Realista para quem trabalha:** 4-5 meses

---

## 🎓 RECURSOS EXTRAS GRATUITOS

### Cursos Completos:
- 🇧🇷 [Curso em Vídeo - Python (Gustavo Guanabara)](https://www.youtube.com/playlist?list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0)
- 🇺🇸 [CS50 Python - Harvard](https://cs50.harvard.edu/python/)
- 🇺🇸 [Python for Everybody - Coursera](https://www.coursera.org/specializations/python)

### Livros Online Gratuitos:
- 📖 [Automate the Boring Stuff](https://automatetheboringstuff.com/)
- 📖 [Think Python (Allen Downey)](https://greenteapress.com/wp/think-python-2e/)
- 📖 [Python Fluente (Luciano Ramalho)](https://pythonfluente.com/) - português!

### Plataformas de Exercícios:
- ⭐ [Exercism](https://exercism.org/tracks/python) - COM MENTORIA!
- 🏅 [HackerRank](https://www.hackerrank.com/domains/python)
- 🧩 [LeetCode](https://leetcode.com/)
- 🎮 [CodeWars](https://www.codewars.com/)
- 🏆 [Advent of Code](https://adventofcode.com/)

### Documentação Essencial:
- 📚 [Python Docs Oficial (PT-BR)](https://docs.python.org/pt-br/3/)
- 🔍 [Real Python](https://realpython.com/)
- 📖 [Python Module of the Week](https://pymotw.com/3/)

---

## 💡 DICA FINAL: O PROJETO PERFEITO PRA VOCÊ

Dado que você trabalha com **segurança bancária e fraude**, considere construir:

### 🚨 **Sistema de Análise de Fraudes e Auditoria**
- Analisador de logs SSH (quem acessou, quando, o que fez)
- Dashboard de monitoramento de acessos privilegiados
- Detector de anomalias (horários incomuns, comandos suspeitos)
- Gerador de relatórios automáticos de compliance
- Integração com APIs do seu cofre de senhas
- Alertas automáticos via Telegram/Slack

**Vantagens:**
- ✅ Aplica diretamente no seu trabalho
- ✅ Demonstra valor real para gestão
- ✅ Portfolio matador para mudança de área (para segurança + Python)
- ✅ Aprende Python resolvendo problemas reais

---

## 🚀 COMECE HOJE!

**Primeiros passos AGORA:**
1. Instale Python 3.11+ (python.org)
2. Instale VS Code + extensão Python
3. Faça "Hello World"
4. Resolva 1 exercício no Exercism
5. Crie conta no GitHub e faça primeiro commit

**Lembre-se:** Todo expert foi iniciante um dia. A diferença é que eles **não desistiram**! 💪

---

**Boa sorte na jornada! 🐍✨**