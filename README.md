# NoteCards
NoteCards is a web application where users can create flashcard notebooks and share with others. Users can login with their Google or Facebook account.

# Tools
Flask, SQLAlchemy, Google API, Facebook API

# How to run
<b>Initialize Vagrant VM </b> <br>
1. Install Vagrant: http://vagrantup.com/ and VirtualBox: https://www.virtualbox.org/ <br>
2. Create a new directory can clone the two files inside:<br>
https://github.com/valeriechizhang/Tournament/blob/master/Vagrantfile <br>
https://github.com/valeriechizhang/Tournament/blob/master/pg_config.sh <br>

3. Clone the NoteCards project inside of the same direcotry <br>
4. Use the command "vagrant ssh" in the direcory to start off the vm <br>

<b>Run the Application</b><br>
5. In the vm, locate the project direcotry using command "cd /vagrant/NoteCards" <br>
6. Run the web application using command "python main.py" <br>
7. The web application should be running on http://localhost:5000 <br>

<b>References</b><br>
Udacity Full Stack Web Developer Nanodegree<br>
