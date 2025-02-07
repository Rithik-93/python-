from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
from configs import config

deepgramApiKey = config.DEEPGRAM

def speech_to_text(audioPath: str) -> str:
    try:
        deepgram = DeepgramClient(deepgramApiKey)

        with open(audioPath, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-3",
            smart_format=True,
        )

        response = deepgram.listen.rest.v("1").transcribe_file(payload, options)
        data = response.results.channels[0].alternatives[0].transcript

        print(data,'laaaaaaaaaaaaaa')
        return data

    except Exception as e:
        print(f"Exception: {e}")


# speech_to_text('./harvard.wav')