# Given a positive number of seconds, convert it into a string in the format "hh:mm:ss"

def make_readable(seconds):
    hours = int(seconds / 3600)
    seconds %= 3600
    minutes = int(seconds/60)
    seconds %= 60
    return "{:0>2d}:{:0>2d}:{:0>2d}".format(hours, minutes, seconds)


print(make_readable(3600))
