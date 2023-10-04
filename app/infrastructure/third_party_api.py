
'''
obtiene resultado de api de trivia
'''
import requests

def get_number_fact(number) -> str:
    '''
    Devuelve el response de la api number

    args:
        number: int 

    return:
        fact: str 
    '''
    url = "http://numbersapi.com/" + str(number)
    response = requests.get(url, timeout= 10)
    if response.status_code == 200:
        fact = response.text
        return fact
    return "An error occurred"