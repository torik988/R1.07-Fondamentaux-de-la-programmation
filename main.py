jour, heure, minute = int(input("Jour:")), int(input("Heure:")), int(input("Minute:"))

sec_finale= (minute*60 + heure * 3600 + jour*86400)
print(sec_finale)