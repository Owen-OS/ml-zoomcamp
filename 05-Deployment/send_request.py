import sys
import requests

def send_request(url, customer):
    response = requests.post(url, json=customer)
    return response.text


if __name__ == "__main__":

    res = None

    args = sys.argv
    if args[1].lower() == "q3":
        url = "http://0.0.0.0:9696/question3_and_4"
        customer = {
            "lead_source": "paid_ads",
            "number_of_courses_viewed": 2,
            "annual_income": 79276.0
        }
        res = send_request(url, customer)
    elif args[1].lower() == "q4":
        url = "http://0.0.0.0:9696/question3_and_4"
        customer = {
            
            "lead_source": "organic_search",
            "number_of_courses_viewed": 4,
            "annual_income": 80304.0
        }
        res = send_request(url, customer)
    elif args[1].lower() == "q6":
        url = "http://0.0.0.0:9696/question6"
        customer = {
            "lead_source": "organic_search",
            "number_of_courses_viewed": 4,
            "annual_income": 80304.0
        }
        res = send_request(url, customer)

    print(res)
    
