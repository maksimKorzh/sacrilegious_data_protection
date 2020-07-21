#########################################
#
#       Sacrilegious web scraping
#        data protection measure
#         created "on the knee"
#
#                  by
#
#           Code Monkey King
#
#########################################

# packages
from flask import *
import json
import csv
import random

# create app instance
app = Flask(__name__)

# add a root route
@app.route('/')
def root():
    # load data from file
    with open('lulu.csv', 'r') as f:
        # output data
        data = [item for item in csv.reader(f)]
        
        # style classes and properties
        styles = []
        
        # loop over data rows
        for index_row in range(len(data)):
            # lop over data columns
            for index_col in range(len(data[index_row])):
                if 'http' not in data[index_row][index_col]:
                    # append tags
                    styles.append({
                        'class': '.item_%s%s' % (index_row, index_col),
                        'top': str(index_row * 100 + 150) + 'px;',
                        'left': str(index_col * 150 + 190) + 'px;' 
                    })
                else:
                    # append tags
                    styles.append({
                        'class': '.item_%s%s' % (index_row, index_col),
                        'top': str(index_row * 100 + 110) + 'px;',
                        'left': str(index_col * 150 + 190) + 'px;' 
                    })
        
        # shuffle styles classes!
        random.shuffle(styles)
        
        # tag's classes and content
        tags = []
        
        # loop over data rows
        for index_row in range(len(data)):
            # lop over data columns
            for index_col in range(len(data[index_row])):
                # append tags
                tags.append({
                    'class': 'item_%s%s' % (index_row, index_col),
                    'content': data[index_row][index_col]
                })
        
        # shuffle HTML tags!
        random.shuffle(tags)
    
        return render_template_string('''
            <html>
              <head>
                <title>Sacrilegious data protecton</title>
              </head>
              <style>
                {% for style in styles %}
                  {{style.class}} {
                    table-layout: fixed;
                    width: 100px;
                    top: {{style.top}};
                    left: {{style.left}};
                    position: absolute;
                  }                    
                {% endfor %}
              </style>
              <body>
                <h1 align="center">Sacrilegious data protection!</h1>
                <p align="center"><strong>You just try to extract data from this site)))</strong><p>
                <div>                  
                  {% for tag in tags %}
                    {% if 'http' not in tag.content %}
                      <div class="{{tag.class}}">
                        <span>{{tag.content}}</span>
                      </div>
                    {% else %}
                      <div class="{{tag.class}}">
                        <img src="{{tag.content}}">
                      </div>
                    {% endif %}
                  {% endfor %}
                </div>
              </body>
            </html>
        ''', data=data, styles=styles, tags=tags, len=len)

# main driver
if __name__ == '__main__':
    app.run(debug=True, threaded=True)








