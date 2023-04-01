from flask import Flask,url_for,render_template,redirect,request,flash,redirect,session
# import sqlite3 as SQL
app = Flask(__name__)
# import tensorflow as tf
from tensorflow import keras
import cv2
# import matplotlib.pyplot as plt
import numpy as np
# import matplotlib.image as mpimg
import os


app.secret_key="Rudy"

# from keras.applications.vgg16 import preprocess_input,VGG16
global graph
UPLOAD_FOLDER = 'static/uploader/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
SIZE = 120

import sqlite3

@app.route('/',methods=['POST','GET'])
def register():
    
    msg="Register successfully"
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        
       
        
        table_name = 'reg'
        conn = sqlite3.connect("reg.db")
        c = conn.cursor()
        c.execute('create table if not exists ' + table_name + ' (name varchar(50),email varchar(50),username varchar(50),password varchar(50))')
        c.execute('insert into '+table_name+'  values (?,?,?,?)',(name,email,username,password))
        conn.commit()
        conn.close()
        flash("Register successfully")
        return render_template('login.html',msg=msg)
    else:
        return render_template('register.html')


@app.route('/login',methods=["GET","POST"])
def login():
    username=None
    password=None
    err="Invalid username and password"
    if request.method=='POST':
        session['username']=request.form['username']
        session['vid']=request.form['password']
        username=request.form['username']
        password=request.form['password']
        conn = sqlite3.connect("reg.db")
        r=conn.cursor()
        r.execute("select name,password,email from reg where name=? and password=?",(username,password))
        rows=r.fetchall()
        print(rows)
        if len(rows)!=0:
            for i in rows:
                

                if i[0]==username and i[1]==password:
                    return redirect(url_for('userpage'))
                    #return render_template('user.html',username=username)
                else:
                    return render_template('login.html',err=err)
        else:
            return render_template('index.html',err=err)
    return render_template('login.html')

@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/upload',methods =['POST','GET']  )
def Upload():
    raph=""
    i=""
    if request.method == 'POST':
        file = request.files['image']
        print(file) 
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],'1.png'))
        
        model = keras.models.load_model(r'D:\alzheimer-stage-classifier-master\model\model2.h5')
        categories = ["NonDemented", "MildDemented", "ModerateDemented", "VeryMildDemented"]

        nimage = cv2.imread(r"D:\alzheimer-stage-classifier-master\static\uploader\1.png", cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(nimage,(SIZE,SIZE))
        image = image/255.0
        prediction = model.predict(np.array(image).reshape(-1,SIZE,SIZE,1))
        pclass = np.argmax(prediction)
        va=categories[int(pclass)]
        pValue = "Predict: {0}".format(categories[int(pclass)])
        print(pValue)
        if(va=='NonDemented'):
            raph='Non-Alzheimer’s dementias remain relatively unknown and often poorly diagnosed. More research is needed, not only for effective pharmacological interventions with disease-modifying effects, but also better differential diagnostic techniques to ensure the proper management and care of patients. A Series of three papers summarises the most common non-Alzheimer’s disorders that cause dementia: frontotemporal, Lewy body, and vascular.'
            i="static/non.png"
        elif(va=='MildDemented'):
            raph="In the mild dementia stage, people may experience: Memory loss of recent events. Individuals may have an especially hard time remembering newly learned information and ask the same question over and over. Difficulty with problem-solving, complex tasks and sound judgments."
            i="static/moderate.png"
        elif(va=='ModerateDemented'):
            raph="During the moderate dementia stage of Alzheimer's disease, people grow more confused and forgetful and begin to need more help with daily activities and self-care. People with the moderate dementia stage of Alzheimer's disease may: Show increasingly poor judgment and deepening confusion."
            i="static/mild.png"
        elif(va=='VeryMildDemented'):
            raph="Patient is in the first stage of alzeimer"
            i="static/verymild.png"
        realvalue = "Real Value 1"
        print('success')
        img = "/uploader/1.png"
        print(i)
        return render_template('result.html',value=pValue,graph=raph,i=i)

    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)