import os
import re
import subprocess
import sys
from pathlib import Path

from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext


setup(
    name="yt_summarizer",
    version="1.0.0",
    author="gptjddldi",
    description="youtube summarizer",
    python_requires=">=3.10",
    packages=find_packages('.'),
    package_dir={'': '.'},
    project_urls={
        'Source': 'https://github.com/gptjddldi/yt-summarizer',
    },
    install_requires=['moviepy', "openai", "pytube", "pywhispercpp", "tiktoken"],
)