# A Turkish Crossword Clue Generator

[[`Paper`](https://arxiv.org/abs/2405.07035)] [[`TAC Dataset`](https://huggingface.co/datasets/Kamyar-zeinalipour/TAC)] [[`T4TAC Dataset`](https://huggingface.co/datasets/Kamyar-zeinalipour/T4TAC)] [[`BibTeX`](#citing-a-turkish-crossword-clue-generator)] 

This repository contains the code for the first Turkish crossword puzzle generator that harnesses the power of large language models (LLMs) to empower education. Our paper, **"A Turkish Crossword Clue Generator"**, delves into the details of the project.

## Key Features

- Crossword Generation: Generate engaging Turkish crossword puzzles on-the-fly, leveraging LLMs to create a stimulating educational experience.
- Dual Dataset Advantage:
  - A dataset of over 180,000 answer-clue pairs fuels the generation of contextually relevant clues for given answers.
  - A separate dataset with over 35,000 text, answer, category, and clue samples enables tailored clue creation for specific texts and keywords within desired categories.
- Interactive Learning Tool: Go beyond mere entertainment! This generator fosters interactive learning, promoting memory retention, vocabulary expansion, and problem-solving skills.
- Annotated Results: We explored two crossword clue creation methods: one with set answers and another categorizing text-generated clues. Both approaches allow educators to inject custom clues for specific learning objectives (see paper). A sample Turkish crossword crafted using this system is depicted in [Figure 1](#a-sample-turkish-crossword) (see paper).
### A sample Turkish Crossword (Figure 1)
<p float="left">
  <img src="assets/tr_crossword (1).png?raw=true" width="75.5%" />
</p>

## Methodology and Evaluation
Our study evaluated three LLM models – *GPT3.5-Turbo*, *Llama-2-7b-chat-hf*, and *Llama-2-13b-chat-hf*– on their ability to generate Turkish crossword clues using the *T4TAC* dataset.  While the base versions of Llama-2 models exhibited initial limitations with Turkish, fine-tuning on *T4TAC* significantly improved their performance.  Human evaluations by native Turkish speakers ensured the linguistic and cultural accuracy of the generated clues (details in the paper).

### Evaluation Results (Figure 2 & Figure 3)

Here, we present the results of our evaluation:

* **Left-hand figure:** This figure shows separate GPT-4 ratings, which are not directly related to the evaluation of the three LLM models in this project. (See Figure 2)
* **Right-hand figure:** This figure depicts the evaluation of the three LLM models – *GPT3.5-Turbo*, *Llama-2-7b-chat-hf*, and *Llama-2-13b-chat-hf* – on their ability to generate Turkish crossword clues using the *T4TAC* dataset. (See Figure 3)
<p float="left">
 <img src="assets/gpt_rating.png?raw=true" width="38.25%" />
 <img src="assets/rating_models.png?raw=true" width="59.5%" /> 
</p>

## Conclusion

This project introduces the Turkish Educational Generator, a novel LLM-powered tool designed to create dynamic crosswords in Turkish for educational purposes.  Educators can leverage this system to generate subject-specific crosswords, enhancing student engagement and learning retention.  We further contribute to the field by providing two comprehensive datasets: one with expert-crafted answer-clue pairs and another with generated clues with corresponding text, answers, and categories.  These datasets are valuable resources for educational system development and research.  Future work includes expanding our tool to additional languages and exploring advanced LLM techniques to refine clue generation, pushing the boundaries of educational technology.

Getting Started
---------------
### Prerequisites

* `Python 3.7` or later
* `PyTorch 1.9` or later
* `Pandas 1.5.3` or later (install with `pip install pandas`)
* Transformers library (install with `pip install transformers`)
* PEFT library (install with `pip install peft`)

### Installation

1. Clone this repository: `git clone https://github.com/your-username/code-completion-generation.git`

 ## Datasets
- **The *TAC* dataset** of over 180,000 answer-clue pairs fuels the generation of contextually relevant clues for given answers.
- **The *T4TAC* dataset**  with over 35,000 text, answer, category, and clue samples enables tailored clue creation for specific texts and keywords within desired categories.
The *TAC* dataset can be downloaded [here](https://huggingface.co/datasets/Kamyar-zeinalipour/*TAC*). The *T4TAC* dataset can be downloaded [here](https://huggingface.co/datasets/Kamyar-zeinalipour/T4TAC). By downloading the datasets you agree that you have read and accepted the terms of the A Turkish Crossword Clue Generator Research License.

### Models

The models used in this project are:

- llama13B_turkish_crossword_clue_gen
- llama7B_turkish_crossword_clue_gen

The llama13B_turkish_crossword_clue_gen model can be downloaded [here](https://huggingface.co/Kamyar-zeinalipour/llama13B_turkish_crossword_clue_gen). The llama7B_turkish_crossword_clue_gen model can be downloaded [here](https://huggingface.co/Kamyar-zeinalipour/llama7B_turkish_crossword_clue_gen).

### Usage

1. Prepare Input: Create a CSV file (e.g., input.csv) with a column named text containing the prompts (answers) for which you want to generate clues.
2. Run the script using the following command:
```
python generate_clues.py --model_path <model_path> --input_file <input_file_path> --output_file <output_file_path> --temperature <set_temp>
```
- Replace <model_path> with the path to the url of the pre-trained model.
- Replace the input <input_file_path> with your input file.
- Replace the input <output_file_path> with your output file path.
- Replace <set_temp> with your desired temperature. 
### Example
```
python generate_clues.py --model_path /path/to/model --input_file input.csv --output_file output.csv --temperature 0.5
```

This will generate code completions for the prompts in `input.csv` using the pre-trained model at `/path/to/model` and save the output to `output.csv` with a temperature value of 0.5.
  
## Notes
- The script includes error handling and retry mechanisms to handle potential issues during generation.
- The **temperature** parameter controls the creativity of the generated clues. A lower temperature leads to more deterministic and coherent clues.
- The script automatically resumes processing from the last processed row in the output file, allowing for interrupted runs to be continued.
  
## License

The model is licensed under the [MIT License](LICENSE).

## Contributors

A Turkish Crossword Clue Generator paper was made possible with the help of many contributors (alphabetical):

Kamyar Zeinalipour, Leonardo Rigutini, Marco Gori, Marco Maggini, Yusuf Gökberk Keptiğ

## Citing A Turkish Crossword Clue Generator
If you use llama13B_turkish_crossword_clue_gen or llama7B_turkish_crossword_clue_gen in your research, please use the following BibTeX entry.

```
@misc{zeinalipour2024turkish,
      title={A Turkish Educational Crossword Puzzle Generator}, 
      author={Kamyar Zeinalipour and Yusuf Gökberk Keptiğ and Marco Maggini and Leonardo Rigutini and Marco Gori},
      year={2024},
      eprint={2405.07035},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
