#!/bin/bash
#SBATCH --job-name=rhy2
#SBATCH --output=logs/rhy2.out
#SBATCH --error=logs/rhy2.err
#SBATCH --partition=general
#SBATCH --nodes=1
#SBATCH --gres=gpu:A6000:1
#SBATCH --time 01:00:00 

echo "LOADING THE ENVIRONMENT"
source ~/.bashrc
eval "$(conda shell.bash hook)"
conda activate med
echo "Starting"

# Your job commands go here




python eval.py "singlePerfect" "title"
python eval.py "singlePerfect" "description"
echo "SINGLE PERFECT DONE!!"




echo "ALL DONE!!"
