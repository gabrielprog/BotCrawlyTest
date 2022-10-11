import requests
from bs4 import BeautifulSoup

def decode_token(token_to_decode: str) -> str:
    
    token_decoded = ""

    if token_to_decode == "":
        return "Token not found"

    key_letters = {
    		'a': 'z',
    		'b': 'y',
    		'c': 'x',
    		'd': 'w',
    		'e': 'v',
    		'f': 'u',
    		'g': 't',
    		'h': 's',
    		'i': 'r',
    		'j': 'q',
    		'k': 'p',
    		'l': 'o',
    		'm': 'n',
    		'n': 'm',
    		'o': 'l',
    		'p': 'k',
    		'q': 'j',
    		'r': 'i',
    		's': 'h',
    		't': 'g',
    		'u': 'f',
    		'v': 'e',
    		'w': 'd',
    		'x': 'c',
    		'y': 'b',
    		'z': 'a',
    		'0': '9',
    		'1': '8',
    		'2': '7',
    		'3': '6',
    		'4': '5',
    		'5': '4',
    		'6': '3',
    		'7': '2',
    		'8': '1',
    		'9': '0'
    }

    token_string_split_in_array = []

    for token_index_of_character in range(0, len(token_to_decode)):
        token_string_split_in_array.append(token_to_decode[token_index_of_character])

    for char_token_splitted in token_string_split_in_array:

        for key_letter in key_letters:
        
            if char_token_splitted == key_letter:

                token_decoded += key_letters[key_letter]

    return token_decoded

def request_api(): 
    
    URL_BASE = "http://applicant-test.us-east-1.elasticbeanstalk.com/"

    request_session = requests.Session()

    result_token_get = request_session.get(URL_BASE)
    soup_token = BeautifulSoup(result_token_get.text, "html.parser")
    value_token = soup_token.find_all(attrs={"name" : "token"})
    token_ready = decode_token(value_token[0]['value'])

    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip',
        'Origin': 'http://applicant-test.us-east-1.elasticbeanstalk.com',
        'Referer': 'http://applicant-test.us-east-1.elasticbeanstalk.com/',
        'Content-Length': '38'
    }
    postdata = {
        'token': token_ready
    }

    result_code_post = request_session.post(URL_BASE, data=postdata, headers=header)
    soup_code = BeautifulSoup(result_code_post.text, "html.parser")
    code_result = soup_code.findAll("span", {"id": "answer"})[0].string
    
    print("Codigo de retorno: " + code_result)

request_api()