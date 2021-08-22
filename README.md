# porkbun_ddns
With this script you can simple update your DNS records at porkbun.com

Script preparation:
1. Get your api and secret keys - https://porkbun.com/account/api and set them as api_key and secret_key
2. Get your DNS records ID's with requests.post('https://porkbun.com/api/json/v3/dns/retrieve/<YOUR_DOMAIN>', json={"secretapikey":secret_key, "apikey":api_key}).json() and write them to records
3. Change <YOUR_DOMAIN> in the file

Run script
