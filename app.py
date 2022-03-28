import os
import web # web.py Framework

urls = (
    '/', 'Index',
)

app = web.application(urls, globals()) # URLs config
wsgiapp = app.wsgifunc()
render = web.template.render('views', base='layout') # Path to views

class Index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    web.config.debug = False # Disable Debug config
    app.run() # ejecuta al web app
