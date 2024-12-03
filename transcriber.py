import os

import openai


def transcribe_audio(file_path: str, api_key: str) -> str:
    """
    Transcribe audio from a file using OpenAI's Whisper API.

    Args:
        file_path (str): Path to the audio file.
        api_key (str): Your OpenAI API key.

    Returns:
        str: The transcription of the audio file.
    """
    openai.api_key = api_key

    try:
        print(f"Uploading audio file '{file_path}' for transcription...")
        with open(file_path, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)

        transcription = response.get("text", "")
        print(f"Transcription for '{file_path}' completed successfully.")
        return transcription
    except openai.error.OpenAIError as e:
        print(f"An OpenAI API error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


def consolidate_transcripts(transcripts: list) -> str:
    """
    Combine a list of transcript texts into a single string.

    Args:
        transcripts (list): List of individual transcript strings.

    Returns:
        str: Combined transcript.
    """
    return " ".join(transcripts)


def transcribe_files(directory_path: str, api_key: str) -> list:
    """
    Transcribe all audio files in a directory.

    Args:
        directory_path (str): The path to the directory containing audio files.
        api_key (str): Your OpenAI API key.

    Returns:
        list: List of transcriptions for all audio files in the directory.
    """
    transcripts = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.mp3', '.wav', '.m4a', '.flac')):  # Filter audio files
            file_path = os.path.join(directory_path, filename)
            print(f"Processing file: {filename}")
            transcript = f"Wypowiedź {os.path.splitext(filename)[0]}: {transcribe_audio(file_path, api_key)}"
            if transcript:  # Only add valid transcripts
                transcripts.append(transcript)

    return transcripts


def prepare_prompt(transcripts: list) -> str:
    """
    Prepare a prompt for analysis based on the provided transcripts.

    Args:
        transcripts (list): List of transcript texts.

    Returns:
        str: Formatted prompt string.
    """
    context = consolidate_transcripts(transcripts)
    prompt = (
        
    )
    return prompt
