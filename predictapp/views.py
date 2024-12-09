from django.shortcuts import render,HttpResponse

import os
import joblib
import re
import nltk
#import sklearn
nltk.download('stopwords')


# Use the correct path to the model file
model = joblib.load('static/trained_model_rf.joblib')

# Create your views here.

def index(request):
    #return HttpResponse("This is home page")
    return render(request, 'index.html')

def visualizations(request):
    return render(request, 'visualizations.html')

def prediction(request):
    return render(request, 'prediction.html')

def template(request):
    return render(request, 'template.html')

# Function to clean tweets
def clean_tweet(tweet):
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet)  # Remove URLs
    tweet = re.sub(r'[^A-Za-z0-9 ]+', '', tweet)  # Remove special characters
    return tweet.lower()  # Convert to lowercase

# View for prediction
def predict_tweet(request):
    result = None
    if request.method == "POST":
        tweet = request.POST.get('tweet')
        if tweet:
            try:
                # Load the trained model
                model = joblib.load('static/trained_model_rf.joblib')
                cleaned_tweet = clean_tweet(tweet)
                prediction = model.predict([cleaned_tweet])[0]
                result = "🚨 Disaster Tweet" if prediction == 1 else "✅ Non-Disaster Tweet"
            except Exception as e:
                result = f"Error: {e}"
    return render(request, 'template.html', {'result': result})
