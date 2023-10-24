from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class nlp:

    def __init__(self):
        self.dbo=Database()
        self.apio=API()
        self.root=Tk()
        self.root.title('NLPAPP')
        #self.root.configure(bg='red')
        self.login_gui()
        self.root.mainloop()


    def login_gui(self):
        self.clear()


        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 24, 'bold'))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10))

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 24, 'bold'))

        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(10, 10))

        login_btn = Button(self.root, text='Login', width=30, height=2,command=self.perform_login)
        login_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Name')
        label1.pack(pady=(10, 10))
        label1.configure(font=('verdana', 24, 'bold'))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10))

        label2 = Label(self.root, text='Enter Email')
        label2.pack(pady=(10, 10))
        label2.configure(font=('verdana', 24, 'bold'))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(10, 10))

        label3 = Label(self.root, text='Enter Password')
        label3.pack(pady=(10, 10))
        label3.configure(font=('verdana', 24, 'bold'))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(10, 10))

        register_btn = Button(self.root, text='Register', width=30, height=2,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label4 = Label(self.root, text='Already a member?')
        label4.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def perform_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        response=self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success','registration succesful.you can login now')

        else:
            messagebox.showinfo('Error','Email Already Exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success','login successful')
            self.home_gui()

        else:
            messagebox.showinfo('Error','Incorrect email/password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='sentiment analysis',command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition',command=self.ner_gui)
        ner_btn.pack(pady=(30, 30))

        emotion_btn = Button(self.root, text='Emotion Prediction',command=self.emotion_gui)
        emotion_btn.pack(pady=(30, 30))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(30, 30))

    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(30, 30))
        heading2.configure(font=('verdana', 24, 'bold'))

        label = Label(self.root, text='Enter the text')
        label.pack(pady=(20, 10))

        self.text_input = Entry(self.root, width=50)
        self.text_input.pack(pady=(10, 10))

        analyze_btn = Button(self.root, text='Analyze',command=self.do_sentiment_analysis)
        analyze_btn.pack(pady=(30, 30))

        self.sentiment_result = Label(self.root, text='',fg='red')
        self.sentiment_result.pack(pady=(20, 10))
        self.sentiment_result.configure(font=('verdana', 24, 'bold'))

        goback_btn = Button(self.root, text='Go back',command=self.home_gui)
        goback_btn.pack(pady=(30, 30))

    def do_sentiment_analysis(self):
        text=self.text_input.get()
        response=self.apio.sentiment(text)
        print(response)
        result=sorted(response['sentiment'].items(),key=lambda x:x[1],reverse=True)[0][0]
        print(result)
        self.sentiment_result['text']=result


    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#34495E', fg='white')
        heading2.pack(pady=(30, 30))
        heading2.configure(font=('verdana', 24, 'bold'))

        label = Label(self.root, text='Enter the text')
        label.pack(pady=(20, 10))

        self.text_input = Entry(self.root, width=50)
        self.text_input.pack(pady=(10, 10))

        analyze_btn = Button(self.root, text='Analyze',command=self.do_ner)
        analyze_btn.pack(pady=(30, 30))

        self.ner_result = Label(self.root, text='',fg='red')
        self.ner_result.pack(pady=(20, 10))
        self.ner_result.configure(font=('verdana', 24, 'bold'))

        goback_btn = Button(self.root, text='Go back',command=self.home_gui)
        goback_btn.pack(pady=(30, 30))


    def do_ner(self):
        text=self.text_input.get()
        result=self.apio.ner(text)
        print(result)
        self.ner_result['text']=result['entities']

    def emotion_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(30, 30))
        heading2.configure(font=('verdana', 24, 'bold'))

        label = Label(self.root, text='Enter the text')
        label.pack(pady=(20, 10))

        self.text_input = Entry(self.root, width=50)
        self.text_input.pack(pady=(10, 10))

        analyze_btn = Button(self.root, text='Analyze', command=self.do_emotion)
        analyze_btn.pack(pady=(30, 30))

        self.emotion_result = Label(self.root, text='',fg='red')
        self.emotion_result.pack(pady=(20, 10))
        self.emotion_result.configure(font=('verdana', 24, 'bold'))

        goback_btn = Button(self.root, text='Go back', command=self.home_gui)
        goback_btn.pack(pady=(30, 30))

    def do_emotion(self):
        text=self.text_input.get()
        result=self.apio.emotion(text)
        print(result)

        result = sorted(result['emotion'].items(), key=lambda x: x[1], reverse=True)[0][0]

        self.emotion_result['text'] = result

    def clear(self):

        for i in self.root.pack_slaves():
            i.destroy()






nl=nlp()