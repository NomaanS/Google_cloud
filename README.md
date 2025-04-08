# Google Cloud VM Deployment (Python Script)

## Overview
This project contains a Python script that automates the deployment of a VM on Google Cloud Platform using the `gcloud` CLI.

## Features
- Creates an Ubuntu 20.04 VM with:
  - 2 vCPUs
  - 8GB RAM
  - 250GB disk
  - Static external IP
- Opens ports for HTTP and SSH
- Tags the VM with `http-server` for firewall rules

## Prerequisites
- Google Cloud SDK installed and authenticated (`gcloud init`)
- Billing enabled on your GCP project
- APIs enabled:
  - Compute Engine API
  - IAM API

## Usage

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/gcp-vm-deployment.git
   cd gcp-vm-deployment
   ```

2. Run the Python script:
   ```bash
   python3 main.py
   ```

3. SSH into your VM:
   ```bash
   gcloud compute ssh my-vm --zone=us-central1-a
   ```

4. On the VM, install Apache and test HTTP:
   ```bash
   sudo apt update
   sudo apt install apache2 -y
   echo "Hello World from GCP!" | sudo tee /var/www/html/index.html
   ```

5. Visit your external IP to see the page.

## Troubleshooting
- If firewall rules already exist, use `gcloud compute firewall-rules list` to check.
- Use `gcloud compute instances list` to confirm the VM was created.
