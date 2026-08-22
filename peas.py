class IntelligentAgent:
    def __init__(self, performance, environment, actuators, sensors):
        self.performance = performance
        self.environment = environment
        self.actuators = actuators
        self.sensors = sensors

    def display_peas(self):
        print("========== PEAS Representation ==========")
        print("Performance Measure :", self.performance)
        print("Environment         :", self.environment)
        print("Actuators           :", self.actuators)
        print("Sensors             :", self.sensors)

vacuum_agent = IntelligentAgent(
    performance="Clean all rooms with minimum time and energy",
    environment="Rooms with dust",
    actuators="Move Left, Move Right, Suck Dirt",
    sensors="Dirt Sensor, Location Sensor"
)
vacuum_agent.display_peas() 
