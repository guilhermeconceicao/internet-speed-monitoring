# The Problem
The idea of this project started with a problem. An unstable internet bandwidth problem. I started to notice that my internet was fluctuating during the whole day. I knew it, but I could not measure.
So, I found out this wonderful repo [speedtest-cli](https://github.com/sivel/speedtest-cli) that uses [speedtest](https://www.speedtest.net/) for testing internet bandwidth.

# The "Solution"
I developed this python script that consumes the *speedtest-cli* data and save the ping, download/upload speed and others informations about my bandwidth on a CSV file.
Then, I created a windows scheduled task that executes my script every 5 minutes. So, every 5 minutes my script appends a new row with my bandwidth info into my CSV file. Now, I have my precious monitoring report about my internet and I can measure better my internet bandwidth fluctuation.
I know, there are N variables that makes my internet bandwidth fluctuate and others N variables that makes my report unreliable. However, was fun develop this script and learn new things.
And, of course, the solution, will be change my internet service provider :laughing:

![image](https://user-images.githubusercontent.com/45015234/156172122-211eb5fb-a51a-438c-8675-e1de39a1905b.png)

