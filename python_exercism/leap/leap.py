import calendar

def is_leap_year(date):
	if date%400 == 0:
		return True
	if date%100 == 0:
		return False
	if date%4 == 0:
		return True
	return False
