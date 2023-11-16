public class Time {
    public int hours;
    public int minutes;

    public Time addTime(Time otherTime){
        int godziny = this.hours + otherTime.hours;
        int minuty = this.minutes + otherTime.minutes;
        Time returnTime = new Time();
        if(godziny > 23){
            System.out.println("Za duzo godzin");
            return returnTime;
        }
        if(minuty > 59){
            System.out.println("Za duzo minut");
            return returnTime;
        }

        returnTime.minutes = minuty;
        returnTime.hours = godziny;
        return returnTime;
    }
}
