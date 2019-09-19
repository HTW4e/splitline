#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################################################
# Description: tool wich make a line break after x characters
# Author: hinkelsteinli
# Version: 1.0
# Script Name: splitlines.py
###############################################################################################################
# Copyright (c) Hinkelsteinli <hinkelsteinli@hinkelstein.li>

# This software is licensed to you under the GNU General Public License.
# There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/gpl.txt

# Import Modules
import os
import cgi, cgitb

# HTML
print("Content-Type: text/html\r\n")
print('<html>')
print('<head>')
print('<meta charset="utf-8" />')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0" />')
print('<link rel="stylesheet" href="/css/style.css">')
print('<title>Impressum</title>')
print('</head>')
print('<body>')
print('<div class="topnav">')
print('<a href="http://127.0.0.1/cgi-bin/splitline.cgi">SplitLine</a>')
print('<a class="active" href="http://127.0.0.1/cgi-bin/impressum.cgi">Impressum</a>')
print('</div>')
print('<div class="impressum">')
print('<h2>Kontaktadresse</h2>')
print('<p>Mike Gubser</p>')
print('<p>Schweiz</p>')
print('<p><a href="mailto:support@ict4u.li">support@ict4u.li</a></p>')
print('<p>&nbsp;</p>')
print('<h2>Haftungsausschluss</h2>')
print('<p>Der Autor übernimmt keinerlei Gewähr hinsichtlich der  inhaltlichen Richtigkeit, Genauigkeit, Aktualität, Zuverlässigkeit und  Vollständigkeit der Informationen.</p>')
print('<p>Haftungsansprüche gegen den Autor wegen Schäden materieller  oder immaterieller Art, welche aus dem Zugriff oder der Nutzung bzw.  Nichtnutzung der veröffentlichten Informationen, durch Missbrauch der  Verbindung oder durch technische Störungen entstanden sind, werden  ausgeschlossen.</p>')
print('<p>Alle  Angebote sind unverbindlich. Der Autor behält es sich ausdrücklich vor, Teile  der Seiten oder das gesamte Angebot ohne gesonderte Ankündigung zu verändern,  zu ergänzen, zu löschen oder die Veröffentlichung zeitweise oder endgültig  einzustellen.</p>')
print('<p>&nbsp;</p>')
print('<h2>Urheberrechte</h2>')
print('<p>Die Urheber- und alle anderen Rechte an Inhalten, Bildern, Fotos oder anderen Dateien auf der Website gehören ausschliesslich <strong>Hinkelsteinli</strong> oder den speziell genannten  Rechtsinhabern. Für die Reproduktion jeglicher Elemente ist die schriftliche Zustimmung der Urheberrechtsträger im Voraus einzuholen.</p>')
print('<p>&nbsp;</p>')
print('</div>')
print('</body>')
print('</html>')
