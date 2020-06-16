# ex2_ground_station_website

In this repository we are attempting to make a functional and extendable groundstation for the operators of the [Ex-Alta 2 satellite](https://albertasat.ca/ex-alta-2/). It is a Flask web app that uses a REST API for the back end (Python), paired with a React MaterialUI interface on the front end (JavaScript). Also included in this repository is a "satellite simulator" python module used to simulate the interaction between our app and a real cubesat. A "comm" (communications) module intermediates this exchange. Finally, a collection of scripts are used to achieve the goal of automating some aspects of the groundstation app. Follow the links below to see the documentation.

[![Build Status](https://travis-ci.com/UAlberta-CMPUT401/AlbertaSat.svg?token=TRHuLXSMdv9x8426GEpU&branch=dev)](https://travis-ci.com/UAlberta-CMPUT401/AlbertaSat)

---

### Links

**[How to install, run, and develop the project](INSTALL.md)** - Details installation, usage, and notes on important modules.

**[Generated source code documentation](https://ualberta-cmput401.github.io/AlbertaSat/)** - This is automatically generated documentation from the Python code. It lives in `/docs`. When you make changes to the Python code, update this documentation to match it using `source ./update_docs.sh`. If you would like to view the docs locally, serve it with `python3 -m http.server` and go to http://0.0.0.0:8000/ in your browser.

**[REST API backend documentation](https://documenter.getpostman.com/view/9298924/SW11YKEd)** - This is documentation for the REST backend API (`groundstation/backend_api`) of this Flask app. There are examples of requests that you can make to the backend and what responses to expect.

**[Glossary](https://github.com/UAlberta-CMPUT401/AlbertaSat/wiki/Glossary)** - Go here if you're confused about a word or phrase that we keep using.

**[Wiki](https://github.com/UAlberta-CMPUT401/AlbertaSat/wiki)** - See more information about the project's design and development.
