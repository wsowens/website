Title: Sunsetting the Swamp
Author: William Owens
Date: 3-13-2020 9:00PM
Summary: Or, what I learned from my first Python package.
Slug: python-project

I will never write another line of code for [swampymud](https://github.com/ufosc/swampymud), my longest-running project.
As of today, I've authored 389 commits pushed across 119 unique days.
I've plunged at least 400 hours into this project by my own estimation, and though it remains tragically unfinished, I will never push another line of code again.

I began swampymud in Spring of 2018, after being elected President of the [Open Source Club](https://ufopensource.club) at UF.
I wanted a project that would appeal to new members, and a *text-based*, *UF-themed*, *role-playing game* seemed like the perfect fit.
You can read more history here (link pending), but I'll keep this brief.
Over the course of two years, the project evolved from a few tweaks to [Mark Frimston's code](https://github.com/Frimkron/mud-pi) to a complete [Python package](https://pypi.org/project/swampymud/).

This project has captured more of my time than any other project I've worked on.
I have fond memories of blowing entire 2 hour Digital Logic lectures in the Python interpreter, probing deep into the language internals as Dr. Schwartz talked about mixed logic bubbles on a NAND gate or something.

Somewhere along the way, I learned a new programming language just to write [sockterm](https://github.com/wsowens/sockterm), a web-based terminal emulator to function as a cross-platform client.
In the final stages of my monomaniacal work on this project, I wrote a simple [context-dependent parser generator](https://github.com/ufosc/swampymud/blob/fe5bfa683e63370c3db14f6fa9b6c1bb088b3627/swampymud/util/parser.py).
If you don't know what that means, just realize that there's no reason why a text-based RPG library with exactly 0 users should have a 1000 line parser generator.

I bought a domain name [swampymud.net](https://swampymud.net) that I don't plan on renewing.
Oh, I made a pretty slick logo too:

![logo](https://raw.githubusercontent.com/ufosc/swampymud/2e28f9db1f0f4e1c4aafccdf7f58bf2a22b82366/images/sm_logo_animated.svg)

On the whole, I'm cautiously proud of this project.
I learned a great deal about Python, project management, and programming in general.
I suppose, rather than just ruminate about my pre-COVID college years, I'll summarize what I've learned.

### What I learned from swampymud

I love Python.
Beyond this ill-fated MUD engine, Python has been my weapon of choice for everything from automating small tasks to munging through terabyte datasets of genomic data.
However, it's not without major downsides.

Any good software engineer will tell you that unit tests are essential for a moderately sized programming project, and Python is certainly no exception.
But, as an interpreted language, Python *throws away* an opportunity to catch bugs at compile time.
As a single developer, your chance for making bugs is high.
This means writing even more testing code than you might have to in other languages.
To put this in perspective, about 4800 lines of the ~10000 codebase is devoted just to testing.
Granted, I focused on condensing and simplifying actual library and made little effort to clean up the bloated test cases.
Nevertheless, writing these test cases was pure drudgery, and I could have gotten away with far fewer had I chosen a language with more functional programming elements.

On a related note, [Python is arguably slower than any other language with widespread adoption](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-go.html).
For small scripts, this difference is negligible.
Given a 50x performance difference, who cares if your program takes 0.5 seconds instead of 10 ms?
Again, the Python user *throws away* a major opportunity to make a better program. **Whatever my next project is, it will be in a compiled language, not Python.**

Out of everything, **my biggest regret is not quitting sooner**.
My friend, OSC founder Matthew Booe, warned me about the [sunk-cost fallacy](https://en.wikipedia.org/wiki/Sunk_cost#Fallacy_effect).
"Nonsense! This project will be done next month."
As it turns out, "next month" isn't a month on the calendar, but rather a mirage that always hovers about 4-5 weeks ahead.

A few months into the project, I saw [this video](https://youtu.be/3tO3h9APNbM).
TL;DW: one of Tom Scott's first viral successes came from a low-effort, one-off project.
The CEO of the company I work at has offered similar stories of his time in graduate school.
He talks about how he helped create [OpenWetWare](https://openwetware.org/wiki/Main_Page), entirely as a side project.
He recommends having 3 projects, taking about 60%, 30%, and 10% of your time.
If the 10% project starts to become more interesting than the 30% project, then it should be bumped up.
If a new project emerges that seems more interesting than anything else, then toss the 10% project.

Simply put, you can't reliably predict what will and won't succeed.
Once a side project is no longer rewarding and the end isn't in sight, you're better off ditching it for something else.
If you have a deep-seated excitement for what you're doing, then you'll be vastly more successful.

On a related note, **I wish we had released the project sooner** (or at all).
The past 6 months in the startup world has shown me the value of shorter iterations.
I'm learning to abandon perfectionism and just deliver something buggy.
Upon reflection, had we made the game and released it on the UF Facebook meme pages, we could have cracked a few smiles.
Maybe there would be a few people with a more lasting interest, and in that case, we could tailor the game to their experience, attract a few more users, and so on.
If swampymud were ever to be successful, it would be through that formula: a grassroots, serendipitous novelty that attracted a small crowd for a few weeks. 
Instead, we have a much more polished project in exchange for no users.

I wish I had done something graphical.
Most users can't appreciate how elegant your architecture is, or how optimized your loops are.
Much of my passion for the library came from the design, creating a server that supported websockets and telnet simultaneously, writing a custom client but supporting legacy clients, and so on.
I was enamored with my own cleverness.
Even if the users could read your source code, they probably wouldn't care. 
**The only thing that really matters to users is *functionality*, that topmost layer of the stack that they see.**
Everything else is an order of magnitude less important than delivering a tangible product that they want to use.

The product I finally delivered was all the less functional because I insisted on writing everything myself.
There's immense pedagogical value in learning things for yourself.
(The only real way to learn about something is to just do it.)
But, to prioritize usefulness for other people, then you must pause any academic exercises so you can (again) **release the project sooner** with more ***functionality***.

This is especially true of game development.
Take a look on any game development forum, and you'll find this ubiquitous piece of advice:

> If you try to make a game without using an engine, you will⁠—by necessity⁠—wind up writing a game engine first.

(c.f. [Greenspun's Tenth Rule](https://en.wikipedia.org/wiki/Greenspun%27s_tenth_rule).)
Save yourself time, **utilize other people's hard work** and import a popular, existing library.
The library you write will be more buggy, slower, and (most importantly) demand more of your time.

In summary:

1. Use the tools that make your project easier.
2. Many small projects are better than one large project. Quit when it gets boring and move on.
3. Ship early, ship often.
4. Practical functionality beats theoretical beauty.
5. Use existing work. Don't try to do it all yourself.

Looking at these points now, if you trained a neural network on Hacker News comments and asked it for "software engineering advice", it would probably spit out something about like that list.
Even if I should have known better, sometimes it takes getting burned to accept the common wisdom about playing with the fire.

And while I learned this in a software-engineering context, these principles generalize to other fields like my current career as a scientist.
For instance, Principle #3 might be understood as "perform lots of experiments, and analyze the data quickly rather than trying to answer a dozen divergent questions in 1 crude experiment."
Principle #5 reminds us that we should always rely upon work that's already done, staying up to date  And finally, Principle #4 reminds us that no matter how sophisticated your model or lofty your hypothesis, until you deliver *the data*, that bar graph or scatter plot, nobody will care.

These reflections may sound self-critical, but to reiterate, I loved working on this project, even until the end.
The lessons above will serve me well in science or wherever I wind up next.
Goodnight, swampymud, hello... something new.
