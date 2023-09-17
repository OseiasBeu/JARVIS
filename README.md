# Jarvis - Assistente de Comando por Voz em Python

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

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos para o projeto Jarvis. Basta criar um fork do repositório, fazer suas alterações e enviar uma solicitação pull.

## Licença

Este projeto é licenciado sob a [Licença GNU](LICENSE).

---

**Nota:** Este README ainda não está completo! Estamos trabalhando na melhoria dele!
```
