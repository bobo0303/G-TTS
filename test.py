import requests  
import urllib.parse  
import re  
  
# 設定要發送請求的 URL  
url = "http://0.0.0.0/to_speech"  
  
# 構建請求的 payload  
payload = {  
    "text": "tgier one go cover"  
}  
  
# 發送 POST 請求  
response = requests.post(url, json=payload)  
  
# 確認請求成功  
if response.status_code == 200:  
    # 獲取音檔的文件名（從回應頭中獲取）  
    content_disposition = response.headers.get('content-disposition')  
    if content_disposition:  
        # 使用正則表達式來匹配文件名  
        match = re.search(r'filename\*=utf-8\'\'(.+)', content_disposition)  
        if match:  
            # 解碼 URL 編碼的文件名  
            filename = urllib.parse.unquote(match.group(1))  
        else:  
            filename = 'default_filename.wav'  # 當無法提取文件名時，使用預設文件名  
    else:  
        filename = 'default_filename.wav'  
  
    # 將回應的音檔內容寫入文件  
    with open(filename, 'wb') as file:  
        file.write(response.content)  
  
    print(f"音檔已保存為: {filename}")  
else:  
    print(f"請求失敗，狀態碼: {response.status_code}")  