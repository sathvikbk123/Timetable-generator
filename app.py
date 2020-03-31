from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import random

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'),Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql=MySQL(app)

def timetableGenerator():
	subject={
    1:{"name":"os","Theory":3,"Lab":0,"Total":3,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
    2:{"name":"dbms","Theory":3,"Lab":1,"Total":4,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
    3:{"name":"cn","Theory":4,"Lab":0,"Total":4,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
    4:{"name":"java","Theory":3,"Lab":0,"Total":3,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
    5:{"name":"ai","Theory":3,"Lab":0,"Total":3,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
    6:{"name":"ipr","Theory":2,"Lab":0,"Total":2,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
    7:{"name":"dbmslab","Theory":0,"Lab":1,"Total":1,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
    8:{"name":"cnlab","Theory":0,"Lab":1,"Total":1,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
    9:{"name":"javalab","Theory":0,"Lab":1,"Total":1,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False}
	};

	subject1={
	    11:{"name":"os","Theory":3,"Lab":0,"Total":3,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    12:{"name":"dbms","Theory":3,"Lab":1,"Total":4,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    13:{"name":"cn","Theory":4,"Lab":0,"Total":4,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    14:{"name":"java","Theory":3,"Lab":0,"Total":3,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    15:{"name":"ai","Theory":3,"Lab":0,"Total":3,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    16:{"name":"ipr","Theory":2,"Lab":0,"Total":2,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    17:{"name":"dbmslab","Theory":0,"Lab":1,"Total":1,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    18:{"name":"cnlab","Theory":0,"Lab":1,"Total":1,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    19:{"name":"javalab","Theory":0,"Lab":1,"Total":1,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False}
	};

	subject2={
	    21:{"name":"os","Theory":3,"Lab":0,"Total":3,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    22:{"name":"dbms","Theory":3,"Lab":1,"Total":4,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    23:{"name":"cn","Theory":4,"Lab":0,"Total":4,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    24:{"name":"java","Theory":3,"Lab":0,"Total":3,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    25:{"name":"ai","Theory":3,"Lab":0,"Total":3,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    26:{"name":"ipr","Theory":2,"Lab":0,"Total":2,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    27:{"name":"dbmslab","Theory":0,"Lab":1,"Total":1,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    28:{"name":"cnlab","Theory":0,"Lab":1,"Total":1,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False},
	    29:{"name":"javalab","Theory":0,"Lab":1,"Total":1,"TheoryAllotted":0,"LabAllotted":0,"TotalAllotted":0,"Skip":False}
	};

	teacher={
	    1:"Vandana Sudhakar Sardar",
	    2:"Aparna R.",
	    3:"Sanjeetha R.",
	    4:"Hanumantha Raju R.",
	    5:"Mr. Shreekant Jere",
	    6:"Dr. Jagadish S. Kallimani",
	    7:"Bheemappa Halavar",
	    8:"Dr. Shilpa Shashikant Chaudhari",
	    9:"Dr. Geetha J.",
	    11:"Chandrika Prasad",
	    12:"Mrs. Sini Anna Alex",
	    13:"Meeradevi A. K.",
	    14:"Pramod Sunagar",
	    15:"Sowmya B. J.",
	    #16:"jag",
	    17:"shreen",
	    #18:"hmr",
	    19:"Dr. T.N.R.Kumar",
	    #21:"chan",
	    22:"Mamatha Jadhav V",
	    #23:"shil",
	    24:"Dr. S. Rajarajeswari",
	    #25:"soum",
	    #26:"tnr"
	    #27:"maharaj",
	    #28:"geeta"
	    #29:vand
	};


	# In[6]:


	takes={
	    1:1,
	    2:2,
	    3:3,
	    4:4,
	    5:5,
	    6:6,
	    7:7,
	    8:8,
	    9:9,
	    11:11,
	    12:12,
	    13:13,
	    14:14,
	    15:15,
	    16:6,
	    17:17,
	    18:4,
	    19:19,
	    21:11,
	    22:22,
	    23:9,
	    24:24,
	    25:15,
	    26:19,
	    27:11,
	    28:9,
	    29:1
	};


	# In[7]:


	class5a={
	    1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	    2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	    3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	    4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	    5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	    6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	};
	class5b={
	    1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	    2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	    3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	    4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	    5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	    6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	};
	class5c={
	    1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	    2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	    3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	    4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	    5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	    6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	};


	# In[8]:


	teachertimetable={
	    1:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    2:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    3:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    4:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    5:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    6:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    7:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    8:{
	       1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    9:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    11:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    12:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    13:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    14:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    15:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    17:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    19:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    22:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    },
	    24:{
	        1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	        2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	        3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	        4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	        5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	        6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	    }
	 #   27:{
	 #       1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	 #       2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	 #       3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	 #       4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	 #       5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	 #       6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	 #   },
	 #   28:{
	 #       1:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Monday"},
	 #       2:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Tuesday"},
	 #       3:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Wednesday"},
	 #       4:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Thursday"},
	 #       5:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Friday"},
	 #       6:{1:"nil",2:"nil",3:"nil",4:"nil",5:"nil",6:"nil",7:"nil","day":"Saturday"}
	  #  }
	}


	# In[9]:


	def getteacherforsubject(i):
	    return takes[i]


	# In[10]:


	def getfreeperiod(class5,x):
	    for i in range(1,8):
	        if class5[x][i]=="nil":
	            return (x,i)
	    return (0,0)


	# In[11]:


	def isteacherfree(teacheris,day,period):
	    if teachertimetable[teacheris][day][period]=="nil":
	        return True
	    else:
	        return False


	# In[12]:


	def issubjectonday(class5,subject,day):
	    for i in range(1,8):
	        if class5[day][i]==subject:
	            return True
	    return False


	# In[13]:


	def generate(class5,subject,sec):
	    i=0
	    j=1
	    #flag=(subject[1]["Skip"]==False or subject[2]["Skip"]==False or subject[3]["Skip"]==False or subject[4]["Skip"]==False or subject[5]["Skip"]==False or subject[6]["Skip"]==False or subject[7]["Skip"]==False or subject[8]["Skip"]==False or subject[9]["Skip"]==False)
	    flag=False
	    while(flag==False):
	        i=i+1
	        i=i%9
	        if i==0:
	            i=9
	        if(sec=="class5b"):
	            i=i+10
	        elif(sec=="class5c"):
	            i=i+20
	        if (subject[i]["Skip"]==False):
	            if (subject[i]["TotalAllotted"]!=subject[i]["Total"]):
	                if (subject[i]["TheoryAllotted"]!=subject[i]["Theory"]):
	                    teacheris=getteacherforsubject(i)
	                    #newly added to find a random day
	                    daylist=[1,2,3,4,5,6]
	                    templist=[]
	                    count=0
	                    subname=subject[i]["name"]
	                    while(True):
	                        count=count+1
	                        var1=random.choice(list(set(daylist)-set(templist)))
	                        (day,period)=getfreeperiod(class5,var1)
	                        if day==0:
	                            templist.append(var1)
	                        else:
	                            break
	                        if count==10:
	                            print("Something went wrong..")
	                            exit(0)
	                    #(day,period)=getfreeperiod(random.choice([1,2,3,4,5,6]))
	                    if issubjectonday(class5,subname,day)==True:
	                        continue
	                    teacherfree=isteacherfree(teacheris,day,period)
	                    if (teacherfree==True):
	                        class5[day][period]=subject[i]["name"]
	                        teachertimetable[teacheris][day][period]=sec
	                        subject[i]["TheoryAllotted"]+=1
	                        subject[i]["TotalAllotted"]+=1
	                        if (subject[i]["TotalAllotted"]==subject[i]["Total"]):
	                            subject[i]["Skip"]=True
	                elif (subject[i]["LabAllotted"]!=subject[i]["Lab"]):
	                    teacheris=getteacherforsubject(i)
	                    #newly added to find a random day
	                    daylist=[1,2,3,4,5,6]
	                    templist=[]
	                    count=0
	                    subname=subject[i]["name"]
	                    while(True):
	                        count=count+1
	                        var1=random.choice(list(set(daylist)-set(templist)))
	                        (day,period)=getfreeperiod(class5,var1)
	                        if day==0:
	                            templist.append(var1)
	                        else:
	                            break
	                        if count==10:
	                            print("Something went wrong..")
	                            exit(0)
	                    #(day,period)=getfreeperiod(random.choice([1,2,3,4,5,6]))
	                    if issubjectonday(class5,subname,day)==True:
	                        continue
	                    if period!=2 and period!=4 and period!=7:
	                        teacherfree1=isteacherfree(teacheris,day,period)
	                        teacherfree2=isteacherfree(teacheris,day,period+1)
	                        if (teacherfree1==True and teacherfree2==True):
	                            class5[day][period]=subject[i]["name"]
	                            class5[day][period+1]=subject[i]["name"]
	                            teachertimetable[teacheris][day][period]=sec
	                            teachertimetable[teacheris][day][period+1]=sec
	                            subject[i]["LabAllotted"]+=1
	                            subject[i]["TotalAllotted"]+=1
	                            if (subject[i]["TotalAllotted"]==subject[i]["Total"]):
	                                subject[i]["Skip"]=True

	        if(sec=="class5b"):
	            i=i-10
	        elif(sec=="class5c"):
	            i=i-20
	        j=j+1
	        flag=True
	        for z in range(1,10):
	            if(sec=="class5b"):
	                z=z+10
	            elif(sec=="class5c"):
	                z=z+20
	            if (subject[z]["Skip"]==False):
	                flag=False
	        if (j==100000):
	            break


	# In[14]:


	generate(class5a,subject,"class5a")


	# In[15]:


	generate(class5b,subject1,"class5b")


	# In[16]:


	generate(class5c,subject2,"class5c")


	# In[17]:


	#print(class5a)
	x=1
	while(x<=6):
	    print(class5a[x])
	    x+=1
	    
	print("----\n\n")

	#print(class5a)
	x=1
	while(x<=6):
	    print(class5b[x])
	    x+=1
	print("----\n\n")
	#print(class5a)
	x=1
	while(x<=6):
	    print(class5c[x])
	    x+=1
	print("----\n\n")    

	x=1
	for i in teachertimetable:
	    print(teacher[i])
	    while (x<=6):
	        print(teachertimetable[i][x])
	        x=x+1
	    print("---")
	    x=1


	# In[18]:


	sqlqueries=[]

	teacheridlist=[]
	for i in takes.values():
	    if i not in teacheridlist:
	        teacheridlist.append(i)

	sqlqueries.append("DROP TABLE if exists class5a")
	sqlqueries.append("DROP TABLE if exists class5b")
	sqlqueries.append("DROP TABLE if exists class5c")
	sqlqueries.append("CREATE TABLE if not exists class5a( `1` varchar(100), `2` varchar(100), `3` varchar(100), `4` varchar(100), `5` varchar(100), `6` varchar(100), `7` varchar(100), `day`  varchar(100))")
	sqlqueries.append("CREATE TABLE if not exists class5b( `1` varchar(100), `2` varchar(100), `3` varchar(100), `4` varchar(100), `5` varchar(100), `6` varchar(100), `7` varchar(100), `day`  varchar(100))")
	sqlqueries.append("CREATE TABLE if not exists class5c( `1` varchar(100), `2` varchar(100), `3` varchar(100), `4` varchar(100), `5` varchar(100), `6` varchar(100), `7` varchar(100), `day`  varchar(100))")
	    
	for i in teacheridlist:
		sql="DROP TABLE if exists teacher"+str(i);sqlqueries.append(sql)
		sql="CREATE TABLE if not exists teacher"+str(i)+"( `1` varchar(100), `2` varchar(100), `3` varchar(100), `4` varchar(100), `5` varchar(100), `6` varchar(100), `7` varchar(100), `day`  varchar(100))"
		sqlqueries.append(sql)


	for mydict in class5a:
	    #placeholders = ', '.join(['%s'] * len(class5a[mydict]))
	    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in class5a[mydict].keys())
	    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in class5a[mydict].values())
	    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('class5a', columns, values)
	    sqlqueries.append(sql)
	    #print(sql)
	#print()
	for mydict in class5b:
	    #placeholders = ', '.join(['%s'] * len(class5b[mydict]))
	    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in class5b[mydict].keys())
	    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in class5b[mydict].values())
	    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('class5b', columns, values)
	    sqlqueries.append(sql)
	    #print(sql)
	#print()
	for mydict in class5c:
	    #placeholders = ', '.join(['%s'] * len(class5c[mydict]))
	    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in class5c[mydict].keys())
	    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in class5c[mydict].values())
	    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('class5c', columns, values)
	    sqlqueries.append(sql)
	    #print(sql)
	#print()

	for id in teachertimetable:
	    for mydict in teachertimetable[id]:
	        #placeholders = ', '.join(['%s'] * len(teachertimetable[id][mydict]))
	        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in teachertimetable[id][mydict].keys())
	        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in teachertimetable[id][mydict].values())
	        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ("teacher"+str(id), columns, values)
	        sqlqueries.append(sql)
	        #print(sql)
	    #print()
	return sqlqueries


@app.route('/', methods=['GET', 'POST'])
def index():
	sqlqueries = timetableGenerator()
	cur = mysql.connection.cursor()
	for i in sqlqueries:
		cur.execute(i)
		mysql.connection.commit()
	cur.close()
	return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
	if request.method == 'POST':
		formoutput = request.form
		choice = formoutput['choice']
		if choice == 'teacher':
			#Blah
			print('bllahha')
			return redirect('/teachers')
		else:
			#Blah
			print('blah')
			return redirect('/classes')
	
	return render_template('generate.html')


@app.route('/classes')
def classes():
	cur1 = mysql.connection.cursor()
	resultValue1 = cur1.execute("SELECT * FROM class5a")
	cur2 = mysql.connection.cursor()
	resultValue2 = cur2.execute("SELECT * FROM class5b")
	cur3 = mysql.connection.cursor()
	resultValue3 = cur3.execute("SELECT * FROM class5c")
	class_TT_5a = cur1.fetchall()
	class_TT_5b = cur2.fetchall()
	class_TT_5c = cur3.fetchall()
	return render_template('classes.html', class_TT_5a=class_TT_5a, class_TT_5b=class_TT_5b, class_TT_5c=class_TT_5c)


@app.route('/teachers')
def teachers():
	cur1 = mysql.connection.cursor()
	resultValue1 = cur1.execute("SELECT * FROM teacher1")

	cur2 = mysql.connection.cursor()
	resultValue2 = cur2.execute("SELECT * FROM teacher2")
	
	cur3 = mysql.connection.cursor()
	resultValue3 = cur3.execute("SELECT * FROM teacher3")
	
	cur4 = mysql.connection.cursor()
	resultValue4 = cur4.execute("SELECT * FROM teacher4")
	
	cur5 = mysql.connection.cursor()
	resultValue5 = cur5.execute("SELECT * FROM teacher5")
	
	cur6 = mysql.connection.cursor()
	resultValue6 = cur6.execute("SELECT * FROM teacher6")
	
	cur7 = mysql.connection.cursor()
	resultValue7 = cur7.execute("SELECT * FROM teacher7")
	
	cur8 = mysql.connection.cursor()
	resultValue8 = cur8.execute("SELECT * FROM teacher8")
	
	cur9 = mysql.connection.cursor()
	resultValue9 = cur9.execute("SELECT * FROM teacher9")
	
	cur11 = mysql.connection.cursor()
	resultValue11 = cur11.execute("SELECT * FROM teacher11")
	
	cur12 = mysql.connection.cursor()
	resultValue12 = cur12.execute("SELECT * FROM teacher12")
	
	cur13 = mysql.connection.cursor()
	resultValue13 = cur13.execute("SELECT * FROM teacher13")

	cur14 = mysql.connection.cursor()
	resultValue14 = cur14.execute("SELECT * FROM teacher14")

	cur15 = mysql.connection.cursor()
	resultValue15 = cur15.execute("SELECT * FROM teacher15")
	
	cur17 = mysql.connection.cursor()
	resultValue17 = cur17.execute("SELECT * FROM teacher17")
	
	cur19 = mysql.connection.cursor()
	resultValue19 = cur19.execute("SELECT * FROM teacher19")
	
	cur22 = mysql.connection.cursor()
	resultValue22 = cur22.execute("SELECT * FROM teacher22")
	
	cur24 = mysql.connection.cursor()
	resultValue24 = cur24.execute("SELECT * FROM teacher24")
	
	teacher_TT_1 = cur1.fetchall()
	teacher_TT_2 = cur2.fetchall()
	teacher_TT_3 = cur3.fetchall()
	teacher_TT_4 = cur4.fetchall()
	teacher_TT_5 = cur5.fetchall()
	teacher_TT_6 = cur6.fetchall()
	teacher_TT_7 = cur7.fetchall()
	teacher_TT_8 = cur8.fetchall()
	teacher_TT_9 = cur9.fetchall()
	teacher_TT_11 = cur11.fetchall()
	teacher_TT_12 = cur12.fetchall()
	teacher_TT_13 = cur13.fetchall()

	teacher_TT_14 = cur14.fetchall()
	teacher_TT_15 = cur15.fetchall()
	teacher_TT_17 = cur17.fetchall()

	teacher_TT_19 = cur19.fetchall()
	teacher_TT_22 = cur22.fetchall()
	teacher_TT_24 = cur24.fetchall()
	return render_template('teachers.html', teacher_TT_1=teacher_TT_1, teacher_TT_2=teacher_TT_2,
							 teacher_TT_3=teacher_TT_3, teacher_TT_4=teacher_TT_4, teacher_TT_5=teacher_TT_5,
							  teacher_TT_6=teacher_TT_6, teacher_TT_7=teacher_TT_7, teacher_TT_8=teacher_TT_8,
							   teacher_TT_9=teacher_TT_9, teacher_TT_11=teacher_TT_11, teacher_TT_12=teacher_TT_12,
							    teacher_TT_13=teacher_TT_13, teacher_TT_14=teacher_TT_14, teacher_TT_15=teacher_TT_15,
							     teacher_TT_17=teacher_TT_17, teacher_TT_19=teacher_TT_19, teacher_TT_22=teacher_TT_22,
							       teacher_TT_24=teacher_TT_24)

@app.route('/nmit_test')
def nmit_test():
    value=0.6933
    return render_template('temp_nmit.html',value=value)

if __name__ == '__main__':
    app.run(debug=True)