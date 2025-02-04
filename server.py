from flask import Flask, render_template, url_for, request, redirect #flask is a framework
import csv
app = Flask(__name__) #use the Flask class to instantiate an app #created an instance of our Flask app #the name of our app is __main__, basically
print(__name__) #this just means the main file we're running 

@app.route('/') #('/<username>/<int:post_id>') #this is a decorator #gives us extra tools to build a server #everytime we hit a /, do this...
def my_home(): #username=None, post_id=None #username equals the username that we receive
    return render_template('index.html') #pass on the variable #, name=username, post_id=post_id

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data): #a function that receives data
    with open('database.txt', mode='a') as database: #open database #append to that file
        email = data["email"] #telling where to find it
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject},{message}') 
        #new line everytime there's an entry
        # #writes what we want--email, subject, message 
        # #extracts from data that we passed in 


def write_to_csv(data): #have to use CSV module
    with open('database.csv', mode='a', newline='') as database2: #open csv file
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL) 
        #writing to the database with some options 
        # #delimiter makes it so each comma means a different column 
        # #don't say "file = " here #writes to our csv file
        csv_writer.writerow([email,subject,message]) #will contain the data we want


#request data that a client can send to the server

@app.route('/submit_form', methods=['POST', 'GET']) #get: browser wants us to send info #post: browser wants us to save info
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #access different parts of data #turns form into a dictionary for simplicity
            write_to_csv(data) #see write_to_csv function
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again.' #transfer data to Visual Studios!





























#@app.route('/about.html') #Links to 'Learn More'???
#def about(about):
 #  return f'About: {about}'

#@app.route('/learnmore.html') 
#def learn_link(learn):
 #   return f'Learn: {learn}'

#accept different URL parameters
#@app.route('/<string:page_name>')
#def html_page(page_name): #as input
 #   return render_template('about.html') #render data that was in the URL



#now we have multiple routes
#@app.route('/shop') 
#def blog():
 #   return 'Shop New Releases'

#@app.route('/discussions') 
#def blog2():
 #   return 'Join the Discussion Forum'


#for HTML: <!-- web\ server/Scripts/activate.bat -->
#static files: files like JS and CSS, where, once we send them out, they rarely get changed.
#use in Command Prompt: set FLASK_APP=server.py
#then use: python -m flask run
#http://127.0.0.1:5000
#turn on debugger mode: set FLASK_DEBUG=1

#if deletes, do this!!!
#set FLASK_APP=main.py
#$env:FLASK_APP = "main.py"
#flask run