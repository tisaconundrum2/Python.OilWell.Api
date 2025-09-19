from app import create_app

loader = load_db()
app = create_app()

if __name__ == '__main__':
    loader.load_data()
    app.run(debug=True)
