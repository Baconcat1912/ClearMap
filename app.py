from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    #Serve a simple placeholder page.
    return render_template_string(
        """
        <!doctype html>
        <html lang=\"en\">
        <head>
        <meta charset=\"utf-8\">
        <title>AI Mind Map</title>
        </head>
        <body>
            <h1>AI Mind Map Generator</h1>    
            <p>Coming soon...</p>
        </body>
        </html>
        """
    )
if __name__ == '__main__'
    app.run(debug=True)
    #CHANGE THIS WHEN DEPLOYMENT, should be "app.run()"
    
