import os 


def main():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_folder)
    streamlit_command = "python -m streamlit run ui.py"
    os.system(streamlit_command)

if __name__ == "__main__":
    main()