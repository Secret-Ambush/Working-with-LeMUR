import pygame

def play_music(file_path):
    print("Working")
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print(f"Cannot load or play the file: {file_path}")
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()

print("Playing")
# Replace 'file_path' with the path to your MP3 file
file_path = '/Users/bristi/Downloads/generated_audio4.mp3'
play_music(file_path)
