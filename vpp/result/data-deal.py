

class Data:
        def __init__(self, speed, trans, retr, cwnd):
                self.speed = speed
                self.trans = trans
                self.retr = retr
                self.cwnd = cwnd
	def show(self):
		return "\t".join([str(self.speed), str(self.trans), str(self.retr), str(self.cwnd)])

def fetchDataFromFile(filename):
	result = []
	fin = open(filename, 'r')
	for line in fin:
		b = ""
		while len(b) != len(line):
			b = line
			line = line.replace("  "," ")	
		l = line.split(" ")
		if len(l) == 12:
			speed = float(l[6])
			trans = float(l[4])
			if trans < 2:
				trans *= 1000
			retr = int(l[8])
			cwnd = float(l[9])
			if cwnd < 2:
				cwnd *= 1000		
			result.append(Data(speed, trans, retr, cwnd))
	fin.close()
	return result

infile = raw_input()
result = fetchDataFromFile(infile)


#outfile = infile + "-out"
#fout = open(outfile, 'w')
#for data in result:
#	print >> fout, data.show()

from numpy import *
import matplotlib
import matplotlib.pyplot as plt
width = 1
f1 = plt.figure(1)
ax1 = f1.add_subplot(221)
ax1.set_title("Speed")
ax1.scatter([i for i in range(len(result)/width)], [result[i*width].speed for i in range(len(result)/width)],s=1,marker='.')
ax1.set_ylabel("Gb/s")

ax2 = f1.add_subplot(222)
ax2.set_title("Trans")
ax2.scatter([i for i in range(len(result)/width)], [result[i*width].trans for i in range(len(result)/width)],s=1,marker='.')
ax2.set_ylabel("MB")

ax3 = f1.add_subplot(223)
ax3.set_title("Retr")
ax3.scatter([i for i in range(len(result)/width)], [result[i*width].retr for i in range(len(result)/width)],s=1,marker='.')


ax4 = f1.add_subplot(224)
ax4.set_title("Cwnd")
ax4.scatter([i for i in range(len(result)/width)], [result[i*width].cwnd for i in range(len(result)/width)],s=1,marker='.')
ax4.set_ylabel("KB")

plt.show()
