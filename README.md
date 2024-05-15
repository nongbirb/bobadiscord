## Before We Dive into the Fun:
Make sure you've got these essentials:

1. Python: You know, the magical language of programming snakes. When installing, don't forget to tick the box that says, "Add Python 3.9 to PATH." It's like inviting Python to join your party.

2. Notepad++ or Microsoft Visual Studio: It's like choosing between a ninja editor and a wizard's wand. Visual Studio is cool, but if you're into simplicity, go with Notepad++. It's like coding with a cozy blanket.

### Let the Fun Begin:
1. Install Python:

 - Click on the Python link above and download it. Think of it as inviting a snake into your computer, but don't worry; this one won't bite. 🐍
 - During installation, don't forget to check the box to add Python to the PATH. It's like giving Python a GPS to find its way around your computer. Genius, right?
 - Once installed, Python will be chilling on your computer, ready to work its magic. No need to talk to it directly; it's quite independent. 😉
2. Download the Automation Script:

 - Click on the provided link to access the script code. It's like finding a treasure map to automation island!
 - Download the zip file and unleash the script onto your desktop. Prepare for some serious coding adventures! 🚀

3. Configure the Script:

 - Open config.jason. Who's Jason, you ask? Well, he's the keeper of secrets in this script. Fill in your Discord Token ID in 'token' (input between ""). It's like giving the script the keys to your Discord kingdom.
 - Input your Discord Channel ID in 'channelids'. Think of it as telling the script where the party's at. 🎉
 - Save the changes and get ready to unleash the script onto the world! Just remember, with great power comes great responsibility. 💪

4. Let the Magic Happen:

 - Open a command prompt in the folder where your script is located. It's like summoning the spirits of code.
 - Type py main.py and hit Enter. Watch as the script works its magic, spreading joy and automation across the land. 🧙‍♂️

### Docker File Update!

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]

```

This Dockerfile is like a recipe for baking automation cakes. Just follow the instructions, and soon you'll have a delicious container full of automation goodness! 🍰