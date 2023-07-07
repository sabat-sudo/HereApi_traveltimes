import requests 
import csv 

with open('DIRECTORY/YOURDATASET.csv', mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') 
    line_count = 0 
    for row in csv_reader: 
    	if len(row):
        	print(f'Calcolo da {row[0]} _ {row[1]} a {row[2]} _ {row[3]}')
        	line_count += 1 
	        o_lon= row[0]
        	o_lat= row[1] 
	        d_lon= row[2]
	        d_lat= row[3]
	        url = f"https://router.hereapi.com/v8/routes?transportMode=car&origin={o_lat},{o_lon}&destination={d_lat},{d_lon}&return=summary&&departureTime=any&apiKey=YOURKEY"
	        print(url) #debug
	        resp = requests.get(url) 
	        print(resp)
	        try: 
            durata = resp.json()["routes"][0]["sections"][0]["summary"]["duration"]
	        except Exception as e: 
	        	print(e) 
	        	durata=e
	        print(f"Durata: {durata}")

	        with open('risultati_dya.csv', mode='a') as f: 
	        	writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 

	        	writer.writerow([o_lat, o_lon, d_lat, d_lon, durata]) #scrivo la riga in quest ordine
	        print(f"scritta riga {line_count}") #debug

    print(f'Processati {line_count} percorsi.')
