# Project Jarvis - Assistente de Comando por Voz em Python

## ETHAN: Entidade Tecnológica de Assistência Natural
Jarvis é um assistente de comando por voz simples e eficaz em Python que utiliza reconhecimento de fala para executar várias tarefas, como pesquisar na Wikipedia, reproduzir músicas no YouTube, obter informações de cotação de ações e interagir com o modelo de linguagem GPT-3 da OpenAI.

## Pré-requisitos

Antes de usar o Jarvis, você precisa ter os seguintes pré-requisitos instalados em seu sistema:

- Python 3.x
- Bibliotecas Python: speech_recognition, pyttsx3, wikipedia, pywhatkit, yfinance, openai
- Uma chave de API da OpenAI (você pode obtê-la em https://openai.com)

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu_usuario/jarvis.git
   ```

2. Instale as dependências Python:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure a chave de API da OpenAI:

   - Crie um arquivo chamado `.env` no diretório do projeto.
   - Adicione sua chave de API da OpenAI ao arquivo `.env` da seguinte forma:

     ```
     app_key=sua_chave_de_api_aqui
     ```

## Uso

1. Execute o Jarvis:

   ```bash
   python jarvis.py
   ```

2. Aguarde até que o Jarvis comece a escutar. Ele responderá quando ouvir a palavra "Jarvis".

3. Diga um comando como:

   - "Procure por <termo>": Para buscar informações na Wikipedia.
   - "Toque <música>": Para reproduzir música no YouTube.
   - "Responda <pergunta>": Para obter respostas do modelo de linguagem GPT-3.
   - "Cotação <símbolo_da_ação>": Para obter informações de cotação de ações.

4. O Jarvis responderá com os resultados ou informações solicitados.

5. Para sair, digite "sim" quando for solicitado.

## Todo
-[ ] Criação de GUI

-[ ] Criar configurações de inicialização
   -[ ] Login
   -[ ] Senha
   -[ ] FaceID
   -[ ] Voz ID
-[ ] Criar função de criação de venv

-[ ] Criar função de instalação de preparação do ambiente

-[ ] Criar módulos de testes

-[ ] Criar documentação para todos os módulos e classes

-[ ] Criar sistema de logs

- [ ] Abertura de págins web / sites específicos

- [ ] Previsão do tempo

- [ ] Notícias do dia 

- [ ] escreva um nota

- [ ] DistÂncia entre duas localizações

- [ ] Minha cocalização 

- [ ] Eventos em calendários

-[ ] Previsão do tempo: Adicione a capacidade de obter informações meteorológicas, como a previsão do tempo para uma determinada cidade. Você pode usar bibliotecas como "pyowm" ou "requests" para obter dados meteorológicos de uma API de previsão do tempo.

-[ ]  Informações sobre filmes ou séries: Integre o assistente com uma API de dados sobre filmes e séries para fornecer informações sobre lançamentos, elenco, sinopse e avaliações.

-[ ] Comandos de controle do computador: Permita que o assistente execute tarefas no computador, como abrir programas, criar lembretes, agendar eventos ou fazer capturas de tela.

-[ ] Tradução de idiomas: Adicione a funcionalidade de tradução para permitir que o assistente traduza palavras ou frases para outros idiomas.

-[ ] Pesquisa em outros mecanismos de busca: Além da pesquisa no Wikipedia, permita que o assistente pesquise em outros mecanismos de busca, como o Google, para fornecer resultados mais abrangentes.

-[ ] Respostas a perguntas gerais: Melhore o modelo de linguagem para que o assistente possa responder a perguntas gerais com base em seu conhecimento prévio, em vez de depender exclusivamente do Wikipedia.

-[ ] Lembrete de compromissos: Implemente uma funcionalidade para agendar e lembrar compromissos ou tarefas importantes.

-[ ] Controle de dispositivos inteligentes: Se você tiver dispositivos inteligentes compatíveis em casa, pode adicionar a capacidade de controlá-los através do assistente, como ligar/desligar luzes, ajustar termostatos, etc.

-[ ] Suporte a comandos personalizados: Implemente a capacidade de adicionar comandos personalizados para tarefas específicas, de acordo com as necessidades do usuário.

## Ultimas Atualizações
-[x] Substituir o ChatGPT
   Agora não utilizamos o chatgpt na função criativa, mas ainda utilizamos um modelos degenerativo para aprendizagem e criação. 

- [x] Criar função de saida 
   Implementei a função de saída com a fala, agora para sair basta dizer: `sair` ou `fechar programa` que ele será desligado.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos para o projeto Jarvis. Basta criar um fork do repositório, fazer suas alterações e enviar uma solicitação pull.

## Licença

Este projeto é licenciado sob a [Licença GNU](LICENSE).

---

**Nota:** Este README ainda não está completo! Estamos trabalhando na melhoria dele!
```
