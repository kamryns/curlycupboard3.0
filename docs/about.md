{% include navigation.html %}
# About our team!

Our team is all composed of students who took APEL this year! We all really love reading and that's why we thought a reading website would be great for us to build.
- [Riya Github Page](https://ranand2445.github.io/curly-knife/)
- [Kamryn Github Page](https://kamryns.github.io/curly-spork/)
- [Brian Github Page](https://bgt072105.github.io/curly-ladle/)
- [Alice Github Page](https://tangalice.github.io/curly-chopstick/index)
- [Sreeja Github Page](https://sreejavad.github.io/curly-spatula/)


*Team Roles:*
- Riya Anand: Scrum Master. Job is to manage scrum board, read me time box, and keep everything organized. Can help github admin with github pages See Scrum board Policies: [Policies](https://github.com/kamryns/curly-cupboard/wiki/Scrum-Board-POLICIES)
- Kamryn Sinsuan: Github Admin. Manages repo, branches, pull requests, etc. Also updates the Github pages, and makes sure that nobody's commits get overriden by preparing policies
- Brian Tang: Technical Officer. Their job is to try and impliment the new Tech Talk Topics, and explain and help team members understand what they are doing, and make sure team members are able to apply it as well.
- Sreeja Vadlamudi: Deployment manager. Using a Pi, or something similar, they must deploy our team website (VNC viewer)
- Alice Tang: Designer. Uses Bootstrap organization, Sassy, etc. and creates an organized theme throughout our website (can extend base.html)

Week 1 Jobs:
- Riya: Working on Local Storage
- Sreeja: Working on creating the cozy music/timer page
- Kamryn: Creating two directories: kids who like reading, kids who don't
- Brian: Dictionary API
- Alice: Implimenting basic theme into website

Week 2 Jobs:
 - Sreeja: Deployment Plan
   - Hardware: Ordered CanaKit Raspberry Pi 4 for the deployment process
   - download VNC viewer so you can access the Raspberry Pi anywhere
   - use terminal to set up Github environment on deployment host - make sure clone and cd name match repository
   - verify virtual environment and set up PIP packages to run the Web Application - needs requirements.txt
   - install and use terminal to test Gunicorn in browser - now the virtual environment is ready
   - create Gunicorn and Nginx configuration files to run Web Application as a service - validate these files to enable permanent services
   - visit freenom.com to register public IP address to a domain
   - use certbot to ensure Web Application is secure 
   
 Frequency/Release Day Policies 
   - Any updates/commits to the deployed website will need to be added using the terminal
   - Website should be updated at least once a week, but twice a week is ideal
   - All commits should be done and pushed to the website the evening before the deadline
   - Backup Deployment Managers in order: Kamryn, Riya, Alice, Brian
   - Order of commits to deployed website: Sreeja, Kamryn, Riya, Alice, Brian
   - In order to update, open a new terminal in VNC viewer and cd to github repo, "curlycupboard3.0". Then, use the command "git pull" to get the latest changes on the deployed website.
   - curlycupboard3.0$ source homesite/bin/activate
   - pip install -r requirements.txt
   - sudo systemctl restart homesite.service
