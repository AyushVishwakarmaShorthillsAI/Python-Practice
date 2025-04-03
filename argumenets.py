# Parameter Vs Arguments
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that are sent to the function when it is called.
# parameter => inside fun def
# agrumnets => send while calling

## various types of arguments are there
# 1. Default arguments

def f(points=100, ans=True):
    if(ans == False):
        print("Default variable changed")
        print("The value of points had been doubled")
        points*=2
        print(f"the value of points is : {points}")
    else:
        print("deaful value of points not invoked")
        print("points not doubled")
        print(points)


# both arguments given
f(28, True)
f(28, False)

print()
# second function call with all default parameter used
f()

print()
# only one argument given
f(9)

# -----------------------------------------------------
# keyword argument

hekdi_nikalne_wale_dialogues = [
    "Bhai, tujhe dekh ke lagta hai confidence aur overconfidence ka koi beech ka level bhi hota hai!",
    "Bhai tujhe dekh ke lagta hai, duniya waise nahi chalti jaise tu soch raha hai, balki jaise sab soch rahe hain, waise tu chal raha hai!",
    "Tera attitude dekh ke lagta hai, teri aukaat aur sapne ek hi jagah nahi rehte!",
    "Bhai, tu itna udta kyu hai? Air India ka pilot hai kya?",
    "Are bhai bhai bhai, zara dheere bol, yahan tere fan nahi hain, bas dost hain!",
    "Bhai, agar overconfidence se sapne poore hote na, toh tu Elon Musk ka boss hota!",
    "Tere jaise log motivation ki kitaabein padte hain, lekin apply nahin karte!",
    "Bhai, tera swag aur reality ek baar aamne saamne mil le, dono ko shock lagega!",
    "Tu soch raha hoga ki tu cool lag raha hai, magar asal mein hum sab tera stand-up comedy dekh rahe hain!",
    "Zyada uda mat bhai, warna log sochenge ki tu Red Bull pi ke paida hua hai!"
]

import random

dark_roast_dialogues = [
    "Bhai, tujhe dekh ke lagta hai ki life me ek undo button hona chahiye… takki tere jaise log **by mistake** exist na karein! 🚫💀 Matlab jo confidence tu leke ghoom raha hai, woh ek aise future ke liye hai jo **kabhi aane wala hi nahi!** 😆🔮",
    
    "Tu itna overconfident hai ki agar Titanic chalane ka chance milta, toh tu **'iceberg kya hota hai?'** bolke seedha cruise ko uske andar le jaata! 🚢💥 Matlab bhai, thoda chill kar… nahi toh ek din tera attitude bhi teri reality se **collision** maar lega! 😆❄️",
    
    "Tera logic aur WiFi signal ek jaise hi hain… **2 step door hote hi kaam karna band!** 📶🚫 Matlab dimaag bhi aise chal raha hai jaise **Nokia 3310 pe YouTube chalane ki koshish ho rahi ho!** Ek baar try kar, shayad reboot hone se thoda upgrade ho jaye! 🤖⚡",
    
    "Bhai, tujhe lagta hai log tujhe dekh ke impress hote hain? 😂 Sorry bro, reality yeh hai ki **log tujhe dekh ke bas mute button dhoondte hain!** 🔇 Matlab itna **filterless version of overconfidence** dekha hai ki ek baar toh duniya bhi soche, 'Bhai, ye auto-generated NPC hai ya real banda?' 🤡🎭",
    
    "Bhai, tu itna slow process kar raha hai ki lagta hai **Pentium 1 processor** pe chal raha hai! 🖥️ Matlab agar tere brain ko RAM upgrade milta, toh bhi tu ek WhatsApp message likhne me **5 minute** le leta! 🐢💨 Koi Ctrl+Alt+Delete daba de yaar, system hang ho gaya hai! 🤣🔄",
    
    "Tu itna ud raha hai ki lagta hai **Red Bull ka overdose le liya hai!** 🪽😂 Bro, ek baat bata, kya tujhe sach me lagta hai ki log tere charm se attract hote hain? **Ya sirf teri bekar baaton se bore hoke neend aati hai?** 😴💀",
    
    "Tere logic ka bhi ek alag hi level hai… Matlab agar tu history likhta toh Titanic Iceberg se **takrata nahi, usse dosti kar leta!** 🚢❄️ Bhai, thoda soch, nahi toh log samjhenge **tera dimaag trial version pe chal raha hai!** 🤖🚫",
    
    "Bhai, agar attitude se success milti na, toh tu **Google ka founder hota!** 🤡 Reality check le, warna log tujhe motivational speaker nahi, **comedy show ka host** samajhne lagenge! 🎤😂",
    
    "Bhai, tera dimaag **dark mode** pe permanently chala gaya hai ya bus duniya ki light tujhe nazar nahi aa rahi?** 🌑 Matlab itna overconfidence hai ki lagta hai ek din apne khud ke hi shadow se takra ke gir jayega! 🤦‍♂️💥",
    
    "Tu itna overhyped hai ki lagta hai tera dimaag bhi **Marvel ki multiverse theory** me atak gaya hai! 🌌😂 Bhai, **reality me aa ja, nahi toh ek din tera ego bhi tujhse zyada intelligent niklega!** 🧠🔥"
]

# Random savage roast print karne ke liye:
# Random dark roast print karne ke liye:
# print(random.choice(dark_roast_dialogues))


# Random dialogue print karne ke liye:
import random
# print(random.choice(hekdi_nikalne_wale_dialogues))

def jawab(hekdiNikale=True, dostKaNaam='Kittu', darkKrun=True):
    if hekdiNikale==False:
        print("aur bhai kaisa hai")
    
    print(f"Aur mere dost ye lo khatarnak reply, {dostKaNaam} bura lge to aur bhi hai :)")
    if(darkKrun):
        print(random.choice(dark_roast_dialogues))
    else:
        print(random.choice(hekdi_nikalne_wale_dialogues))


hekdiNikalniHai=input('hekdi nikalu ya normal rhoge ? : ')
dostKaNaam=input('dost ka shubh naam : ')
darkRoast=input('drak roast krna hai')

jawab(hekdiNikalniHai, dostKaNaam, darkRoast)

# here generally the user will not enter anything, but bcoz of default the function will work

#------------------------------------------------------------------------------------------------------------

# Keyword arguments
# the arguments(passed on calling fn) that can have their names

def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')

#-----------------------------------------------------------------------------------------
# Arbitrary arguments : when we do not know in advance the number of argumentsn == *arg

# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)


# ------------------------------------------------------------------------------------------
# *Args and **Kwarrgs
# Both of them allow funcitons to accept an arbitrary number of arguments

# *args example
def fun(*args):
    return sum(args)

print(fun(1, 2, 3, 4)) 
print(fun(5, 10, 15))   


# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)


#NOTE : '*' makes the variable passed to function as iterable
# args are for non-keyword arguments 
# kwargs are for keyword arguments

#Note : the name of 'agrv' or kwargv' are not that important -> can change their names

# Using both Args and Kwargs
def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

fun(1, 2, 3, a=4, b=5)
