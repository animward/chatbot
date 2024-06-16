# Ultimate Chatbot Solution

### Seamlessly Fine-Tunable and Performance-Optimized

Unlock the full potential of your interactions with our incredibly straightforward yet powerful chatbot. Designed for simplicity and efficiency, this chatbot can be effortlessly fine-tuned to meet your specific needs.

## Key Features

- **Intuitive Fine-Tuning**: Easily customize and adapt the chatbot to suit your unique requirements and preferences.

- **Data Cleaning Mastery**: Automatically cleans and processes input data, ensuring only the highest quality data is utilized.

- **Optimized Output**: Delivers refined and enhanced responses for superior performance and user experience.

## Getting Started

To get started with the chatbot, follow these simple steps:

1. **Clone the repository**:
git clone https://github.com/animward/chatbot.git


2. **Navigate to the project directory**:
cd chatbot


3. **Install the required packages**:
pip install -r requirements.txt


4. **Add your input data**: Place your input data into the `data/input/example_data.txt` file.

5. **Run the chatbot**:
python run.py


## Example Usage

Place your input data in the `data/input/example_data.txt` file. The cleaned output will be saved in the `data/output/output_cleaned.txt` file.

## Using the AI to Generate Prompts for Itself

One of the standout features of this chatbot is its ability to generate prompts for itself. Here's how you can leverage this feature:

1. **Prepare Input Data**: Ensure your `example_data.txt` contains relevant information or data you want the AI to process.

2. **Run the Script**: Execute the script to clean the data and generate prompts.
python run.py

3. **Review Output**: Check the `data/output/output_cleaned.txt` file for the cleaned data and generated prompts.

4. **Use Generated Prompts**: Utilize the generated prompts to further enhance the chatbot’s responses or to guide its interactions more effectively.

### Other Features
1. **Letter-by-Letter Printing**: Implements a typewriter effect for displaying the chatbot's responses, enhancing the user experience by simulating real-time typing.

1. **Chat Memory**: Preserves conversation history to maintain context, ensuring more coherent and contextually aware interactions.

1. **File Reading and Cleaning**: Automates reading and preprocessing of text files, including normalizing whitespace, removing unwanted characters, converting to lowercase, and eliminating duplicate lines.

1. **Prompt Generation**: Utilizes pre-cleaned data from files to generate contextually relevant prompts, improving the relevance and quality of responses.

![Self-Prompt Generation Example](images/prompt_generation_example.PNG)

## Contribution

Feel free to fork this repository, make enhancements, and submit pull requests. We welcome contributions that improve the functionality, performance, or usability of the chatbot.
