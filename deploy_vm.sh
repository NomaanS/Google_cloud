#!/bin/bash
gcloud compute instances create my-vm \
  --zone=us-central1-a \
  --machine-type=e2-standard-2 \
  --image-family=ubuntu-2004-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=250GB \
  --tags=http-server \
  --address=my-vm-ip
