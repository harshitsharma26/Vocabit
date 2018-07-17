import Tkinter as Tk
import requests
import json
import notify2
import subprocess
def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

form = Tk.Tk()
previousData = form.clipboard_get()				
form.withdraw()
while True:
	data = form.clipboard_get()										# fetching word from the clipboard
	if data == None:
		continue
	if previousData != data:										# checking if there is a change in the word in clipboard
		app_id = ''											# use your Oxford Api-id here
		app_key = ''				# use your Oxford Api-key here

		language = 'en'
		word_id = data
		print(word_id)
		url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

		r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
		previousData=data
		print("code {}\n".format(r.status_code))					# Status code
		if(r.status_code == 200):
			total=r.json()											# Json response					
			ans= []
			if 'results' in total:									# Extracting meaning from json response		
				for results in total['results']:					
					if 'lexicalEntries' in results:
						for lexicalEntries in results['lexicalEntries']:
							if 'entries' in lexicalEntries:
								for entries in lexicalEntries['entries']:
									if 'senses' in entries:
										for senses in entries['senses']:
											if 'definitions' in senses:
												ans.append(senses['definitions'])

			k=[]
			for i in ans:
				k.append(i[0])							
			print(k)
			notify2.init(data)
			n = notify2.Notification(data, k[0])					# notify2 showing the meaning
			notify2.URGENCY_NORMAL
			n.show()	
