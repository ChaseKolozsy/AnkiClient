import requests

def study(deck_id, action, base_url='http://localhost:5001'):
    url = f"{base_url}/api/study"
    response = requests.post(url, json={"action": action, "deck_id": deck_id})
    
    return response.json(), response.status_code

if __name__ == "__main__":
    # Start a review session
    try:
        print(study(1716329734843, 'start'))
    except Exception as e:
        print(e)

    # Flip the current card
    try:
        print(study(1716329734843, 'flip'))
    except Exception as e:
        print(e)

    ## Answer the current card with ease level 3
    try:
        print(study(1716329734843, '3'))
    except Exception as e:
        print(e)

    ## Close the review session
    print(study(1716329734843, 'close'))

