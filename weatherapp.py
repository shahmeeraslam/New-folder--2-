import requests
import json 
import subprocess

try: 
        city = input("ENTER YOUR CITY")
        url =f"https://api.weatherapi.com/v1/current.json?key=573a71f21fa244e59b5115212252911&q={city}" 
        re = requests.get(url)
        dic = json.loads(re.text)
       
        temp =  dic["current"]["temp_c"]
        lupdate = dic["current"]["last_updated"]
        country = dic["location"]["country"]
        text = f"the temperature of your city : {city} in {country} is {temp} and it is lastly updated at {lupdate}"
        ps_script = f"""
        Add-Type -AssemblyName System.Speech
        $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
        $synth.Speak('{text}')
            """
        subprocess.run(['powershell' , '-command' , ps_script])
        print(text)
except Exception as a:
     print("write correctly")   