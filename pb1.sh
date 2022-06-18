echo "Cloning Software from github"
git clone https://github.com/monkmakes/pi_box_1.git
echo "Moving folder to /home/pi/mu_code"
mv pi_box_1 /home/pi/mu_code
echo "Installing GUI Zero"
pip3 install guizero
echo "Installing PiAnalog"
git clone https://github.com/simonmonk/pi_analog.git
cd pi_analog
sudo python3 setup.py install
cd /home/pi