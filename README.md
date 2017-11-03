# SMS-API WEB-587 WEB-588

> SMS-API which takes two parameters ( List of recipients and text ) and sends via web app.

# Requirements

SMS-API which takes two parameters , A list of phone numbers, A text message and sends it.

A web frontend for the SMS-API which allows  input  of text / list of recipents or  selection of Contacts and Text from predefined templates


Current SMS provider is GLUE (https://wiki.mt.local/web/doku.php?id=externe_services:smsbutler)

Create a static webpage using JavaScript to communicate with the SMS-API.

Form which sends a message to a number(s). After sending, show a success/failure notification.

Showing the current credit balance, show the log as per existing functionality

Create an app which allows maintenance of Contacts and Template Text .



![](header.png)

## Installation

Linux:

git@gitlab.mt.local:web_software/smsapi.git

see requirements.txt


## Setup / Usage



**smscontacts** app allows setup of Contacts / Contact Groups and Template Text
run via Django  ( python manage.py runserver )


http://127.0.0.1:8000/admin/         : **username/password** **asa**/**asa**  

http://127.0.0.1:8000/templatetext/  : template list

http://127.0.0.1:8000/group/         : contact grouping list

http://127.0.0.1:8000/contact/       : contact listing


**smsapp.py**  flask web app to send SMS configurable for :

SMS provider (**smsapp.cfg**  provider and logfilename (created in $HOME) )

hipchat notifications (**hipchat.cfg**   url and token )


**Modules :** 


**dynamicimport.py**  used to dynamically call module for sms provider. Provider name is from cfg file 

**hipchat.py**  used to send messages to Chatroom incase of critical error (e.g running out of credits )

**phonefilter.py**      parsed recipients are cleaned and validated , duplicates removed and converted  to  E.164 standard

**handybutler.py**      get recipents and chunk into groups of 10 (if > 10) , add message and recipients to log file. check actual response body for positive response i.e. <okay id. if not ok then send message to hipchat room

**smsapp.py**           setup logging information , get the sms service povider from config file , ensure there is valid data to send , return Response Code / Text 




**smstool.html**  web page for sending sms to contact group or comma separated recipients using predefined templates or free format text




## Release History


* 0.0.1
    * Work in progress

## Meta



Avtar Sandhu – 2020sandhu@gmail.com