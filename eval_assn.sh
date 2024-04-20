#!/bin/bash
#SBATCH --job-name=assonance
#SBATCH --output=logs/assonance.out
#SBATCH --error=logs/assonance.err
#SBATCH --partition=general
#SBATCH --nodes=1
#SBATCH --gres=gpu:A6000:1
#SBATCH --time 08:00:00 

echo "LOADING THE ENVIRONMENT"
source ~/.bashrc
eval "$(conda shell.bash hook)"
conda activate med
echo "Starting"

# Your job commands go here




python eval.py "assonance" "title"
python eval.py "assonance" "description"
echo "ASSONANCE DONE!!"






echo "ALL DONE!!"