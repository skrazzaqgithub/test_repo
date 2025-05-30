"""
Write a program that generates a HTML webpage.
Prompt the user for webpage title and webpage body contents.
The webpage body should contain
 - one main header,
 - one sub header, and
 - at least 2 paragraphs.

A sample output is shown below :
<html>
    <head>
        <title>
            My webpage title
        </title>
    </head>

    <body>
        <h1>Webpage Banner</h1>
        <p>This is a sample story for my first webpage
        </p>
        <p>This is a how my sample story ends
        </p>
    </body>
</html>
"""

# URL = input("http://www.w3.org/1999/xhtml")
# print("Entered URL is: ", URL)
# for i in URL:
#     if i == "XHTML namespace":
#         print(i)


def generate_html():
    # Prompt user for input
    title = input("Enter the webpage title: ")
    main_header = input("Enter the main header: ")
    sub_header = input("Enter the sub header: ")

    # Prompt for paragraphs
    paragraph1 = input("Enter the first paragraph: ")
    paragraph2 = input("Enter the second paragraph: ")

    # Create the HTML content
    html_content = f"""<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head profile="http://www.w3.org/2003/g/data-view">
  <meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8">
  <title>XHTML namespace</title>
  <link rel="stylesheet" type="text/css" href="https://www.w3.org/StyleSheets/TR/base">
  <link rel="transformation" href="https://www.w3.org/2008/07/rdfa-xslt">
  <link xmlns:data-view="http://www.w3.org/2003/g/data-view#" about="http://www.w3.org/1999/xhtml" rel="data-view:namespaceTransformation" href="https://www.w3.org/2008/07/rdfa-xslt">
</head>

<body>

<div class="head">
<p><a href="https://www.w3.org/"><img class="head" src="https://www.w3.org/Icons/WWW/w3c_home" alt="W3C"></a></p>
</div>

<h1><abbr title="Extensible HyperText Markup Language">XHTML</abbr>
namespace</h1>

<p>The namespace name <tt>http://www.w3.org/1999/xhtml</tt> is intended for use
in various specifications such as:</p>

<p>Recommendations:</p>
<ul>
  <li><cite><a href="https://www.w3.org/TR/html5/">HTML 5: A vocabulary and
    associated APIs for HTML and XHTML</a></cite></li>
  <li><cite><a href="https://www.w3.org/TR/xhtml1"><abbr>XHTML</abbr>™ 1.0:
    The Extensible HyperText Markup Language</a></cite></li>
  <li><cite><a href="https://www.w3.org/TR/xhtml-modularization"><abbr>XHTML</abbr>
    Modularization</a></cite></li>
  <li><cite><a href="https://www.w3.org/TR/xhtml11"><abbr>XHTML</abbr>
    1.1</a></cite></li>
  <li><cite><a href="https://www.w3.org/TR/xhtml-basic"><abbr>XHTML</abbr>
    Basic</a></cite> </li>
  <li><a href="https://www.w3.org/TR/xhtml-print/"><cite>XHTML
  Print</cite></a></li>
  <li><a href="https://www.w3.org/TR/rdfa-syntax/"><cite>XHTML+RDFa</cite></a></li>
</ul>

<p>Other Documents:</p>
<ul>
  <li><cite><a href="https://www.w3.org/TR/html51/">HTML 5.1</a></cite></li>
  <li><cite><a href="https://www.w3.org/TR/html52/">HTML 5.2</a></cite></li>
</ul>

<p>The charters of the following W3C Working Groups include work on HTML that
may impact this namespace: </p>
<ul>
  <li><a href="https://www.w3.org/WebPlatform/WG/">Web Platform Working Group</a>, chartered
    October 2015</li>
</ul>

<p>For more information about <abbr>XML</abbr> namespaces, please refer to
<cite><a href="https://www.w3.org/TR/REC-xml-names">Namespaces in
<abbr>XML</abbr></a></cite>.</p>
<hr>
<address>
  Michael Smith, W3C HTML Activity Lead 
</address>
<address>
  Last edited: $Date: 2016/09/07 14:16:54 $ <br>
</address>


</body></html>"""

    # Output the HTML content
    print("\nGenerated HTML:")
    print(html_content)


# Run the function
generate_html()

