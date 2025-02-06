from deepgram import DeepgramClient, PrerecordedOptions, FileSource
from configs import config  

deepgramApiKey = config.API_KEY

async def speech_to_text(audioPath: str):
    try:
        if not deepgramApiKey:
            raise ValueError("Deepgram API key is missing. Set the 'DEEPGRAM_API_KEY' environment variable.")

        deepgram = DeepgramClient(deepgramApiKey)
        with open(audioPath, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {"buffer": buffer_data}

        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        response = deepgram.listen.rest.v("1").transcribe_file(payload, options)
        data = response["results"]["channels"][0]["alternatives"][0]["transcript"]
        print("Transcript:", data)

        return data

    except Exception as e:
        print(f"Exception: {e}")