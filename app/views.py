from flask import render_template
from app import app
from .request import get_source,get_articles,get_articles_headlines,get_articles_by_category

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    general_news=get_source()
    science_news = get_articles_headlines('us','science')
    technology_news = get_articles_headlines('us','technology')
    health_news = get_articles_headlines('us','health')
    sports_news = get_articles_headlines('us','sports')
    entertainment_news = get_articles_headlines('us','entertainment')

    
    title = 'Home - TITRAVIC LIVE NEWS '
    return render_template('index.html',
                           title=title,
                           general=general_news,
                           health=health_news,
                           technology=technology_news,
                           sports=sports_news,
                           entertainment=entertainment_news,
                           science=science_news
                           )



@app.route('/articles')
def articles():
    '''
    View articles page => function that returns the articles page from a source id 
    '''
    # Getting articles based on the source id
    articles = get_articles("general")
    title = "NEWS TODAY"
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