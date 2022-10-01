from flask import Flask,render_template,request,send_file,send_from_directory,url_for
import cv2 as cv
from flask_uploads import UploadSet , IMAGES,configure_uploads
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import SubmitField
from flask_wtf import FlaskForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ANKSHR'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos',IMAGES)
configure_uploads(app,photos)

class UploadForm(FlaskForm):
    photo = FileField(
        validators=[
            FileAllowed(photos,'Only images are allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit = SubmitField('Upload')

@app.route('/upload/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'],filename)



@app.route("/",methods=['GET','POST'])
def Upload_image():
    #return "<p>Hello, World!</p>"
    form = UploadForm() 
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file',filename=filename)
        print(file_url)
    else :
        file_url = None
    return render_template('index.html',form=form,file_url=file_url)    
            






@app.route('/download')
def download():
    path = 'samplefile.pdf'
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
