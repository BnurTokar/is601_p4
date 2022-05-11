#Development mode test
#Production mode test
#Testing mode test

def test_development_config(application):
    application.config.from_object('app.config.DevelopmentConfig')
    assert not application.config['TESTING']

def test_production_config(application):
    application.config.from_object('app.config.ProductionConfig')
    assert not application.config['TESTING']

