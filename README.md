# Selenium for Web Scraping
 
### What is Selenium
<hr>

- It is a tool or framework for automating web browsers.
- An API for web browsers
- Recording tools for automated testing
- Selenium server for remote execution

<br>

### Why automated testing
<hr>

- Regression [ Falling Backword ] : Sometimes has been stopped.
- Testing like a real a real user.
- Combinatorial Testing : Some test are better automated than manual.
- Exact requirements : Automated testing are exact and deterministic and not open for interpretation

<br>

### Selenium archtechture
<hr>

![image](https://user-images.githubusercontent.com/32831848/150167204-6ed59eac-606a-4a6f-a3b1-5f37fad178e8.png)

<br>

Now we will discuss about Web scraping terminology

<br>

### XPATH
<hr>

XPath is a technique in Selenium to navigate through the HTML structure of a page. XPath enables testers to navigate through the XML structure of any document, and this can be used on both HTML and XML documents.

While other locators in Selenium that search for elements using tags or CSS class names are simpler to use, they may not be sufficient to select all DOM elements of an HTML document. XPath provides an option to dynamically search for an element within a web page [Reference](https://www.browserstack.com/guide/xpath-in-selenium#:~:text=XPath%20is%20a%20technique%20in,both%20HTML%20and%20XML%20documents)


    <html>
    <head>...</head>
    <body>
    ...
    <form id="loginForm">
    <input name="name" type="text" value="First Name" />
    <input name="name" type="text" value="Last Name" />
    <input name="email" type="text" value="Business Email" />
    <input name="password" type="password" />
    <input name="continue" type="submit" value="Sign Me Up" />
    </form>
    </body>
    </html>


In this above example select the business email field is as follows:

1. Absolute Path : 
    > html/body/form/input[3]

2. Relative Path :
    > //form/input[3]
