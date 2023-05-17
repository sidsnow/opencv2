import json, os
import pyttsx3, vosk, pyaudio, requests
import webbrowser
import time

tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voices', 'ru')

model = vosk.Model('vosk-model-small-ru-0.4')
record = vosk.KaldiRecognizer(model, 16000)
pa = pyaudio.PyAudio()

stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=16000,
                 input=True,
                 frames_per_buffer=8000)

stream.start_stream()


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if record.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(record.Result())
            if answer['text']:
                yield answer['text']


def speak(say):
    tts.say(say)
    tts.runAndWait()


print('start')

# for text in listen():
#     if text == 'закрыть':
#         quit()
#     elif text == 'блокнот':
#         os.system('notepad.exe')
#     elif text == 'во что бы поиграть?':
#         speak('а ты закрылась?')
#         text = listen()
#         if text == 'да':
#             speak('открой третью с конца игру в библиотеке стима')
#         else:
#             speak('много хочешь.')
#             webbrowser.open('https://www.youtube.com/watch?v=avXxjwyFMKE')
#     else:
#         speak('я не понимаю, что ты от меня хочешь, кожаный мешок.')


while True:
    text = input()
    if text == 'закрыть':
        quit()
    elif text == 'блокнот':
        os.system('notepad.exe')
    elif text == 'во что бы поиграть?':
        speak('а ты закрылась?')
        text = input()
        if text == 'да':
            speak('открой третью с конца игру в библиотеке стима')
        else:
            speak('много хочешь.')
            webbrowser.open('https://www.youtube.com/watch?v=avXxjwyFMKE')
    else:
        speak('я не понимаю, что ты от меня хочешь, кожаный мешок.')