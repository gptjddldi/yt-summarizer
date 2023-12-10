## About The Project
Because most consumer computers only have a CPU and not a high-performance GPU, many end users cannot run the original Whisper model out of the box.
This program summarises a YouTube video using the Whisper model on a laptop without a GPU.
It's slower than a programme that uses a GPU, but it's still useful.

## Features
- Takes an English-speaking YouTube URL and summarises it for you
- Efficiently breaks up long conversations
- Rambling summaries with great prompts

## Installation
1. Install ```ffmpeg```
```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

2. Install ```yt_summarizer``` from GitHub
```
pip install git+https://github.com/gptjddldi/yt-summarizer.git
```

## Example

```python
from yt_summarizer import summarizer

sumarizer = summarizer.Summarizer(open_ai_key="YOUR OPEN_AI KEY")

print(sumarizer.summarize_youtube("https://www.youtube.com/watch?v=iNyUmbmQQZg"))
```

#### result
```
The main idea of the conversation is the potential of artificial intelligence (AI) 
and deep learning models in revolutionizing the fields of biomedical research, 
protein structure prediction, medical diagnostics, and patient care.

Key Points:
1. AlphaFold, a derivative of DeepMind, has significantly accelerated protein structure prediction from two to three years to just two to three minutes.
2. AI and deep learning models can predict three-dimensional protein structures, RNA, antibodies, and even identify missense mutations in the genome.
3. AI has the ability to create new proteins that do not exist in nature.
4. The conversation questions whether the AI should be recognized separately from the researchers who developed the transformer model.
5. Medical errors and diagnostic accuracy are significant challenges in the healthcare system.
6. AI can aid in precision medicine by improving diagnostic accuracy and identifying conditions before clinical symptoms manifest.
7. Retina scans and medical imaging can be analyzed by AI to detect various diseases and conditions, often outperforming expert physicians.
8. Machine vision during colonoscopy has shown better detection of polyps compared to gastroenterologists.
9. AI can analyze slides in pathology to determine genomic mutations, tumor location, and patient prognosis.
10. Deep neural networks and transformer models like GPT-4 have the potential to revolutionize medicine by providing multimodal capabilities and self-supervised learning.
11. AI can liberate clinicians and patients from data entry tasks, enable synthetic notes derived from conversations, and streamline healthcare processes.
12. Chat GPT can assist in diagnosing challenging cases and perform as well as or better than expert clinicians in certain scenarios.
13. The conversation emphasizes the importance of validation and ensuring that the benefits of AI outweigh any risks.
14. The integration of AI in healthcare has the potential to transform the patient-doctor relationship and provide more personalized care with the gift of time.

Key Terms and Phrases: Scripps Research, protein structure prediction, AlphaFold, artificial intelligence, deep learning models, 
medical errors, diagnostic accuracy, precision medicine, retina scans, medical imaging, colonoscopy, pathology slides, 
deep neural networks, transformer models, GPT-4, machine vision, keyboard liberation.

Concepts and Ideas:
1. AlphaFold, a derivative of DeepMind, significantly speeds up protein structure prediction.
2. AI has the potential to improve diagnostic accuracy and enable precision medicine.
3. Deep learning models, such as GPT-4, can integrate language, images, and speech, revolutionizing healthcare.
4. AI can liberate clinicians from data entry tasks and improve the patient-doctor relationship.

Summary:
The conversation explores the potential of AI and deep learning models in transforming various aspects of biomedical research and healthcare. 
AlphaFold, a derivative of DeepMind, has revolutionized protein structure prediction, while AI has shown promise in improving diagnostic accuracy and enabling precision medicine. Medical imaging, 
including retina scans and chest x-rays, can be analyzed by AI to detect diseases and conditions better than expert physicians. 
AI's integration, particularly in deep neural networks and transformer models like GPT-4, offers significant advancements in multimodal capabilities and self-supervised learning. 
The conversation emphasizes the importance of validation and balancing the benefits and risks of AI in healthcare. 
Ultimately, the integration of AI has the potential to liberate clinicians from administrative tasks and enhance the patient-doctor relationship with the gift of time.

```
