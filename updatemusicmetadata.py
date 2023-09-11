import os
from mutagen.easyid3 import EasyID3

directory = "/home/victorodg/Storage/Music"

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        # Load the file's metadata
        filepath = os.path.join(directory, filename)
        audio = EasyID3(filepath)

        # Check if the metadata contains the substring we're looking for
        for key, value in audio.items():
            if isinstance(value, list):
                value = value[0]
            if '(*emaster*)' in value:
                # Remove the substring from the metadata
                new_value = value.split('(*emaster*)')[0].strip()
                audio[key] = new_value
            elif '[*emaster*]' in value:
                # Remove the substring from the metadata
                new_value = value.split('[*emaster*]')[0].strip()
                audio[key] = new_value

        # Save the updated metadata
        audio.save()
