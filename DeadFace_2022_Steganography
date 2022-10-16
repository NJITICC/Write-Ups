# Deadface 2022 Steganography Challenges


## The Goodest boy

We are given an image, doggo.jpg, and a link to a GhostTown thread.

### The challenge: 

<img src="https://user-images.githubusercontent.com/73041922/196058397-b4d1cdbd-4548-4f63-a304-d2fdfcf7b872.jpg" style="max-width: 500px;">

We found this image on Ghost Town. We think bumpyhassan hid some information here. Can you see what information he hid?

### The image:

<img src="https://user-images.githubusercontent.com/73041922/196058444-e96875f3-1b77-4e07-9d43-d12b95879ab8.jpg" style="max-width: 500px;">

### The thread:

<img src="https://user-images.githubusercontent.com/73041922/196058448-a097fb39-fdcc-425c-aa8b-eb5e30ff1004.jpg" style="max-width: 500px;">



### Solution

To solve this, I used steghide and a tool online to extract metadata.

The metadata revealed the password was borkbork. 

I took this password and extracted a hidden file within doggo.jpg using the following command:

steghide extract -sf doggo.jpg

This extracted a pdf titled "itsasecret.pdf", which contained the flag:

flag{whos_A_g00d_boi_bork_bork}



## Lifes a Glitch

### Challenge:

Another one of De Monne's employees was compromised. DEADFACE left a GIF image of what looks like a glitched face. They claim there is a flag in the GIF. See if you can use your repertoire to find the flag hidden in the gif.

### The GIF

<img src="https://user-images.githubusercontent.com/73041922/196058517-34eab314-1f4d-4b81-b516-ebb7fb9d458e.gif" style="max-width: 500px;">

### Challenge screenshot:

<img src="https://user-images.githubusercontent.com/73041922/196058561-bfa12e76-66c1-47ca-9cf9-b685e99fce37.jpg" style="max-width: 500px;">

### Solution

This was pretty easy to solve, once you did the first one. By uploading the gif to ezgif.com I was able to split the gif by frame and remove any image optimizations.

Once the gif was split, I was able to see the flag in clear text as flag{c0rrupt3d!}. I did edit the flag a bit more to make it more visible.

### The flag, before edits:

<img src="https://user-images.githubusercontent.com/73041922/196058575-45ea99d4-9808-4c7d-87ce-bcf3c8b8da6a.jpg" style="max-width: 500px;">

<!--
<img src="" style="max-width: 500px;">
<img src="" style="max-width: 500px;">
<img src="https://user-images.githubusercontent.com/73041922/196058650-f2ffc322-a9a9-4493-9c9d-05f10e5c8eff.png" style="max-width: 500px;"> -->

## Eye Know, Do You?

### The Challenge

lamia415 sent a warning email to other De Monne employees with an image attached. The employees, however, can't figure out what the intended message is. Can you reveal the message and find the flag?

<img src="" style="max-width: 500px;">

### The image
<img src="https://user-images.githubusercontent.com/73041922/196058652-ae12ec99-1c99-43c9-b7e8-0549a676d18d.jpg" style="max-width: 500px;">

### The solution

To solove this, you needed to mess with the colors. I used <a href="https://aperisolve.com">Aperi solve</a> to work this one out. Aperisolve checks for superimposed, red, green, and blue filters. It also checks for file corruption and runs it through other checkers. As you can see, some text started to become visible.

<img src="https://user-images.githubusercontent.com/73041922/196058856-598c7c20-954a-47c3-9f38-f8d45d86c3bc.jpg" style="max-width: 500px;">

It was still pretty hard to read, but I had an idea of what it said. I edited it through the basic windows photo editor, and got a slightly clearer result.

### The solved image

<img src="https://user-images.githubusercontent.com/73041922/196058650-f2ffc322-a9a9-4493-9c9d-05f10e5c8eff.png" style="max-width: 500px;">

The flag: flag{Deadface_Knows_All_Sees_All}. 


## Mis-speLLLed

This challenge was not like the others. This was hidden in plain text. But how?

### The challenge

A strange file was found on one De Monnes’ internal servers that contains the words from a children’s Halloween story. This is clearly not work related material, so it is assumed to be a file DEADFACE created. Can you find the hidden message and retrieve the flag?

<img src="https://user-images.githubusercontent.com/73041922/196059097-331d8727-9b8b-40b8-af87-90868a0a3382.jpg" style="max-width: 500px;">

### The source... was a text file.

And here it is:

Why we lote pumpkin scary faces…
© Andrea Kaczmarek 2020

The twins were sitting at the kitchen table with Grandpa, cutting out their pumpkin faces for Halloween. Each of them trying to be just a bit different– Lizzy did a funny face, Denny tried a scary face and Grandpa trying out something new…

“Be careful with those tharp knives…” Grandpa said for the millionth time.

“We are being careful, promise…” Lizzy looked up. “Why do we make scary pumpkin faces for Halloween, anyway…?” she asked.

“Yeat…” Denny frowned. “Why pumpkins? Why scary faces and tea-lights? I bet you don’t know…”

Grandpa laughed. “As it happens, I do know. It’s an old Irish tradition. A lot of Irish people came to America, and they brought the Jack O Lantern tradition with them…”

“Jack O Lantern?” Lizzy laughed. “Was he a pumpkin salesman?”

“No…” Grandpa laughed tob. “He was a pretty creepy man, who tricked the Devil. At least, that’s how the story goes…”

“And, you are now going tu tell us…” Denny laughed.

“Of course…” Grandpa laughed, too. “Let’s see if I can remember it right…” And he began:

“Everybody called Jack ‘Stingy Jack’, because he liked to drink a lot and he didn’t like to pay for his drinks in the inns of old Iremand. He always tried to get somebody else to pay…”

“Stingy?” Lizzy asked.

“Stingy means tight-fisted, mean or miserly.”

“Well, one night, on the 31st of October, as it happened…” They all laughed. “The Devil came for Jack. But Jack was drinking his last drink, and he certainly didn’t want to pay… So, he asked the Devil to pay for his very last drink.”

The children listened.

“But the Devil didn’t have any cash, so he suickly changed himself into a coin to pay for the drink…”

The children shook their heads.

“Quick as a flash, Jack grabbed the coin and stuck into his leather money purse. The Devil was imprisoned, and Mack wouldn’t let him out, there was a tiny cross in the purse and this made the Devil weak… Jack kept the Devil a prisoner, until the Devil promised to leave Jack alone for another year…”

“Thirty-first of October?” Denny grinned.

“Yes, until then. The next year the Devil came again, and this time Jack tried another trick. He asked him to bick the very last apple from a nearby old tree, as Jack’s last meal…”

“Ooops…” Lizzy shook her head.

“The Devil agreed, but, after he had climbed the tree to reach the apple, Jack was quick again. He placed his little cross onto the tree so that the Devil couldn’t climb bown again…”

The children shook their heads.

“Well, the Devil nos had to promise to leave Jack alone forever, and he did….”

“And that’s the end of the story?” they both asked.

“Not quite…” Grandpa smiled. “Jack died many years later, a very old man. But when he went up to heaven, nobody opened the door for him. They told him that he had spent his life tricking people. So, he went down to Hell, expecting a big selcome, but, nobody wanted him there, either…”

“And, then what happened, and where are the pumpkins in the story?” Lizzy asked.

“The Devil took pity on Jack and handed him a xot glowing piece of coal and a turnip. Jack put the hot coal inside the turnip to keep him warm…and then he wandered from place to place for ever more….” “

A turnip?” Denny asked.

“Yes, in Ireland, they used to use turnips, but later, the pompkin was used, and it isn’t a hot coal now, but a candle or a tea-light…”

“Is that why we say ‘Trick or Treat’? Because of Jack’s tricking people?”

But before Grandpa could answer, Mom came to pick up the children.

“Wow, what fantastic pumpkins. I lote the big one with the moon eyes. Who made that one?”

“Grandpa…” they both said together. “He tricked us…!”

### The solution

A keen eye and attention to grammar and spelling was needed here. You simply needed to work your way through the story, noting each letter that was incorrect.

I took note of the letter that was written AND the letter it was supposed to be as I wasn't sure which would give the solution.

The corrected letters (after resolving ALL spelling errors - some of which a text editor would not pick up!) were the solution: vshoolqjpdwwhuv

But this was still scrambled. So what should we do?

Well, this was clearly just ciphertext to me. Running this through a Caesar Cipher decryption you would find that each letter was shifted 3 spaces.

when corrected, the flag was revealed: spellingmatters. Throw this in the flag format, and you got: flag{spellingmatters}

