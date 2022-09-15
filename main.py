import speech_recognition as sr
from selenium import webdriver

# Website dictionary
# Dicionário de sites
websites_dict = {'google':'https://www.google.com', 'wikipedia':'https://www.wikipedia.com', 'youtube':'https://www.youtube.com'}

# Instantiating the microphone
# Instanciando o microfone
with sr.Microphone() as source:
    print("\n Please, say the website you wish to open | Por favor, diga o site que deseja abrir :")
    
    # Instantiating the recognition class and handling ambi# Applying the recognition class on the captured audio and looking up the website address in the dictionaryent noise
    # Instanciando a classe de reconhecimento e tratando o ruído do ambiente
    recog = sr.Recognizer()
    audio = recog.adjust_for_ambient_noise(source)
    audio = recog.listen(source)
    
    # Applying the recognition class on the captured audio and looking up the website address in the dictionary
    # Aplicando a classe de reconhecimento sobre o áudio captado e buscando o endereço do site no dicionário
    try:
        txt = recog.recognize_google(audio)
        website = websites_dict.get(txt.lower())
        if website: 
            driver = webdriver.Firefox()
            driver.get(website)
        else:
            print('Unknow website | Não conheço este site')
            print(txt)
    except sr.UnknownValueError:
        print("The voice recognition failed | O reconhecimento de voz falhou.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

