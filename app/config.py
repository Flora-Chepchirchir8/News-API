class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = 'NEWS_API_KEY'
    SECRET_KEY = 'SECRET_KEY'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?category={}&language=en&from=2022-04-16&apiKey={}'
    NEWS_API_ARTICLES_URL =  'https://newsapi.org/v2/top-headlines/sources?/{}?&language=en&from=2022-04-16&apiKey={}'
   
    
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True