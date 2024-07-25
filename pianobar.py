import subprocess

# Variable initialization
output_list = []
song_title = "Gathering"
artist = "Information"

# Create subprocess object
pianobar = subprocess.Popen(['pianobar'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Display default message to LCD
print(song_title)
print(artist)

while True:
    output = pianobar.stdout.readline()

    if output == "" and pianobar.poll() is not None:
        break

    # Get song title and artist name
    if 'SONG' in  output:
        output_list = output.split(':')
        song_title = output_list[1].strip()
        artist = output_list[2].strip()
        print(song_title)
        print(artist)

print("Done")
