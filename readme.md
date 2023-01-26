Project Title: Simple Strength, a website for developing strength using barbell training
Video URL:
Description:
I created a website that generates a month of training from Canditos Linear Progression, a freely available training program by a youtuber and successful powerlifter, which has a very good reputation online and in the stregnth training world. The user signs up for an account, inputs their Maxes or Rep maxes (ability to lift a weight for a certain amount of reps) and then it gives 4 weeks of training with the sets and reps laid out over various webpages.

Initial vision:
I have a passion for strength training, having purchase a home gym and have always had an interest in working out, powerlifting and strongman. My friends often ask my for lifting/training advice and I felt that translating that into an online resource using a well liked or popular program could be useful for myself and my friends and even the wider community. This also alows the project to grow and change as I become better at webdev, as I would like to contine with CS50W to hone my skills in that field.

I feel a good way to describe the project is to detail each webpage

layout.html:
This included all the boilerplate including the doctype, importing bootstrap and declaring my Navbar. Initally the name and navbar included very few items, and a lot of iteration took place. Simple Strength started out as simply "Workout" as a placeholder title. 

login.html:
This is a basic login function, I debated having a recover password function but it would require something that is above my skillset, great for future expansions though.

Having a background with a card in HTML was a challenge, especially laying things out, but it was a great learning experience, especially because this was one of the first pages done in the project. This of course led to the register page

register.html:
This is quite a simple page that requires the user to register, but it also requried the creation of the main database called Exercise.db, this required some brainstorming on what data types would be used, the uniqueness of those data types etc.

I decided to use the hash function introduced and modelled in CS50, seeing as its something I have used before and am quite familiar with, and after bug testing it worked quite well. After the user is created it will send the user to the Welcome page

welcome.html:
This is a basic page that introduces the user to what the website is, how it works and also links to the PDF that contains the main training document, it then leads the user to the Calibration page. This page is fairly simple with a layout showing some shots of people exercising and a positve and peppy bit of text to get the user excited about beginning to work out.

calibrate.html:
This prompts the user through a card and input system to show their current levels of strength by inputing a rep max, this will be stored in a database or updated should the user require further updating of rep maxes. This prompted me to create an error page too, as errors were crashing the website, also one of the earliest features and making sure the prompt fit a good amount of detail without being verbose took quite a bit of brainstorming.

Many of the assistance exercises where based of the main 3 lifs (Squat, Bench, Deadlift) for simplicity sake as a percentage, as asking the user for each and every assistance exercise would be time consuming and not that useful, as the main lifts already indicate the users overall strength, so being conservative here and taking away some choice would lead to a smoother long term training program.

week1.html:
This was the hardest page to design becuase implementing an aesthetic way to lay out an entire weeks worth of training while being engaging, readable, well spaced and not too wordy was a challenge. I decided against using a tabled format as it made things look a bit too stuffy. Using Jinja templating to draw from the database required some experiementation as I am not all to familiar with this but it was satisfying to learn.

This is basically the beating heart of the project and took the longest to implement, as weeks2/3/4 are basically continuations of this idea. Spacing in particular was quite challenging and involved lots of trial and error to arrive at something that wasn't too cluttered or to spread apart.

week2.html:
This is a continuation of week 1, with the major decision points being the rate of progression among exercises, and seeing as I wante this to be applicable to as many trainees as possible, I went with the conservative side, which is better in the long term for the majority of people anyways. brainstorming on how to format the Jinja required for increasing loads without showing decimal points was also a challenge in this step

week3.html:
Seeing as this was one of the last weeks things were quite set in stone, this week was mainly making sure percentages fit at he the strucure made sense in the real world.

week4.html:
The final week of training! This week concluded the progression and made me think more of the images, the rest day information was also thought of here. I decided to go with resting animals as it adds some levity and cuteness, appealing to a wider audience as well as just being adorable. I also spent a decent amount of time looking for royalty free common use picture of people doing exercises that are applicable to the program.

index.html:
For the longest time this was a blank page, but I decided to use it as a navigation page, similar to the Navbar but with a bit more description, this should show as the user logs in, it hints and navigation items in the Navbar and is there to get the user excited about using the site.

howTo.html:
This includes links on how to lift, inclulding tutorials from youtube on each lift of this program, including a little explanation of each lift with a title, simple but vital for correct techinque and follow through on the exercise program.

FAQ.html:
This includes commonly asked questions, such as the origins of the program, warming up and rest periods, why the program was chosen, a bit about the author etc. This was decided later in the project because I felt extra information was lacking.

Overall thoughts on the project: Although it started as a simple design, I feel the project was an overall success, I also have many future ideas and ways I can see the project improving such as:

* Allowing the user to choose their rate of increase for each lift each week
* Integrating a full calendar which days can be mapped into
* Allowing the tracking of strength with a bar chart
* Allowing customizable assistance exercises
* Allowing the user to have notes, including rate of perceived exertion (RPE) and just overall thoughts





