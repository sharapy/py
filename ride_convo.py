try:
	data = open('convo.txt')

	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			print role+'said:'+line_spoken,
			#print line_spoken
		except ValueError:
			pass
	data.close()
except IOError:
	print "The data file is missing!"