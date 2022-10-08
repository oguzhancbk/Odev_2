import requests

#HalkaAçık

valorant_param = {
    "language" : "tr-TR",
    "isPlayableCharacter" : "true"
}
response = requests.get("https://valorant-api.com/v1/maps", params=valorant_param)


print("\n",response.json(),"\n")

url = "https://reqres.in/api/users/"
list_users_param = {
    "page" : 2
}
get_list_users = requests.get(url, params=list_users_param)
print("GET_LIST_USERS\n",get_list_users.json(),"\n")

post_create_users_data = {
    "name": "oguzhan",
    "job": "specialist"
}

post_create_users = requests.post(url, json=post_create_users_data)
print("POST_CREATE_USERS\n", post_create_users.json() , "\n")

put_param = {
    "name": "oguzhan",
    "job": "manager"
}
put_users = requests.put(url+"2", params=put_param)
print("PUT_USERS\n", put_users.json(), "\n")





