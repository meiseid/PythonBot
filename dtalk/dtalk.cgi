#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import codecs
import cgi
import os
import sys
import io
import mysql.connector
import MeCab
from urllib.parse import urlparse

def mecab_list(text):
    tagger = MeCab.Tagger("-Ochasen")
    tagger.parse('')
    node = tagger.parseToNode(text)
    word_class = []
    while node:
        word = node.surface
        wclass = node.feature.split(',')
        if wclass[0] != u'BOS/EOS':
            if wclass[6] == None:
                word_class.append((word,wclass[0],wclass[1],wclass[2],""))
            else:
                word_class.append((word,wclass[0],wclass[1],wclass[2],wclass[6]))
        node = node.next
    return word_class

#mecab = MeCab.Tagger("-Ochasen")

form = cgi.FieldStorage()

honbun = ''
if 'honbun' in form:
	honbun = form['honbun'].value

#outer = ''
#mecab.parse('')
#node = mecab.parseToNode(honbun)
#while node:
#	outer += str(node.feature)
#	outer += str(node.feature.split(","))
#	node = node.next
#	word = node.surface
#	pos = node.feature.split(",")[1]
#	if word != '' and pos != '*':
#	outer += '{0} , {1}'.format(word, pos) + '<br>\n'
#	node = node.next

test = mecab_list(honbun)

print("Content-Type: text/html; charset=UTF-8\r\n\r\n",end="")
for ttt in test:
	i = 0
	for tt in ttt:
		if i > 1:
			print(",",end="")
		print(tt,end="")
		if i == 0:
			print("　[")
		i += 1
	print("]<br>\n",end="")
