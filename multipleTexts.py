'''
	multipleTexts allows the user to send multiple text messages of the same string.
    Copyright (C) 2013 Wesley A. Bowman

    This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA


This program was written to send one string of text as numerous text messages through a gmail account.
THIS REQUIRES A GMAIL ACCOUNT FOR THIS TO WORK.
Also make sure there is a providers file in the same folder as gmail.py and annoy.py
The information needed for the providers.txt file can be found at:
https://en.wikipedia.org/wiki/List_of_SMS_gateways

An example of the format of the providers.txt:
att=@txt.att.net

To correctly use the GUI, just hit enter after you have filled in the text box. After enter is pressed on the last text box,
the program will run, and once it is finished the GUI will close. 
'''

#imports needed for mail()
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#imports needed for the GUI
import wx

#setting up variables
userItems=[]
items=[]
userInfo=[]
service={}

class getUserData(wx.Frame):
    """ Get the information to send a text """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300,300))
        
        menuBar=wx.MenuBar()
        first=wx.Menu()
        second=wx.Menu()
        
        first.Append(wx.NewId(),'New Window','This is a new Window')
        first.Append(wx.NewId(),'Open...','This opens a new menu')
        
        menuBar.Append(first,'File')
        menuBar.Append(second,'Edit')
        
        self.SetMenuBar(menuBar)
        

        #Close window when X is pressed
        self.Bind(wx.EVT_CLOSE, self.closewindow)
        
        # create the main sizer
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        # Add a panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)

        self.lbls = ["Number:", "Provider:", "Number of text to be sent:","Message:"]
        for lbl in self.lbls:
            self.buildLayout(lbl)
        self.panel.SetSizer(self.mainSizer)
           
        self.Center()   #Centers the window
        self.Show()
        
    def closewindow(self, event):
        self.Destroy()

    def buildLayout(self, text):
        """"""
        lblSize = (160,-1)
        lbl = wx.StaticText(self.panel, label=text, size=lblSize)
        self.text=text
        txt = wx.TextCtrl(self.panel,style=wx.TE_PROCESS_ENTER)
        txt.Bind(wx.EVT_TEXT_ENTER, self.txtControl, txt)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(lbl, 0, wx.ALL|wx.ALIGN_LEFT, 5)
        sizer.Add(txt, 0, wx.ALL, 5)
        self.mainSizer.Add(sizer)
    
    def txtControl(self,event):
        item=event.GetString()
        items.append(item)
        
        if len(items)==4:
                        
            try:
                service[items[1]]
            except KeyError:
                print "No such service provider in file"
            
            #defining the variables to make them easier to work with
            number=int(items[0])
            provider=str(items[1])
            count=int(items[2])
            message=str(items[3])
            
            email='%d%s' %(number,service[provider])
            
            for i in range(0,count,1):
                #userInfo is the username and password, which is set in readInFiles()
                mail(userInfo[0],userInfo[1],email,"",message)
            
            self.Close()
            
        else:
            event.EventObject.Navigate()

class getUserEmail(wx.Frame):
        """ If it's the first time running the program, get the username and password"""
        def __init__(self, parent, title):
            wx.Frame.__init__(self, parent, title=title, size=(300,300))
              
            #Close window when X is pressed
            self.Bind(wx.EVT_CLOSE, self.closewindow)
            
            # create the main sizer
            self.mainSizer = wx.BoxSizer(wx.VERTICAL)
    
            # Add a panel so it looks the correct on all platforms
            self.panel = wx.Panel(self, wx.ID_ANY)
    
            self.lbls = ["Username:", "Password:"]
            for lbl in self.lbls:
                self.buildLayout(lbl)
            self.panel.SetSizer(self.mainSizer)
               
            self.Center()   #Centers the window
            self.Show()
        
        def closewindow(self, event):
            self.Destroy()

        def buildLayout(self, text):
            lblSize = (160,-1)
            lbl = wx.StaticText(self.panel, label=text, size=lblSize)
            self.text=text
            txt = wx.TextCtrl(self.panel,style=wx.TE_PROCESS_ENTER)
            txt.Bind(wx.EVT_TEXT_ENTER, self.txtControl, txt)
    
            sizer = wx.BoxSizer(wx.HORIZONTAL)
            sizer.Add(lbl, 0, wx.ALL|wx.ALIGN_LEFT, 5)
            sizer.Add(txt, 0, wx.ALL, 5)
            self.mainSizer.Add(sizer)
    
        def txtControl(self,event):
            item=event.GetString()
            userItems.append(item)
            event.EventObject.Navigate()
            if len(userItems)==2:
                userItems[0]='%s@gmail.com' %(userItems[0],)
                with open("username.txt",'w') as f:
                    for item in userItems:
                        f.write("%s\n" %(str(item),))
                    
                self.Close()

def mail(gmail_user,gmail_pwd,to, subject, text):
    '''I did not write this portion of the program. I found it online some time ago and made modifications to suite my needs.
    The original code can be found here:
    http://kutuma.blogspot.ca/2007/08/sending-emails-via-gmail-with-python.html
    
    '''
    
    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text))
    
       
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()

def readInFiles():
    '''Read in the service providers information and the username and password'''
    #List of some service providers listed as a dictionary
    with open("providers.txt", 'r') as f:
        for line in f:
            k, v = line.strip().split('=')
            service[k.strip()] = v.strip()
    
    with open("username.txt",'r') as f:
        for line in f:
            userInfo.append(line)
    
def makeUserFile():
    '''If there is no file called username.txt, then this will make one, prompting for a username and password '''
    app=wx.App()
    getUserEmail(None,'Username and Password')
    app.MainLoop()

def main():
    ''' Main loop for sending the text '''
    app=wx.App()
    getUserData(None,'Annoy those who annoy you')
    app.MainLoop()

if __name__=='__main__':
    
    # Tries to read in the providers, username, and password.
    try:
        readInFiles()
    # If there is no username.txt, it will make one then read it in. This should only have to run the first time you run the program.
    except IOError:
        makeUserFile()
        readInFiles()
    # Now that the program has all the information about your email, it will ask about the text message details.
    main()
