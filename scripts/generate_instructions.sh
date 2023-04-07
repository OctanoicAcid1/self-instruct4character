batch_dir="../data/gpt3_generations/"
data_dir="../data/seed_tasks.json"
openai_api="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"

python ../self_instruct/bootstrap_instructions.py \
    --batch_dir ${batch_dir} \
    --num_instructions_to_generate 500 \
    --seed_tasks_path ${data_dir} \
    --engine "davinci" \
    --api_key ${openai_api}