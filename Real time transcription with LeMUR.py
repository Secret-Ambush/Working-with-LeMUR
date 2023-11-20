import assemblyai as aai

text = ""
aai.settings.api_key = f"c4eeac28c47a41a49602463b427503a0"

def getValues(text):
    prompt = "Which of the following directions is in the script (Straight/Left/Right)?"
    result1 = text.lemur.task(prompt)
    
    if result1 != "Straight" | "Left" | "Right":
        result1 == "Stop"
    
    prompt2 = "How many units is mentioned in the script? Mention the number only. In case of no number, output 0" 
    result2 = text.lemur.task(prompt2)
    
    print(result1 + " " + result2)

def on_open(session_opened: aai.RealtimeSessionOpened):
    print("Session ID:", session_opened.session_id)

def on_error(error: aai.RealtimeError):
    print("An error occured:", error)

def on_close():
    print("Closing Session")
    getValues(text)
    
    
def on_data(transcript: aai.RealtimeTranscript):
    if not transcript.text:
        return

    if isinstance(transcript, aai.RealtimeFinalTranscript):
        print(transcript.text, end="\r\n")
        text = transcript.text
        on_close()
        
        
    else:
        print(transcript.text, end="\r")

transcriber = aai.RealtimeTranscriber(
    sample_rate=16_000,
    on_data=on_data,
    on_error=on_error,
    on_open=on_open,
    on_close=on_close,
)

transcriber.connect()
print("Hello there!")
microphone_stream = aai.extras.MicrophoneStream(sample_rate=16_000)
transcriber.stream(microphone_stream)
transcriber.close()