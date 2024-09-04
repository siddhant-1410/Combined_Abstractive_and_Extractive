# Combined_Abstractive_and_Extractive
## Demo Link -  https://combinedabstractiveandextractive-2317.streamlit.app/
* The link might be slow as the project is uploaded on streamlit's free tier. Instead check out the demo video below.

  ## Demo Video :
  

https://github.com/user-attachments/assets/f3e4488f-25bc-47e9-8f79-1cee925f2302



  # Abstractive Text Summarization :
  This approach generates a summary by understanding and rephrasing the original content, often using natural language generation techniques to create new sentences that convey the main ideas
  * Used t5-small model for the project.
 
  # Extractive Text Summarization :
  This method selects and compiles key sentences or phrases directly from the original text to form a summary, focusing on identifying the most relevant parts of the content.
  Evaluated 3 different methods for text summarization:
  * TF-IDF Method
  * LSA Method
  * Frequency Count Method.

  # Performance Metrics
  * Extractive Text Summarization :- Achieved 50% summarization value by retaining most important sentences from the corpus.
  * Abstractive Text Summarization :- Achieved following ROGUE Scores over 5 epochs:-
    ![image](https://github.com/user-attachments/assets/4928aefe-d157-40eb-99cb-db6ec5790391)

  # To run the app
  ```bash
  pip install -r requirements.txt
  ```
  ```bash
  streamlit run app.py
  ```
  # Note -
  * If you torch installed with **CUDA** enabled uncomment the following line and comment the line below it.
    ![image](https://github.com/user-attachments/assets/0bc7e5a9-4392-4721-a6d9-da2d83e34f13)

    The Line was commented so to upload the app on **streamlit cloud**

