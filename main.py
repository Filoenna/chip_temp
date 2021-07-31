import requests

response = requests.get("https://api2.hiveos.farm/api/v2/farms",  headers={'Authorization': 'Bearer <token>'})

temp = 0
chip_temp = 0
workers_count = 0

farms = response.json()['data']
for farm in farms:
    print(f"Farm: {farm['id']}")
    url = 'https://api2.hiveos.farm/api/v2/farms/' + str(farm['id']) + '/workers'
    temp_response = requests.get(url,  headers={'Authorization': 'Bearer <token>'})
    workers = temp_response.json()['data']
    for worker in temp_response.json()['data']:
        print(f'\tWorker id: {worker["id"]}')
        cores = (worker['asic_stats']['boards'])
        for core in cores:
            chip_temp += core['temp']
        print(f'\tTemp: {chip_temp/len(cores)}')
        temp += chip_temp/len(cores)
        chip_temp = 0
        workers_count += 1
    print(f'Avg chip temp for farm: {temp/workers_count}')
    workers_count = 0
    temp = 0
    



