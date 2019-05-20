#!/usr/bin/env python
#copyrighted by RemsFlems.
import base64,sys,os;
e2=10;e3=4;e4=60
inputf=open(sys.argv[1],'rb');
tm=os.stat(sys.argv[1]).st_size
try:
	e2=int(sys.argv[2])
	e3=int(sys.argv[3])
	e4=int(sys.argv[4])
except:
	pass
rs="";bs=1;rsb=[];fd=0;ts=0;
os.system('clear')
print "Base64 pattern finder"

def main(rs,bs,rsb,fd,ts,inputf,e2,e3,e4):
	tu=0
	sys.stdout.write("\r[Found]:"+str(fd)+" [Trusts]:"+str(ts)+" [Progress]:"+str(round(float(tu)/tm*100,4))+"%")
	sys.stdout.flush()
	while 1:
		try:
			a=inputf.read(10000)
			if not a:
				sys.stdout.write("\r[Found]:"+str(fd)+" [Trusts]:"+str(ts)+" [Progress]:"+str(round(float(tu)/tm*100,4))+"%")
				displayer(rs,rsb,e2);
				sys.exit();
			sz=len(a);
			tu=tu+sz
			for t in xrange(e4,e3,-1):
				for s in range(sz-t):
					try:
						dcd=base64.b64decode(a[s:s+t]);rcd=base64.b64encode(dcd)
						ai=''.join([x if ord(x)<128 else '?' for x in dcd])
						if rcd==a[s:s+t] and '?' not in ai and isinstance(dcd, str):
							e=0
							for i,c in enumerate(rsb):
								if ai in c:
									e=1
									ts=ts+1
								if c in ai:
									e=2
									rsb[i]=ai
									if len(ai) > bs:
										bs=len(ai);
										rs=ai
							if e==0:
								fd=fd+1
								rsb.append(ai)
								if len(ai) > bs:
										bs=len(ai);
										rs=ai
						
					except KeyboardInterrupt: 
						displayer(rs,rsb,e2);
						sys.exit();
					except:
						pass
				sys.stdout.write("\r[Found]:"+str(fd)+" [Trusts]:"+str(ts)+" [Progress]:"+str(round(float(tu)/tm*100,4))+"%")
				sys.stdout.flush()
		except KeyboardInterrupt: 
			sys.stdout.write("\r[Found]:"+str(fd)+" [Trusts]:"+str(ts)+" [Progress]:"+str(round(float(tu)/tm*100,4))+"%")
			displayer(rs,rsb,e2);
			sys.exit();

def displayer(rs,rsb,e2):
	print "\n[MOST PROBABLE]: ["+rs.replace("\n","\\n")+"]";
	rsb.sort(lambda x,y: cmp(len(y),len(x)))
	try: 
		rk=int(e2)
	except: rk=15;
	o=[v.replace("\n","\\n")+"]" for v in rsb[:rk] if v!=rs]; 
	exec("for p in o: print '[other]: ['+str(p)", locals(),globals())

main(rs,bs,rsb,fd,ts,inputf,e2,e3,e4)
sys.exit()

