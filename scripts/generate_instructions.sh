batch_dir="../data/gpt3_generations/"
data_dir="../data/seed_tasks.json"
openai_api="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"

python ../self_instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
    --num_instructions_to_generate 100 \
    --seed_tasks_path ${data_dir} \
    --engine "davinci" \
    --api_key ${openai_api}