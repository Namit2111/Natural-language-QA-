import requests

BASE_URL = "http://127.0.0.1:5000/api/chat"

def test_document_upload(file_path):
    url = 'http://127.0.0.1:5000/api/documents/process'  

    with open(file_path, 'rb') as f:
        files = {'file': (file_path, f)}
        response = requests.post(url, files=files)
    
    if response.status_code == 200:
        print("Success:", response.json())
        return response.json()
    else:
        print("Error:", response.json())


def test_start_chat(assetid):
    response = requests.post(f"{BASE_URL}/start", json={"asset_id": assetid})
    if response.status_code == 201:
        data = response.json()
        chat_thread_id = data.get("chat_thread_id")
        print(f"Test Start Chat: Success - Chat Thread ID: {chat_thread_id}")
        return chat_thread_id
    else:
        print(f"Test Start Chat: Failed - Status Code: {response.status_code}, Response: {response.json()}")
        return None

def test_send_message(chat_thread_id,user_query):
    response = requests.post(f"{BASE_URL}/message", json={"chat_thread_id": chat_thread_id, "message": user_query})
    if response.status_code == 200:
        data = response.json()
        agent_response = data.get("agent_response")
        print(f"Test Send Message: Success - Agent Response: {agent_response}")
    else:
        print(f"Test Send Message: Failed - Status Code: {response.status_code}, Response: {response.json()}")

def test_get_chat_history(chat_thread_id):
    response = requests.get(f"{BASE_URL}/history", params={"chat_thread_id": chat_thread_id})
    if response.status_code == 200:
        data = response.json()
        chat_history = data.get("chat_history")
        print(f"Test Get Chat History: Success - Chat History: {chat_history}")
    else:
        print(f"Test Get Chat History: Failed - Status Code: {response.status_code}, Response: {response.json()}")

def test_get_asset_by_chat_thread(chat_thread_id):
    response = requests.get(f"{BASE_URL}/asset", params={"chat_thread_id": chat_thread_id})
    if response.status_code == 200:
        data = response.json()
        asset_id = data.get("asset_id")
        print(f"Test Get Asset by Chat Thread: Success - Asset ID: {asset_id}")
    else:
        print(f"Test Get Asset by Chat Thread: Failed - Status Code: {response.status_code}, Response: {response.json()}")

def main():
    data = test_document_upload(file_path="productDetails.pdf")
    asset_id = data.get('asset_id')
    chat_thread_id = test_start_chat(assetid=asset_id)
    test_send_message(chat_thread_id=chat_thread_id,user_query="what is the company about")
    test_send_message(chat_thread_id=chat_thread_id,user_query="what are the reviews")
    test_get_chat_history(chat_thread_id=chat_thread_id)

if __name__ == "__main__":
    main()
