from PIL import Image

# Memuat gambar
image = Image.open('example.jpg')

cropped_image = image.crop((10, 10, 200, 200))

resized_image = cropped_image.resize((100, 100))

from PIL import ImageFilter

filtered_image = resized_image.filter(ImageFilter.BLUR)

from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('example.mp3')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama

combined_audio = audio + clipped_audio

audio.export('result.wav', format='wav')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB