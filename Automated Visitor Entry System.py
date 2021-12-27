def face():	
	import Face_Comparision as fr
	live_image=fr.load_image_file('person.jpeg')
	id_image=fr.load_image_file('id.jpeg')

	def detect_face(img,i):
	    img1=fr.face_locations(img,1,model='hog')
	    top=img1[0][0]
	    right=img1[0][1]
	    bottom=img1[0][2]  
	    left=img1[0][3]
	    face=img[top:bottom,left:right]
	    return face

	live=detect_face(live_image,1)
	id=detect_face(id_image,2)
	biden_encoding = fr.face_encodings(live)[0]
	unknown_encoding = fr.face_encodings(id)[0]
	results = fr.compare_faces([biden_encoding], unknown_encoding,.5)

	if results[0]:
	    print("Same Persons")
	else:
	    print("Different Persons")


def convert():
	import pytesseract

	f=open("recognized.txt","w+")
	f.truncate()

	pytesseract.pytesseract.tesseract_cmd = r'tesseract'
	f.write(pytesseract.image_to_string(r'id.jpeg'))
	f.close()

	g=open("recognized2.txt","w+")
	g.truncate()

	pytesseract.pytesseract.tesseract_cmd = r'tesseract'
	g.write(pytesseract.image_to_string(r'id2.jpeg'))
	g.close()
def extract():
	done=0
	with open('recognized.txt','r') as f:
	    
	    for line in f:
	        if ("INCOME" in line) or ("Income" in line) or ("income" in line) or ("NCOME" in line):
	            done=1
	            print("Pan Card")
	            count=0
	            br=0
	            for line in f:
	                if count==0:
	                    if (line[0]>='a' and line[0]<='z') or (line[0]>='A' and line[0]<='Z'):
	                        count=1
	                if count==1:
	                    print("Name: "+line)
	                    for line in f:
	                        if line[0]>='0' and line[0]<='9':
	                            print("Date: "+line[0:10])
	                            br=1
	                            break
	                if br==1:
	                    break
	            pan=0
	            for line in f:
	                if pan==0:
	                    if ("PERMANENT" in line) or ("Permanent" in line) or ("permanent" in line):
	                        pan=1
	                br1=0
	                if pan==1:
	                    for line in f:
	                        if (line[0]>='a' and line[0]<='z') or (line[0]>='A' and line[0]<='Z'):
	                            print("Pan no: "+line)
	                            br1=1
	                            break
	                if br1==1:
	                    break
	                        
	        if ("REPUBLIC" in line) or ("Republic" in line) or ("republic" in line):
	            done=1
	            print("Passport")
	            br=0
	            for line in f:
	                length=len(line)
	                i=0
	                while(i<length-7):
	                    if(line[i]>='a' and line[i]<='z') or (line[i]>='A' and line[i]<='Z'):
	                        flag=1
	                        for j in range(1,8):
	                            if(line[i+j]<'0') or (line[i+j]>'9'):
	                                flag=0
	                                break
	                        if(flag==1):
	                            print(line[i:i+8])
	                            br=1
	                            break
	                    i+=1
	                if br==1:
	                        break
	            br2=0
	            for line in f:
	                if ("INDIAN" in line) or ("indian" in line) or ("Indian" in line):
	                    length=len(line)
	                    i=0
	                    while(i<length-7):
	                        if(line[i]=='/'):
	                            print(line[i-2:i+8])
	                            br2=1
	                            break
	                        i+=1
	                if br2==1:
	                    break
	            br3=0
	            for line in f:
	                if "<" in line:
	                    length=len(line)
	                    i=0
	                    while(i<length-3):
	                        if(line[i]=='I' or line[i]=='i') and (line[i+1]=='N' or line[i+1]=='n') and (line[i+2]=='D' or line[i+2]=='d'):
	                            j=i+3
	                            while j<length:
	                                if(line[j]>='a' and line[j]<='z') or (line[j]>='A' and line[j]<='Z'):
	                                    k=j+1
	                                    while (line[k]>='a' and line[k]<='z') or (line[k]>='A' and line[k]<='Z'):
	                                        k+=1
	                                    p=k+1
	                                    while not((line[p]>='a' and line[p]<='z') or (line[p]>='A' and line[p]<='Z')):
	                                        p+=1
	                                    q=p+1
	                                    while (line[q]>='a' and line[q]<='z') or (line[q]>='A' and line[q]<='Z'):
	                                        q+=1
	                                    print(line[j:k])
	                                    print(line[p:q])
	                                    br3=1
	                                    break
	                                j+=1
	                        if br3==1:
	                            break
	                        i+=1
	                if br3==1:
	                    break
	        if("ELECTION" in line) or ("Election" in line) or ("election" in line):
	            done=1
	            print("Voter's Card")
	            br=0
	            for line in f:
	                if ("CARD" in line) or ("Card" in line) or ("card" in line):
	                    for line in f:
	                        if(len(line)>=10):
	                            print("Voter's Number: ",line)
	                            br=1
	                            break
	                if br==1:
	                    break
	            br2=0
	            for line in f:
	                if("Elector" in line) or ("ELECTOR" in line) or ("elector" in line):
	                    i=0
	                    length=len(line)
	                    while(i<length):
	                        if(line[i:i+4]=="Name") or (line[i:i+4]=="NAME") or (line[i:i+4]=="name"):
	                            print("Name: ",line[i+7:])
	                            br2=1
	                            break
	                        i+=1
	                if br2==1:
	                    break
	            for line in f:
	                i=0
	                length=len(line)
	                while(i<length-9):
	                    if(line[i]>="0" and line[i]<="9") and (line[i+1]>="0" and line[i+1]<="9") and (line[i+2]=="/") and (line[i+3]>="0" and line[i+3]<="9") and (line[i+4]>="0" and line[i+4]<="9") and (line[i+5]=="/"):
	                        print("DOB: ",line[i:i+10])
	                        break
	                    i+=1
	                    
	if done==0:
	    with open('recognized2.txt','r') as f2:
	        for line in f2:
	            if ("Unique Identification Authority" in line) or ("UNIQUE IDENTIFICATION AUTHORITY" in line) or ("unique identification authority" in line) or ("uidai" in line):
	                done=1
	                print("Aadhar")
	                with open('recognized.txt','r') as f:
	                    for line in f:
	                        if ("DOB" in line) or ("dob" in line) or ("DoB" in line) or ("Dob" in line) or ("doB" in line):
	                            print(line[-11:])
	                            break
	                    for line in f:
	                        if (len(line))>=14:
	                            cc=0
	                            i=0
	                            while i<len(line):
	                                if(line[i]>="0" and line[i]<="9"):
	                                    cc=cc+1
	                                i=i+1
	                            if(cc==12):
	                                print(line)
	                                break
	            if done==1:
	                break

face()
convert()
extract()