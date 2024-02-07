from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os

def speak(text, lang="ko", speed=False):
    tts = gTTS(text=text, lang=lang, slow=speed)
    filename = "./tts.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

Recognizer = sr.Recognizer()
mic = sr.Microphone()

while True:
    with mic as source:
        print("듣고 있어요...")
        audio = Recognizer.listen(source)
    try:
        data = Recognizer.recognize_google(audio, language="ko")
        print(f"인식된 문장: {data}")
        if "안녕" in data:
            speak("네, 어떻게 도와드릴까요?")
            print("BOT : 네, 어떻게 도와드릴까요?")
        else:
            speak("다시 말씀해 주세요.")
    except sr.RequestError as e:
        # Google 음성 인식 서비스에 요청을 보내는데 실패했을 때
        speak("음성 서비스에 문제가 발생했습니다; {0}".format(e))
