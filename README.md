# Literature Mashup Bot

A Twitter bot that mashs up two different French author and their works to create new titles.

## Bots inspiration

Inspired by [FlagMashupBot](https://github.com/antooro/FlagsMashupBot).
Inspired by defacto133/twitter-world-cloud-bot

## Books API

ISBNdb.com/apidocs
Google Books API
OpenLibrary.org/dev/docs/api

## TODO

- Add new methods to mashup titles:
  * join two title parts (of two different original titles)
  * machine learning with list of titles
- Create original title with the following format:
  * word alone (or with article e.g. "La Pluie" or "Pluie")
  * word with a qualification (e.g. "La Douce Pluie")
  * word with a context (e.g. "La Pluie du matin")
- Add new cover type _Folio_ and more (need to download a picture and to find the font)
- Add optional red banner _Goncourt 2020_
- Add optional _Preface_
- Add tests
- Publish repository
- Add possibility to create our own mashup (need a better website):
  * with a list of authors
  * totally free
- Find the type based on the book title
- Fix the function get_author_name_cut_join
