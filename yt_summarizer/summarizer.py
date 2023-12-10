from openai import OpenAI
import yt_summarizer.constants as constants
import yt_summarizer.utils as utils
import tiktoken

class Summarizer:
    def __init__(self, open_ai_key: str, model: str = 'small.en'):
        self.client = OpenAI(api_key=open_ai_key)
        self.whisper_model = model
        pass

    def summarize_youtube(self, url):
        file_path = utils.extract_audio(url)
        segments = utils.transcribe_audio(file_path, self.whisper_model)
        output_file_path = utils.write_txt(constants.TRANSCRIBE_OUTPUT_FILE_NAME, segments)

        file_content = utils.read_file_content(output_file_path)

        return  self.__send(prompt=constants.SUMMARIZE_PROMPT, text_data=file_content)
    
    def __send(
        self,
        prompt,
        text_data=None,
        chat_model="gpt-3.5-turbo",
        max_tokens=2500,
    ):
        tokenizer = tiktoken.encoding_for_model(chat_model)
        token_integers = tokenizer.encode(text_data)

        chunk_size = max_tokens - len(tokenizer.encode(prompt))
        chunks = [
            token_integers[i : i + chunk_size]
            for i in range(0, len(token_integers), chunk_size)
        ]

        chunks = [tokenizer.decode(chunk) for chunk in chunks]

        messages = [
            {"role": "user", "content": prompt},
            constants.CHUNK_START_MESSAGE,
        ]

        for chunk in chunks:
            messages.append({"role": "user", "content": chunk})
            response = self.client.chat.completions.create(model=chat_model, messages=messages)

        messages.append(constants.CHUNK_END_MESSAGE)
        response = self.client.chat.completions.create(model=chat_model, messages=messages)
        final_response = response.choices[0].message.content.strip()

        return final_response

