# Liveplot

So, this is building and hosting a matplotlib figure (.png) format on flask, then sourcing into html. The script in liveplot.html checks if the image loads, then immediately updates the custom URL for it based on time to reload that individual element. You can see I have stuff commented out, you can restrict how often it refreshes the image, but I guess the first way is better cause it's dynamic.

Original Demonstration of flask method here: https://gist.github.com/wilsaj/862153
And then google-fu helped me figure out how to reload the src without refreshing the entire browser.

Love,

Gonzo