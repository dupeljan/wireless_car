import subprocess

file = "bark.mp3"

def play(audio_file_path):
    subprocess.call(["ffplay", "-nodisp", "-autoexit", audio_file_path])

def main():
	play(file)
if __name__ == '__main__':
	main()