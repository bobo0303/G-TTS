from gtts import gTTS
import time
import string
import datetime

def tts(text):
    """  
    Convert text to speech and save it as an audio file.  
  
    This function takes a text input, converts it to speech using the gTTS (Google translate),  
    normalizes the text by removing punctuation and converting it to lower case, and then saves the resulting  
    audio file in the './audio' directory.  
  
    :param text: The text to be converted to speech.  
    :type text: str  
  
    :return: The file path of the saved audio file.  
    :rtype: str  
    """  
    
    # text to audio (https://gtts.readthedocs.io/en/latest/module.html)
    tts = gTTS(text, lang="zh")
    
    """
    # text norm
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    if len(text) >= 20:
        text = text[:20] + "... "
    """
    
    # save file
    saved_file_path = f'./audio/{datetime.datetime.now()}.wav'
    tts.save(saved_file_path)
    
    return saved_file_path


if __name__ == "__main__":
    # 示例使用
    
    text = "123"
    
    start = time.time()
    audio_path = tts(text)
    end = time.time()
    print("audio save path:", audio_path)
    print("spent time:", end - start)

