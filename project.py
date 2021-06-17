import datetime
import time 
import wikipedia 
import webbrowser
from multiprocessing import Process

          
class userinput():        
    def time(self):
        
        hour = int(datetime.datetime.now().hour)
            
        if hour >= 0 and hour < 12:
                print("Good Morning Sir")
       
        elif hour >= 12 and hour<18:
            print("Good Afternoon Sir")
        
        else:
            print("Good Evening Sir")

    def r_write(self, text, file_name):
        reminder_file = open(file_name , "w")
        reminder_content = reminder_file.write(text)
        print("\nYour file is Written into ",file_name)

    def r_read(self, file_name):
        reminder_file = open(file_name, "r")
        reminder_content = reminder_file.read()
        reminder_file.close()
        reminder =  reminder_content
        return reminder
    
    def r_append(self, extra, file_name):
        reminder_file = open(file_name, "a")
        file = reminder_file.write(extra)
        reminder_file.close()
        print("Append complete")
    
    def reminder(self, file_name, remember, timer):
        reminder = self.r_write(remember, file_name)
        timer = timer * 60 #Doing this because python sleep function only works in seconds so need to convert to mintues
        print("Reminder started")
        time.sleep(timer)
        print(self.r_read(file_name))   
        print("Reminder alert!...check reminder Sir")
        

        
    def chat_main(self):
        while True:
            query_of_user = input("Please enter what you'd like me to do?")
            query_of_user.lower() 
            if 'wikipedia' in query_of_user:
                ask_user = input("Sir I have two options..would you like to search or open the website? Open/search")
                if ask_user.lower() == "open wikipedia":
                    operator = webbrowser.get()
                    operator.open("https://en.wikipedia.org/wiki/Main_Page")
                elif ask_user.lower() == "search":
                    results = input("What would you like to search?")
                    print("Searching Wikipedia...")
                    results = wikipedia.search(results)
                    query_of_user = query_of_user.replace("","")
                    print("According to Wikipedia")
                    print(results)
        
            elif 'open youtube' in query_of_user:
                operator = webbrowser.get()
                operator.open("https://www.youtube.com")

            elif 'open google' in query_of_user:
                operator = webbrowser.get()
                operator.open("https://www.google.com")

            elif 'open stackoverflow' in query_of_user:
                operator = webbrowser.get()
                operator.open("https://www.stackoverflow.com")

            elif "the time" in query_of_user:
                thetime = datetime.datetime.now()
                print("Sir the time is currently...{}".format(thetime))
                
            elif 'reminder' in query_of_user:
                new_ask_user = input("Would you like to be reminded of someting? Y/N")
                if new_ask_user.lower() == "y":
                    file_name = input("What do you want to be reminded and the filename?")
                    remember = input("What would you like to be reminded about Sir?")
                    timer = float(input("In how many mintues should I remind you Sir?"))
                    remind_process = Process(target=self.reminder, args=(file_name, remember, timer))
                    remind_process.start()
                    print("Reminder process Started")
                time.sleep(0.3)
                ask_user = input("Would you like to Read/Write/Append the file Sir? Read/Write/Append")    
                if ask_user.lower() == "read":
                    file_name = str(input("What should the File name be?"))
                    remind = self.r_read(file_name)
                    print(remind)
                elif ask_user.lower() == "append":
                    extra = str(input("What do you want to add?"))
                    file_name = str(input("What should the File name be?"))
                    self.r_append(extra, file_name)
                elif ask_user.lower() == "write":
                    text = str(input("What do you want to be reminded of?"))
                    file_name = str(input("What should the File name be?"))
                    self.r_write(text,file_name)
                else:
                    continue

            
            elif 'notepad' in query_of_user:
                notesobj = open("notepad.txt" , "w") 
                print("Please enter if you'd like to write in the file")
                notesobj.write(input())
                notesobj.close()
                print("Success")
                ask_user = input("Would you like to read/write to that file Sir? Read/append")
                if ask_user.lower() == "read":
                    notesobj = open("notepad.txt", "r")
                    print(notesobj.read())
                elif ask_user.lower() == "append":
                    notesobj = open("notepad.txt", "a")
                    notesobj = open("notepad.txt", "a")
                    print("please write what you'd like to say sir")
                    notesobj.write(input())
                    notesobj.close() 
                ask_user = input("Would you like to create another file sir? Y/N")
                if ask_user.lower() == "y":
                    notesobj = opepn("notepad1.txt" , "w")
                    print("What would you like to write sir?")
                    notesobj.write(input())
                    notesobj.close()
                    print("Success")
                    ask_user = input("Would like to read/append that file sir? Read/Append")
                    if ask_user.lower() == "read":
                        notesobj = open("notepad1.txt", "r")
                    elif ask_user.lower() == "append":
                        print("please write what you'd like to say sir")
                        notesobj = open("notepad1.txt", "a")
                        notesobj.write(input())
                        notesobj.close() 
                elif ask_user.lower() == "n":
                    continue
                    
            
            elif 'open spotify' in query_of_user:
                operator = webbrowser.get()
                operator.open("https://www.spotify.com/uk/")
            
            elif 'exit' in query_of_user:
                print("Sure no problem Sir, goodbye")
                break
            
            else:
                print("Sorry please try again Sir.")
                

        


if __name__ == "__main__":
    print("""
    
    Please choose from the following options Sir:
    
    -----Wikipedia
    ----Notepad
    ----reminders
    ----Spotify
    ----the time
    ----the stackoverflow
    ----google
    ----youtube
    ----exit
    """
         )
    thread_one = userinput()
    thread_one.chat_main()
