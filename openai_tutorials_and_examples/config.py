import numpy as np
import pandas as pd
import time
import os
import openai
from openai.embeddings_utils import distances_from_embeddings

openai.api_key = os.environ["ChatGPT"]

model = "gpt-3.5-turbo"
