## Importing all the neccessary libraries
from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler
import pickle


app = Flask(__name__)
model = pickle.load(open('model3.pkl', 'rb'))     ## Importing model pickle file
scalar = pickle.load(open('SC.pkl', 'rb'))        ## Importing scalar pickle to perform scalar transformation


@app.route('/')
@app.route('/Try Again')
def home():
    return render_template('home.html')


    
@app.route('/predict', methods = ['POST'])
def predict():
    
    
    
    sc = StandardScaler()
    
    int_features = [ [float(x) for x in request.form.values()]]
    print(int_features)
    
    
    
    final_features = scalar.transform(int_features)
    
    
    prediction = model.predict(final_features)
   
    
    if prediction == 0:
         return render_template('result.html', result = 'The predicted value is 0, which means there is a possibility that payment will not default for the next month.')
    else:
         return render_template('result.html', result = 'The predicted value is 1, which means there is a possibility that payment will default for the next month.')
    
    
if __name__=='__main__':
    app.run(debug=True)