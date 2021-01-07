# WebLibrary
It is simply django app, that use Rest Api in this case DRF

You can import books, and opinions from csv files. 
Informations you can put in book.csv files is:
  - isnb
  - author
  - name of book
  - genre.
  
Information you must put in opinions files is:
  -isnb
  -mark
  -opinion.
  
This informations will be store in data-base, and can be download via link:
eq. /api_v1/books/
