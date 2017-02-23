# NoteCards
NoteCards is a web application where users can create flashcard notebooks and share with others. Users can login with their Google or Facebook account.

# Tools
Flask, SQLAlchemy, Google API, Facebook API

# How to run
<b>Initialize Vagrant VM
1. Install Vagrant: http://vagrantup.com/ and VirtualBox: https://www.virtualbox.org/ 
2. Create a new directory can clone the two files inside:
- https://github.com/valeriechizhang/Tournament/blob/master/Vagrantfile
- https://github.com/valeriechizhang/Tournament/blob/master/pg_config.sh
3. Clone the NoteCards project inside of the same direcotry
4. Use the command "vagrant ssh" in the direcory to start off the vm

<b>Run the Application
5. In the vm, locate the project direcotry using command "cd /vagrant/NoteCards"
6. Run the web application using command "python main.py"
7. The web application should be running on http://localhost:5000

<b>References</b>
Udacity Full Stack Web Developer Nanodegree
