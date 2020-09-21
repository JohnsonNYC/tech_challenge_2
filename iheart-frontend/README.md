iHeartMedia - Music Lab - Code Challenge
This challenge is designed to give us an idea of what point in the code spectrum you're currently on. There are no tricks, deceptive or complex issues to work through.

This does not need to be the fanciest, most complex, or most impressive code we've ever seen. Focus on human readability, then performance as a secondary factor.

Everything will be written in JavaScript / Node, or TypeScript if you're feeling froggy.

Fork this repo and share the link when you are finished!

UI Checklist
Create a client side rendered web app written with React. √

It is highly recommended to use create-react-app to accomplish this.√
Create a React App using functional based components and hooks. No class based components, please. √
The app needs to have at least 2 pages (views): √

A landing page. √
A page renders a table displaying a list songs coming from the API. √
On mount of the this page, make a request to your API, fetching the songs and display the results in a table. √
Feel free to use whatever attributes you'd like (artist, song name, label, etc.) √
Use React Router to allow the user to change the page they are viewing. √
Style is not important, meaning you won't be evaluated on looks or design. If you'd like to make it look nice, by all means.

It does not need to be mobile responsive.

API Notes
Create a simple REST API that will serve the content needed for the client to render it. √

The most direct approach would be to make an Express API, but if you're familiar with a different framework, that's okay.√
Authentication is not necessary. √

In the data/ folder, create a file called songs.json. 

When someone makes a get request to /songs, send back the contents of songs.json. 
If you're unfamiliar with Express, or REST APIs, you'll need to setup a route handler listening for get requests for the /songs path. √

You do not need to deploy or host this anywhere.

Bonus
Big bonus points for any of these, monumental points for 2, unfathomable points for all.

Make UI Columns Sortable
Allow the songs to be sorted when a user clicks on the header for the corresponding column.

Write Some Tests
The engine is up to you, but take a look at Jest, as this is our primary test runner.

AWS Serverless
Instead of using Express for the API, serve the same content with an AWS serverless API using the Serverless Framework.

GraphQL
Instead of a REST API, serve the same content from a GraphQL API.