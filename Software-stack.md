# KissaPissa Software stack

## Minimum requirements

- [ ] A website / web server for controlling & monitoring the devices
    - [ ] Must be accessible from a web browser and a mobile phone.
    - [ ] Must show: 
        1. [ ] Box state (Cleaned or uncleaned since last clean)
        2. [ ] Today's visit count
        3. [ ] Time of last cleaning
        4. [ ] Cleaning history
        5. [ ] Live Camera feed
    - [ ] Must be able to configure the device remotely through said web:
        - [ ] Configure wifi (preferably)
        - [ ] Configure HA (if user has)
        - [ ] Configure NH3 threshold
        - [ ] Mark litterbox as cleaned
    - [ ] A dashboard reporting all sensors values, including camera feed.
        - [ ] This requires Backend APIs reporting sensors value and camera output.

`Note:` Machine Learning is currently a goal under aim, not a required feature.

- [ ] The backend server -- In this sense / context, is the `app` (TM). It orchestrates everything, including serving the frontend, hosting API, managing Machine Learning, and the physical user-interface -- namely, the KissaPissa.
    - [ ] A `daemon` (for now) managing the sensors: 
        1. [ ] Camera
        2. [ ] Gas sensor
        3. [ ] PIR sensor
        4. [ ] Load cell sensors
        5. [ ] Machine Learning 
    - [ ] APIs to fetch sensors' values and outputs:
        1. [ ] Camera
        2. [ ] Gas sensor
        3. [ ] PIR sensor
        4. [ ] Load cell sensors
    - [ ] A simple app library to manage MQTT-related task:
        - [ ] Sending MQTT to an optional HomeAss
    - [ ] Control device feedback via the RGB LED states.

## Appendix
HA  :   Home Assistent
