# Assistente de Notas por Voz

Projeto desenvolvido na UFCD 10790 — Projeto de Programação.

## Funcionalidades Atuais
- Menu principal via consola.
- Captação de áudio via microfone.

## Como executar
1. Instalar dependências:
## Versão 1.1
- Áudio captado é agora transcrito automaticamente para texto em português de Portugal.
## Versão 1.2
- Análise de palavras-chave implementada.
- O sistema sugere automaticamente o tema da nota (trabalho, pessoal, lembrete ou ideia).
## Versão 1.3
- Notas agora são guardadas automaticamente em ficheiros `.csv`.
- Ficheiros são nomeados por data e incluem hora, tema e conteúdo.
## Versão 1.4
- Implementada funcionalidade de consulta de notas guardadas.
- Possível listar por ficheiro e aplicar filtro por tema.
## Versão 1.5
- Interface gráfica com `Tkinter` adicionada.
- Utilizador pode escolher entre modo consola ou interface com botões.
## Versão final 1.6
# Assistente de Notas por Voz

## Descrição
Aplicação desenvolvida em Python que permite gravar notas por voz, transcrevê-las para texto, classificar por tema e guardar em ficheiro CSV. Inclui interface gráfica opcional.

## Funcionalidades
- Gravação de áudio via microfone.
- Transcrição automática de fala para texto.
- Classificação de notas por tema com base em palavras-chave.
- Armazenamento automático em ficheiros CSV por data.
- Consulta de notas guardadas com opção de filtro por tema.
- Interface gráfica com Tkinter.

## Estrutura do Projeto
- `main.py` → Ponto de entrada, escolha entre terminal ou GUI.
- `audio.py` → Captação de áudio e chamada às funções de transcrição e armazenamento.
- `voz_para_texto.py` → Conversão de áudio para texto.
- `analise.py` → Extração de palavras-chave e classificação de tema.
- `armazenamento.py` → Gravação de notas em CSV.
- `consulta.py` → Consulta de notas guardadas.
- `interface.py` → Interface gráfica com Tkinter.

## Requisitos
pip install SpeechRecognition
pip install PyAudio
pip install tkintertable