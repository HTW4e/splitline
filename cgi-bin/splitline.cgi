#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################################################
# Description: tool wich make a line break after x characters
# Author: HTW4e
# Version: 1.0
# Script Name: splitlines.cgi
###############################################################################################################
# Copyright (c) HTW4e <htw4e@htw4e.li>

# This software is licensed to you under the GNU General Public License.
# There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/gpl.txt

# Import Modules
import os
import sys
import cgi
import cgitb; cgitb.enable()
import textwrap

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Variables
txtinput = form.getvalue("textinput")

# HTML
print("Content-Type: text/html\r\n")
print('<html>')
print('<head>')
print('<meta charset=utf-8 />')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0" />')
print('<link rel="stylesheet" href="/css/style.css">')
print('<title>SplitLine</title>')
print('</head>')
print('<body>')
print('<div class="topnav">')
print('<a class="active" href="https://' + os.environ["HTTP_HOST"] + '/cgi-bin/splitline.cgi">SplitLine</a>')
print('<a href="https://' + os.environ["HTTP_HOST"] + '/cgi-bin/impressum.cgi">Impressum</a>')
print('</div>')
print('<div class="splitline">')
print('<h2>SplitLine</h2>')

### Begin Form ###
print('<form action="splitline.cgi" method="post">')
print('<input type="radio" id="57" name="radiochar" value="57"> 57 Zeichen <br>')
print('<input type="radio" id="76" name="radiochar" value="76" checked="checked"> 76 Zeichen <br>')
print('<input type="radio" id="xxx" name="radiochar" value="xxx">')
print('<input type="number" name="textlenght" min="10" max="100" value="40"> Zeichen <br>')
print('<br> Text: <br><textarea name="textinput" cols="100" rows="20"></textarea><br>')
print('<br><input type="submit" value="Senden" />')
print('</form>')
### End  Form ###

### Set the variable for textlenght ###
if form.getvalue("radiochar") == "xxx":
    characters = form.getvalue("textlenght")
else:
    characters = form.getvalue("radiochar")
### End Set the variable for textlenght ###

### Cut the input text and print it out ###
try:
    wrapper = textwrap.TextWrapper(width=int(characters))
    word_list = wrapper.wrap(text=txtinput)
    ### Black Line over whole page ###
    print('<div id="blackRow">&nbsp;</div><br>')
    ### End Black Line over whole page ###
    print('Output: Maximale Zeichenlänge pro Zeile ' + characters + ' Zeichen <br>')
    print('<br>')
    ### Black Line over whole page ###
    print('<div id="blackRow">&nbsp;</div><br>')
    ### End Black Line over whole page ###
    for element in word_list:
        print(element + '<br>')
except:
    sys.exit(0)
### End Cut the input text and print it out ###

print('</div>')
print('</body>')
print('</html>')
