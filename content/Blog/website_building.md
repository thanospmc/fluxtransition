Title: Building this blog with Pelican and Github pages
Date: 2018-08-15 10:10
Tags: Untagged
Author: Thanos Poulos
Cover: images/fig1.png
Summary: I have been meaning to start a blog for some time now. I actually started one a few years ago using Tumblr's engine but it was short-lived as I did not know what to do with it. This blog is supposed to be more of a journal...

## Starting a blog


I have been meaning to start a blog for some time now. I actually started one a few years ago using Tumblr's engine but it was short-lived as I did not know what to do with it. This blog is supposed to be more of a journal that could be used as way to share things as well.
{: style="text-align: justify"}

## Finding Jekyll and Pelican


I decided that this time I wanted to create a blog that I would be able to control rather that use any service that is available online. While following some data science blogs, I saw a few websites created using a static site generator called [Jekyll](https://jekyllrb.com/). What interested me about Jekyll were the availability of themes, such as the gorgeous [Hyde](http://hyde.getpoole.com/) theme. However, as soon as I started looking at it, it seems like Jekyll had a few deficiencies, very well presented [here](https://ihommani.github.io/pelican.html), of which all were important for me.
{: style="text-align: justify"}

## Getting Started with Pelican


After reading this, I Was sold on [Pelican](http://docs.getpelican.com)! Plus, it is written in Python with which I am more accustomed than Ruby. I was even able to find themes that resembled Hyde, like [Flex](http://flex.alxd.me/blog/) and [hyde](http://jvanz.com/). The best thing about Pelican is that it allows for changing themes with very few modifications of the templates. If the theme is well made, only changes in the base HTML file are needed and we are good to go.
{: style="text-align: justify"}

I got started by following this tutorial by [Just Alfred](https://blog.justalfred.com/getting-started-with-pelican-on-github-pages.html) but this only get you so far. After I chose the [voce](https://github.com/limbenjamin/voce) theme, I got to modifying it a bit so that it is as I wanted it.
{: style="text-align: justify"}

## Modifying the theme


The **voce** theme is easy to understand and well made. Everything about the site is located in the ``base.html`` and all other template pages are extensions to the base page. This means that almost all changes are in the base page with minimal changes to all other ``html`` files. The overall theme of the website (organization, colour theme, layout) has been kept as it is clean and beautiful. I will focus mostly on the changes on the ``base.html`` file since these are the most important while the others are simple HTML or CSS changes.
{: style="text-align: justify"}

The **voce** theme by default has space in all the pages for a logo instead of a blog title. This is problematic for me for now, as I do not have a logo for my blog. So, using the easy way that Pelican uses to created the website, I added an _if_ statement to add a title instead:
{: style="text-align: justify"}

```html
<div id="logo">
    {% if USE_LOGO %}
        <span class="site-name"><a class="navbar-brand" href="{{ SITEURL }}"><img width="310" src="{{ USER_LOGO_URL }}" class="attachment-full size-full" alt="logo"></a>
        </span><!-- end of .site-name -->
    {% else %}
        <div id="web-title">
            {{ SITENAME }}
        </div> 
    {% endif%}
</div><!-- end of #logo -->
```


In the code above, I create a new variable ``USE_LOGO`` that, if true, will add an image with the logo. Otherwise, it will just add the site name using the ``SITENAME`` variable. This variable can be activated and deactivated by changing it to ``True`` or ``False`` in the ``pelicanconf.py`` file.
{: style="text-align: justify"}

Another thing that I did not particularly like is the tag line at the top of the page. I prefer it at the bottom so all I needed to do what to move appropriate block to the bottom of the base file while at the same time avoiding the tag line effect in CSS by consolidating the two variables, ``TAGS_URL`` and ``ARCHIVES_URL``, in one variable ``TAGS_ARCHIVES_URL``. In any case, I would use these at the same time anyways.
{: style="text-align: justify"}

```html
{% if TAGS_ARCHIVES_URL %}
    <div class="tagline">
    </div>
    <div class="tagline">
    {% for tag, articles in tags|sort %}
        <a href="{{ SITEURL }}/{{ tag.url }}" {{ 'class="active"' if  output_file == tag.url }}>{{ tag }} ({{ articles|count }})</a> &#124; 
    {% endfor %}
    <a href="{{ SITEURL }}/{{ ARCHIVES_URL }}" {{ 'class="active"' if  output_file == ARCHIVES_URL }}>{{ 'Archives ('+ articles|count|string + ')' if  articles|count > all_articles|count  else 'Archives (' + all_articles|count|string + ')'}}</a>
    </div>
{% endif %}
```


Finally, I change the footer by adding the links again. I used another variable ``REUSE_LINKS`` which by default will show nothing. Another variable ``USE_PRIVACY_POLICY`` is used to add a link to the privacy policy of the page.
{: style="text-align: justify"}

```html
{% if REUSE_LINKS %}
    {% for name, link in LINKS %}
        {{ display_link(name, link, name) }}|
    {% endfor %}
{% endif %}
{% if USE_PRIVACY_POLICY %}
    <a href="{{ SITEURL }}/pages/privacy-policy">Privacy Policy</a> 
{% endif %}
```


That's it! Now I have a page that I can control as I wish! There are a few things that need improvement (like syntax highlighting) but all in all, it was not as hard as I imagined.
{: style="text-align: justify"}