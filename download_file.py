from urllib import request

url = 'http://www.google.com/finance/historical?q=NASDAQ:GOOG&output=csv'

def download_hist_data(csv_url):
	response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\n")
	dest_url = r'soup.csv'
	fx = open(dest_url, "w")
	for line in lines:
		fx.write(line + "\n")
	fx.close()

download_hist_data(url)