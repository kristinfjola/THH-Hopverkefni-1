def bla(upphaed, n, v):
	temp = 0.0
	i = 0
	for i in range(1, n+1):
		temp = temp + (1+v)**i
	return 1.0*upphaed/temp