# KissaPissa Software stack

## Minimum requirements

- [ ] A website / web server for controlling & monitoring the devices
    - [ ] Must be accessible from a web browser and a mobile phone.
    - [ ] Must show: 
        1. [ ] Box state (Cleaned or uncleaned since last clean)
        2. [ ] Today's visit count
        3. [ ] Time of last cleaning
        4. [ ] Live Camera feed
    - [ ] Must be able to configure the device remotely through said web:
        - [ ] Configure wifi (preferably)
    - [ ] A dashboard reporting all sensors values, including camera feed.
        - [ ] This requires Backend APIs reporting sensors value and camera output.

- [ ] The backend server -- In this sense / context, is the `app` (TM). It orchestrates everything, including serving the frontend, hosting API, and managing Machine Learning.
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

