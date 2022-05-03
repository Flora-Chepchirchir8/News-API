from flask import render_template
from app import app
from .request import get_source,get_articles,get_articles_headlines,get_articles_by_category

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news=get_source('general')
    

    articles_news = get_articles('general')
      # get articles from bbc-news
    bbc_news = get_articles_headlines('bbc-news')
    # get articles from al-jazeera-english
    aljazeera = get_articles_headlines('al-jazeera-english')
    cnn_home = get_articles_headlines('cnn')
    bbc_news_home = get_articles_headlines('bbc-news')
    cbc_news = get_articles_headlines('cbc-news')

    
    title = 'Home - TITRAVIC LIVE NEWS '
    return render_template('index.html',
                           title=title,
                           general=general_news,
                           articles=articles_news,
                           bcc=bbc_news_home,
                           bbc_news=bbc_news,
                           cnn_home=cnn_home,
                           cbc_news=cbc_news,
                           aljazeera=aljazeera,
                           
                           )



@app.route('/articles')
def articles():
    '''
    View articles page => function that returns the articles page from a source id 
    '''
    # Getting articles based on the source id
    articles = get_articles("general")
    title = "TITRAVIC LIVE NEWS"

    return render_template('articles.html', title=title, articles=articles)



@app.route('/sports')
def sports():
    '''
    View sports page 
    '''
    sports =get_articles_by_category('sports')
    title = 'Sports - Welcome to The best Hot News in the world'
    return render_template('sports.html',
                           title=title,
                           sports=sports
                           )



@app.route('/business')
def business():
    '''
    View business page function that returns the business page and its data
    '''
    business = get_articles_by_category('business')
    title = 'business - Welcome to The best business News in the world'
    return render_template('business.html',
                           title=title,
                           business=business
                           )