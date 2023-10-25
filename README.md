# TriSonics 4003 ROMI Code

This is a repository that contains RobotPy based projects for a ROMI robot.

## Lessons learned so far:
- The ROMI isn't great at alerting to a low battery. It will look powered on
and operating but no WiFi network will come up. Putting a volt meter to it
and verifying that you've got 9.0V of power from the batteries is a good idea
when things aren't going according to plan. The Raspberry Pi on top will
appear to boot and run, but does not function properly.

- The Command V2 framework, which existed in Java, follows the same patterns as
before, reducing the learning curve, but is a bit more verbose than other
frameworks available in RobotPy.

- The MagicBot framework reduces some of the "boilerplate" code needed to
instantiate and make available objects to all aspects of the system. While
this is nice and convienient it does appear to be a pattern that won't work
well with Python linters. For this reason I'm leaning toward using the Command
V2 framework.





