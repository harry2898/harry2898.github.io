package hw2;

public class ClockRadioTest {
	
	public static void main(String args[]) {
        System.setOut(new java.io.PrintStream(System.out) {

            private StackTraceElement getCallSite() {
                for (StackTraceElement e : Thread.currentThread()
                        .getStackTrace())
                    if (!e.getMethodName().equals("getStackTrace")
                            && !e.getClassName().equals(getClass().getName()))
                        return e;
                return null;
            }

            @Override
            public void println(String s) {
                println((Object) s);
            }

            @Override
            public void println(Object o) {
                StackTraceElement e = getCallSite();
                String callSite = e == null ? "??" :
                    String.format("%s.%s(%s:%d)",
                                  e.getClassName(),
                                  e.getMethodName(),
                                  e.getFileName(),
                                  e.getLineNumber());
                super.println(o + "\t\tat " + callSite);
            }
        });
		System.out.println("Constructor Tests");
		System.out.println();
		System.out.println();
		
		ClockRadio r = new ClockRadio();
		System.out.println("New Standard Radio Constructed");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Alarm Time in Military Mode. Expecting: '01:00' Result: " + r.getAlarmTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Alarm Time in Standard Mode. Expecting: '01:00 AM' Result: " + r.getAlarmTimeAsString());
		System.out.println();
		
		System.out.println("Get Alarm Time in Raw Mode. Expecting: '60' Result: " + r.getAlarmTimeRaw());
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode. Expecting: '00:00' Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode. Expecting: '12:00 AM' Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode. Expecting: '0' Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r = new ClockRadio(320);
		System.out.println("New Advanced Radio Constructed. Set to: '320'");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Alarm Time in Military Mode");
		System.out.println("Expecting: '01:00'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Alarm Time in Standard Mode");
		System.out.println("Expecting: '01:00 AM'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();
		
		System.out.println("Get Alarm Time in Raw Mode");
		System.out.println("Expecting: '60'");
		System.out.println("Result: " + r.getAlarmTimeRaw());
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '05:20'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '05:20 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '320'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r = new ClockRadio(640);
		System.out.println("New Advanced Radio Constructed. Set to: '640'");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Alarm Time in Military Mode");
		System.out.println("Expecting: '01:00'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Alarm Time in Standard Mode");
		System.out.println("Expecting: '01:00 AM'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();
		
		System.out.println("Get Alarm Time in Raw Mode");
		System.out.println("Expecting: '60'");
		System.out.println("Result: " + r.getAlarmTimeRaw());
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:40'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:40 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '640'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r = new ClockRadio(755);
		System.out.println("New Advanced Radio Constructed. Set to: '755'");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Alarm Time in Military Mode");
		System.out.println("Expecting: '01:00'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Alarm Time in Standard Mode");
		System.out.println("Expecting: '01:00 AM'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();
		
		System.out.println("Get Alarm Time in Raw Mode");
		System.out.println("Expecting: '60'");
		System.out.println("Result: " + r.getAlarmTimeRaw());
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '12:35'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '12:35 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '755'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r = new ClockRadio(925);
		System.out.println("New Advanced Radio Constructed. Set to: '925'");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Alarm Time in Military Mode");
		System.out.println("Expecting: '01:00'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Alarm Time in Standard Mode");
		System.out.println("Expecting: '01:00 AM'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();
		
		System.out.println("Get Alarm Time in Raw Mode");
		System.out.println("Expecting: '60'");
		System.out.println("Result: " + r.getAlarmTimeRaw());
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '15:25'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '03:25 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '925'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r = new ClockRadio(1309);
		System.out.println("New Advanced Radio Constructed. Set to: '1309'");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Alarm Time in Military Mode");
		System.out.println("Expecting: '01:00'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Alarm Time in Standard Mode");
		System.out.println("Expecting: '01:00 AM'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();
		
		System.out.println("Get Alarm Time in Raw Mode");
		System.out.println("Expecting: '60'");
		System.out.println("Result: " + r.getAlarmTimeRaw());
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '21:49'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '09:49 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1309'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r = new ClockRadio(2090);
		System.out.println("New Advanced Radio Constructed. Set to: '2090'");
		System.out.println();

		r.set24HourDisplay(true);

		System.out.println("Get Alarm Time in Military Mode");
		System.out.println("Expecting: '01:00'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Alarm Time in Standard Mode");
		System.out.println("Expecting: '01:00 AM'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();

		System.out.println("Get Alarm Time in Raw Mode");
		System.out.println("Expecting: '60'");
		System.out.println("Result: " + r.getAlarmTimeRaw());
		System.out.println();

		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:50'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:50 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '650'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();

		r = new ClockRadio(2288);
		System.out.println("New Advanced Radio Constructed. Set to: '2288'");
		System.out.println();

		r.set24HourDisplay(true);

		System.out.println("Get Alarm Time in Military Mode");
		System.out.println("Expecting: '01:00'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Alarm Time in Standard Mode");
		System.out.println("Expecting: '01:00 AM'");
		System.out.println("Result: " + r.getAlarmTimeAsString());
		System.out.println();

		System.out.println("Get Alarm Time in Raw Mode");
		System.out.println("Expecting: '60'");
		System.out.println("Result: " + r.getAlarmTimeRaw());
		System.out.println();

		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '14:08'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '02:08 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '848'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		System.out.println();
		System.out.println();
		System.out.println();
		System.out.println();
		System.out.println();
		System.out.println();
		
		System.out.println("Set Time Tests");
		System.out.println();
		
		r.setTime(320);
		System.out.println("Set Time to 320");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '05:20'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '05:20 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '320'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(640);
		System.out.println("Set Time to 640");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:40'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:40 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '640'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(755);
		System.out.println("Set Time to 755");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '12:35'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '12:35 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '755'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(925);
		System.out.println("Set Time to 925");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '15:25'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '03:25 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '925'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(1309);
		System.out.println("Set Time to 1309");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '21:49'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '09:49 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1309'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(2090);
		System.out.println("Set Time to 2090");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:50'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:50 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '650'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(2288);
		System.out.println("Set Time to 2288");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '14:08'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '02:08 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '848'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(5, 20, false);
		System.out.println("Set Time to 05:20 AM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '05:20'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '05:20 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '320'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(10, 40, false);
		System.out.println("Set Time to 10:40 AM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:40'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:40 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '640'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(12, 35, true);
		System.out.println("Set Time to 12:35 PM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '12:35'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '12:35 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '755'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(3, 25, true);
		System.out.println("Set Time to 03:25 PM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '15:25'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '03:25 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '925'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(9, 49, true);
		System.out.println("Set Time to 09:49 PM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '21:49'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '09:49 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1309'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(10, 50, false);
		System.out.println("Set Time to 10:50 AM");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:50'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:50 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '650'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(2, 8, true);
		System.out.println("Set Time to 02:08 PM");
		System.out.println();
		
		r.set24HourDisplay(true);
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '14:08'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '02:08 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '848'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		System.out.println();
		System.out.println();
		System.out.println();
		System.out.println();
		System.out.println();
		System.out.println();
		
		System.out.println("Advance Time Tests");
		System.out.println();
		
		r.setTime(0);
		System.out.println("Set Time to 0");
		System.out.println();
		
		r.advanceTime(320);
		System.out.println("Advanced Time to 320");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '05:20'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '05:20 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '320'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(640);
		System.out.println("Advanced Time to 640");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:40'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:40 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '640'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(755);
		System.out.println("Advanced Time to 755");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '12:35'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '12:35 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '755'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(925);
		System.out.println("Advanced Time to 925");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '15:25'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '03:25 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '925'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(1309);
		System.out.println("Advanced Time to 1309");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '21:49'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '09:49 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1309'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(2090);
		System.out.println("Advanced Time to 2090");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:50'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);


		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:50 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '650'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(2288);
		System.out.println("Advanced Time to 2288");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '14:08'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '02:08 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '848'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(5, 20);
		System.out.println("Advanced Time to 05:20 AM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '05:20'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '05:20 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '320'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(10, 40);
		System.out.println("Advanced Time to 10:40 AM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:40'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:40 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '640'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(12, 35);
		System.out.println("Advanced Time to 12:35 PM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '12:35'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '12:35 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '755'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(15, 25);
		System.out.println("Advanced Time to 03:25 PM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '15:25'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '03:25 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '925'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(21, 49);
		System.out.println("Advanced Time to 09:49 PM");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '21:49'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '09:49 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1309'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(10, 50);
		System.out.println("Advanced Time to 10:50 AM");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '10:50'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:50 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '650'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(0);
		System.out.println("Reset Time to 0");
		System.out.println();
		
		r.advanceTime(14, 8);
		System.out.println("Advanced Time to 02:08 PM");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '14:08'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '02:08 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '848'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(3, 0, false);
		System.out.println("Set Time to 3:00 AM");
		System.out.println();
		
		r.advanceTime(320);
		System.out.println("Advanced Time by 320");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '08:20'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '08:20 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '500'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(63);
		System.out.println("Reset Time to 63");
		System.out.println();
		
		r.advanceTime(640);
		System.out.println("Advanced Time by 640");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '11:43'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '11:43 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '703'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(485);
		System.out.println("Reset Time to 485");
		System.out.println();
		
		r.advanceTime(755);
		System.out.println("Advanced Time by 755");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '20:40'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '08:40 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1240'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(515);
		System.out.println("Reset Time to 515");
		System.out.println();
		
		r.advanceTime(925);
		System.out.println("Advanced Time by 925");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '00:00'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '12:00 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '0'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(3, 20, false);
		System.out.println("Reset Time to 3:20 AM");
		System.out.println();
		
		r.advanceTime(1309);
		System.out.println("Advanced Time by 1309");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '01:09'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '01:09 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '69'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(12, 0, true);
		System.out.println("Reset Time to 12:00 PM");
		System.out.println();
		
		r.advanceTime(2090);
		System.out.println("Advanced Time by 2090");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '22:50'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:50 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1370'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(6008);
		System.out.println("Reset Time to 6008");
		System.out.println();
		
		r.advanceTime(2288);
		System.out.println("Advanced Time to 2288");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '18:16'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '06:16 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1096'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(180);
		System.out.println("Set Time to 180");
		System.out.println();
		
		r.advanceTime(5, 20);
		System.out.println("Advanced Time by 5:20");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '08:20'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '08:20 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '500'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(1, 3, false);
		System.out.println("Reset Time to 1:03 AM");
		System.out.println();
		
		r.advanceTime(10, 40);
		System.out.println("Advanced Time by 10:40");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '11:43'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '11:43 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '703'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(8, 5, false);
		System.out.println("Reset Time to 8:05 AM");
		System.out.println();
		
		r.advanceTime(12, 35);
		System.out.println("Advanced Time by 12:35");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '20:40'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '8:40 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1240'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(515);
		System.out.println("Reset Time to 515");
		System.out.println();
		
		r.advanceTime(15, 25);
		System.out.println("Advanced Time by 15:25");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '00:00'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '12:00 AM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '0'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(3, 20, true);
		System.out.println("Reset Time to 3:20 PM");
		System.out.println();
		
		r.advanceTime(21, 49);
		System.out.println("Advanced Time by 21:49");
		System.out.println();
		
		r.set24HourDisplay(true);
		
		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '13:09'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);
		
		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '01:09 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();
		
		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '789'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(12, 0, true);
		System.out.println("Reset Time to 12:00 PM");
		System.out.println();
		
		r.advanceTime(34, 50);
		System.out.println("Advanced Time by 34:50");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '22:50'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '10:50 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode");
		System.out.println("Expecting: '1370'");
		System.out.println("Result: " + r.getClockTimeRaw());
		System.out.println();
		
		r.setTime(6008);
		System.out.println("Reset Time to 6008");
		System.out.println();
		
		r.advanceTime(38, 8);
		System.out.println("Advanced Time by 38:08");
		System.out.println();
		
		r.set24HourDisplay(true);

		System.out.println("Get Clock Time in Military Mode");
		System.out.println("Expecting: '18:16'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		r.set24HourDisplay(false);

		System.out.println("Get Clock Time in Standard Mode");
		System.out.println("Expecting: '06:16 PM'");
		System.out.println("Result: " + r.getClockTimeAsString());
		System.out.println();

		System.out.println("Get Clock Time in Raw Mode. Expecting: '1096' Result: " + r.getClockTimeRaw());
		System.out.println();
	}
}
