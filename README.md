# minimal QGIS-plugin 

## github-pages server
Enable a static page with the xml, like https://fdobad.github.io/qgis-plugin-server/plugins.xml  

Put `plugins.xml` inside `github_page` folder, then configure a StaticHTML github page:  
`Settings > Pages > Source 'GithubActions' > Static HTML 'Configure'`

On editing the .github/workflows/static.yml, change to the path of the xml
```
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          # Upload entire repository
          path: 'github_page'
```


## flask-server

- Host a flask web server with the following [xml](templates/plugins.xml)
- Put the plugin.zip in static folder

### Local Dev
#### install
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
#### run local
```
source .venv/bin/activate
flask run
```
Click on the http link to display
```
(.venv) fdo@macbp52:~/dev/qgis-plugin-server$ flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [25/Apr/2023 11:55:27] "GET / HTTP/1.1" 200 -
```

# References
- ask: https://gis.stackexchange.com/questions/135859/is-it-possible-to-set-up-a-local-qgis-plugin-repository
- tutorial: https://gis-ops.com/qgis-3-plugin-tutorial-set-up-a-plugin-repository-explained
- super: https://github.com/qgis/QGIS-Django
- complex: https://github.com/planetfederal/qgis-plugins-xml
- simpler: https://gitlab.com/GIS-projects/phpQGISrepository 
- sample: https://plugins.stuyts.xyz/
- azure: https://learn.microsoft.com/en-us/azure/app-service/quickstart-python
- flask: https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/
