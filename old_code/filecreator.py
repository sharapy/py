
fh1 = open("trial.txt", "w")

i = 0
t = 10
while i <= t:
	fh1.writelines("Sharad bought Royal Enfield Thunderbird 350 on 26 September 2014\n")
	i = i + 1
fh1.close()
