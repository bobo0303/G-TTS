from gtts import gTTS
import string
import time

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
    
    # text to audio
    tts = gTTS(text)
    
    # text norm
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.lower()
    
    # save file
    saved_file_path = f'./audio/{text}.wav'
    tts.save(saved_file_path)
    
    return saved_file_path


if __name__ == "__main__":
    # 示例使用
    
    text = "one tiger"
    
    start = time.time()
    audio_path = tts(text)
    end = time.time()
    print("audio save path:", audio_path)
    print("spent time:", end - start)

