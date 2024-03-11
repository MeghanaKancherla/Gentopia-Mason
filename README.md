# Gentopia-Mason

**IMPORTANT NOTICE: This code repository was adapted from [Gentopia.AI](https://github.com/Gentopia-AI) to support Mason Activities.** 

Author: Ziyu Yao (ziyuyao@gmu.edu)
Copyright and license should go to Gentopia.AI.

## Installation 💻
First, clone this repository:
```
git clone git@github.com:LittleYUYU/Gentopia-Mason.git
cd Gentopia-Mason
```
Next, we will create a virtual environment and install the library:
```
conda create --name gentenv python=3.10
conda activate gentenv
pip install -r requirements.txt
```

Most of the agent construction and execution activities will happen within `GentPool`. For the `gentopia` library to be used within `GentPool`, set up the global environment:
```
export PYTHONPATH="$PWD/Gentopia:$PYTHONPATH"
```
In addition, since we will be using OpenAI's API, we also need to create a `.env` file under `GentPool` and put the API Key inside. The key will be registered as environmental variables at run time.
```
cd GentPool
touch .env
echo "OPENAI_API_KEY=<your_openai_api_key>" >> .env
```
Now you are all set! Let's create your first Gentopia Agent.


## Quick Start: Clone a Vanilla LLM Agent
GentPool has provided multiple template LLM agents. To get started, we will clone the "vanilla agent" from `GentPool/gentpool/pool/vanilla_template` with the following command:
```
./clone_agent vanilla_template <your_agent_name> 
```
This command will initiate an agent template under `./GentPool/gentpool/pool/<your_agent_name>`. The agent configuration can be found in `./GentPool/gentpool/pool/<your_agent_name>/agent.yaml` (note the agent type `vanilla`). The vanilla prompt it uses can be found in the source code of `Gentopia`; see `./Gentopia/gentopia/prompt/vanilla.py`.

You can now run your agent via:
```
python assemble.py <your_agent_name>
```
This vanilla agent simply sends the received user query to the backend LLM and returns its output. Therefore, for many complicated tasks, such as those requiring accessing the latest materials, it will fail. 

## Implement a Scholar LLM Agent with Tool Augmentation
In the second trial, we will create a Scholar agent which is augmented with multiple functions to access Google Scholar in real time.

This is based on the `scholar` agent we have created in the pool. As before, in this demo we simply clone it:
```
./clone_agent scholar <your_agent_name> 
```
Like before, this command created an agent under `./GentPool/gentpool/pool/<your_agent_name>`. Note from its configuration that scholar is an `openai`-type agent. As stated in its [Gentopia's implementation](./Gentopia/gentopia/agent/openai), this type of agent allows for function calling:
> OpenAIFunctionChatAgent class inherited from BaseAgent. Implementing OpenAI function call api as agent.

The available functions to the scholar agent have been listed in its configuration file `./GentPool/gentpool/pool/<your_agent_name>/agent.yaml`, and the implementation of these tools can be found in Gentopia's source code (mostly coming from the [google_scholar.py](./Gentopia/gentopia/tools/google_scholar.py) file, in this example).

Now, you are all set to query this scholar agent for the latest papers by certain authors, the summary of a certain paper, paper citations, etc.


## Remove an Agent
Sometimes an agent can upset you. To wipe it out completely,
```
./delete_agent <your_agent_name> 
```
## Implementing GoogleSearch and PDF reader
In this trail, I have implemented the GoogleSearch method within the Scholar agent, since the google_search is already defined under tools, I had to only use this in the agent.yaml file. 
The pdf reader which I have implemented, the user searches for a paper and it is being searhed with the 'google_search' tool and returns pdf download url, then this url is read by pdf reader tool to answer the question.

```
pip install PyPDF2
```
```
./clone_agent scholar <your_agent_name> 
```
This will have both the GoogleSearch and PDF Reader functionality. 

## Bonus
GentCopy is an agent, it can search through wikipedia and give results, and it calculates math problems and gives solutions, it also converts text to speech. 
The GentCopy can be cloned.

```
./clone_agent GentCopy <your_agent_name> 
```
You can now run your agent via:
```
python assemble.py <your_agent_name>
```


