# Pauser

One way to improve spoken language is to imitate. This program is a little tool
to help to make imitating materials yourself. It will insert pauses into the
audio so you can get time to repeat after the speaker.

## Installation

### python 2.7
If you have no python (version 2.7) installed on your machine, download and
install the right version for your operating system.

[https://www.python.org/downloads/](https://www.python.org/downloads/)

### pydub
pauser requires pydub library. pydub can be installed via pip:

	sudo pip install pydub
	
If the command 'pip' is not found, you need to install it first. Check:

[https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)

### ffmpeg
Download and install ffmpeg if you are going to manipulate mp3 format audio file.

[https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

### pauser
Finally, download pauser: 

[https://github.com/freemandealer/pauser/archive/master.zip](https://github.com/freemandealer/pauser/archive/master.zip)

	

## Usage

Use cmdline to change to pauser directory. For linux/unix/osx, use your terminal. For Microsoft Windows, click 'start' and run 'cmd'. Then issue:

	cd /path/to/where/you/download/pauser

Then, issue command:

	python pauser -f /path/to/your/audio/file
	
After operation completes, you will get your own material to imitate!

Also, pauser supports some other options. You can use them to twist the process till you are satisfied with the output. For example, if you want to extend the duration of the blank so you can have time to repeat twice , you can issue:

	python pauser -f /path/to/your/audio/file -e 3000

Now you can get extra 3 seconds in each pause. Or you can simply issue:

	python pauser -f /path/to/your/audio/file -b 2
	
This will double the duration.

You can also adjust the granularity of chunks with -g options. The default granularity is 400.

Granularity is also determined by -d option. If your audios have non-ignorable background noise, you are suggested to use -d options followed by a smaller threshold. The default threshold is 70.

Enjoy!

---

Report bugs to <freeman.zhang1992@gmail.com>

