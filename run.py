import platform

arch = platform.architecture()[0]
if arch == "64bit":
	import Twofactor
else:
	print(" [x] Your Device is Not Supported!");
