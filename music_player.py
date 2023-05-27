from playsound import playsound
print("no.of available song \n1.Butter\n2.Fairytale\n3.HenryJackman\n4.likeyou\n5.RahogiMeri")
order = input("enter the music which you wantto play:") 
if "Butter" in order :
    playsound("C:\\Users\\Bhushan kakde\\OneDrive\\Desktop\\music b\\Butter.mp3")
elif "Fairytale" in order:
    playsound("C:\\Users\\Bhushan kakde\\OneDrive\\Desktop\\music b\\Fairytale.mp3")
elif "HenryJackman" in order:
    playsound("C:\\Users\\Bhushan kakde\\OneDrive\\Desktop\\music b\\HenryJackman.mp3")
elif "likeyou" in order:
    playsound("C:\\Users\\Bhushan kakde\\OneDrive\\Desktop\music b\\likeyou.mp3")
elif "RahogiMeri" in order:
    playsound("C:\\Users\\Bhushan kakde\\OneDrive\\Desktop\\music b\\RahogiMeri.mp3")