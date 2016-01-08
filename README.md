#Project: Downloading All XKCD Comics

Blogs and other regularly updating websites usually have a front page with the most recent post as well as a Previous button on the page that takes you to the previous post. Then that post will also have a Previous button, and so on, creating a trail from the most recent page to the first post on the site. If you wanted a copy of the site’s content to read when you’re not online, you could manually navigate over every page and save each one. But this is pretty boring work, so let’s write a program to do it instead.

XKCD is a popular geek webcomic. The front page at http://xkcd.com/ has a Prev button that guides the user back through prior comics. Downloading each comic by hand would take forever, but this can be done with a python 3 script to do this in a  couple of minutes.

Here’s what the program does:

* Loads the XKCD home page.
* Saves the comic image on that page.
* Follows the Previous Comic link.
* Repeats until it reaches the first comic.

