const quotes=[
    {
        quote:"Be the change you wish to see in the world.",
        author:"Mahatma Gandhi",
    },
    {
        quote:"The greatest glory in living lies not in never falling, but in rising every time we fall.",
        author:"Nelson Mandela",
    },
    {
        quote:"The way to get started is to quit talking and begin doing.",
        author:"Walt Disney",
    },
    {
        quote:"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
        author:"Steve Jobs",
    },
    {
        quote:"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
        author:"Oprah Winfrey",
    },
    {
        quote:"The future belongs to those who believe in the beauty of their dreams.",
        author:"Eleanor Roosevelt",
    },
    {
        quote:"The only thing we have to fear is fear itself.",
        author:"Franklin D. Roosevelt",
    },
    {
        quote:"Do one thing every day that scares you.",
        author:"Eleanor Roosevelt",
    },
    {
        quote:"It is during our darkest moments that we must focus to see the light.",
        author:"Aristotle",
    },
    {
        quote:"Do not go where the path may lead, go instead where there is no path and leave a trail.",
        author:"Ralph Waldo Emerson",
    },
]

const quote=document.querySelector('#quote span:first-child');
const author=document.querySelector('#quote span:last-child');

const todaysQuotes=quotes[Math.floor(Math.random()*quotes.length)];

quote.innerText=todaysQuotes.quote;
author.innerText=todaysQuotes.author;
