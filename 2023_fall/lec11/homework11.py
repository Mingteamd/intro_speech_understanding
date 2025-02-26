import speech_recognition as sr

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.

    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)

    @returns:
    text (str) - the recognized speech
    '''
    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    return None


