Google Cloud VM Deployment (Python Script)
==========================================

📋 Overview
-----------
This project automates the deployment of a Virtual Machine (VM) on Google Cloud Platform using Python and the `gcloud` CLI. It provisions infrastructure and hosts a simple Apache-powered webpage — all with one script.

🚀 Features
-----------
- Deploys an Ubuntu 20.04 VM with:
  - 2 vCPUs
  - 8GB RAM
  - 250GB boot disk
  - Static external IP address
- Opens ports for HTTP (80) and SSH (22)
- Configures a firewall rule with the `http-server` tag
- Automates the setup using Python and shell commands

🧰 Prerequisites
----------------
- Google Cloud SDK installed and initialized (`gcloud init`)
- Billing enabled on your GCP project
- Required APIs enabled:
  - Compute Engine API
  - IAM API
- Python 3 installed on your machine

🛠️ Usage
---------
1. Clone this repository
   > git clone https://github.com/NomaanS/Google_cloud.git
   > cd Google_cloud

2. Run the deployment script
   > python main.py

3. SSH into your VM
   > gcloud compute ssh my-vm --zone=us-central1-a

4. Install Apache and host a web page (on the VM)
   > sudo apt update
   > sudo apt install apache2 -y
   > echo "Hello World!" | sudo tee /var/www/html/index.html

5. Open your browser and visit your external IP
   > http://<34.57.97.136>

🐛 Troubleshooting
------------------
- Use `gcloud compute instances list` to verify VM creation.
- Use `gcloud compute firewall-rules list` to confirm port access.
- Restart Apache if the webpage doesn't load:
  > sudo systemctl restart apache2
- Confirm the VM has the `http-server` tag:
  > gcloud compute instances describe my-vm --zone=us-central1-a --format="get(tags.items)"

📂 Files
--------
- main.py – Python deployment script
- README.txt – Project documentation
- requirements.txt – (empty, no external packages needed)

👨‍💻 Author
-----------
Nomaan S

GitHub: https://github.com/NomaanS/Google_cloud