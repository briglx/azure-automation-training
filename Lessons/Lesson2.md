# Lesson 2

This lesson covers the following

- Create New Project
- Containerize Job for Local deployment

## Training – Section 1.2 – Create New Project

Open Previous Project (Training) From Lesson 1
-	Navigate to `/path/to/src/training`
-	Activate training conda environment `conda activate training`
-	Open VS Code with `code .`

Install VSCode Extensions
-	Open the Extension tab in VSCode (ctrl + shift+x)
-	Install Python Extension
-	Install Docker Extension

Create Requirements Files
-	Create two files named `requirements.txt` and `requirements-dev.txt`
-	In `requirements-dev.txt` add
    - black
    - flake8
-	Install project dev requirements with `python -m pip install -r requirements-dev.txt`

Run Dev Tools from the command line

```bash
flake8 main main.py
black main.py
```

## Training – Section 1.4 – Containerize Job for Local deployment

Create Docker File in your project
-	Create a new file called `dockerfile`
-	Edit the file to match the example found https://github.com/briglx/PythonAzureVmUtilization/blob/master/dockerfile.dev

Build and run your image. From the cammand line

```bash
> docker build --pull --rm -f "dockerfile" -t training:latest "."
> docker run --rm -it  training:latest

# From the docker command prompt run your app
docker#> python main.py

```