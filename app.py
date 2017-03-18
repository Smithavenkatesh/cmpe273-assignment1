from flask import Flask
from github import Github
import sys, base64, yaml, json
 
url = sys.argv[1]
given_repo = (url.split(".com/")[1]).split("/")[1]
username = (url.split(".com/")[1]).split("/")[0]

global d
d={}

app = Flask(__name__)


@app.route('/v1/<filename>')
def get_config_file(filename):
	try:
		repo = Github().get_user(username).get_repo(given_repo)
		decodedContent = base64.b64decode(repo.get_contents(filename).content)
		finalString=""

		if(filename.endswith(".yml")):
			d = yaml.load(decodedContent)#converts the string decodedContent to Dictionary d
			for keys,values in d.items():
				finalString = str(finalString)+str(keys)+" - "+str(values)+"<br/>"

		else:
			d = json.loads(decodedContent)
			finalString="{<br/>"
			for keys,values in d.items():
				finalString = str(finalString)+str(keys)+" - "+str(values)+"<br/>"
			finalString=str(finalString)+"}"

	except:
		finalString = "Can not find the file or Repository" 
			
	return finalString
	
if __name__ == "__main__":
	   app.run(debug=True,host='0.0.0.0')















