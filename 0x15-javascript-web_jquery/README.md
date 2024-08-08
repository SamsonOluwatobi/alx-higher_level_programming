# 0x15. Javascript - Web JQuery

## Description

Learning objectives of this project:

- Selecting HTML elements in Javascript and jQuery
- Understanding the differences between ID, class, and tag name selectors
- Modifying HTML element style and content
- Manipulating the DOM
- Making GET and POST requests with jQuery Ajax
- Listening and binding to DOM and user events

---

### [0. No jQuery](./0-script.js)

- Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`) using `document.querySelector` instead of jQuery API.

### [1. With jQuery](./1-script.js)

- Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`) using the jQuery API instead of `document.querySelector`.

### [2. Click and turn red](./2-script.js)

- Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header` using the jQuery API.

### [3. Add `.red` class](./3-script.js)

- Javascript script that adds the class red to the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag`DIV#red_header` using the jQuery API.

### [4. Toggle classes](./4-script.js)

- Javascript script that toggles the class of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#toggle_header` using the jQuery API.

### [5. List of elements](./5-script.js)

- Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item using the jQuery API.

### [6. Change the text](./6-script.js)

- Javascript script that updates the text of the HTML tag `HEADER` to “New Header!!!” when the user clicks on `DIV#update_header` using the jQuery API.

### [7. Star wars character](./7-script.js)

- Javascript script that fetches and replaces the name of this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json` in the HTML tag `DIV#character` using the jQuery API.

### [8. Star Wars movies](./8-script.js)

- Javascript script that fetches and lists all movies title by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json` in the HTML tag `UL#list_movies` using the jQuery API.

### [9. Say Hello!](./9-script.js)

- Javascript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of hello from that fetch in the HTML’s tag `DIV#hello` using the jQuery API. The translation of “hello” must be displayed in the HTML tag `DIV#hello`. The script must work when it is imported from the `HEAD` tag.

### [10. No jQuery - document loaded](./100-script.js)

- Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):
    - Must use `document.querySelector` to select the HTML tag.
    - Can’t use the jQuery API.
    - The script must work when it is imported from the `HEAD` tag.

### [11. List, add, remove](./101-script.js)

- Javascript script that adds, removes and clears LI elements from a list when the user clicks:
    - The new element must be: `<li>Item</li>`
    - The new element must be added to `UL.my_list`
    - When the user clicks on `DIV#add_item` a new element is added to the list
    - When the user clicks on `DIV#remove_item` a last element is removed to the list
    - When the user clicks on `DIV#clear_list` all elements of the list are removed
    - Can’t use `document.querySelector` to select the HTML tag.
    - Must use the jQuery API.
    - The script must work when it is imported from the `HEAD` tag.

### [12. Say hello to everybody!](./102-script.js)

- Javascript script that fetches and prints how to say “Hello” depending on the language
    - Use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
    - The language code will be the value entered in the tag `INPUT#language_code` (ex: es, fr, en etc.)
    - The translation must be fetched when the user clicks on `INPUT#btn_translate`
    - The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
    - Can’t use `document.querySelector` to select the HTML tag.
    - Must use the jQuery API.
    - The script must work when it is imported from the `HEAD` tag.

### [13. And press ENTER](./103-script.js)

- Javascript script that fetches and prints how to say “Hello” depending on the language
    - Use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
    - The language code will be the value entered in the tag `INPUT#language_code` (ex: es, fr, en etc.)
    - The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses ENTER when the focus is on `INPUT#language_code`
    - The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
    - Can’t use `document.querySelector` to select the HTML tag.
    - Must use the jQuery API.
    - The script must work when it is imported from the `HEAD` tag.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Open the desired script file in your preferred code editor.
4. Run the script in your browser or using a JavaScript runtime environment.

## Dependencies

This project requires the following dependencies:

- jQuery library

You can include the jQuery library by adding the following script tag to your HTML file:

```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```



## Author

- **Lana Samson Oluwatobi** - [SamsonOluwatobi](https://github.com/SamsonOluwatobi)

