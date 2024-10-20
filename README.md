# Time-Series-Simulation-Engine

I built a time-series simulation engine that processes a sequence of time-stamped data ponts. The engine will simulate how a system would transition between an "active" state and "inactive" state based on a decision-making strategy applied to the time-series data.

Firtly, I designed a Python class that:
- Processes a sequence of time-series data.
- Applies a strategy function to decide when to transition between the states.
- Outputs performance metrics that indicate the behavior of the system over time.

1. The class TimeSeriesSimulationEngine - this engine will simulate the behavior of a system that toggles between two states: "active" and "inactive". It starts in the "inactive" state and can transition between states based on the strategy.

2. Data format: the input will be a time-series dataset where each point contains: a timestamp and a numerical value (representing any time-based measurement, like temperature, stock prices or sensor readings)

   data = [
    {"timestamp": "2024-09-01 10:00:00", "value": 100},
    {"timestamp": "2024-09-01 11:00:00", "value": 105},
    {"timestamp": "2024-09-01 12:00:00", "value": 102},
    {"timestamp": "2024-09-01 13:00:00", "value": 98},
    {"timestamp": "2024-09-01 14:00:00", "value": 110},
    {"timestamp": "2024-09-01 15:00:00", "value": 115},
    {"timestamp": "2024-09-01 16:00:00", "value": 112},
    {"timestamp": "2024-09-01 17:00:00", "value": 120},
    {"timestamp": "2024-09-01 18:00:00", "value": 118},
    {"timestamp": "2024-09-01 19:00:00", "value": 120},
    {"timestamp": "2024-09-01 20:00:00", "value": 125},
    {"timestamp": "2024-09-01 21:00:00", "value": 130}
]

3. Methods:
   - initialization: __init__ (self, data) - the engine takes a list of time-series data points, each containing a timestamp and a numerical value.
   - run simulation: run(self, strategy) - the engine will traverse the time series data, applying the strategy function at each step to decide whether to transition between states.
   - output metrics: after running the simulation, the engine should return total transitions (total number of states, from "inactive" to "active" and vice versa), active time percentage (the percentage of total time the system spent in "active" state, relative to the full time span of the data) and number of activations (the number of times the system transitioned from "inactive" to "active").

4. Strategy function: the strategy function determines whether to transition between states based on the current value, previous value and the current state. I used a simple strategy, activate if the current value is higher than the previous value and deactivate if the current value is lower than the previous value. The strategy function can be changed.
  
5. State transition logic:
   - the system starts in the "inactive" state.
   - it can transition to the "active" state based on the strategy's "activate" recommendation.
   - it can transition to the "inactive" state based on the strategy's "deactivate" recommendation.
   - if the strategy says "stay", no state change occurs.
  
  
