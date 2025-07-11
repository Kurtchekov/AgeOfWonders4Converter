**This requires Python 3 installed!**

## Steam to GOG

Put all files in the same folder as your empire/pantheon `FILE` resides, normally
`C:\Program Files (x86)\Steam\userdata\[YOUR STEAM ID]\1669000\remote\Empire\[SOME UUID NUMBER]\`. 
Then, run the "steam_to_gog" specific to your system (sh for linux and bat for windows).

This python script will append a header to your pantheon FILE and automatically generate a nice uuid name for it. 
Once it's done, you should get a new file in the same folder with a uuid name that resembles the format used in the 
GOG version of the game.
Move the generated file to `C:\users\[YOUR USERNAME]\My Documents\Paradox Interactive\Age of Wonders 4\Storage\Empire\` 
and that should do the trick!

## GOG to Steam

Put all files in the same folder as your empire/pantheon UUID file resides, normally
`C:\users\[YOUR USERNAME]\My Documents\Paradox Interactive\Age of Wonders 4\Storage\Empire\`. 
Then, run the "gog_to_steam" specific to your system (sh for linux and bat for windows).
The script will automatically scan its folder for any UUID files and turn them to a file named `FILE`.
Move that file to `C:\Program Files (x86)\Steam\userdata\[YOUR STEAM ID]\1669000\remote\Empire\[OLD UUID FROM GOG]\` and
that's it!

This version is a bit simpler than the Steam to GOG one as it simply strips the header from the UUID file.