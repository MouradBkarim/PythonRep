import cherrypy

class ChPy_server(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"
        
if __name__ == '__main__':
    cherrypy.quickstart(ChPy_server())
