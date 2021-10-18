import speech_recognition as sr

def reconocer(duracion):
    global r
    r = sr.Recognizer()
    global source
    with sr.Microphone() as source:
        if ("None" in duracion):
            r.adjust_for_ambient_noise(source, duration = 1)
            audio = r.listen(source,phrase_time_limit = None)
        else:
            r.adjust_for_ambient_noise(source, duration = 1)
            audio = r.listen(source,phrase_time_limit = int(duracion))
        
        try:
            response = r.recognize_google(audio, language="es-CO")
            print("Logro reconocer: '" + response + "'")
            return response
        except sr.UnknownValueError:
            return 'No reconozco'
        except sr.RequestError as e:
            print("GSR; {0}".format(e))
            return 'No logre reconocer entrada de audio'

