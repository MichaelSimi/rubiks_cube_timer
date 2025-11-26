Welcome!

I decided to create a Rubik's Cube timer, similar to CStimer.

It turned out great!

Here is an overview of all features:

1. There is a scrambler that randomly generates a 20 move long scramble using the random module. You can generate a new scramble by simply pressing the "next scramble" button on the top-right.
2. There is a timer! Press any key on your keyboard, and when you release it, the timer starts running! To stop the timer, press down any key. The elapsed time will be showing on the screen. When the timer stops, a new scramble automatically gets generated, and it shown on the top of the screen. This is done using the time module.
3. Near the top of the screen, it says your average. It automatically calculates the average using all your solves. 
4. As well as the average, it says your best and worst times too. This is near the right of the screen.
5. If you click “Show times”, you will see all of the times you made, in seconds. The time that is the color green is the solve you just did, and the red ones are the solves you did previously. When the times reach the bottom, you can use your scroller to move up and down to see all of the times you got. To make the times disappear again, simply click “Show times” once more.
6. If the timer goes into minutes or hours, it autimatically formats the time to be: hours:minutes:seconds.

Note: The display is made using the pygame library.

And that is pretty much all! Enjoy!
