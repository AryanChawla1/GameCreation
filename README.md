# Game Creation
The point of this project is to design a tower defense game similar to legendary wars.

## Models
Models contain the classes for the basic objects

## Notes
I want mana to be generated essentially forever (until game is over) but I am not sure how to do this effectively. My current idea is to use a process/thread to generate mana but I am not sure if it will properly allow other things to access the current mana. Maybe, I could make it so the process loops forever but constantly yield the mana?