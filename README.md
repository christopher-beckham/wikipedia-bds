Wikipedia bidirectional search 
===

A set of scripts for the generation and analysis of a bidirectional search between two Wikipedia articles.

For example, given two articles, can we find a common article between both of them?

Screenshot
---

![Screenshot](http://raw.githubusercontent.com/chrispy645/wikipedia-bds/master/images/out20.txt.png)

We can see here that the two starting articles were **Obsamu_Kobayashi** and **Out_and_In**. **Osamu_Kobayashi** had a link to **Osamu_Kobayashi_(animation_director)**, then to **Tokyo** and finally to **Rock_music**.

**Out_and_In** had a link to **Single_(music)** which had a link to **Rock_music**, so both starting articles had **Rock_music** in common.

Usage
---

The main scripts are `search.py` and `plot.py`. `search.py` outputs the network topology in plaintext, while `plot.py` reads in this information and generates an actual graph that is saved to disk.

`search.py` can be run in two ways - if you run it without command line arguments, it will do a bidirectional search between two random Wikipedia articles, otherwise you can specify the two articles yourself. For example:

`python search.py Pagurus_bernhardus Baron_Glanusk > output.txt`

`output.txt` will contain the graph topology in plaintext. We then run:

`python plot.py output.txt` which will generate a graph and output it to a window.
