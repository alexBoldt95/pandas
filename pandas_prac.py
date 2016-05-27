import pandas as pd

def readandprocess(name):
    f = open(name)
    head = True
    container = []
    for line in f:
    	line = line.strip()
    	if head:
    		header = line.split(",")
    		head = False
    	else:
    		linelist = []
    		qlist = [] 
    		for i in range(len(line)):
    			if line[i] == '"':
    				qlist.append(i)
    		#print (line)
    		#print (qlist)
    		
    		if len(qlist) == 0:
    			linelist = line.split(",")
    		elif len(qlist) == 2:
    			if qlist[0]==0:
    				linelist.append(line[qlist[0]+1:qlist[1]])
    				linelist.extend(line[qlist[1]+2:].split(","))
    			else:
    				linelist.extend(line[:qlist[0]-1].split(","))
    				linelist.append(line[qlist[0]+1:qlist[1]])
    				linelist.extend(line[qlist[1]+2:].split(","))
    		else:
    			linelist.append(line[qlist[0]+1:qlist[1]])
    			linelist.extend(line[qlist[1]+2:qlist[2]-1].split(","))
    			linelist.append(line[qlist[2]+1:qlist[3]])
    			linelist.extend(line[qlist[3]+2:].split(","))
    		container.append(linelist)
    f.close()
    return container, header

def dataFrameEyeBall(container, header):


    df = pd.DataFrame(container, columns=header)
    print (df)

if __name__ == '__main__':
	c, h = readandprocess("9600movies.csv")
	dataFrameEyeBall(c,h)