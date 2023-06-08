from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()


# Membuat window
window.title = "Pemandangan Pantai"
window.borderless = False
window.fullscreen = True
window.exit_button.visible = True

# Membuat objek langit (skybox)
sky = Sky()
sky.texture = load_texture('sky_sunset')

# Membuat objek matahari
sun = DirectionalLight()
sun.color = color.white
sun.rotation = Vec3(45, 45, 0)

# Membuat lantai parkir
jalan_raya = Entity(model='plane', scale=(20, 3, 100), texture='Texture/aspal.jpg', collider='box', texture_scale=(1, 1))

# Membuat lantai parkir
parkir = Entity(model='plane', scale=(20, 3, 100),
                texture='brick', collider='box', texture_scale=(100, 100))
parkir.position = (20, 0, 0)
# parkir.x = jalan_raya.x + jalan_raya.scale_x # Menempatkan lantai pasir setelah lantai parkir

# Membuat lantai pantai
pasir = Entity(model='plane', scale=(100, 0, 200),
               texture='Texture/pasir.jpg', collider='box', texture_scale=(100, 100))
pasir.position = (80, 0, 0)  # Menempatkan lantai pasir setelah lantai parkir

# Membuat lantai laut
laut = Entity(model='plane', scale=(100, 0, 200),
               texture='Texture/laut.jpeg', collider='mesh', texture_scale=(100, 100))
laut.position = (180, 0, 0)  # Menempatkan laut setelah pasir

# entitas gate
gate = Entity(model='3d/gate.obj', collider='mesh',texture = 'Texture/batu.jpg')
gate.scale = 0.05
gate.position = (35,-2,0)

# entitas mobil truck2
parkir = Entity(model='3d/truck.obj', collider='box')
parkir.texture = 'Texture/Truck.png'
parkir.position = (20, 0.2, 10)
parkir.scale = 1
parkir.rotation_y = 90

# entitas mobil truck2
parkir = Entity(model='3d/porsche.obj', collider='box')
parkir.texture = 'Texture/Truck.png'
parkir.position = (20, 0.7, 15)
parkir.scale = 1
parkir.rotation_y = -90

# entitas mobil truck2
parkir = Entity(model='3d/porsche.obj', collider='box')
parkir.texture = 'Texture/Truck.png'
parkir.position = (20, 0.7, 20)
parkir.scale = 1
parkir.rotation_y = -90

# # entitas mobil porsche1
# car1 = Entity(model='3d/porsche.obj', collider='box')
# car1.texture = 'Texture/Truck.png'
# car1.position = (5, 1, 30)
# car1.scale = 1

# # entitas mobil porsche2
# car2 = Entity(model='3d/porsche.obj', collider='box')
# car2.texture = 'Texture/Truck.png'
# car2.position = (5, 1, -30)
# car2.scale = 1

# entitas lampu1
lampu = Entity(model='3d/lamp.obj', collider='mesh')
lampu.position = (9, 0, 50)
lampu.scale = 0.005

# entitas lampu2
lampu = Entity(model='3d/lamp.obj', collider='mesh')
lampu.position = (9, 0, 20)
lampu.scale = 0.005

# entitas lampu3
lampu = Entity(model='3d/lamp.obj', collider='mesh')
lampu.position = (9, 0, 0)
lampu.scale = 0.005

# entitas lampu4
lampu = Entity(model='3d/lamp.obj', collider='mesh')
lampu.position = (9, 0, -20)
lampu.scale = 0.005

# entitas lampu5
lampu = Entity(model='3d/lamp.obj', collider='mesh')
lampu.position = (9, 0, -50)
lampu.scale = 0.005

# entitas kursi1
kursi = Entity(model='3d/benchdua.obj', collider='mesh')
kursi.texture = 'Texture/kayu.jpg'
kursi.position = (50, 1, 20)
# entitas payung
payung = Entity(model='3d/umbrella.obj', collider='mesh')
payung.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna
payung.position = (50, 0, 21)
payung.scale = 0.05
payung.rotation_x = -90


# entitas kursi
kursi = Entity(model='3d/benchdua.obj', collider='mesh')
kursi.texture = 'Texture/kayu.jpg'
kursi.position = (50, 1, 40)
# entitas payung
payung = Entity(model='3d/umbrella.obj', collider='mesh')
payung.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna
payung.position = (50, 0, 41)
payung.scale = 0.05
payung.rotation_x = -90

# entitas kursi
kursi = Entity(model='3d/benchdua.obj', collider='mesh')
kursi.texture = 'Texture/kayu.jpg'
kursi.position = (50, 1, 60)
# entitas payung
payung = Entity(model='3d/umbrella.obj', collider='mesh')
payung.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna
payung.position = (50, 0, 61)
payung.scale = 0.05
payung.rotation_x = -90

# entitas kursi
kursi = Entity(model='3d/benchdua.obj', collider='mesh')
kursi.texture = 'Texture/kayu.jpg'
kursi.position = (50, 1, 80)
# entitas payung
payung = Entity(model='3d/umbrella.obj', collider='mesh')
payung.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna
payung.position = (50, 0, 81)
payung.scale = 0.05
payung.rotation_x = -90

# entitas kursi
kursi = Entity(model='3d/benchdua.obj', collider='mesh')
kursi.texture = 'Texture/kayu.jpg'
kursi.position = (50, 1, 0)
# entitas payung
payung = Entity(model='3d/umbrella.obj', collider='mesh')
payung.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna
payung.position = (50, 0, 1)
payung.scale = 0.05
payung.rotation_x = -90

# entitas kursi
kursi = Entity(model='3d/benchdua.obj', collider='mesh')
kursi.texture = 'Texture/kayu.jpg'
kursi.position = (50, 1, -20)
# entitas payung
payung = Entity(model='3d/umbrella.obj', collider='mesh')
payung.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna
payung.position = (50, 0, -19)
payung.scale = 0.05
payung.rotation_x = -90

# entitas kursi
kursi = Entity(model='3d/benchdua.obj', collider='mesh')
kursi.texture = 'Texture/kayu.jpg'
kursi.position = (50, 1, -40)
# entitas payung
payung = Entity(model='3d/umbrella.obj', collider='mesh')
payung.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna
payung.position = (50, 0, -39)
payung.scale = 0.05
payung.rotation_x = -90

# entitas kursi
kursi = Entity(model='3d/benchdua.obj', collider='mesh')
kursi.texture = 'Texture/kayu.jpg'
kursi.position = (50, 1, -60)
# entitas payung
payung = Entity(model='3d/umbrella.obj', collider='mesh')
payung.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna
payung.position = (50, 0, -59)
payung.scale = 0.05
payung.rotation_x = -90

# entitas kursi
kursi = Entity(model='3d/benchdua.obj', collider='mesh')
kursi.texture = 'Texture/kayu.jpg'
kursi.position = (50, 1, -80)
# entitas payung
payung = Entity(model='3d/umbrella.obj', collider='mesh')
payung.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna
payung.position = (50, 0, -79)
payung.scale = 0.05
payung.rotation_x = -90
# # entitas kursi
# kursi = Entity(model='3d/benchdua.obj', collider='mesh')
# kursi.texture = 'Texture/kayu.jpg'
# kursi.position = (55, 1, 0)

# kursi = Entity(model='3d/benchdua.obj', collider='mesh')
# kursi.texture = 'Texture/kayu.jpg'
# kursi.position = (50, 1, 0)

# kursi = Entity(model='3d/benchdua.obj', collider='mesh')
# kursi.texture = 'Texture/kayu.jpg'
# kursi.position = (50, 1, -10)

# kursi = Entity(model='3d/benchdua.obj', collider='mesh')
# kursi.texture = 'Texture/kayu.jpg'
# kursi.position = (55, 1, -10)

# kursi = Entity(model='3d/benchdua.obj', collider='mesh')
# kursi.texture = 'Texture/kayu.jpg'
# kursi.position = (55, 1, -20)


#untuk looping pohon
class Pohon(Entity):
    def __init__(self, position):
        super().__init__(
            model='3d/Tree.obj',
            collider='mesh',
            texture='Texture/tree.jpg',
            scale=0.5
        )
        self.position = position
        self.rotation_y = random.uniform(0, 360)  # Rotasi Y acak antara 0 dan 360

# Membuat 5 entitas Tree dengan posisi dan rotasi acak
pohon = []
for _ in range(10):
    x = random.uniform(30, 40)  # Posisi X acak antara -50 dan 50
    z = random.uniform(-75, 75)  # Posisi Z acak antara -50 dan 50
    pohon1 = Pohon(position=(x, 0, z))
    pohon.append(pohon1)

#looping pohon dengan asset yang berbeda
class Tree(Entity):
    def __init__(self, position):
        super().__init__(
            model='3d/palm_tree.obj',
            collider='mesh',
            texture='Texture/tree.jpg',
            scale=0.005
        )
        self.position = position
        self.rotation_y = random.uniform(0, 360)  # Rotasi Y acak antara 0 dan 360

# Membuat 5 entitas Tree dengan posisi dan rotasi acak
trees = []
for _ in range(5):
    x = random.uniform(50, 100)  # Posisi X acak antara -50 dan 50
    z = random.uniform(-50, 50)  # Posisi Z acak antara -50 dan 50
    tree = Tree(position=(x, 0, z))
    trees.append(tree)

# entitas gunung
gunung = Entity(model='3d/gunungs.obj', collider='mesh',
                color=color.rgb(194, 178, 128))
# gunung.texture = 'pasir.jpg'
gunung.position = (100, 0, 85)
gunung.scale = 5

# entitas papan seluncur
papan_seluncur = Entity(model='3d/surfer.obj', collider='mesh',
                        color=color.blue, highlight_color=color.green)
papan_seluncur.position = (100, 1.5, 50)
papan_seluncur.scale = 0.005

# rumah rumahan
rumah = Entity(model='3d/rumahpantai.obj', collider='mesh',texture='Texture/rumah_kayu.jpg')
rumah.position = (100, 0, -85)
rumah.scale = 1.5

# mercusuar
mercusuar = Entity(model='3d/mercusuar.obj', collider='box',texture='Texture/merah putih.jpg',texture_scale=(1,1))
mercusuar.position = (100, 0, -70)
mercusuar.scale = 3

# coconut
palm = Entity(model='3d/coconutpalm.obj', collider='mesh', texture='Texture/tree.jpg')
palm.position = (100, 0, -50)
palm.scale = 1

# mobil rusak
mobill = Entity(model='3d/mobil rusak.obj', collider='box')
mobill.position = (40, 0, -40)
mobill.scale = 1
mobill.rotation_y = 180
mobill.color = color.black

# stand makanan
stand = Entity(model='3d/stand.obj', collider='box',position=(25,-0.3,-40),texture='Texture/kayu.jpg')
stand.scale = 0.3
stand.rotation_y = 90

# stand makanan
stand = Entity(model='3d/Market Stall.obj', collider='box',position=(25,0,-30),texture='Texture/plank.png')
stand.scale = 3
stand.rotation_y = 90

# stand makanan
stand = Entity(model='3d/Market Stall.obj', collider='box',position=(25,0,-20),texture='Texture/plank.png')
stand.scale = 3
stand.rotation_y = 90

class Perahu(Entity):
    def __init__(self, model, position, speed):
        super().__init__(
            model=model,
            collider='mesh',
            position=position
        )
        self.speed = speed
        self.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))
        self.randomize_color()

        if model == model_perahu[0]:
            self.scale = 0.009
        elif model == model_perahu[1]:
            self.scale = 1

    def update(self):
        self.z += self.speed

        if self.z > boundary:
            self.z = -boundary
            self.randomize_color()
        if self.z < -boundary:
            self.z = boundary
            self.randomize_color()

    def randomize_color(self):
        self.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))

model_perahu = ['3d/perahu kayu viking.obj', '3d/perahu kayu.obj']
perahu1 = Perahu(model=random.choice(model_perahu), position=(190, 0, 50),speed=-0.5)
perahu2 = Perahu(model=random.choice(model_perahu), position=(200, 0, -50), speed=0.5)
perahu3 = Perahu(model=random.choice(model_perahu), position=(180, 0, 50),speed=-0.5)
perahu4 = Perahu(model=random.choice(model_perahu), position=(170, 0, -50), speed=0.5)

def update():
    perahu1.update()
    perahu2.update()
    perahu3.update()
    perahu4.update()

#fungsi untuk random Seluncur
class Seluncur(Entity):
    def __init__(self, position):
        super().__init__(
            model='3d/surfer.obj',
            collider='mesh',
            scale=0.005
        )
        self.position = position
        self.rotation_y = random.uniform(0, 360)  # Rotasi Y acak antara 0 dan 360
        self.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))  # Random warna


# Membuat 5 entitas Seluncur dengan posisi dan rotasi acak
Seluncuran = []
for _ in range(7):
    x = random.uniform(100, 120)  # Posisi X acak antara -50 dan 50
    z = random.uniform(-60, 60)  # Posisi Z acak antara -50 dan 50
    luncur = Seluncur(position=(x, 1.5, z))
    Seluncuran.append(luncur)




class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.initial_position = self.position
        self.prev_position = self.position
        self.is_jumping = False

    def update(self):
        if self.position.y < -10:
            self.position = self.initial_position

        super().update()

        # Memainkan suara berjalan saat karakter bergerak
        if self.position != self.prev_position:
            if not walk_sound.playing:
                walk_sound.play()
        else:
            walk_sound.stop()

        # Memainkan suara lompat saat karakter melompat
        if held_keys['space']:
            self.jump()

        self.prev_position = self.position


# untuk keluar dari game
def input(key):
    if key == 'escape':
        application.quit()

# Membuat suara berjalan
walk_sound = Audio("Sfx/walk.wav", loop=True, autoplay=False)

# Membuat suara lompat
jump_sound = Audio("Sfx/jump.wav", autoplay=False)

#membuat fungsi agar mobil looping
boundary = jalan_raya.scale_z / 2

speed = 0.5



class Mobil(Entity):
    def __init__(self, model, position, speed):
        super().__init__(
            model=model,
            collider='mesh',
            scale=1,
            position=position
        )
        self.speed = speed
        self.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))
        self.randomize_color()

        # if model == model_mobil[0]:
        #     self.rotation_y= 180
        # elif model == model_mobil[1]:
        #     self.rotation_y = -180

    def update(self):
        self.z += self.speed

        if self.z > boundary:
            self.z = -boundary
            self.randomize_color()
        if self.z < -boundary:
            self.z = boundary
            self.randomize_color()

    def randomize_color(self):
        self.color = color.rgb(random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))

model_mobil = ['3d/truck.obj', '3d/porsche.obj']
mobil1 = Mobil(model=random.choice(model_mobil), position=(-3, 1, 30),speed=-0.5)
mobil2 = Mobil(model=random.choice(model_mobil), position=(5, 1, -30), speed=0.5)

def update():
    mobil1.update()
    mobil2.update()

# Membuat objek FirstPersonController
player = Player()
player.position = (10, 0, 0)
player.rotation_y = 90
player.speed = 10

# Menjalankan aplikasi
app.run()
