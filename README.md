# **Daily Translation**

Initial Commit -- 5/27/2019

*ToDo : Write usage readme
*

The purpose of this project is to develop a translation engine which will be text translated text to the user daily. The idea is to become better at several languages at once through daily practice. This follows a three step process:

1.  Pull quotes or random sentences from varying APIs
2.  Run these quotes through Google translation API to get a list of translated text
3.  Format and send these translations as a text message to the user so he/she can compare and practice

Right now the code has minimal functionality and can be improved in a dozen ways (probably more)

Future Implementations:
1. Host on Google Cloud -- Today it is running locally for testing
2. Subclass the quotes from a Quote superclass to make it more dynamic -- Today it is just running as a script with basic functions
