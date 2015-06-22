import web
from web import form
import TweetVisualizer as tv


urls = (
  '/', 'Index'
)

render = web.template.render('templates/')
app = web.application(urls, globals())



dates = [range(31)]
myform = form.Form( form.Textbox("Keyword", form.notnull),
                    form.Textbox("Tweet Count",
                                 form.Validator('must be between 20-2000', lambda x:(int(x)<=2000) and (int(x) >= 20))))
    
class Index(object):
    def GET(self):
        form = myform()
        return render.formtest(form)

    def POST(self): 
        form = myform()
        if not form.validates(): 
            return render.formtest(form)
            print "Invalid"
        elif int(form["Tweet Count"].value) > 100:
            tv.visualize_sentiment(form.d.Keyword,
                                   int(form["Tweet Count"].value), 
                                    method = 'streaming')
        else:
            tv.visualize_sentiment(form.d.Keyword,
                                   int(form["Tweet Count"].value))
                
if __name__ == "__main__": 
        app.run()   
