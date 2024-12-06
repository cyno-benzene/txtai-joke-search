# Reddit Jokes Search using txtai and Streamlit
This project is a web application that allows users to search for jokes using natural language queries. The application leverages the txtai library to perform semantic search on a dataset of jokes, providing relevant results based on the user's input. It was also made with the purpose of experimenting with txtai's search capabilities and potential for RAG.

## Features
- Search Jokes: Enter a search query to find jokes that match the input.
- Adjustable Results Limit: Select the number of search results to display (10, 20, 50, or 100).
- Responsive Layout: The search results are displayed in a responsive grid layout.


## Installation
To run this project, you need to have Python installed on your machine. Follow the steps below to set up and run the application:

1. Clone the repository:
    ```
    git clone https://github.com/cyno-benzene/jokes-search-txtai.git
    cd jokes-search-txtai
    ```

2. Create a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```   

4. Run all the cells in the notebook to generate embeddings for all the jokes(195K) in the dataset, else, ensure that the jokes embeddings is available at ./data/jokes.tar.gz.

5. Run the application:
    ```
    streamlit run app.py
    ```

6. Usage

    Open your web browser and navigate to` http://localhost:8501.`
    Enter a search query in the input box.

    Adjust the number of results to display using the slider.

    View the search results, which include the joke text, answer, and relevance score.

## Project Structure
- app.py: The main application file that contains the Streamlit code and the search logic.
- data/jokes.tar.gz: The dataset file containing the jokes embeddings.
- requirements.txt: A list of dependencies required to run the application.
## Dependencies
- streamlit: For building the web application interface.
- pandas: For data manipulation and analysis.
- txtai: For performing semantic search on the jokes dataset.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue.


## Acknowledgements
The txtai library for providing powerful semantic search capabilities.
The creators of the <a href="https://github.com/taivop/joke-dataset">jokes dataset</a> used in this project.
Enjoy searching for jokes and have fun! 🤡

