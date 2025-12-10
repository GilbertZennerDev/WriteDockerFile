"""
the purpose is to generate a working Dockerfile based on inputs
I just load the Dockerfile and save it with new content
"""
import sys

def getStuff(ac, av, symbol):
	return [av[i] for i in range(2, ac, 2) if av[i - 1] == symbol and '-' not in av[i]]

def getCondition(ac, av):
	return getStuff(ac, av, '-condition')

def getFiles(ac, av):
	return getStuff(ac, av, '-f')

def getFrom(ac, av):
	return getStuff(ac, av, '-from')

def FROM(src):
	if src == "": src = "python:3.12-slim"
	return f"FROM {src}\n"

def WORKDIR():
	return f"WORKDIR /app\n"

def COPY(src):
	return f'COPY {src} /app/\n'

def COPYFILES(files):
	return "".join(COPY(f) for f in files)
	
def CMD(who, dest):
	return f'CMD [{who}, {dest}]\n'

def composeDockerFile(files, from_):
	return FROM(from_) + WORKDIR() + COPYFILES(files) + COPY("entry.sh") + CMD("\"sh\"", "\"entry.sh\"")
	
def writeDockerFile(content):
	try: open("Dockerfile", "w"). write(content)
	except Exception as e: print(e); exit()

def main():
	av = sys.argv
	ac = len(av)
	if ac < 2: print("Add at least a file with -f filename"); exit()
	from_ = getFrom(ac, av)
	files = getFiles(ac, av)
	writeDockerFile(composeDockerFile(files, ""))
	print("DONE writing Dockerfile")
	
if __name__ == '__main__': main()
