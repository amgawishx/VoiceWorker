import streamlit as st
from faster_whisper import WhisperModel
from torch import cuda
from typing import List

# List of available model sizes
AVAILABLE_MODELS: List[str] = [
    "tiny", "tiny.en", "base", "base.en", "small", "small.en", 
    "medium", "medium.en", "large-v1", "large-v2"
]

# Supported language codes
LANGUAGE_CODES: List[str] = [
    "auto", "af", "sq", "am", "ar", "hy", "as", "az", "ba", "eu", "be", "bn", "bs", "br", "bg", "my", 
    "ca", "zh", "hr", "cs", "da", "nl", "en", "et", "fo", "fi", "fr", "gl", "ka", "de", "el", "gu", "ht", 
    "ha", "haw", "he", "hi", "hu", "is", "id", "it", "ja", "jv", "kn", "kk", "km", "ko", "lo", "la", "lv", 
    "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "ne", "no", "nn", "oc", "ps", "fa", "pl", 
    "pt", "pa", "ro", "ru", "sm", "gd", "sr", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", 
    "tl", "tg", "ta", "tt", "te", "th", "ti", "tn", "tr", "tk", "uk", "ur", "uz", "vi", "cy", "xh", "yi", 
    "yo", "zu"
]

# Streamlit page configuration
st.set_page_config(page_title="VoiceWorker")
st.title("Transcribe _Audio_ :microphone: with :red[Whisper]")
st.write("#### Quick Settings")

# Model and language selection
settings_col1, settings_col2 = st.columns(2)
with settings_col1:
    model_size: str = st.selectbox("**Choose your model:**", AVAILABLE_MODELS, index=len(AVAILABLE_MODELS) - 1)
with settings_col2:
    language: str = st.selectbox("**Choose your language:**", LANGUAGE_CODES, index=0)

st.write("\n#### Options")

# Audio input options
options_col1, options_col2 = st.columns(2)
if "audio_file" not in st.session_state:
    st.session_state.audio_file = False
if "audio_input" not in st.session_state:
    st.session_state.audio_input = False

with options_col1:
    audio_file = st.file_uploader(
        "**Upload your audio/video file for transcription:**",
        accept_multiple_files=False,
        disabled=st.session_state.audio_input,
    )
    st.session_state.audio_file = True if audio_file else False

with options_col2:
    audio_input = st.audio_input(
        "**Record your audio for transcription:**", disabled=st.session_state.audio_file
    )
    if audio_input and not st.session_state.audio_input:
        st.session_state.audio_input = True
        st.rerun()
    elif not audio_input and st.session_state.audio_input:
        st.session_state.audio_input = False
        st.rerun()

# Determine device availability
device: str = "cuda" if cuda.is_available() else "cpu"
segments: List[str] = None

# Load Whisper model
with st.spinner("Loading your model, please wait..."):
    global model
    model = WhisperModel(model_size, device=device, compute_type="float16")

# Handle audio input and transcription
if audio_file or audio_input:
    input_audio = audio_file if audio_file else audio_input

    with st.spinner("Transcribing your audio, please wait..."):
        if language != "auto":
            segments, info = model.transcribe(input_audio, language=language, vad_filter=True)
        else:
            segments, info = model.transcribe(input_audio, vad_filter=True)

# Display transcription results
st.write("\n#### Transcription: ")
if segments:
    st.text_area("**Output:**", value=" ".join([segment.text for segment in segments]), disabled=True)
else:
    st.info("Please upload or record an audio to transcribe!")
