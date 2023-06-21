import pygame
import carla

class AutomaticControlCar:
    def __init__(self):
        self.client = carla.Client('localhost', 2000)
        self.client.set_timeout(5.0)
        self.world = self.client.get_world()
        self.map = self.world.get_map()
        self.vehicle = None
        self.sensors = []

        self._create_vehicle()
        self._create_sensors()
        self._setup_keybindings()

        self.world.on_tick(self._update)

    def _create_vehicle(self):
        blueprint_library = self.world.get_blueprint_library()
        vehicle_blueprint = blueprint_library.find('vehicle.tesla.model3')
        spawn_point = carla.Transform(carla.Location(x=10, y=10, z=2), carla.Rotation())
        self.vehicle = self.world.spawn_actor(vehicle_blueprint, spawn_point)

    def _create_sensors(self):
        camera_blueprint = self.world.get_blueprint_library().find('sensor.camera.rgb')
        camera_blueprint.set_attribute('image_size_x', '800')
        camera_blueprint.set_attribute('image_size_y', '600')
        camera_blueprint.set_attribute('fov', '90')

        sensor_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
        sensor = self.world.spawn_actor(camera_blueprint, sensor_transform, attach_to=self.vehicle)
        self.sensors.append(sensor)

        lidar_blueprint = self.world.get_blueprint_library().find('sensor.lidar.ray_cast')
        lidar_blueprint.set_attribute('channels', '32')
        lidar_blueprint.set_attribute('points_per_second', '100000')
        lidar_blueprint.set_attribute('rotation_frequency', '10')
        lidar_blueprint.set_attribute('range', '50')

        sensor_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
        sensor = self.world.spawn_actor(lidar_blueprint, sensor_transform, attach_to=self.vehicle)
        self.sensors.append(sensor)

    def _setup_keybindings(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Automatic Control Car')
        self.clock = pygame.time.Clock()

    def _update(self, timestamp):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_L:
                    self.vehicle.toggle_light()
                elif event.key == pygame.K_LSHIFT:
                    self.vehicle.toggle_high_beam()
                elif event.key == pygame.K_z:
                    self.vehicle.toggle_right_blinker()
                elif event.key == pygame.K_x:
                    self.vehicle.toggle_left_blinker()
                elif event.key == pygame.K_i:
                    self.vehicle.toggle_interior_light()
                elif event.key == pygame.K_TAB:
                    self._change_sensor_position()
                elif event.key == pygame.K_BACKQUOTE:
                    self._next_sensor()
                elif event.key >= pygame.K_1 and event.key <= pygame.K_9:
                    sensor_index = event.key - pygame.K_1
                    self._change_to_sensor(sensor_index)
                elif event.key == pygame.K_g:
                    self.vehicle.toggle_radar_visualization()
                elif event.key == pygame.K_c:
                    self._change_weather()
                elif event.key == pygame.K_o:
                    self.vehicle.toggle_all_doors()
                elif event.key == pygame.K_t:
                    self.vehicle.toggle_telemetry()

        self.clock.tick_busy_loop(60)
        pygame.display.flip()

    def _quit(self):
        pygame.quit()
        self.client.apply_batch([carla.command.DestroyActor(x) for x in self.sensors])
        self.client.apply_batch([carla.command.DestroyActor(self.vehicle)])
        self.vehicle = None
        self.sensors = []
        self.world.on_tick(self._update, clear=True)
        self.world = None
        self.map = None
        self.client = None


# Create and run the automatic control car
if __name__ == '__main__':
    automatic_control_car = AutomaticControlCar()
