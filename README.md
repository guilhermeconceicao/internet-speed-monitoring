# The problem
The idea of this project started with a problem. An unstable internet bandwidth problem. I started to notice that my internet was fluctuating during the whole day. I knew it, but I could not measure.
So, I found out this wonderful repo [speedtest-cli](https://github.com/sivel/speedtest-cli) that uses [speedtest](https://www.speedtest.net/) for testing internet bandwidth.

# The "solution"
I developed this python script that consumes the *speedtest-cli* data and save the ping, download/upload speed and others informations about my bandwidth on a CSV file.
Then, I created a windows scheduled task that executes my script every 5 minutes. So, every 5 minutes my script appends a new row with my bandwidth info into my CSV file. Now, I have my precious monitoring report about my internet and I can measure better my internet bandwidth fluctuation.
I know, there are N variables that makes my internet bandwidth fluctuate and others N variables that makes my report unreliable. However, was fun develop this script and learn new things.
And, of course, the solution, will be change my internet service provider :laughing:

![image](https://user-images.githubusercontent.com/45015234/156172122-211eb5fb-a51a-438c-8675-e1de39a1905b.png)

# How to create a windows scheduled automatic task for this script
## Install python
Install [python](https://www.python.org/downloads/) 3.9 or higher

## Clone this repository
[learn to clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## Creating the task

### Open the Task Scheduler
**I am really sorry about the portuguese version of windows. At the moment that this article has been writing, I am using the Windows 11 Home Single Language and can't change to english language. My apologies.**

![image](https://user-images.githubusercontent.com/45015234/156177966-b0b92bb2-ecb0-452e-8d33-f480fb8d0378.png)

### Action => Create Task...
![image](https://user-images.githubusercontent.com/45015234/156178335-5ec36d2d-5327-4ff3-8d39-1452b17d33ee.png)

#### Give a name for the task
![image](https://user-images.githubusercontent.com/45015234/156178589-71c77304-b5ba-4f3f-81b7-4df99f60ab34.png)

### Actions => New...
![image](https://user-images.githubusercontent.com/45015234/156178761-d0431e20-f3a2-4822-833e-7d86f03198de.png)

##### Setting the *Program/script* field
Open the windows cmd (command prompt) and find the python path. Execute the *where python* command for this step.
![image](https://user-images.githubusercontent.com/45015234/156179149-a4fdc100-0986-40e2-b271-8af52b513b36.png)
Now, you got the python path. Copy this info and past on the program/script field.
![image](https://user-images.githubusercontent.com/45015234/156179457-e93c67e2-37ea-4901-81f8-902b0ba7b215.png)

#### Setting the *Add arguments* and *Start in* fields
Go to where this repository was cloned and find the *internet_speed_monitoring* script
![image](https://user-images.githubusercontent.com/45015234/156180362-bd2ce570-a126-4fc6-8dd5-7683cf64d1d2.png)
- The *Add arguments* field you will set with the python script name, in this case: *internet_speed_monitoring.py*
- The *Start in* field you will set with the location of your python file, in my case: *C:\Users\guilh\source\repos\Internet.Speed.Monitoring*

### Triggers => New...
In my case, I will configure this task to execute every 5 minutes indefinitely
![image](https://user-images.githubusercontent.com/45015234/156181744-2612e7b5-ec8e-40af-844a-c33743a924f3.png)

# And... It is done!
Now, I have my windows scheduled automatic task that executes this script every 5 minutes, creating my internet speed report.
![image](https://user-images.githubusercontent.com/45015234/156182050-3e8ff94c-1eb1-40cf-8dd7-2e6a26db42b1.png)

# Feel free to get in touch
Please, if you have any doubts or anything else that you want talk with me about, feel free to contact me anytime!






