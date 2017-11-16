sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt-get install portaudio19-dev libjack-jackd2-dev
sudo apt-get install libpulse-dev
sudo apt-get install pulseaudio
sudo apt-get install swig
sudo apt install python-pip
sudo -H pip install --upgrade pip setuptools wheel
sudo -H apt-get install python-pyaudio python3-pyaudio
sudo -H pip install pyaudio --upgrade
sudo -H pip install --upgrade pocketsphinx
sudo -H pip install pyttsx
sudo -H pip install SpeechRecognition
sudo apt-get install gspread
sudo -H pip install gspread
sudo -H pip install --upgrade oauth2client
sudo apt-get install espeak
sudo -H pip install -U textblob
python -m textblob.download_corpora
sudo apt-get install festlex-cmu
cd /usr/share/festival/voices/english/
sudo wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_bdl_arctic-0.95-release.tar.bz2
sudo tar jxf cmu_us_bdl_arctic-0.95-release.tar.bz2
#rm /usr/share/festival/voices/english/cmu_us_bdl_arctic-0.95-release.tar.bz2
sudo ln -s cmu_us_bdl_arctic cmu_us_bdl_arctic_clunits
sudo cp /etc/festival.scm /etc/festival.scm.backup
sudo echo "(set! voice_default 'voice_cmu_us_bdl_arctic_clunits)" >> /etc/festival.scm
exit