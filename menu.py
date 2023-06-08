import os
from ursina import *

app = Ursina()

window.title = "Main Menu"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = True

game_started = False  # Melacak status permainan (apakah permainan sudah dimulai atau belum)

def start_game():
    global game_started
    game_started = True
    os.system("laut.py")  # Memulai file game yang diinginkan setelah menekan tombol "Mulai"

def input(key):
    if key == 'escape':
        application.quit()
    if not game_started:
        return  # Mengabaikan input saat berada di menu utama

    # Logika input permainan di sini

background = Entity(model='quad', texture='bg_pantai.jpg')
background.scale_x = window.aspect_ratio * 10  # Mengubah skala lebar latar belakang sesuai dengan aspek rasio layar
background.scale_y = 10  # Mengubah skala tinggi latar belakang agar sesuai dengan tinggi layar

# Membuat entitas menu utama
title = Text(text="Virtual Beach", scale=3, origin=(0, 0), y=0.3,color = color.black, font='Font/entropicbrush.otf')  # Judul di tengah dengan y=0.2
start_button = Button(text="Mulai", scale=(0.2,0.1), origin=(0, 0), y=0, on_click=start_game)  # Button "Mulai" di tengah dengan y=0

tutorial = [
    "How To Play",
    "A,S,W,D = Movement",
    "Mouse = Look Around",
    "Space = Jump"
]


# Membuat entitas teks untuk menampilkan nama-nama di bawah tombol "Mulai"

tutorial_text = Text(
    text='\n'.join(tutorial),
    scale=1,
    origin=(0.0, 1.9),
    y=0.01,
    eternal=True,
    color = color.white,
    text_stroke=color.black,
    font = 'Font/Montserrat-SemiBold.ttf'
 )

credit = [
    "Fakhriza Fauzi     065121131",
    "Satrio Pinandito   065121147",
    "Siti Halimah       065121145",
    "Ilham Abdul        065121136",
    "Ilham Khairan      065121126"
]

credit_text = Text(
    text='\n'.join(credit),
    scale=0.7,
    origin=(0, 4),
    y=0.01,
    eternal=True,
    color = color.white,
    text_stroke=color.black,
    font = 'Font/Montserrat-SemiBold.ttf'
 )


app.run()
