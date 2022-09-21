echo 'Installing Honeypot VPN Enviroment'
echo 'Author: Ivan Yuquilima - 2022'
apt install git
curl -fsSL https://get.docker.com -o get-docker.sh
sh ./get-docker.sh
mkdir -p ~/.docker/cli-plugins/
curl -SL https://github.com/docker/compose/releases/download/v2.3.3/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
chmod +x ~/.docker/cli-plugins/docker-compose
apt-get install docker-compose -y
echo 'Creating user honeypot'
useradd –m honeypot
chsh –s /bin/bash honeypot
echo 'Using user honeypot to start the Honeypot VPN'
su – honeypot
echo 'Cloning REPO'
git clone https://github.com/ivan3129/honeypot-vpn.git
cd honeypot-vpn/
echo 'Honney environment created successfully!' 
echo 'User honeypot was added'
ls
echo 'To start the Honeypot VPN run the script with sudo ./start-honeypot-docker.sh'
echo 'To stop the Honeypot VPN run the script with sudo ./stop-honeypot-docker.sh'


