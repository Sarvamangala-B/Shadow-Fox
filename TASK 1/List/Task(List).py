# Initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial team:", justice_league)

# 1. Number of members
print("Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding new members:", justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman as leader:", justice_league)

# 4. Separate Aquaman and Flash with Green Lantern
index_flash = justice_league.index("Flash")
justice_league.insert(index_flash, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)

# 5. Replace with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

# 6. Sort alphabetically
justice_league.sort()
print("Sorted team:", justice_league)
print("New leader:", justice_league[0])  # BONUS answer
