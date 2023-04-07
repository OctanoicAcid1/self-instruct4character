batch_dir="../data/gpt3_generations/"
openai_api="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"

python ../self_instruct/generate_instances.py \
    --batch_dir ${batch_dir} \
    --input_file machine_generated_instructions.jsonl \
    --output_file machine_generated_instances.jsonl \
    --max_instances_to_gen 5 \
    --engine "davinci" \
    --request_batch_size 5 \
    --api_key ${openai_api} \
    --num_instructions 5 \
    --generation_tasks_only