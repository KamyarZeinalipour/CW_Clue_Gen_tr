import argparse
import time
import pandas as pd
import torch
from transformers import AutoTokenizer
from peft import AutoPeftModelForCausalLM

def get_code_completion(prompt, model, tokenizer, temperature):
    try:
        model.eval()
        outputs = model.generate(
            input_ids=tokenizer(prompt, return_tensors="pt").input_ids.cuda(),
            max_new_tokens=128,
            temperature=temperature,
            top_k=50,
            top_p=0.95,
            do_sample=True,
            no_repeat_ngram_size=4,
            repetition_penalty=1.0,
        )
        return tokenizer.batch_decode(outputs, skip_special_tokens=False)[0]
    except Exception as e:
        print(f"Error during code generation: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Generate code completions using a pre-trained model.')
    parser.add_argument('--model_path', type=str, help='Path to the pre-trained model')
    parser.add_argument('--input_file', type=str, help='Path to the input file containing prompts')
    parser.add_argument('--output_file', type=str, help='Path to save the output file')
    parser.add_argument('--temperature', type=float, default=0.2, help='Temperature for generation')
    args = parser.parse_args()

    MODEL_PATH = args.model_path
    INPUT_FILE = args.input_file
    OUTPUT_FILE = args.output_file
    TEMPERATURE = args.temperature

    print('Generation Starts')

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoPeftModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.bfloat16)
    model.cuda()

    try:
        processed_df = pd.read_csv(OUTPUT_FILE, sep='\t')
        last_index = processed_df.index[-1] if not processed_df.empty else -1
    except (FileNotFoundError, pd.errors.EmptyDataError):
        processed_df = pd.DataFrame(columns=['prompt', 'output'])
        last_index = -1

    df = pd.read_csv(INPUT_FILE)

    for i, row in df.iterrows():
        if i <= last_index:
            continue

        print("Row Number:", i)
        prompt = row['text']
        try:
            response = get_code_completion(prompt, model, tokenizer, TEMPERATURE)
            print(f'Traversing index at: {i}')
            print(response)

            processed_df = processed_df.append({'prompt': prompt, 'output': response}, ignore_index=True)

            if i % 10 == 0:
                processed_df.to_csv(OUTPUT_FILE, sep='\t', index=False)

        except Exception as e:
            print(f"Error encountered at row {i}: {e}. Waiting 2 minutes before retrying...")
            time.sleep(120)

    processed_df.to_csv(OUTPUT_FILE, sep='\t', index=False)
    print("Generation complete.")

if __name__ == "__main__":
    main()
