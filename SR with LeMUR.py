import assemblyai as aai
import speech_recognition as sr


text = ""
aai.settings.api_key = f"c4eeac28c47a41a49602463b427503a0"

def getValues(audio):
    prompt = "Which of the following directions is in the script (Straight/Left/Right)?"
    result1 = audio.lemur.task(prompt)
    
    if result1 != "Straight" | "Left" | "Right":
        result1 == "Stop"
    
    prompt2 = "How many units is mentioned in the script? Mention the number only. In case of no number, output 0" 
    result2 = audio.lemur.task(prompt2)
    
    print(result1 + " " + result2)


r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening now: ")
    audio = r.listen(source, timeout=2)
    print("Stopped Listening")
    getValues(audio)
