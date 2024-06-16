echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/protullen /forward-bot-premium
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/protullen /forward-bot-premium -b $BRANCH /forward-bot-premium
fi
cd  protullen/forward-bot-premium
pip3 install -U -r requirements.txt
echo "Starting Bot...."
gunicorn app:app & python3 main.py
