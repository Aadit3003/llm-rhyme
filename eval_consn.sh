#!/bin/bash
#SBATCH --job-name=l2_consonance
#SBATCH --output=logs/llama2/consonance.out
#SBATCH --error=logs/llama2/consonance.err
#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=aaditd@andrew.cmu.edu
#SBATCH -N 1
#SBATCH -p general
#SBATCH --gres=gpu:A6000
#SBATCH --mem=32G
#SBATCH --time=08:00:00

echo "LOADING THE ENVIRONMENT"
source ~/.bashrc
eval "$(conda shell.bash hook)"
conda activate med
echo "Starting"

# Your job commands go here




python eval.py "llama2" "consonance" "title"
# python eval.py "llama2" "consonance" "description"
echo "CONSONANCE DONE!!"






echo "ALL DONE!!"
