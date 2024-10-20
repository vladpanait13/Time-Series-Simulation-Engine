from typing import List, Dict, Union
from datetime import datetime

class TimeSeriesSimulationEngine:
    
    def __init__(self, data: List[Dict[str, Union[str, float]]]):
        self.data = [
            {'timestamp': datetime.strptime(point['timestamp'], '%Y-%m-%d %H:%M:%S'), 'value': point['value']}
            for point in data
        ]
        self.current_state = 'inactive'
        self.transitions = 0
        self.activations = 0
        self.active_time = 0
        self.total_time_span = 0
        
    def run(self, strategy):
        # Run the simulation using the strategy
        previous_value = None
        last_transition_time = self.data[0]['timestamp']
        
        for i, point in enumerate(self.data):
            current_value = point['value']
            current_timestamp = point['timestamp']
            
            if previous_value is not None:
                decision = strategy(current_value, previous_value, self.current_state)
                if decision == 'activate' and self.current_state == 'inactive':
                    self.transitions += 1
                    self.activations += 1
                    self.current_state = 'active'
                    self.total_time_span += (current_timestamp - last_transition_time).total_seconds()
                    last_transition_time = current_timestamp
                
                elif decision == 'deactivate' and self.current_state == 'active':
                    self.transitions += 1
                    self.current_state = 'inactive'
                    self.active_time += (current_timestamp - last_transition_time).total_seconds()
                    last_transition_time = current_timestamp

            previous_value = current_value

    # After the last data point, add time spent in the final state
        final_timestamp = self.data[-1]['timestamp']
        if self.current_state == 'active':
            self.active_time += (final_timestamp - last_transition_time).total_seconds()
        else:
            self.total_time_span += (final_timestamp - last_transition_time).total_seconds()

        # Calculate performance metrics
        total_time_span = (self.data[-1]['timestamp'] - self.data[0]['timestamp']).total_seconds()
        active_time_percentage = (self.active_time / total_time_span) * 100 if total_time_span > 0 else 0
        
        return {
            'total_transitions': self.transitions,
            'active_time_percentage': active_time_percentage,
            'num_activations': self.activations
        }

def simple_strategy(current_value, previous_value, current_state):
    if current_value > previous_value and current_state == "inactive":
        return "activate"
    elif current_value < previous_value and current_state == "active":
        return "deactivate"
    else:
        return "stay"
        
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

engine = TimeSeriesSimulationEngine(data)
metrics = engine.run(simple_strategy)
print(metrics)