const Gpio = require('pigpio').Gpio; 

const led1 = new Gpio(22, {mode: Gpio.OUTPUT});
const led2 = new Gpio(27, {mode: Gpio.OUTPUT});

const microSwitch = new Gpio(17, {
  mode: Gpio.INPUT,
  pullUpDown: Gpio.PUD_DOWN,     
  edge: Gpio.EITHER_EDGE       
});

microSwitch.on('interrupt', (level) => {  
  led1.digitalWrite(level);   
  led2.digitalWrite(!level);       
});
