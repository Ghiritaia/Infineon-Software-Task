# Infineon-Software-Task
A small software Task consisting of reading an Excel file and adding up some values

### Intro
This is my attempt at solving a task given by the infineon. The task was to write an Excel file reader that would take some cmd parameters and would look up some data in the file.

### Approach
There are a million ways to do this task. I decided to go with python this time because of my experience with the language and its flexibility for such small tasks. The Script uses one external package (explained later) and is kept as simple as possible but also packed with features. The task at hand hand was described as one hour task so I tried not to overengineer it.

### Features and usage
When you first start the script a Prompt will appear which asks you to input the path to the excel File. Only full paths work at the moment no relative paths. If the script is able to find an excel file at the given location the user will be asked to input his/her commands. The software will check is the input is valid and return the desired value. If the input is deemed invalid, the program will tell its user with part it did not like. Typing:

`quit`

anywhere in the the programm will stop it imidiatly. If you provided a valid path but the script still says it cant open the file, an import the error might br the case. I provided my virtual enviroment for testing purposes which should include the needed package, if you don't want to use my venv to test the code, you can just install the package yourself using:

`pip install xlrd`

everything should work from here.

### Acknowledgements
As I was trying to resemble my real work output for this task some aspects of the program came in short. There are a few things that i could be inproved:
1. Accepting relative paths would be a nice to have feature
2. Accepting mutliple sheets of an excel file. The code only works on the first sheet of the xlsx file. Should there be multiple sheets the programm would never know about them. Now this would be an advanced feature of this little tool that could be implemented if needed. 
3. Code assumes that the skills column is always the second column. Now this would not be a lot of work to implement. While coding this I assumed that this Excel files are machine generated and will always look the same no matter what. The reason I did this is because i only got this one test file so I assumed all files would look like this.
4. Input restrictions: At the current state the tool expects its input exactly as described in the task: 

    `<skill> <year> <month>`

    A nice to have feature would be if the parameters would be more soft. For example the year could be two-digit or four digit and the code would convert between them or the   month could be text or number or a short text, the skills could be case insensitive and so on. This would all be nice features that are not that hard to implement, but again that is not what i am trying to demonstrate.

The task was described as a small task that should take around an hour to complete. I was given a day to work on this task. I could have overengineered and polished it to death, but i did not want to. I want to demonstrate what my skills can manage in approx. 60 Minutes. The research on the topic, and the coding took me aroung 67 minutes.

Thank you for reading this

