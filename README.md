# openai-py-samples

**THESE SAMPLES WILL WORK ONLY WITH openai library version less than 1.0. Use pip install openai==0.28**

This repository has demo samples that showcase capabilities of azure open ai, as applied to scenarios across industry verticals. Most of the examples can be run as a streamlit app.

## Content Description

The folder **'aoai-samples'** is the root folder that contains the source code for samples related to different industry verticals.
Each sample/folder (most of them) contain a streamlit app, with filename bot-app.py than be run independently.

**Before running the samples, set the Azure open AI config parameters in aoai-samples\0_common_config\config_data.py**
**You will also need to install all python libraries mentioned in the requirements.txt file in the same folder**

The folder **'aoai-samples-shortcuts'** is the root folder that contains .bat files corresponding to the streamlit apps in the other folder. The batch files provide an easy way to run each demo on a Windows computer. It also opens up related files that can be used when running the demo scenario.

If you want to, you can of course run the streamlit app directly without the .bat files


Note: There are a few examples that point to components deployed inside an Azure Subscription. These cannot be run from this repository. 