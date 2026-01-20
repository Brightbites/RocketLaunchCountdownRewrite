import csv
import io
import requests

session = requests.Session()

def fetch_gonogo(Manual, GUIVariables, link):
    # Make GoNoGo Global
    global weather, Range, vehicle
    # if GUI controlled
    if Manual:
        try:
            # Get Range, Weather and vehicle from GUI
            Range = GUIVariables[0]
            weather = GUIVariables[1]
            vehicle = GUIVariables[2]
            return[Range, weather, vehicle]
        except:
            print("YOU IDIOT, YOU DIDNT DECLARE THE VARIABLES")
            return[None, None, None]
    else:
        # Get Range, Weather and vehicle from spreadsheet
        Range   = pullSpreedsheet(12, 2, link)
        weather = pullSpreedsheet(14, 2, link)
        vehicle = pullSpreedsheet(16, 2, link)
        return[Range, weather, vehicle]

def fetch_major_concerns(Manual = False, GUIVariables = None, link = None):
    # Make concerns global
    global concerns
    # if GUI controlled
    if Manual:
        # Get Major Concerns from GUI
        try:
            concerns = GUIVariables
            return[concerns]
        except:
            print("YOU IDIOT, YOU DIDNT DECLARE THE VARIABLES")
            return[None]
    else:
        # Get Major Concerns from spreadsheet
        concerns = pullSpreedsheet(11, 4, link)
        return concerns 

def update_gonogo():
    return[Range, weather, vehicle]

def update_major_concerns():
    return concerns

def pullSpreedsheet(inputCol, inputRow, link):
    col = int(inputCol) - 1
    rows = [
        int(inputRow) - 1,
    ]
    try:
        resp = session.get(link, timeout=3)
        resp.raise_for_status()
        reader = csv.reader(io.StringIO(resp.text))
        data = list(reader)
        pulledcell = []
        for r in rows:
            val = "N/A"
            if 0 <= r < len(data) and len(data[r]) > col:
                val = data[r][col]
            pulledcell.append(val.strip().upper())
        return pulledcell[0]
    except Exception as e:
        print(f"[ERROR] Failed to fetch Go/No-Go from sheet: {e}")
        return None