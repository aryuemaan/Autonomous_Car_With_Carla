import carla
import time

def calculate_collision_time(pedestrian, vehicle):
    pedestrian_location = pedestrian.get_location()
    vehicle_location = vehicle.get_location()
    distance = pedestrian_location.distance(vehicle_location)
    collision_time = distance / vehicle.get_velocity().x
    return collision_time

def on_collision(event):
    actor_type = 'Pedestrian' if 'walker' in event.other_actor.type_id else 'Vehicle'
    print(f"Collision with {actor_type} occurred at time: {event.timestamp.elapsed_seconds}")

try:
    client = carla.Client('localhost', 2000)
    client.set_timeout(5.0)

    world = client.get_world()
    blueprint_library = world.get_blueprint_library()

    map = world.get_map()
    spawn_points = map.get_spawn_points()
    vehicle_bp = blueprint_library.find('vehicle.tesla.model3')
    vehicle = world.spawn_actor(vehicle_bp, spawn_points[0])

    pedestrian_bp = blueprint_library.find('walker.pedestrian.0001')
    pedestrian_transform = carla.Transform(carla.Location(x=40, y=0, z=0), carla.Rotation())
    pedestrian = world.spawn_actor(pedestrian_bp, pedestrian_transform)

    world.on_collision(on_collision)
    vehicle.set_autopilot(True)

    while True:
        world.tick()

        collision_time = calculate_collision_time(pedestrian, vehicle)
        if collision_time < 3.0:
            print(f"Collision predicted in {collision_time} seconds.")
            vehicle.set_autopilot(False)  # Stop the vehicle
            break

        time.sleep(0.1)

finally:
    pedestrian.destroy()
    vehicle.destroy()
