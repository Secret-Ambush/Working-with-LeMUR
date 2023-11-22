from elevenlabs import generate, set_api_key
from pydub import AudioSegment
from pydub.playback import play
import io

# Set your API key here
set_api_key("ebecdfe96e0ec7f40b0d03aeed91443b")

# Generate audio
audio = generate(
    text="Hi! I'm the world's most advanced text-to-speech system, made by elevenlabs.",
    voice="Bella"
)

# Convert the audio bytes to AudioSegment
audio_data = AudioSegment.from_file(io.BytesIO(audio), format="mp3")

# Play the audio using pydub's playback
play(audio_data)