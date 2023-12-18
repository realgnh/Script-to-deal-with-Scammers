# Script-to-deal-with-Scammers
this is a script that wastes the money of a scammer trying to steal your cc information by putting in a cc number that is fake but validates luhn's algorithm, everytime it declines it takes $0.5-$1 from the scammer


1. HOW TO GET THE URL OF THE WEBSITE: press right click on the website you're in --> inspect --> network --> you should see the url --> copy and paste it in the code

2. HOW TO GET THE DATA: fill out the fields with a random name, city --> put a cc number that validates with luhn's algorithm --> right click --> inspect --> network --> you should see something called "data" --> copy and paste in the code

   EXPLANATION FOR CODE:
   basically when someone tries scamming you out of your cc they give you a website, you open it with proxies or incognito doesn't matter, usually the website tells you that you won smth for free then tells you there's a delivery fee or smth similar, it then tells you to fill out your cc info, sometimes name, city, address + cc info. However, when you put a cc number that validates with luhn's algorithm but it declines the scammer gets charged a $0.5-$1 fee for the decline, this script is meant to put in the same info as the data you put in and website should decline, and the script repeats this over and over until YOU decide to stop.
