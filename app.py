from flask import Flask #library for web apps

app = Flask(__name__) #all web application saved as object in this variable, name links it to file location to find related resources (html)


@app.route("/") #connects a URL to a Python function, when user visits root url run the function below (decorator)
def home():
    #return, returns below HTML to vistor's browser
    return """ 
    <h1>Zarya's Cloud Roadmap</h1> 
    <p>My first cloud engineering application is running.</p>
    """
#HTML first one, h1 creates main heading, p creates paragraph, triple quotes allows multi-line string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Host is the IP addresses the server will allow to listen/ recieve. (0.0.0.0 means all available IP addresses)
# Server is an apartment building, each website has an aprtment unit (door) that request go to.
# if file is run directly (not an imported module), run the app on all available IP addresses (host="0.0.0.0") on port 5000 
