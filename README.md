# Metar

# Requirements
1. Python v3.8.10
2. Django v4.0.2
3. Redis-server v6.2.6


#### Installation Guide

1. Navigate to some directory named metar
3. git clone https://github.com/faisalwaleed1/metar.git
4. pip3 install virtualenv
5. virtualenv env
6. source env/bin/activate
7. pip3 install -r requirements.txt


### Run migrations
- Navigate to metar directory
- Run `python3 manage.py migrate`

### Run project
- open two terminals  
- run `redis-server` on one terminal
- run `python3 manage.py runserver 8080` on second terminal


### To check Pong
visit [http://localhost:8080/metar/ping]

### To check NWS Report
visit [http://localhost:8080/metar/info?scode=station_code]
