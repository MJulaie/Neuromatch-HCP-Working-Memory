# Neuromatch-HCP-Working-Memory

## Introduction
The Default Mode Network (DMN) is a network of brain regions that show higher activity when the mind is at rest compared to when it is focused on external tasks. Working Memory (WM) refers to the system responsible for temporarily holding and manipulating information. Understanding the interplay between DMN and WM during tasks and rest periods can provide insights into cognitive functions and neural mechanisms.

In this project, we utilize data from the Human Connectome Project (HCP), specifically focusing on task and behavior data. By leveraging HCP data, this project aims to shed light on the dynamic relationship between networks in resting-state and active cognitive processes.

## Getting Started
1. Creating python virtual environment inside the project directory:
```shell
python -m venv .venv
```

2. Activate development environment:

```shell
source .venv/bin/activate

## for verification only
which python
```

3. Install dependencies:
```shell
pip install -r requirements.txt
```

4. Run Jupyter Lab:
```shell
jupyter lab
```

5. Open `download_hcp_data.ipynb` and download dataset in `data` directory

## References
1. [Neuromatch Guide on fMRI Data](https://compneuro.neuromatch.io/projects/fMRI/README.html)
2. [Brain Connectivity Related to Working Memory Performance](https://www.jneurosci.org/content/jneuro/26/51/13338.full.pdf)
3. [Is a Responsive Default Mode Network Required for Successful Working Memory Task Performance?](https://www.jneurosci.org/content/35/33/11595.short)
4. [Coactivation of the Default Mode Network regions and Working Memory Network regions during task preparation](https://www.nature.com/articles/srep05954)
5. [The Default Mode Network and the Working Memory Network Are Not Anti-Correlated during All Phases of a Working Memory Task](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0123354)
6. [DOES THE DEFAULT-MODE FUNCTIONAL CONNECTIVITY OF THE BRAIN CORRELATE WITH WORKING-MEMORY PERFORMANCES?](https://www.architalbiol.org/index.php/aib/article/view/14711)
7. [Age-related alterations in default mode network: impact on working memory performance](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2842461/)