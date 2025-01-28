# # import os
# # import requests
# # from dotenv import load_dotenv
# # from flask import Flask, jsonify, request, render_template
# #
# # # Load environment variables
# # load_dotenv(dotenv_path='clientid.env')
# #
# # # Flask App
# # app = Flask(__name__)
# #
# # # API Credentials
# # CLIENT_ID = os.getenv('CLIENT_ID')
# # CLIENT_SECRET = os.getenv('CLIENT_SECRET')
# #
# # # Function to Get Access Token
# # def get_access_token():
# #     token_url = 'https://ext-api.vasttrafik.se/token'
# #     auth = (CLIENT_ID, CLIENT_SECRET)
# #     data = {'grant_type': 'client_credentials'}
# #     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# #
# #     response = requests.post(token_url, data=data, headers=headers, auth=auth)
# #     if response.status_code == 200:
# #         return response.json()['access_token']
# #     else:
# #         return None
# #
# # # Fetch Tram Positions
# # def fetch_tram_positions(line, direction):
# #     access_token = get_access_token()
# #     if not access_token:
# #         return {"error": "Unable to retrieve access token"}
# #
# #     api_url = "https://ext-api.vasttrafik.se/pr/v4/positions"
# #     params = {
# #         'lowerLeftLat': 57.630000,
# #         'lowerLeftLong': 11.890000,
# #         'upperRightLat': 57.750000,
# #         'upperRightLong': 12.040000,
# #         'transportModes': 'tram',
# #         'lineDesignations': line,
# #         'limit': 100
# #     }
# #     if direction:  # Only apply direction filter if a direction is selected
# #         params['direction'] = direction
# #
# #     headers = {'Authorization': f'Bearer {access_token}'}
# #     response = requests.get(api_url, headers=headers, params=params)
# #
# #     if response.status_code == 200:
# #         data = response.json()
# #         return data
# #     else:
# #         return {"error": "Failed to fetch tram positions"}
# #
# # # Fetch Available Directions
# # def fetch_available_directions(line):
# #     access_token = get_access_token()
# #     if not access_token:
# #         return {"error": "Unable to retrieve access token"}
# #
# #     api_url = "https://ext-api.vasttrafik.se/pr/v4/positions"
# #     params = {
# #         'lowerLeftLat': 57.630000,
# #         'lowerLeftLong': 11.890000,
# #         'upperRightLat': 57.750000,
# #         'upperRightLong': 12.040000,
# #         'transportModes': 'tram',
# #         'lineDesignations': line,
# #         'limit': 100
# #     }
# #     headers = {'Authorization': f'Bearer {access_token}'}
# #     response = requests.get(api_url, headers=headers, params=params)
# #
# #     if response.status_code == 200:
# #         data = response.json()
# #         directions = set(tram.get('direction') for tram in data if tram.get('direction'))
# #         return list(directions)
# #     else:
# #         return {"error": "Failed to fetch directions"}
# #
# # # Routes
# # @app.route('/')
# # def index():
# #     return render_template('index.html')
# #
# # @app.route('/tram_positions', methods=['GET'])
# # def tram_positions():
# #     line = request.args.get('line', '')
# #     direction = request.args.get('direction', '')
# #     positions = fetch_tram_positions(line, direction)
# #     return jsonify(positions)
# #
# # @app.route('/available_directions', methods=['GET'])
# # def available_directions():
# #     line = request.args.get('line', '')
# #     directions = fetch_available_directions(line)
# #     return jsonify(directions)
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
# import os
# import requests
# from dotenv import load_dotenv
# from flask import Flask, jsonify, request, render_template
#
# # Load environment variables
# load_dotenv(dotenv_path='clientid.env')
#
# # Flask App
# app = Flask(__name__)
#
# # API Credentials
# CLIENT_ID = os.getenv('CLIENT_ID')
# CLIENT_SECRET = os.getenv('CLIENT_SECRET')
#
# # Function to Get Access Token
# def get_access_token():
#     token_url = 'https://ext-api.vasttrafik.se/token'
#     auth = (CLIENT_ID, CLIENT_SECRET)
#     data = {'grant_type': 'client_credentials'}
#     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#
#     response = requests.post(token_url, data=data, headers=headers, auth=auth)
#     if response.status_code == 200:
#         return response.json()['access_token']
#     else:
#         return None
#
# # Fetch Tram Positions
# def fetch_tram_positions(line, direction):
#     access_token = get_access_token()
#     if not access_token:
#         return {"error": "Unable to retrieve access token"}
#
#     api_url = "https://ext-api.vasttrafik.se/pr/v4/positions"
#     params = {
#         'lowerLeftLat': 57.630000,
#         'lowerLeftLong': 11.890000,
#         'upperRightLat': 57.750000,
#         'upperRightLong': 12.040000,
#         'transportModes': 'tram',
#         'lineDesignations': line,
#         'limit': 100
#     }
#     if direction:  # Only apply direction filter if a direction is selected
#         params['direction'] = direction
#
#     headers = {'Authorization': f'Bearer {access_token}'}
#     response = requests.get(api_url, headers=headers, params=params)
#
#     if response.status_code == 200:
#         data = response.json()
#         return data
#     else:
#         return {"error": "Failed to fetch tram positions"}
#
# # Fetch Available Directions
# def fetch_available_directions(line):
#     access_token = get_access_token()
#     if not access_token:
#         return {"error": "Unable to retrieve access token"}
#
#     api_url = "https://ext-api.vasttrafik.se/pr/v4/positions"
#     params = {
#         'lowerLeftLat': 57.630000,
#         'lowerLeftLong': 11.890000,
#         'upperRightLat': 57.750000,
#         'upperRightLong': 12.040000,
#         'transportModes': 'tram',
#         'lineDesignations': line,
#         'limit': 100
#     }
#     headers = {'Authorization': f'Bearer {access_token}'}
#     response = requests.get(api_url, headers=headers, params=params)
#
#     if response.status_code == 200:
#         data = response.json()
#         directions = set(tram.get('direction') for tram in data if tram.get('direction'))
#         return list(directions)
#     else:
#         return {"error": "Failed to fetch directions"}
#
# # Fetch Departure Board for a Stop
# def fetch_departure_board(stop_id):
#     access_token = get_access_token()
#     if not access_token:
#         return {"error": "Unable to retrieve access token"}
#
#     api_url = "https://ext-api.vasttrafik.se/pr/v4/stop-areas"
#     params = {'id': stop_id}
#     headers = {'Authorization': f'Bearer {access_token}'}
#
#     response = requests.get(api_url, headers=headers, params=params)
#
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": "Failed to fetch departure board"}
#
# # Routes
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/tram_positions', methods=['GET'])
# def tram_positions():
#     line = request.args.get('line', '')
#     direction = request.args.get('direction', '')
#     positions = fetch_tram_positions(line, direction)
#     return jsonify(positions)
#
# @app.route('/available_directions', methods=['GET'])
# def available_directions():
#     line = request.args.get('line', '')
#     directions = fetch_available_directions(line)
#     return jsonify(directions)
#
# @app.route('/departure_board', methods=['GET'])
# def departure_board():
#     stop_id = request.args.get('stop_id', '')
#     if not stop_id:
#         return jsonify({"error": "stop_id is required"}), 400
#
#     board = fetch_departure_board(stop_id)
#     return jsonify(board)
#
# if __name__ == '__main__':
#     app.run(debug=True)
import os
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template

# Load environment variables
load_dotenv(dotenv_path='clientid.env')

# Flask App
app = Flask(__name__)

# API Credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Function to Get Access Token
def get_access_token():
    token_url = 'https://ext-api.vasttrafik.se/token'
    auth = (CLIENT_ID, CLIENT_SECRET)
    data = {'grant_type': 'client_credentials'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(token_url, data=data, headers=headers, auth=auth)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None

# Fetch Tram Positions
def fetch_tram_positions(line, direction):
    access_token = get_access_token()
    if not access_token:
        return {"error": "Unable to retrieve access token"}

    api_url = "https://ext-api.vasttrafik.se/pr/v4/positions"
    params = {
        'lowerLeftLat': 57.630000,
        'lowerLeftLong': 11.890000,
        'upperRightLat': 57.750000,
        'upperRightLong': 12.040000,
        'transportModes': 'tram',
        'lineDesignations': line,
        'limit': 100
    }
    if direction:  # Only apply direction filter if a direction is selected
        params['direction'] = direction

    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        for tram in data:
            # Use detailsReference as the unique tram ID
            tram_id = tram.get('detailsReference', 'unknown')
            print(f"Tram ID (detailsReference): {tram_id}")

        return data
    else:
        return {"error": "Failed to fetch tram positions"}

# Fetch Available Directions
def fetch_available_directions(line):
    access_token = get_access_token()
    if not access_token:
        return {"error": "Unable to retrieve access token"}

    api_url = "https://ext-api.vasttrafik.se/pr/v4/positions"
    params = {
        'lowerLeftLat': 57.630000,
        'lowerLeftLong': 11.890000,
        'upperRightLat': 57.750000,
        'upperRightLong': 12.040000,
        'transportModes': 'tram',
        'lineDesignations': line,
        'limit': 100
    }
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        directions = set(tram.get('direction') for tram in data if tram.get('direction'))
        return list(directions)
    else:
        return {"error": "Failed to fetch directions"}

# Fetch Departure Board for a Stop
def fetch_departure_board(stop_gid):
    access_token = get_access_token()
    if not access_token:
        print("Error: Unable to retrieve access token")  # Debugging statement
        return {"error": "Unable to retrieve access token"}

    api_url = f"https://ext-api.vasttrafik.se/pr/v4/stop-areas/{stop_gid}/departures"
    params = {
        'timeSpanInMinutes': 60,
        'maxDeparturesPerLineAndDirection': 2,
        'limit': 10,
        'offset': 0,
        'includeOccupancy': 'false'
    }
    headers = {'Authorization': f'Bearer {access_token}'}

    print(f"Requesting URL: {api_url} with params: {params}")  # Debugging statement

    response = requests.get(api_url, headers=headers, params=params)

    print(f"Response Status Code: {response.status_code}")  # Debugging statement

    if response.status_code == 200:
        data = response.json()
        print(f"API Response Data: {data}")  # Log the data to see its structure
        return data
    else:
        print("Error: Failed to fetch departure board")  # Debugging statement
        return {"error": "Failed to fetch departure board"}

# Fetch Stop Areas based on user input
def fetch_stop_areas(query):
    access_token = get_access_token()
    if not access_token:
        return {"error": "Unable to retrieve access token"}

    api_url = "https://ext-api.vasttrafik.se/pr/v4/locations/by-text"
    params = {
        'q': query,
        'types': 'stoparea',
        'limit': 10,
        'offset': 0,
        'bodSearch': 'false'
    }
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(api_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"API Response: {data}")  # Log the entire API response
        if 'LocationList' in data and 'StopLocation' in data['LocationList']:
            for stop in data['LocationList']['StopLocation']:
                print(f"Stop Name: {stop['name']}, GID: {stop['id']}")  # Log the stop name and GID
        return data
    else:
        print("Failed to fetch stop areas")  # Log failure
        return {"error": "Failed to fetch stop areas"}

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tram_positions', methods=['GET'])
def tram_positions():
    line = request.args.get('line', '')
    direction = request.args.get('direction', '')
    positions = fetch_tram_positions(line, direction)
    return jsonify(positions)

@app.route('/available_directions', methods=['GET'])
def available_directions():
    line = request.args.get('line', '')
    directions = fetch_available_directions(line)
    return jsonify(directions)

@app.route('/departure_board', methods=['GET'])
def departure_board():
    stop_gid = request.args.get('stop_gid', '')
    if not stop_gid:
        return jsonify({"error": "stop_gid is required"}), 400

    board = fetch_departure_board(stop_gid)
    return jsonify(board)

@app.route('/search-stop', methods=['GET'])
def search_stop():
    query = request.args.get('query', '')
    print(f"Search Query: {query}")  # Log the search query
    if not query:
        return jsonify({"error": "query is required"}), 400

    stops = fetch_stop_areas(query)
    print(f"Stops: {stops}")  # Log the stops data
    return jsonify(stops)

if __name__ == '__main__':
    app.run(debug=True)



