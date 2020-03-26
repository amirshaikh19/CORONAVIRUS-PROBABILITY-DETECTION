from flask import Flask,render_template,request
app = Flask(__name__)

import pickle

file = open('model.pk1','rb')
clf=pickle.load(file)
file.close()

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        fever = int(myDict['Fever'])
        age = int(myDict['Age'])
        pain = int(myDict['Pain'])
        runnyNose = int(myDict['Runny Nose'])
        diffBreath = int(myDict['Difficulty in Breathing'])
        inputFeatures = [fever,pain,age,runnyNose,diffBreath] #sample data checking
        infProb= clf.predict_proba([inputFeatures])[0][1]
        print(infProb)
    #return "Hello World!" + str(infProb)
        return render_template('show.html',inf=round(infProb*100))
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)