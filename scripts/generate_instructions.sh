batch_dir="/workspaces/self-instruct4character/data/gpt3_generations/"
data_dir="/workspaces/self-instruct4character/data/seed_tasks.json"

python /workspaces/self-instruct4character/self_instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
    --num_instructions_to_generate 100 \
    --seed_tasks_path ${data_dir} \
    --engine "davinci" \
    --api_key "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"