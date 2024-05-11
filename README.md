# Turkish Crossword Clue Generator

[[`Paper`](paper_link)] [[`Project`](https://segment-anything.com/)] [[`Dataset TAC`](https://huggingface.co/datasets/Kamyar-zeinalipour/TAC)] [[`Dataset T4TAC`](https://huggingface.co/datasets/Kamyar-zeinalipour/T4TAC)] [[`BibTeX`](#citing-turkish-crossword-clue-generator)]

This repository contains code for generating Turkish crossword clues and answer pairs using two different language models: llama-chat-7b and llama-chat-13b.

## Installation
The code requires `python>=3.8`,  `pandas>=1.5.3`, `peft>=0.10.0`, `torch>=1.13.1+cu117` and as well as
`transformers>=4.40.2`. 

```
pip install transformers peft pandas
```

# <a name="GettingStarted"></a>Getting Started
 

### Models

The models used in this project are:

- llama13B_turkish_crossword_clue_gen
- llama7B_turkish_crossword_clue_gen

The llama13B_turkish_crossword_clue_gen model can be downloaded [here](https://huggingface.co/Kamyar-zeinalipour/llama13B_turkish_crossword_clue_gen). The llama7B_turkish_crossword_clue_gen model can be downloaded [here](https://huggingface.co/Kamyar-zeinalipour/llama7B_turkish_crossword_clue_gen).

### Usage


### Prepare Input:
Create a CSV file (e.g., input.csv) with a column named text containing the prompts (answers) for which you want to generate clues.

### Run the Script
```
python generate_clues.py --model_path <model_path> --input_file <input_file_path> --output_file <output_file_path> --temperature <set_temp>
```
- Replace <model_path> with the path to the url of the pre-trained model.
- Replace the input <input_file_path> with your input file.
- Replace the input <output_file_path> with your output file path.
- Replace <set_temp> with your desired temperature. 
  
## Notes
- The script includes error handling and retry mechanisms to handle potential issues during generation.
- The **temperature** parameter controls the creativity of the generated clues. A lower temperature leads to more deterministic and coherent clues.
- The script automatically resumes processing from the last processed row in the output file, allowing for interrupted runs to be continued.

## Datasets

The dataset TAC can be downloaded [here](https://huggingface.co/datasets/Kamyar-zeinalipour/TAC). The dataset T4TAC can be downloaded [here](https://huggingface.co/datasets/Kamyar-zeinalipour/T4TAC). By downloading the datasets you agree that you have read and accepted the terms of the Turkish Crossword Clue Generator Research License.
  
## License

The model is licensed under the [MIT License](LICENSE).

## Contributors

The Segment Anything project was made possible with the help of many contributors (alphabetical):

Kamyar Zeinalipour, Leonardo Rigutini, Marco Gori, Marco Maggini, Yusuf Gökberk Keptiğ

## Citing Turkish Crossword Clue Generator
If you use llama13B_turkish_crossword_clue_gen or llama7B_turkish_crossword_clue_gen in your research, please use the following BibTeX entry.

```
@article{article,
  title={A Turkish Educational Crossword Puzzle
Generator},
  author={Kamyar Zeinalipour, Yusuf Gökberk
Keptiğ, Marco Maggini, Leonardo
Rigutini, and Marco Gori},
  journal={arXiv:number},
  year={2024}
}
```
