from flask import Flask, flash, request, redirect, url_for, render_template
import os
import urllib.request
import main
app=Flask(__name__)
UPLOAD_FOLDER='static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
        if 'files' not in request.files:
	        return redirect(request.url)
        file=request.files['files']
        if file.filename=="":
            return redirect(request.url)
        filename=file.filename
        loc="static/uploads/"+filename
        #print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        output=main.execute(loc)
        return render_template('landing.html',filename=filename,output=output)
    else:
        return render_template("landing.html")
@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__=="__main__":
    app.run(debug=True)

