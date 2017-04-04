import os 

#to know if template path exists
def get_template_path(path):
    #getcwd means get current working directory. it ensures that the path is platform independent since 
    #in windows path are of type \file\path whereas in mac or linux its /file/path 
    file_path = os.path.join(os.getcwd(), path)  
    if not os.path.isfile(file_path):   #checking if path is valid if not we throw an exception below
        raise Exception("This is not a valid template path %s"%(file_path))
    return file_path

def get_template(path):
    file_path = get_template_path(path) #check if path is valid
    return open(file_path).read() #will open the valid file and read it    

def render_context(template_string, context):
    return template_string.format(**context) #**context will convert the dictionary into string format..errors will show if we dont have **

file_ = 'templates/email_message.txt'
file_html = 'templates/email_message.html'
template = get_template(file_) #getting the template path 
template_html = get_template(file_html)
context = {   #specifying the  context as a dictionary..these values will be sent over to the template so {name} will be replaced by Rajat and so on
    "name": "Rajat",
    "date": None,
    "total": None
}

print(render_context(template, context)) 
print(render_context(template_html, context))









"""
/abc/ad/file.txt
\hi\this\ois\a\file.txt
open("\hi\this\ois\a\file.txt").read()
open("/abc/ad/file.txt").read()
"""


