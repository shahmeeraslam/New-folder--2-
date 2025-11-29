import subprocess

if __name__ == "__main__":
     print("TEXT TO SPEECH  \n")
     while True:
        
        try:
            text = input("ENTER TEXT TO SPEAK: ")
            if text == "q":
                break
            ps_script = f"""
            Add-Type -AssemblyName System.Speech
            $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
            $synth.Speak('{text}')
            """
            subprocess.run(['powershell' , '-command' , ps_script])
        
        except Exception as e:
          print(f"check your server {e}" )    