'''
Here's what we need to do:
  * Figure out what we need to know to create a new collection.
  * Make functions that return the appropriate string or boolean for each of those things.
  * Create a script that will add a new collection.'''
  
'''
<p>
<form style="display:inline" action="http://deepblue.lib.umich.edu/handle/2027.42/XXXXXX/browse?">
<input type="submit" value="View all items in this collection"/>
</form>
</p>
<br />


<p><img src="http://deepblue.lib.umich.edu/static/image/bentley-banner.jpg" alt="Bentley Historical Library banner" /></p>

<h2> XXX </h2>

<p>The materials in this online repository form part of a larger XXXX record group / manuscript collection held by the <a href="http://bentley.umich.edu/">Bentley Historical Library</a>.  For a more complete index to the materials, please consult the collection's <a href="http://quod.lib.umich.edu/b/bhlead/umich-bhl-XXXXX">online finding aid</a>.
</p>

<p>The materials in this online repository form part of a larger XXXX record group / manuscript collection held by the <a href="http://bentley.umich.edu/">Bentley Historical Library</a>.  For a more complete index to the materials, please consult the online finding aids for the:
<ul>
  <li><a href="http://quod.lib.umich.edu/b/bhlead/umich-bhl-XXXXX">XXXXX</a></li>
  <li><a href="http://quod.lib.umich.edu/b/bhlead/umich-bhl-XXXXX">XXXXX</a></li>
</ul>
</p>

<p>
Researchers may also be interested in the <a href="http://webarchives.cdlib.org/site/XXXXXX">XXXXX Web Archives</a>.
</p>

<p>
For questions or more information, please contact the Bentley Historical Library's <a href="mailto:bentley.ref@umich.edu">Division of Reference and Access Services</a>
</p>

<p>
<b>Abstract:</b><br />

</p>

<p>
<b>History / Biography:</b><br />

</p>

COPYRIGHT
<h2>Please note:</h2>
<p>Copyright has been transferred to the Regents of the University of Michigan.</p>
<br />
<br />

<p>
Access to digitized sound recordings may be limited to the reading room of the <a href="http://bentley.umich.edu/">Bentley Historical Library</a>, located on the Ann Arbor campus of the University of Michigan.</p> 

LICENSE
As the designated coordinator for this Deep Blue Collection, I am authorized by the Community members to serve as their representative in all dealings with the Repository. As the designee, I ensure that I have read the Deep Blue policies. Furthermore, I have conveyed to the community the terms and conditions outlined in those policies, including the language of the standard deposit license quoted below and that the community members have granted me the authority to deposit content on their behalf.'''

# selenium is used automate web browser interaction, you'll need to install it
import selenium

# beautifulsoup pulls data out of html files, you'll need to install it
from bs4 import BeautifulSoup

# name
name_text = raw_input('Name: ')

# introductory text
view_all_items_in_this_collection = 

# h2 section

# is this part of a larger record group or manuscript collection?
# if yes, which one? if yes, are there many finding aids or just one? <-- out of scope this first time
# web archives?
# where are the finding aids?
# abstract
# history or biography? then text
# digitized sound records?

# copyright text

# liscense

# assign roles

# go back and add handle

