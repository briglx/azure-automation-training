# Lesson 1

This lesson guides you through setting up your environment and creating your first hello world project in python. 

## Install Tools 

- Install Python – Download python 3.8 from https://www.python.org/downloads/release/python-384/ 
- Install VSCode – Download from https://code.visualstudio.com/ 
- Install Git – For Windows download Git for Windows from  https://gitforwindows.org/ 
- Install Anaconda - https://www.anaconda.com/products/individual 
- Install Docker – Download Docker Desktop from https://www.docker.com/products/docker-desktop 
- Create Account on Github – Useful for shared projects through this training 

## Create Your Project

- Open your Anaconda Prompt 
- Create a `src` folder somewhere on your computer 
- Create a new Folder under `src` called `training` 
- Navigate to `/path/to/src/training` 
- Create new conda environment `conda create -n training python=3.8` 
- Activate the new environment `conda activate training` 
- Open VSCode `code .` 
- Create a new file called `main.py` 

```python
#!/usr/bin/python 

if __name__ == "__main__": 

    print("hello world") 
```

Run your file from the Anaconda prompt 

```bash
$(training)path/to/src/training>python main.py 
```
  