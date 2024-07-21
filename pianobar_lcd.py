import sys
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

# Define GPIO pins connected to the LCD
lcd_rs = digitalio.DigitalInOut(board.D25)  # RS pin
lcd_en = digitalio.DigitalInOut(board.D24)  # E pin
lcd_d4 = digitalio.DigitalInOut(board.D23)  # D4 pin
lcd_d5 = digitalio.DigitalInOut(board.D17)  # D5 pin
lcd_d6 = digitalio.DigitalInOut(board.D21)  # D6 pin
lcd_d7 = digitalio.DigitalInOut(board.D22)  # D7 pin

# Define LCD column and row size
lcd_columns = 16
lcd_rows = 2

# Initialize the LCD class
lcd = character_lcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
    lcd_columns, lcd_rows
)

def update_lcd(title, artist):
    lcd.clear()
    lcd.message = f"{title}\n{artist}"

def run_pianobar():
    process = subprocess.Popen(['pianobar'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    title = ""
    artist = ""

    while True:
        output = process.stdout.readline()
        if output = '' and process.poll() is not None:
            break

        if output:
            if "SONG" in output:
                print(output)
                # Testing below
                output_list = output.split(" | ")
                title = output_list[0]
                artist = output_list[1]
                # update_lcd(title, artist)

if __name__ == "__main__":
    run_pianobar()
