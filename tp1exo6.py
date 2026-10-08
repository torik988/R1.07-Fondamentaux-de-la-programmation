sec=int(input("nombre de secondes: "))
jour= (sec // 86400)
sec = sec % 86400
heure= (sec // 3600)
sec= sec % 3600
minute= (sec// 60)

print(f"{jour} jour(s), {heure} heure(s), {minute} minute(s)")