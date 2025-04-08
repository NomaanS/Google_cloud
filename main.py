import subprocess
import time

# Configuration
PROJECT_ID = subprocess.getoutput("gcloud config get-value project")
ZONE = "us-central1-a"
REGION = "us-central1"
VM_NAME = "my-vm"
MACHINE_TYPE = "e2-standard-2"
IMAGE_FAMILY = "ubuntu-2004-lts"
IMAGE_PROJECT = "ubuntu-os-cloud"
DISK_SIZE = "250"
FIREWALL_NAME = "allow-http-ssh"
STATIC_IP_NAME = f"{VM_NAME}-ip"

def run_cmd(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error:\n{result.stderr}")

def main():
    print("Creating external static IP...")
    run_cmd(f"gcloud compute addresses create {STATIC_IP_NAME} --region={REGION}")

    print("Creating firewall rule...")
    run_cmd(f"""
        gcloud compute firewall-rules create {FIREWALL_NAME} \
        --allow=tcp:22,tcp:80 \
        --source-ranges=0.0.0.0/0 \
        --target-tags=http-server
    """)

    print("Creating VM...")
    run_cmd(f"""
        gcloud compute instances create {VM_NAME} \
        --zone={ZONE} \
        --machine-type={MACHINE_TYPE} \
        --image-family={IMAGE_FAMILY} \
        --image-project={IMAGE_PROJECT} \
        --boot-disk-size={DISK_SIZE}GB \
        --tags=http-server \
        --address={STATIC_IP_NAME}
    """)

    print("Waiting for instance to initialize...")
    time.sleep(10)

    print("VM created. SSH in using:")
    print(f"gcloud compute ssh {VM_NAME} --zone={ZONE}")

if __name__ == "__main__":
    main()
