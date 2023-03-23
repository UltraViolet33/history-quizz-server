from app import create_app

if __name__ == "__main__":
    app = create_app()

    # app.config.from_object("config.TestingConfig")

    # print(app.config['SQLALCHEMY_DATABASE_URI'])


    app.run(host = '0.0.0.0', debug=True)