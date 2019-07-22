from guihelper import GUIhelper
from dbhelper import DBhelper

class Tinder(GUIhelper):
    def __init__(self):
        self.db=DBhelper()
        super(Tinder, self).__init__(self.login, self.load_reg_Window)

    def login(self):
        if self._emailInput.get()=="" or self._passwordInput.get()=="":
            self.label2.configure(text="Please fill both the fields",bg="yellow",fg="red")
        else:
            if '@' not in self._emailInput.get():
                self.label2.configure(text="Email input invalid",bg="yellow",fg="red")
            else:
                data=self.db.search('email',self._emailInput.get(),'password',self._passwordInput.get(),'users')


                if len(data)==1:
                    self.sessionId=data[0][0]
                    self.loadProfile()
                else:
                    self.label2.configure(text="Login Failed",bg="red", fg="white")



    def load_reg_Window(self):
        self.regWindow(self.handleRegistration)

    def handleRegistration(self):
        if self._emailInput.get() == "" or self._passwordInput.get()=="" or self._nameInput.get()=="" or self._cityInput.get()=="" or self._genderInput.get()=="" or self._ageInput.get()=="":
            self.label2.configure(text="Please fill all the fields", bg="yellow", fg="red")
        else:
            if len(self._passwordInput.get())<6:
                self.label2.configure(text="Password should be greater than 6 chars", bg="yellow", fg="red")
            else:
                regDict={}
                regDict['user_id']="NULL"
                regDict['name']=self._nameInput.get()
                regDict['email']=self._emailInput.get()
                regDict['password']=self._passwordInput.get()
                regDict['age']=self._ageInput.get()
                regDict['gender']=self._genderInput.get()
                regDict['city']=self._cityInput.get()
                response=self.db.insert(regDict, 'users')

                if response==1:
                    self.label2.configure(text="Registration Successful", bg="white", fg="green")
                else:
                    self.label2.configure(text="Registration Failed", bg="yellow", fg="red")

    def loadProfile(self):
        data=self.db.searchOne('user_id',self.sessionId,'users','LIKE')
        self.mainWindow(self,data,mode=1)

    def viewProfile(self,num):
        data=self.db.searchOne('user_id',self.sessionId,'users','NOT LIKE')
        if num==0:
            self.mainWindow(self, data, mode=2, num=num)
        if num<0:
            self.massage("error","hobe naa")
        if num>len(data)-1:
            self.massage("error", "hobe naa")
        else:
            new_data=[]
            new_data.append(data[num])
            self.mainWindow(self,new_data,mode=2,num=num)

    def propose(self,juliet_id):
        data=self.db.search('romeo_id',str(self.sessionId),'juliet_id',str(juliet_id),'proposals')
        if len(data)==0:

            propDict={}
            propDict['romeo_id']=str(self.sessionId)
            propDict['juliet_id']=str(juliet_id)
            self.db.insert(propDict,'proposals')

            if response==1:
                self.massage("Congrets","proposal send sucessfully.Finger Crossed")

            else:
                self.message("Error","proposal faield.Try Again")
        else:
            self.message("Error","Despo sala")
obj=Tinder()