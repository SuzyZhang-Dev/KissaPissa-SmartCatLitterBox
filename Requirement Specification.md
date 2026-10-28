# Requirement Specification
## Requirement IDs
 Functional requirements start with F and non-functional requirements with NF. 
 The first number names the group, and the second number is the item within that group. 
 Groups follow the product goals but do not set the order of work; the Priority column does (for example, F2.6 belongs to group 2 but has priority 1).

|Group|Name|Scope|
|---|---|---|
|F1.x|Litter box cleanliness|Measure NH₃, detect and count visits, decide when the box needs cleaning, and remind the user. Product goal 1.|
|F2.x|Visit monitoring per cat|Identify each cat and monitor how often and how long it uses the box. Product goal 2.|
|F3.x|Health indicators|Per-cat weight and urine-related indicators. Exploratory; may be dropped. Product goal 3.|
|F4.x|Connectivity and data|Wi-Fi, MQTT, time sync, online status and buffering. Supports all goals.|
|F5.x|User interface and documentation|Web and mobile interface, README user manual. Supports all goals.|
|NF1.x|Quality requirements|How well the system must work. The Category column names the quality: performance, accuracy, reliability, security, privacy, usability, cat welfare, safety, maintainability or power.|

**Priority.**

- **1:** Required for the minimum viable product (target 17 Dec 2026).
- **2:** Planned; to be completed in spring 2027.
- **3:** Stretch goal; done only if time allows.

## Functional Requirements

| ID   | Category        | Description                                                                                                                                                                      | Depends on       | Priority |
| ---- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------- |
| F1.0 | Sensors         | The system must measure the ammonia (NH₃) level inside the litter box at least once per minute.                                                                                  | -                | 1        |
| F1.1 | Visit detection | The system must detect each visit to the litter box (cat entering and leaving).                                                                                                  | -                | 1        |
| F1.2 | Visit detection | The system must count the visits since the last cleaning.                                                                                                                        | F1.1, F1.4       | 1        |
| F1.3 | Cleanliness     | The system must set the box state to "Needs cleaning" when the NH₃ level exceeds a threshold, the visit count reaches **N**, or **X** hours have passed since the last cleaning. | F1.0, F1.2       | 1        |
| F1.4 | Control         | The user must be able to mark the box as cleaned with a button on the device or in the user interface, which resets the visit count and the NH₃ baseline.                        | F1.0             | 1        |
| F1.5 | Local feedback  | The device must show the box state (OK / Needs cleaning / Offline) with an RGB LED.                                                                                              | F1.3, F4.3       | 1        |
| F1.6 | Alerts          | The system must send a push notification to the user's phone when the box needs cleaning.                                                                                        | F1.3, F4.1       | 1        |
| F1.7 | Data            | The system must keep the history of NH₃ readings, visits and cleanings for at least 30 days.                                                                                     | F4.1             | 2        |
| F2.0 | Cat profiles    | The user must be able to register each cat with a name and microchip number.                                                                                                     | -                | 2        |
| F2.1 | Identification  | The system must identify the cat by reading its microchip when it enters the box.                                                                                                | F1.1, F2.0       | 2        |
| F2.2 | Identification  | The system must label a visit as "Unknown cat" when no microchip is read.                                                                                                        | F2.1             | 2        |
| F2.3 | Data            | The system must record the cat, start time and duration of each visit.                                                                                                           | F1.1, F2.1       | 2        |
| F2.4 | User interface  | The user interface must show the number of visits per cat per day and the visit history.                                                                                         | F2.3, F5.0       | 2        |
| F2.5 | Alerts          | The system must notify the user when a cat's visits in 24 hours exceed **X** or its own 7-day average by **X** %.                                                                | F2.3             | 2        |
| F2.6 | Alerts          | The system must notify the user when a single visit lasts longer than **X** minutes, naming the cat when it is identified.                                                       | F1.1             | 1        |
| F3.0 | Sensors         | The system must measure the total weight of the litter box.                                                                                                                      | -                | 3        |
| F3.1 | Health          | The system must record each cat's weight during its visit and show the weight trend.                                                                                             | F3.0, F2.1       | 3        |
| F3.2 | Health          | The system must estimate whether the cat eliminated during a visit from the weight and NH₃ changes.                                                                              | F3.0, F1.0, F2.3 | 3        |
| F3.3 | Health          | The system must detect color changes of health-indicator litter with a camera.                                                                                                   | F2.3             | 3        |
| F4.0 | Network         | The device must connect to the home Wi-Fi network using credentials from a configuration file.                                                                                   | -                | 1        |
| F4.1 | Data            | The device must send sensor readings and visit records to the Home Assistant server via MQTT.                                                                                    | F4.0             | 1        |
| F4.2 | Network         | The device must report its Wi-Fi signal strength (RSSI) every **X** minutes.                                                                                                     | F4.1             | 1        |
| F4.3 | Network         | The system must show whether the device is online or offline.                                                                                                                    | F4.1             | 1        |
| F4.4 | Network         | The device must reconnect automatically after a Wi-Fi or server outage.                                                                                                          | F4.0             | 1        |
| F4.5 | Network         | The device must synchronize its clock over the network (NTP).                                                                                                                    | F4.0             | 1        |
| F4.6 | Data            | The device must buffer data during an outage and send it when the connection returns.                                                                                            | F4.4             | 2        |
| F4.7 | Alerts          | The system must notify the user when the device has been offline for more than **X** minutes.                                                                                    | F4.3             | 2        |
| F5.0 | User interface  | The user interface must be accessible from a web browser and the Home Assistant mobile app.                                                                                      | F4.1             | 1        |
| F5.1 | User interface  | The home screen must show the box state, today's visit count and the time of the last cleaning.                                                                                  | F1.2, F1.3, F5.0 | 1        |
| F5.2 | Documentation   | The project must include a user manual in the README file on GitHub.                                                                                                             | -                | 1        |

## Non-Functional Requirements

| ID     | Category        | Description                                                                                                    | Depends on | Priority |
| ------ | --------------- | -------------------------------------------------------------------------------------------------------------- | ---------- | -------- |
| NF1.0  | Performance     | A cleaning notification must reach the user within 60 seconds after the box state changes.                     | F1.6       | 1        |
| NF1.1  | Performance     | A visit must appear in the user interface within 10 seconds after it ends.                                     | F1.1, F5.0 | 1        |
| NF1.2  | Accuracy        | The system must detect at least 90 % of real visits with at most 5 % false visits, compared with a manual log. | F1.1       | 1        |
| NF1.3  | Accuracy        | The system must read the microchip in at least 90 % of entries.                                                | F2.1       | 2        |
| NF1.4  | Reliability     | The device must run continuously for 7 days without a manual restart.                                          | -          | 1        |
| NF1.5  | Reliability     | The device must reconnect within 60 seconds after the network returns.                                         | F4.4       | 1        |
| NF1.6  | Reliability     | No data must be lost during a network outage of up to 24 hours.                                                | F4.6       | 2        |
| NF1.7  | Security        | Access to the MQTT broker and the user interface must require a password.                                      | F4.1, F5.0 | 1        |
| NF1.8  | Security        | Data between the device and the server must be encrypted with TLS.                                             | F4.1       | 2        |
| NF1.9  | Security        | Passwords and keys must not be stored in the Git repository.                                                   | -          | 1        |
| NF1.10 | Privacy（？）      | Microchip numbers and visit data must be stored only on the local server, not in third-party clouds.           | F2.0, F4.1 | 1        |
| NF1.11 | Usability       | A non-technical user must be able to tell the box state from the home screen within 5 seconds.                 | F5.1       | 2        |
| NF1.12 | Usability       | The lid must be removable for cleaning without unplugging any cable.                                           | -          | 2        |
| NF1.13 | Cat welfare     | The device must not make audible noise, and no light must shine into the box.                                  | F1.5       | 1        |
| NF1.14 | Cat welfare     | The cats must keep using the box normally during the first 7 days after installation.                          | -          | 1        |
| NF1.15 | Safety          | All electronics must run on 5 V and be protected from litter dust and urine.                                   | -          | 1        |
| NF1.16 | Safety          | Cables must be routed and covered so that the cats cannot chew them.                                           | -          | 2        |
| NF1.17 | Maintainability | All code must follow a common style guide and be reviewed in a pull request before merging.                    | -          | 1        |
| NF1.18 | Power           | The whole device must run from a single USB-C power supply.                                                    | -          | 2        |
| NF1.19 | Cost            | The prototype hardware must cost less than **X** €.                                                            | -          | 3        |
| NF1.20 | Accuracy        | The system must measure the duration of a visit within ±10 seconds.                                            | F1.1       | 1        |
