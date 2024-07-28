# Neuromatch-HCP-Working-Memory

## Abstract
Working memory refers to the ability of individuals to temporarily hold and manipulate information in the mind, and constitutes a crucial role in daily functioning (Repovs and Baddeley, 2006). Previous research has characterized working memory as a multicomponent system that correlates with multiple distinct functional connectivity patterns, including activity and interactions between the default mode network (DMN) and frontoparietal network (FPN; Murphy et al., 2020). These studies have used a variety of tasks to study WM, but one popular paradigm is the n-back task. While an understanding of the neural mechanisms underpinning working memory has important clinical implications, predicting individual working memory performance from underlying neural activity has proven challenging thus far. Here, we hypothesized that working memory performance in the 2-back task can be predicted from individuals’ whole-brain functional connectivity patterns. Replicating previous work, we used a connectome-based predictive modeling approach (CPM; Shen et al., 2017; Avery et al., 2020) to predict working memory performance of 339 participants of the Human Connectome Project (HCP). This method leverages the relationship between each individual’s whole-brain functional connectivity pattern and a behavioral measure (here, 2-back accuracy) to construct a linear predictive model of behavior. We found that whole-brain functional connectivity patterns significantly predicted 2-back task performance (positive network: Pearson’s r = 0.26, p = <0.001, MSE = 0.0078; negative network: Pearson’s r = 0.23, p < 0.001, MSE = 0.0081). These results suggest that individual differences in working memory performance can be reliably predicted from task-based functional connectivity patterns, potentially offering a neuroimaging-based biomarker for working memory capacity.

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

## Main Papers
1. [Distributed patterns of functional connectivity predict working memory performance in novel healthy and memory-impaired individuals](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8004893/)
2. [Using connectome-based predictive modeling to predict individual behavior from brain connectivity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5526681/)
3. [Using modular connectome-based predictive modeling to reveal brain-behavior relationships of individual differences in working memory](https://pubmed.ncbi.nlm.nih.gov/37349540/)

## References
1. [Neuromatch Guide on fMRI Data](https://compneuro.neuromatch.io/projects/fMRI/README.html)
2. [Brain Connectivity Related to Working Memory Performance](https://www.jneurosci.org/content/jneuro/26/51/13338.full.pdf)
3. [Is a Responsive Default Mode Network Required for Successful Working Memory Task Performance?](https://www.jneurosci.org/content/35/33/11595.short)
4. [Coactivation of the Default Mode Network regions and Working Memory Network regions during task preparation](https://www.nature.com/articles/srep05954)
5. [The Default Mode Network and the Working Memory Network Are Not Anti-Correlated during All Phases of a Working Memory Task](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0123354)
6. [DOES THE DEFAULT-MODE FUNCTIONAL CONNECTIVITY OF THE BRAIN CORRELATE WITH WORKING-MEMORY PERFORMANCES?](https://www.architalbiol.org/index.php/aib/article/view/14711)
7. [Age-related alterations in default mode network: impact on working memory performance](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2842461/)