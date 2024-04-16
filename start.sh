echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/Rohanthakur360/forward_bot_premium_ultra
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/Rohanthakur360/forward_bot_premium_ultra -b $BRANCH /forward_bot_premium_ultra
fi
cd Rohanthakur360/forward_bot_premium_ultra
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
