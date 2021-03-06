package hw2;

/**
 * This class implements a fully functional alarm clock.
 * @author Harrison Helgevold
 */
public class ClockRadio {
	
	private int timeMinutesPastMidnight;
	
	private int timeHours;
	
	private int timeMinutes;
	
	private String timeAmOrPm;
	
	private int timeMilitaryHours;
	
	private int alarmMinutesPastMidnight;
	
	private int alarmHours;
	
	private int alarmMinutes;
	
	private String alarmAmOrPm;
	
	private int alarmMilitaryHours;
	
	private boolean alarmStatus;
	
	private boolean militaryMode;
	
	private boolean radioMode;
	
	private boolean soundingStatus;

	/**
	 * Number of minutes in a 24-hour day.
	 */
	public static final int MINUTES_PER_DAY = 1440;
	
	/**
	 * Number of minutes to silence the alarm when snoozing.
	 */
	public static final int SNOOZE_MINUTES = 9;
	
	
	/**
	 * Constructs a clock radio with initial clock time 
	 * at 00:00 and alarm time at 01:00.
	 */
	public ClockRadio()
	{
		timeMinutesPastMidnight = 0;
		timeHours = 0;
		timeMinutes = 0;
		timeAmOrPm = "AM";
		timeMilitaryHours = 0;
		
		if (militaryMode == false)
		{
			timeHours = 12;
		}
		
		alarmMinutesPastMidnight = 60;
		alarmHours = 1;
		alarmMinutes = 0;
		alarmAmOrPm = "AM";
		alarmMilitaryHours = 1;
		
		alarmStatus = false;
		militaryMode = true;
		radioMode = false;
		soundingStatus = false;
	}
	
	/**
	 * Constructs a clock radio with the given initial clock 
	 * time and with alarm time at 01:00.
	 * @param givenMinutesPastMidnight Minutes past midnight 
	 * the time will be set for.
	 */
	public ClockRadio(int givenMinutesPastMidnight)
	{
		timeMinutesPastMidnight = givenMinutesPastMidnight;
		while (timeMinutesPastMidnight >= MINUTES_PER_DAY)
		{
			timeMinutesPastMidnight = timeMinutesPastMidnight - MINUTES_PER_DAY;
		}
		
		timeHours = timeMinutesPastMidnight / 60;
		timeMinutes = timeMinutesPastMidnight % 60;
		
		timeMilitaryHours = timeHours;
		
		if (timeHours >= 13)
		{
			timeAmOrPm = "PM";
			timeHours = timeHours - 12;
		}
		else if (timeHours >= 12)
		{
			timeAmOrPm = "PM";
		}
		else if (timeHours == 0)
		{
			timeAmOrPm = "AM";
			timeHours = 12;
		}
		else
		{
			timeAmOrPm = "AM";
		}
		
		alarmMinutesPastMidnight = 60;
		alarmHours = 1;
		alarmMinutes = 0;
		alarmAmOrPm = "AM";
		alarmMilitaryHours = 1;
		
		alarmStatus = false;
		militaryMode = true;
		radioMode = false;
		soundingStatus = false;
	}
	
	/**
	 * Advances the clock time by the specified number 
	 * of minutes.
	 * @param givenMinutes Number of minutes the clock will be
	 * moved forward.
	 */
	public void advanceTime(int givenMinutes)
	{
		timeMinutesPastMidnight = timeMinutesPastMidnight + givenMinutes;
		while (timeMinutesPastMidnight >= MINUTES_PER_DAY)
		{
			timeMinutesPastMidnight = timeMinutesPastMidnight - MINUTES_PER_DAY;
		}
		
		timeHours = timeMinutesPastMidnight / 60;
		timeMinutes = timeMinutesPastMidnight % 60;
		
		timeMilitaryHours = timeHours;
		
		if (timeHours >= 13)
		{
			timeAmOrPm = "PM";
			timeHours = timeHours - 12;
		}
		else if (timeHours >= 12)
		{
			timeAmOrPm = "PM";
		}
		else if (timeHours == 0)
		{
			timeAmOrPm = "AM";
			timeHours = 12;
		}
		else
		{
			timeAmOrPm = "AM";
		}
		
		if (alarmStatus == true && timeMinutesPastMidnight > alarmMinutesPastMidnight)
		{
			soundingStatus = true;
		}
		else
		{
			soundingStatus = false;
		}
	}
	
	/**
	 * Advances the clock time by the given hours and minutes.
	 * @param givenHours Number of hours the clock will be
	 * moved forward.
	 * @param givenMInutes The number of minutes the clock
	 * will be moved forward in addition to the hours.
	 */
	public void advanceTime(int givenHours, int givenMinutes)
	{
		int priorMinutesPastMidnight = timeMinutesPastMidnight;
		int increasingMinutes = givenMinutes + givenHours * 60;
		timeMinutesPastMidnight = timeMinutesPastMidnight + increasingMinutes;
		while (timeMinutesPastMidnight >= MINUTES_PER_DAY)
		{
			timeMinutesPastMidnight = timeMinutesPastMidnight - MINUTES_PER_DAY;
		}
		
		timeHours = timeMinutesPastMidnight / 60;
		timeMinutes = timeMinutesPastMidnight % 60;
		
		timeMilitaryHours = timeHours;
		
		if (timeHours >= 13)
		{
			timeAmOrPm = "PM";
			timeHours = timeHours - 12;
		}
		else if (timeHours >= 12)
		{
			timeAmOrPm = "PM";
		}
		else if (timeHours == 0)
		{
			timeAmOrPm = "AM";
			timeHours = 12;
		}
		else
		{
			timeAmOrPm = "AM";
		}
		
		if (alarmMinutesPastMidnight < priorMinutesPastMidnight)
		{
			if (alarmStatus == true && timeMinutesPastMidnight > alarmMinutesPastMidnight)
			{
				soundingStatus = true;
			}
			else
			{
				soundingStatus = false;
			}
		}
		else if (alarmStatus == true && increasingMinutes > (alarmMinutesPastMidnight - priorMinutesPastMidnight))
		{
			soundingStatus = true;
		}
		else
		{
			soundingStatus = false;
		}
	}
	
	/**
	 * Turns off the alarm, stops it from sounding 
	 * (if it is sounding) and cancels snooze if it 
	 * is in effect.
	 */
	public void alarmDisabled()
	{
		alarmStatus = false;
	}
	
	/**
	 * Turns the alarm on.
	 */
	public void alarmEnabled()
	{
		alarmStatus = true;
	}
	
	/**
	 * Returns the current alarm time as a string in one of 
	 * the following forms, depending on whether the clock 
	 * is currently in 24-hour mode: "hh:mm", "hh:mm AM", 
	 * or "hh:mm PM".
	 * @return The the time the alarm is set to.
	 */
	public String getAlarmTimeAsString()
	{
		String hour = "";
		String minutes = "";
		
		String militaryHour = "";
		
		if (alarmHours < 10)
		{
			hour = "0" + alarmHours;
		}
		else
		{
			hour = "" + alarmHours;
		}
		if (alarmMinutes < 10)
		{
			minutes = "0" + alarmMinutes;
		}
		else
		{
			minutes = "" + alarmMinutes;
		}
		
		if (alarmMilitaryHours < 10)
		{
			militaryHour = "0" + alarmMilitaryHours;
		}
		else
		{
			militaryHour = "" + alarmMilitaryHours;
		}
		
		if (militaryMode == true)
		{
			return militaryHour + ":" + minutes;
		}
		else
		{
			return hour + ":" + minutes + " " + alarmAmOrPm;
		}
	}
	
	/**
	 * Returns the current alarm time as the number of minutes 
	 * past midnight.
	 * @return The time the alarm is set to in the form of
	 * minutes fast midnight.
	 */
	public int getAlarmTimeRaw()
	{
		return alarmMinutesPastMidnight;
	}
	
	/**
	 * Returns the current clock time as a string in one of the 
	 * following forms, depending on whether the clock is 
	 * currently in 24-hour mode: "hh:mm", "hh:mm AM", or
	 * "hh:mm PM".
	 * @return The time the clock is set to.
	 */
	public String getClockTimeAsString()
	{
		String hour = "";
		String minutes = "";
		
		String militaryHour = "";
		
		if (timeMinutes < 10)
		{
			minutes = "0" + timeMinutes;
		}
		else
		{
			minutes = "" + timeMinutes;
		}
		
		if (timeMilitaryHours < 10)
		{
			militaryHour = "0" + timeMilitaryHours;
		}
		else
		{
			militaryHour = "" + timeMilitaryHours;
		}
		
		if (militaryMode == true)
		{
			return militaryHour + ":" + minutes;
		}
		else
		{
			return hour + ":" + minutes + " " + timeAmOrPm;
		}
	}
	
	/**
	 * Returns the current clock time as the number of minutes 
	 * past midnight.
	 * @return The time the clock is set to in the form of 
	 * minutes past midnight.
	 */
	public int getClockTimeRaw()
	{
		return timeMinutesPastMidnight;
	}
	
	/**
	 * Returns the current effective alarm time as a string in 
	 * one of the following forms, depending on whether the 
	 * clock is currently in 24-hour mode: "hh:mm", "hh:mm AM", 
	 * or "hh:mm PM".
	 * @return The time the alarm is set to.
	 */
	public String getEffectiveAlarmTimeAsString()
	{
		return "dummy";
	}
	
	/**
	 * Returns the effective alarm time as the number of 
	 * minutes past midnight.
	 * @return The time the alarm is set to in the form of
	 * minutes past midnight.
	 */
	public int getEffectiveAlarmTimeRaw()
	{
		return 0;
	}
	
	/**
	 * Determines whether the alarm is currently buzzing.
	 * @return True if the alarm is buzzing, and false if it
	 * is not.
	 */
	public boolean isBuzzing()
	{
		if (soundingStatus == true && radioMode == false)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	/**
	 * Determines whether the alarm is currently playing 
	 * the radio.
	 * @return True if the radio is playing, and false if it
	 * is not.
	 */
	public boolean isPlayingRadio()
	{
		if (soundingStatus == true && radioMode == true)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
	
	/**
	 * Determines whether the alarm is currently sounding 
	 * (buzzer or radio).
	 * @return True if the alarm is sounding, and false if it 
	 * is not
	 */
	public boolean isSounding()
	{
		return soundingStatus;
	}
	
	/**
	 * Sets whether the clock should display time strings using 
	 * 24-hour mode.
	 * @param use24HourDisplay Whether or not to display in
	 * 24 hour mode.
	 */
	public void set24HourDisplay(boolean use24HourDisplay)
	{
		if (use24HourDisplay == true)
		{
			militaryMode = true;
		}
		else
		{
			militaryMode = false;
		}
	}
	
	/**
	 * Sets the alarm time to the given number of minutes past 
	 * midnight.
	 * @param givenMinutesPastMidnight Number of minutes past
	 * midnight.
	 */
	public void setAlarmTime(int givenMinutesPastMidnight)
	{
		alarmMinutesPastMidnight = givenMinutesPastMidnight;
		while (alarmMinutesPastMidnight >= MINUTES_PER_DAY)
		{
			alarmMinutesPastMidnight = alarmMinutesPastMidnight - MINUTES_PER_DAY;
		}
		
		alarmHours = alarmMinutesPastMidnight / 60;
		alarmMinutes = alarmMinutesPastMidnight % 60;
		
		alarmMilitaryHours = alarmHours;
		
		if (alarmHours >= 13)
		{
			alarmAmOrPm = "PM";
			alarmHours = alarmHours - 12;
		}
		else if (timeHours >= 12)
		{
			alarmAmOrPm = "PM";
		}		
		else if (timeHours == 0)
		{
			alarmAmOrPm = "AM";
			alarmHours = 12;
		}
		else
		{
			alarmAmOrPm = "AM";
		}
	}
	
	/**
	 * Sets the alarm time to the given hours and minutes.
	 * @param givenHours Number of hours.
	 * @param givenMinutes Number of minutes.
	 * @param isPm Whether the time is Pm or not.
	 */
	public void setAlarmTime(int givenHours, int givenMinutes, boolean isPm)
	{
		alarmHours = givenHours;
		alarmMinutes = givenMinutes;
		int additionalMinutes = 0;
		if (isPm == true)
		{
			alarmAmOrPm = "PM";
			additionalMinutes = 720;
			
			if(alarmHours == 12)
			{
				alarmMilitaryHours = givenHours;
				alarmMinutesPastMidnight = givenHours * 60 + givenMinutes;
			}
			else
			{
				alarmMilitaryHours = givenHours + 12;
				alarmMinutesPastMidnight = givenHours * 60 + givenMinutes + additionalMinutes;
			}
		}
		else
		{
			alarmAmOrPm = "AM";
			alarmMilitaryHours = alarmHours;
			alarmMinutesPastMidnight = givenHours * 60 + givenMinutes;
		}
	}
	
	/**
	 * Sets whether the clock should play the radio or the 
	 * buzzer when sounding the alarm.
	 * @param useRadio Whether to use the radio or not.
	 */
	public void setRadioMode(boolean useRadio)
	{
		if (useRadio == true)
		{
			radioMode = true;
		}
		else
		{
			radioMode = false;
		}
	}
	
	/**
	 * Sets the current clock time to the given number of 
	 * minutes past midnight.
	 * @param givenMinutesPastMidnight The number of minutes
	 * past midnight.
	 */
	public void setTime(int givenMinutesPastMidnight)
	{
		timeMinutesPastMidnight = givenMinutesPastMidnight;
		while (timeMinutesPastMidnight >= MINUTES_PER_DAY)
		{
			timeMinutesPastMidnight = timeMinutesPastMidnight - MINUTES_PER_DAY;
		}
		
		timeHours = timeMinutesPastMidnight / 60;
		timeMinutes = timeMinutesPastMidnight % 60;
		
		timeMilitaryHours = timeHours;
		
		if (timeHours >= 13)
		{
			timeAmOrPm = "PM";
			timeHours = timeHours - 12;
		}
		else if (timeHours >= 12)
		{
			timeAmOrPm = "PM";
		}
		else if (timeHours == 0)
		{
			timeAmOrPm = "AM";
			timeHours = 12;
		}
		else
		{
			timeAmOrPm = "AM";
		}
	}
	
	/**
	 * Sets the current clock time to the given hours 
	 * and minutes.
	 * @param givenHours Number of hours.
	 * @param givenMinutes Number of Minutes.
	 * @param isPm Whether the time is Pm or not.
	 */
	public void setTime(int givenHours, int givenMinutes, boolean isPm)
	{
		timeHours = givenHours;
		timeMinutes = givenMinutes;
		int additionalMinutes = 0;
		if (isPm == true)
		{
			timeAmOrPm = "PM";
			additionalMinutes = 720;
			
			if(timeHours == 12)
			{
				timeMilitaryHours = givenHours;
				timeMinutesPastMidnight = givenHours * 60 + givenMinutes;
			}
			else
			{
				timeMilitaryHours = givenHours + 12;
				timeMinutesPastMidnight = givenHours * 60 + givenMinutes + additionalMinutes;
			}
		}
		else
		{
			timeAmOrPm = "AM";
			timeMilitaryHours = timeHours;
			timeMinutesPastMidnight = givenHours * 60 + givenMinutes;
		}
	}
	
	/**
	 * Stops the clock from sounding and sets the effective 
	 * alarm time for SNOOZE_MINUTES minutes after the current 
	 * clock time.
	 */
	public void snooze()
	{
		
	}
}
