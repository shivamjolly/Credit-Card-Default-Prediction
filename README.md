# Credit-Card-Default-Prediction

This project predicts whether there will be a default in payments or not for the next month based on parameters.

## Table of contents

- [Demo](https://github.com/shivamjolly/Credit-Card-Default-Prediction#demo)
- [Installation](https://github.com/shivamjolly/Credit-Card-Default-Prediction#installation)
- [Deployement](https://github.com/shivamjolly/Credit-Card-Default-Prediction#deployement)
- [Directory Tree](https://github.com/shivamjolly/Credit-Card-Default-Prediction#directory-tree)
- [Technologies Used](https://github.com/shivamjolly/Credit-Card-Default-Prediction#technologies-used)
- [About Pickle files](https://github.com/shivamjolly/Credit-Card-Default-Prediction#about-pickle-files)
- [Future Scope](https://github.com/shivamjolly/Credit-Card-Default-Prediction#future-scope)

## Demo
Link: https://creditdefaultprediction-api.herokuapp.com/

<img src="Credit_default.gif" width="75%" height="50%"/>

## Installation

I have built this whole project using Python version 3.8.10. So, My advice is to install Python if you did not, and if you are using a lower version, upgrade it using the pip package. Lastly, After cloning the repositories, install the required packages and libraries from the following command.

```bash
  pip install -r requirements.txt
```
## Deployement

This project is deployed on Heroku. First, you need to create your account on Heroku, then connect to your Github Account and click on deploy manually.

[<img width = '500px' src = 'https://camo.githubusercontent.com/065f065d12a6ba6b2cfcff767aaafd438a7ed5ae615e3ac39051c022cebaa698/68747470733a2f2f63646e2e776f726c64766563746f726c6f676f2e636f6d2f6c6f676f732f6865726f6b752d312e737667' />](https://www.heroku.com/home)


## Directory Tree

```bash
├── static 
│   ├── styles.css
├── template
│   ├── home.html
│   ├── result.html
├── Credit_Card_code.ipynb
├── Credit_default.gif
├── Procfile
├── README.md
├── SC.pkl
├── UCI_Credit_Card.csv
├── app.py
├── model3.pkl
├── requirements.txt

```
  
## Technologies used

<img src = 'https://camo.githubusercontent.com/3cdf9577401a2c7dceac655bbd37fb2f3ee273a457bf1f2169c602fb80ca56f8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667'>

[<img alighn = 'left' width = '200px' src = 'https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png' />](https://flask.palletsprojects.com/en/2.0.x/)
[<img alighn = 'left' width = '300px' src = 'https://gunicorn.org/images/logo.jpg' />](https://gunicorn.org/)
[<img alighn = 'left' width = '300px' src = 'https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png' />](https://scikit-learn.org/stable/)


## About Pickle Files

Model3.pkl: As I have implemented many models in my code, as you will see in the jupyter notebook, I have selected model3 the best to perform.

SC.pkl: This pickle file is for scaling, as I have implemented Standard Scalar on my dataset. The purpose of this pickle file is to scale the input taken from the form to that based on training set parameters.

## Future Scope
- Try different models and increase the performance of the model.
- Front - end can be better.
- Optimize the codes.




