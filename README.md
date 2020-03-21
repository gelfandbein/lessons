# Advanced Notes Application
#echo "# notes" >> README.md
#git init
#git add README.md
#git commit -m "first commit"
#git remote add origin https://github.com/gelfandbein/notes.git
#git push -u origin master

# Setup
# create virtual env
python -m venv .venv

# setup requirements
pip install -r .\requirements.txt

#Get steps
# Init repository
git init

# check status
git status

# add(stage) files
git add .

# commit files
git commit -m "Message"

# Add remote server (optional)
git remote add origin git@github.com:dyachoksa/notes.git

# push to remote server (first time)
git push -u origin master

# push to remote server (regular)
git push

# clone a new repository
git clone git@github.com:gelfandbein/notes.git

# pull from server
git pull


