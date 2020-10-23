/*
Let the date be DD/MM/CCYY (european format), where DD is the day of the month, MM is the month, CC the century-digits and YY the year within the century. So Wilma's birthday was 23/06/1994. Starting with the century CC-digits, calculate CC/4 - 2*CC-1 and remember the result. With all divisions in this exercise, discard any remainder and just keep the whole part. So, in our example, this is 19/4=4 minus 2*19=38 minus 1, giving minus 35.

Now, using the year YY, calculate 5*YY/4. In this example that's 5*94 = 470/4 = 117, discarding the remainder. Adding this to our existing result gives 117-35 = 82.

Using the month MM, calculate 26*(MM+1)/10. In our example this is 26*7 = 182 / 10 = 18, again discarding the remainder. Add this to our running total giving 82+18 = 100.

Finally just add the day DD. Here 100 + 23 = 123.

Now divide the result by 7, just keeping the remainder; here 123(mod 7) = 4. Counting Sunday as zero, Monday = 1 etc, we get 4 = Thursday. Easy, when you know how :-)

The algorithm is attributed to Gauss. Yes, I do know that Jews and Muslims etc have different calenders and I do know about the various calender reforms, so this only applies to the modern Christian-based standardised dates, don't go using it to check the day of Christ's crucifixion (-fiction?) or even Chaucer's birth.

If you can't do this as mental arithmetic (thus winning beers in the pub) feel free to use pencil and paper (or a calculator).

*/

public String DayOfWeek()
{
    int dayofweek;
    int c,y,m,d; 
    int cc,yy;
    String dayString;
    //Im using the guassian algorithm for finding day of the week 
    cc = year/100;
    yy = year % 100;

    c = (cc/4) - 2*cc-1;
    y = 5*yy/4;
    m = 26*(month+1)/10;
    d = day;

    dayofweek = (c+y+m+d)%7;

    switch(dayofweek)
    {
        case 0: dayString = "Sunday";
        break;
        case 1: dayString = "Monday";
        break;
        case 2: dayString = "Tuesday";
        break;
        case 3: dayString = "Wednesday";
        break;
        case 4: dayString = "Thursday";
        break;
        case 5: dayString = "Friday";
        break;
        case 6: dayString = "Saturday";
        break;
        default: dayString = "Sorry Could not compute month :(";   
    }

    return dayString;
}
