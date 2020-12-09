import os

os.chdir("..")
basedir=os.getcwd()

class Exercise:
    def __init__(self):
        self.description=None
        self.heading=None
        self.subheading=None
        self.image=None
        self.command=None

class Shoulder(Exercise):
    def __init__(self):
        super().__init__()
        self.description='''Lie on the bemch wiht a dumbbell in each hand and your feet flat on the floor.
        You can rest your feet up on the bench if it's more comfortable.Push the dumbbells up so that your arms
        are directly over your shoulders and your palms are up. Pull your abdominals in, and tilt your chin 
        toward your chest.Lower the dumbbells down and a little to the side until your elbows are slightly
        below your shoulders.4.Roll your Shoulder blades back and down, like you're pinching them together
        and accentuating your chest.Push the weights back up, taking care to lock your elbows or allow your shoulder
        blades to rise off the bench.'''

        self.heading="Shoulder"
        self.subheading="Shoulder Press"
        self.image="shoulderpress"
        self.command="python "+basedir+"\\statusbar_webcam.py --camera=./videos/dumbbell_press.mp4 --model=mobilenet_v2_large --exercise=shoulder"

class Bicep(Exercise):
    def __init__(self):
        super().__init__()
        self.description='''Take 2 dumbbells. Stand with you rlegs should with apart, bend your knees slightly.
        Let your arms to hand down with your palms facing each other.Move only your forearms, slowly curl the dumbbells
        up to shoulder level. Turn your palms up when they pass your thighs. Keep your elbows pressed against your sides
        throughout the exercise.'''

        self.heading='Bicep'
        self.subheading="Bicep Curl"
        self.image='bicepcurl'
        self.command="python "+basedir+"\\statusbar_webcam.py --model=mobilenet_v2_large --camera=./videos/bicepcurl.mp4 --exercise=bicep"

class Tricep(Exercise):
    def __init__(self):
        super().__init__()
        self.description='''Using a cable machine raise the pulley above your head, user the bar. Set your feet width apart,
        tuck our wlbows in and lean forward.Now move your hands up and down in a complete range of motion and make sure keep
        your hands in tight with your body.'''

        self.heading='Tricep'
        self.subheading='Pulley Push Down'
        self.image='triceppush'
        self.command="python "+basedir+"\\statusbar_webcam.py --model=mobilenet_v2_large --camera=./videos/pulley_push_down.mp4 --exercise=tricep"