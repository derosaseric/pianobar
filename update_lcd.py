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

# Read artist and title from command line arguments
artist = sys.argv[1]
title = sys.argv[2]

# Display artist and title on the LCD
lcd.clear()
lcd.message = f"{artist}\n{title}"

# Display the message for a few seconds
time.sleep(10)
lcd.clear()
